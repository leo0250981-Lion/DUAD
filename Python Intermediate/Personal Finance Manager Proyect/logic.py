from __future__ import annotations
from dataclasses import asdict
from typing import Dict, List

from models import Category, Movement
from validators import validate_amount, validate_non_empty, validate_not_future


class FinanceManager:
    def __init__(self):
        self.categories: Dict[str, Category] = {}
        self.movements: List[Movement] = []

    # --- Categories ---
    def add_category(self, name: str, color: str = "#FFFFFF") -> Category:
        name = validate_non_empty(name, "category name")
        if name in self.categories:
            raise ValueError("Category already exists")
        cat = Category(name=name, color=color)
        self.categories[name] = cat
        return cat

    def list_categories(self) -> List[str]:
        return sorted(self.categories.keys())

    def _ensure_categories_exist(self) -> None:
        if not self.categories:
            raise RuntimeError("No categories available. Add a category first.")

    # --- Movements ---
    def add_income(self, title: str, amount, category: str, date_str: str) -> Movement:
        self._ensure_categories_exist()
        title = validate_non_empty(title, "title")
        category = validate_non_empty(category, "category")
        if category not in self.categories:
            raise ValueError("Category does not exist")
        validate_not_future(date_str)
        amt = validate_amount(amount)
        if amt <= 0:
            raise ValueError("Income amount must be > 0")

        m = Movement(date=date_str, title=title, amount=float(amt), category=category, type="Income")
        self.movements.append(m)
        return m

    def add_expense(self, title: str, amount, category: str, date_str: str) -> Movement:
        self._ensure_categories_exist()
        title = validate_non_empty(title, "title")
        category = validate_non_empty(category, "category")
        if category not in self.categories:
            raise ValueError("Category does not exist")
        validate_not_future(date_str)
        amt = validate_amount(amount)
        if amt <= 0:
            raise ValueError("Expense amount must be > 0")

        m = Movement(date=date_str, title=title, amount=-float(amt), category=category, type="Expense")
        self.movements.append(m)
        return m

    def to_dict(self) -> dict:
        return {
            "categories": {name: asdict(cat) for name, cat in self.categories.items()},
            "movements": [asdict(m) for m in self.movements],
        }

    @classmethod
    def from_dict(cls, data: dict) -> "FinanceManager":
        fm = cls()
        for name, payload in data.get("categories", {}).items():
            fm.categories[name] = Category(**payload)
        for payload in data.get("movements", []):
            fm.movements.append(Movement(**payload))
        return fm
