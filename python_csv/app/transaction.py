import csv
from datetime import datetime
from pathlib import Path

TRANSACTION_FILE = Path(__file__).parent.parent / "data" / "transactions.csv"

FIELDNAMES = ["date", "type", "sender", "receiver", "amount"]


def save_transaction(
    transaction_type,
    sender,
    receiver,
    amount
):
    needs_header = (
        not TRANSACTION_FILE.exists()
        or TRANSACTION_FILE.stat().st_size == 0
    )

    with open(
        TRANSACTION_FILE,
        "a",
        newline=""
    ) as file:

        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)

        if needs_header:
            writer.writeheader()

        writer.writerow({
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": transaction_type,
            "sender": sender,
            "receiver": receiver,
            "amount": amount
        })


def show_transaction_history(account_number):
    print("\n========== TRANSACTION HISTORY ==========")

    if not TRANSACTION_FILE.exists():
        print("\nNo transactions found.")
        return

    found = False

    with open(
        TRANSACTION_FILE,
        "r",
        newline=""
    ) as file:

        reader = csv.DictReader(file)

        for transaction in reader:

            sender = transaction["sender"]
            receiver = transaction["receiver"]

            if (
                sender == account_number
                or receiver == account_number
            ):
                found = True

                print(
                    f"\nDate       : {transaction['date']}"
                )

                print(
                    f"Type       : {transaction['type']}"
                )

                print(
                    f"Sender     : {sender}"
                )

                print(
                    f"Receiver   : {receiver}"
                )

                print(
                    f"Amount     : Rp{float(transaction['amount']):,.0f}"
                )

    if not found:
        print("\nNo transactions found.")