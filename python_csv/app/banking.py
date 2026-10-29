class BankAccount:
    def __init__(
        self,
        user_id,
        account_number,
        account_holder,
        balance=0,
        pin=""
    ):
        self.user_id = user_id
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.pin = pin

    def deposit(self, amount):
        if amount <= 0:
            print("\nDeposit amount must be greater than 0.")
            return False

        self.balance += amount

        print("\nDeposit successful.")
        print(f"Amount          : Rp{amount:,.0f}")
        print(f"Current balance : Rp{self.balance:,.0f}")

        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("\nWithdrawal amount must be greater than 0.")
            return False

        if amount > self.balance:
            print("\nInsufficient balance.")
            return False

        self.balance -= amount

        print("\nWithdrawal successful.")
        print(f"Amount          : Rp{amount:,.0f}")
        print(f"Current balance : Rp{self.balance:,.0f}")

        return True

    def transfer(self, receiver, amount):
        if amount <= 0:
            print("\nTransfer amount must be greater than 0.")
            return False

        if amount > self.balance:
            print("\nInsufficient balance.")
            return False

        self.balance -= amount
        receiver.balance += amount

        print("\nTransfer successful.")
        print(f"To              : {receiver.account_holder}")
        print(f"Amount          : Rp{amount:,.0f}")
        print(f"Current balance : Rp{self.balance:,.0f}")

        return True

    def show_balance(self):
        print("\n--- Account Information ---")
        print(f"Account holder  : {self.account_holder}")
        print(f"Account number  : {self.account_number}")
        print(f"Balance         : Rp{self.balance:,.0f}")