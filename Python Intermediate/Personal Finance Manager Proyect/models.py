from __future__ import annotations
from dataclasses import dataclass
from typing import Literal

MovementType = Literal["Income", "Expense"]


@dataclass(frozen=True)
class Category:
    name: str
    color: str = "#FFFFFF"  # optional


@dataclass
class Movement:
    date: str          # dd/mm/yyyy
    title: str
    amount: float      # positive for Income, negative for Expense (or enforce by type)
    category: str
    type: MovementType
