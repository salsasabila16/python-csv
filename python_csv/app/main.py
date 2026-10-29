from python_csv.app.auth import (
    load_users,
    login,
    find_account,
    save_users
)

from python_csv.app.transaction import (
    save_transaction,
    show_transaction_history
)

from python_csv.app.validation import (
    validate_amount,
    validate_transfer
)


def dashboard(account, accounts):

    while True:

        print("\n================================")
        print("          BANKING SYSTEM")
        print("================================")
        print(f"Welcome, {account.account_holder}")
        print("================================")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Logout")
        print("================================")

        choice = input("Choose an option: ")

        # CHECK BALANCE
        if choice == "1":

            account.show_balance()

        # DEPOSIT
        elif choice == "2":

            try:
                amount = float(
                    input("Deposit amount: Rp")
                )

                if not validate_amount(amount):
                    print("\nAmount must be greater than 0.")
                    continue

                success = account.deposit(amount)

                if success:

                    save_users(accounts)

                    save_transaction(
                        "DEPOSIT",
                        "-",
                        account.account_number,
                        amount
                    )

            except ValueError:

                print("\nPlease enter a valid number.")

        # WITHDRAW
        elif choice == "3":

            try:
                amount = float(
                    input("Withdrawal amount: Rp")
                )

                if not validate_amount(amount):
                    print("\nAmount must be greater than 0.")
                    continue

                success = account.withdraw(amount)

                if success:

                    save_users(accounts)

                    save_transaction(
                        "WITHDRAW",
                        account.account_number,
                        "-",
                        amount
                    )

            except ValueError:

                print("\nPlease enter a valid number.")

        # TRANSFER
        elif choice == "4":

            receiver_number = input(
                "Receiver account number: "
            )

            receiver = find_account(
                accounts,
                receiver_number
            )

            if receiver is None:

                print("\nReceiver account not found.")
                continue

            if not validate_transfer(
                account,
                receiver
            ):

                print("\nYou cannot transfer to yourself.")
                continue

            try:

                amount = float(
                    input("Transfer amount: Rp")
                )

                if not validate_amount(amount):

                    print("\nAmount must be greater than 0.")
                    continue

                success = account.transfer(
                    receiver,
                    amount
                )

                if success:

                    save_users(accounts)

                    save_transaction(
                        "TRANSFER",
                        account.account_number,
                        receiver.account_number,
                        amount
                    )

            except ValueError:

                print("\nPlease enter a valid number.")

        # TRANSACTION HISTORY
        elif choice == "5":

            show_transaction_history(
                account.account_number
            )

        # LOGOUT
        elif choice == "6":

            print("\nLogging out...")
            break

        else:

            print("\nInvalid option. Please choose 1-6.")


def main():

    accounts = load_users()

    while True:

        print("\n================================")
        print("       WELCOME TO BANKING")
        print("================================")
        print("1. Login")
        print("2. Exit")
        print("================================")

        choice = input("Choose an option: ")

        if choice == "1":

            account = login(accounts)

            if account is not None:

                dashboard(
                    account,
                    accounts
                )

        elif choice == "2":

            print(
                "\nThank you for using Banking System."
            )

            break

        else:

            print("\nInvalid option.")


if __name__ == "__main__":
    main()