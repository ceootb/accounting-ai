"""Core accounting engine — deterministic backbone for Accounting AI.

Ini LAPISAN yang harus PASTI BENAR (bukan ditebak AI): struktur COA, aturan
double-entry, validasi balance, dan perhitungan pajak. Model AI mengusulkan
jurnal; engine ini yang MENGUNCI kebenarannya (balance + akun valid + PPN benar).

Pure Python, tanpa dependency. Reusable untuk: edge AI, app UMKM, enterprise, SPI.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
import json
import os


class AccountType(str, Enum):
    ASSET = "ASSET"
    LIABILITY = "LIABILITY"
    EQUITY = "EQUITY"
    REVENUE = "REVENUE"
    EXPENSE = "EXPENSE"


# Saldo normal: ASSET & EXPENSE = debit; sisanya = kredit.
_DEBIT_NORMAL = {AccountType.ASSET, AccountType.EXPENSE}


@dataclass(frozen=True)
class Account:
    code: str
    name: str
    type: AccountType

    @property
    def normal_balance(self) -> str:
        return "debit" if self.type in _DEBIT_NORMAL else "credit"


class ChartOfAccounts:
    """Bagan Akun (COA). Sumber kebenaran daftar akun."""

    def __init__(self, accounts=None):
        self._by_code = {}
        for a in (accounts or []):
            self.add(a)

    def add(self, account: Account):
        self._by_code[account.code] = account

    def get(self, code):
        return self._by_code.get(code)

    def __len__(self):
        return len(self._by_code)

    @classmethod
    def from_json(cls, path):
        data = json.load(open(path, encoding="utf-8"))
        return cls([Account(a["code"], a["name"], AccountType(a["type"])) for a in data])

    @classmethod
    def default_id(cls):
        return cls.from_json(os.path.join(os.path.dirname(__file__), "coa_id_default.json"))


def _money(x) -> float:
    return round(float(x), 2)


@dataclass
class JournalLine:
    account: str            # kode akun
    debit: float = 0.0
    credit: float = 0.0


@dataclass
class JournalEntry:
    description: str
    lines: list = field(default_factory=list)
    date: str = ""

    def add(self, account, debit=0.0, credit=0.0):
        self.lines.append(JournalLine(account, _money(debit), _money(credit)))
        return self

    @property
    def total_debit(self) -> float:
        return _money(sum(l.debit for l in self.lines))

    @property
    def total_credit(self) -> float:
        return _money(sum(l.credit for l in self.lines))

    @property
    def is_balanced(self) -> bool:
        return self.total_debit == self.total_credit and self.total_debit > 0

    def validate(self, coa: "ChartOfAccounts | None" = None) -> list:
        """Kembalikan daftar error (kosong = valid)."""
        errs = []
        if not self.lines:
            errs.append("jurnal kosong")
        if self.total_debit != self.total_credit:
            errs.append(f"tidak balance: debit {self.total_debit} != kredit {self.total_credit}")
        for l in self.lines:
            if l.debit and l.credit:
                errs.append(f"baris {l.account}: tidak boleh debit & kredit sekaligus")
            if l.debit < 0 or l.credit < 0:
                errs.append(f"baris {l.account}: nilai negatif")
            if coa is not None and coa.get(l.account) is None:
                errs.append(f"akun '{l.account}' tidak ada di COA")
        return errs

    def assert_valid(self, coa=None) -> bool:
        errs = self.validate(coa)
        if errs:
            raise ValueError("Jurnal tidak valid: " + "; ".join(errs))
        return True


# --- Pajak (Indonesia) ---
PPN_RATE = 0.11


def ppn(dpp, rate: float = PPN_RATE) -> float:
    """PPN dari DPP (harga sebelum pajak)."""
    return _money(_money(dpp) * rate)


def split_inclusive(total, rate: float = PPN_RATE):
    """Pecah harga TERMASUK PPN menjadi (DPP, PPN)."""
    dpp = _money(_money(total) / (1 + rate))
    return dpp, _money(_money(total) - dpp)
