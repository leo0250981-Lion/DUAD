class BankAccount:
    def __init__(self, initial_balance: float = 0.0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self._balance = initial_balance

    @property
    def balance(self) -> float:
        """Return current account balance (read-only)."""
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount


class SavingsAccount(BankAccount):
    def __init__(self, initial_balance: float, min_balance: float):
        if min_balance < 0:
            raise ValueError("Minimum balance cannot be negative.")
        if initial_balance < min_balance:
            raise ValueError("Initial balance cannot be less than minimum balance.")
        super().__init__(initial_balance)
        self._min_balance = min_balance

    @property
    def min_balance(self) -> float:
        return self._min_balance

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        if self._balance - amount < self._min_balance:
            raise ValueError(
                "Withdrawal denied: balance cannot go below the minimum balance."
            )

        self._balance -= amount


def main() -> None:
    print("=== BankAccount Example ===")
    account = BankAccount(100.0)
    print("Initial balance:", account.balance)

    account.deposit(50.0)
    print("After deposit:", account.balance)

    account.withdraw(30.0)
    print("After withdrawal:", account.balance)

    print("\n=== SavingsAccount Example ===")
    savings = SavingsAccount(initial_balance=500.0, min_balance=200.0)
    print("Initial balance:", savings.balance)

    savings.withdraw(100.0)
    print("After withdrawal:", savings.balance)

    try:
        savings.withdraw(250.0)
    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
