class BankAccount:
    def __init__(self, initial_balance: float = 0.0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.__balance = initial_balance  # Encapsulated Attribute

    @property
    def balance(self) -> float:
        """Return current account balance (read-only)."""
        return self.__balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount

#Example 
def main() -> None:
    account = BankAccount(100.0)

    print("Initial balance:", account.balance)

    account.deposit(50.0)
    print("After deposit:", account.balance)

    account.withdraw(30.0)
    print("After withdrawal:", account.balance)

    # Example of validation with an exception
    try:
        account.withdraw(500.0)
    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
