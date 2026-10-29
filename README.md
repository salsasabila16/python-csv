# Account Management System — Python CLI

A command-line account and transaction management system built with Python. User accounts, balances, and transaction history are stored in structured CSV files without requiring an external database.

---

## Folder Structure

```text
python/
├── README.md
└── python_csv/
    ├── app/
    │   ├── main.py           # Entry point and main menu
    │   ├── auth.py           # Login and user data management
    │   ├── banking.py        # Account model and balance management
    │   ├── transaction.py    # Transaction recording and history
    │   └── validation.py     # Input validation
    └── data/
        ├── users.csv         # User account data
        └── transactions.csv  # Complete transaction history
```

---

## Backend Modules

### `banking.py` — BankAccount

The main module for managing user account information and balances. Each account contains `user_id`, `account_number`, `account_holder`, `balance`, and `pin`.

| Method | Description |
|---|---|
| `deposit(amount)` | Adds funds to an account |
| `withdraw(amount)` | Deducts funds from an account |
| `transfer(receiver, amount)` | Transfers funds to another account |
| `show_balance()` | Displays account information and balance |

### `auth.py` — Authentication and Persistence

Handles the login process and reads and saves user data using CSV files.

| Function | Description |
|---|---|
| `load_users()` | Loads account data from `users.csv` |
| `find_account(accounts, account_number)` | Finds an account by account number |
| `login(accounts)` | Authenticates users using their account number and PIN |
| `save_users(accounts)` | Saves updated account data to `users.csv` |

### `transaction.py` — Transaction Recording

Handles transaction records and displays users' transaction history.

| Function | Description |
|---|---|
| `save_transaction(type, sender, receiver, amount)` | Saves a transaction to `transactions.csv` |
| `show_transaction_history(account_number)` | Displays transaction history for a specific account number |

### `validation.py` — Input Validation

Ensures that user input meets the required rules before an operation is performed.

| Function | Description |
|---|---|
| `validate_amount(amount)` | Ensures the transaction amount is greater than zero |
| `validate_transfer(sender, receiver)` | Prevents transfers to the sender's own account |

---

## CSV Storage Format

### `users.csv`

```csv
id,nama,no_rekening,saldo,pin
1,Andi Pratama,1001000001,15010000,1234
```

| Column | Description |
|---|---|
| `id` | Unique user ID |
| `nama` | Account holder's name |
| `no_rekening` | Account number |
| `saldo` | Account balance in Indonesian Rupiah (IDR) |
| `pin` | User PIN |

### `transactions.csv`

```csv
date,type,sender,receiver,amount
2026-09-25 10:00:00,DEPOSIT,-,1001000001,100000.0
```

| Column | Description |
|---|---|
| `date` | Transaction timestamp |
| `type` | Transaction type: `DEPOSIT`, `WITHDRAW`, or `TRANSFER` |
| `sender` | Sender's account number |
| `receiver` | Recipient's account number |
| `amount` | Transaction amount in Indonesian Rupiah (IDR) |

---

## Features

- **Login** — Authenticates users using their account number and PIN.
- **Balance Inquiry** — Displays account information and the current balance.
- **Deposit** — Adds funds to an account.
- **Withdrawal** — Withdraws funds from an account.
- **Transfer** — Transfers funds to another account.
- **Transaction History** — Displays records of incoming and outgoing transactions.

---

## How to Run

Run the following command from the project directory containing the `python_csv` folder:

```bash
python3 -m python_csv.app.main
```

Make sure Python 3.x is installed.

---

## Technical Notes

- CSV files are used for data storage without an external database.
- Balance changes are saved to `users.csv`.
- Successful transactions are recorded in `transactions.csv` along with their timestamps.

---

** 功课👍🏻 ** 
