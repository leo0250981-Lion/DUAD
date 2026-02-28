import unittest
from datetime import date, timedelta

from logic import FinanceManager


class TestFinanceManager(unittest.TestCase):

    def setUp(self):
        self.fm = FinanceManager()

    # 1) Cannot add movement if no categories
    def test_add_income_without_categories_raises(self):
        with self.assertRaises(RuntimeError):
            self.fm.add_income("Salary", 1000, "Work", "01/07/2025")

    # 2) Add category OK
    def test_add_category_success(self):
        cat = self.fm.add_category("Food", "#FFA500")
        self.assertEqual(cat.name, "Food")
        self.assertIn("Food", self.fm.categories)

    # 3) Duplicate category raises
    def test_add_category_duplicate_raises(self):
        self.fm.add_category("Food")
        with self.assertRaises(ValueError):
            self.fm.add_category("Food")

    # 4) Add income creates positive amount
    def test_add_income_success(self):
        self.fm.add_category("Work")
        m = self.fm.add_income("Salary", 1000, "Work", "02/07/2025")
        self.assertEqual(m.type, "Income")
        self.assertEqual(m.amount, 1000.0)

    # 5) Add expense stores negative amount
    def test_add_expense_success(self):
        self.fm.add_category("Food")
        m = self.fm.add_expense("Pizza", 40, "Food", "03/07/2025")
        self.assertEqual(m.type, "Expense")
        self.assertEqual(m.amount, -40.0)

    # 6) Division of invalid category raises
    def test_add_income_invalid_category_raises(self):
        self.fm.add_category("Work")
        with self.assertRaises(ValueError):
            self.fm.add_income("Salary", 1000, "NotExists", "02/07/2025")

    # 7) Future date raises
    def test_future_date_raises(self):
        self.fm.add_category("Work")
        future = (date.today() + timedelta(days=5)).strftime("%d/%m/%Y")
        with self.assertRaises(ValueError):
            self.fm.add_income("Salary", 1000, "Work", future)

    # 8) Filter by date range returns expected
    def test_filter_by_date_range(self):
        self.fm.add_category("Work")
        self.fm.add_category("Food")
        self.fm.add_income("Salary", 1000, "Work", "02/07/2025")
        self.fm.add_expense("Food", 20, "Food", "03/07/2025")
        self.fm.add_expense("Clothes", 50, "Food", "12/07/2025")

        filtered = self.fm.filter_by_date_range("01/07/2025", "10/07/2025")
        self.assertEqual(len(filtered), 2)
        self.assertEqual([m.title for m in filtered], ["Salary", "Food"])

    # 9) Totals calculation
    def test_totals(self):
        self.fm.add_category("Work")
        self.fm.add_category("Food")
        self.fm.add_income("Salary", 1200, "Work", "01/07/2025")
        self.fm.add_expense("Lunch", 100, "Food", "02/07/2025")

        totals = self.fm.totals()
        self.assertEqual(totals["income"], 1200.0)
        self.assertEqual(totals["expense"], 100.0)
        self.assertEqual(totals["net"], 1100.0)


if __name__ == "__main__":
    unittest.main()
