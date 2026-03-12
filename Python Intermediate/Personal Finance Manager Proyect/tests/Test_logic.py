import unittest
from datetime import date, timedelta

from logic import FinanceManager


class TestFinanceManager(unittest.TestCase):
    def setUp(self):
        self.fm = FinanceManager()

    def test_no_categories_add_income_raises(self):
        with self.assertRaises(RuntimeError):
            self.fm.add_income("Salary", 1000, "Work", "01/07/2025")

    def test_add_category_success(self):
        cat = self.fm.add_category("Food", "#FFA500")
        self.assertEqual(cat.name, "Food")
        self.assertIn("Food", self.fm.categories)

    def test_add_category_duplicate_raises(self):
        self.fm.add_category("Food")
        with self.assertRaises(ValueError):
            self.fm.add_category("Food")

    def test_add_income_success(self):
        self.fm.add_category("Work")
        m = self.fm.add_income("Salary", 1000, "Work", "02/07/2025")
        self.assertEqual(m.type, "Income")
        self.assertEqual(m.amount, 1000.0)

    def test_add_expense_success(self):
        self.fm.add_category("Food")
        m = self.fm.add_expense("Pizza", 40, "Food", "03/07/2025")
        self.assertEqual(m.type, "Expense")
        self.assertEqual(m.amount, -40.0)

    def test_invalid_category_raises(self):
        self.fm.add_category("Work")
        with self.assertRaises(ValueError):
            self.fm.add_income("Salary", 1000, "Other", "02/07/2025")

    def test_future_date_raises(self):
        self.fm.add_category("Work")
        future = (date.today() + timedelta(days=2)).strftime("%d/%m/%Y")
        with self.assertRaises(ValueError):
            self.fm.add_income("Salary", 1000, "Work", future)

    def test_invalid_amount_type_raises(self):
        self.fm.add_category("Work")
        with self.assertRaises(TypeError):
            self.fm.add_income("Salary", "NOT_A_NUMBER", "Work", "02/07/2025")

    def test_income_amount_must_be_positive(self):
        self.fm.add_category("Work")
        with self.assertRaises(ValueError):
            self.fm.add_income("Salary", 0, "Work", "02/07/2025")


if __name__ == "__main__":
    unittest.main()
