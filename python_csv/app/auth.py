import csv
from pathlib import Path
from python_csv.app.banking import BankAccount

USERS_FILE = Path(__file__).parent.parent / "data" / "users.csv"


def load_users():
    accounts = []

    with open(USERS_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)

        for user in reader:
            account = BankAccount(
                user["id"],
                user["no_rekening"],
                user["nama"],
                float(user["saldo"]),
                user["pin"]
            )

            accounts.append(account)

    return accounts


def find_account(accounts, account_number):
    for account in accounts:
        if account.account_number == account_number:
            return account

    return None


def login(accounts):
    print("\n========== LOGIN ==========")

    account_number = input("Account number : ")
    pin = input("PIN            : ")

    account = find_account(
        accounts,
        account_number
    )

    if account is None:
        print("\nAccount not found.")
        return None

    if account.pin != pin:
        print("\nIncorrect PIN.")
        return None

    print(f"\nWelcome, {account.account_holder}!")

    return account


def save_users(accounts):
    with open(USERS_FILE, "w", newline="") as file:

        fieldnames = [
            "id",
            "nama",
            "no_rekening",
            "saldo",
            "pin"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for account in accounts:
            writer.writerow({
                "id": account.user_id,
                "nama": account.account_holder,
                "no_rekening": account.account_number,
                "saldo": account.balance,
                "pin": account.pin
            })