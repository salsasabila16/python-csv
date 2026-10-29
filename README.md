# Account Management System — Python CLI

Aplikasi pengelolaan akun dan transaksi berbasis command line yang dibangun menggunakan Python. Data pengguna, saldo, dan riwayat transaksi disimpan secara terstruktur menggunakan file CSV tanpa memerlukan database eksternal.

---

## Struktur Folder

```text
python/
├── README.md
└── python_csv/
    ├── app/
    │   ├── main.py           # Entry point dan menu utama
    │   ├── auth.py           # Login dan pengelolaan data pengguna
    │   ├── banking.py        # Model akun dan pengelolaan saldo
    │   ├── transaction.py    # Pencatatan dan riwayat transaksi
    │   └── validation.py     # Validasi input
    └── data/
        ├── users.csv         # Data akun pengguna
        └── transactions.csv  # Riwayat seluruh transaksi
```

---

## Modul Backend

### `banking.py` — BankAccount

Modul utama untuk mengelola data akun dan saldo pengguna. Setiap akun memiliki informasi berupa `user_id`, `account_number`, `account_holder`, `balance`, dan `pin`.

| Method | Fungsi |
|---|---|
| `deposit(amount)` | Menambahkan saldo akun |
| `withdraw(amount)` | Mengurangi saldo akun |
| `transfer(receiver, amount)` | Memindahkan saldo ke akun lain |
| `show_balance()` | Menampilkan informasi akun dan saldo |

### `auth.py` — Autentikasi dan Persistensi

Mengelola proses login serta membaca dan menyimpan data pengguna menggunakan file CSV.

| Fungsi | Keterangan |
|---|---|
| `load_users()` | Membaca data akun dari `users.csv` |
| `find_account(accounts, account_number)` | Mencari akun berdasarkan nomor rekening |
| `login(accounts)` | Memproses login menggunakan nomor rekening dan PIN |
| `save_users(accounts)` | Menyimpan data akun terbaru ke `users.csv` |

### `transaction.py` — Pencatatan Transaksi

Mengelola pencatatan dan penampilan riwayat transaksi pengguna.

| Fungsi | Keterangan |
|---|---|
| `save_transaction(type, sender, receiver, amount)` | Menyimpan transaksi ke `transactions.csv` |
| `show_transaction_history(account_number)` | Menampilkan riwayat transaksi berdasarkan nomor rekening |

### `validation.py` — Validasi Input

Memastikan input memenuhi aturan yang ditentukan sebelum operasi dijalankan.

| Fungsi | Keterangan |
|---|---|
| `validate_amount(amount)` | Memastikan jumlah transaksi lebih dari nol |
| `validate_transfer(sender, receiver)` | Mencegah transfer ke akun sendiri |

---

## Format Penyimpanan CSV

### `users.csv`

```csv
id,nama,no_rekening,saldo,pin
1,Andi Pratama,1001000001,15010000,1234
```

| Kolom | Keterangan |
|---|---|
| `id` | ID unik pengguna |
| `nama` | Nama pemegang akun |
| `no_rekening` | Nomor rekening |
| `saldo` | Saldo akun dalam Rupiah |
| `pin` | PIN pengguna |

### `transactions.csv`

```csv
date,type,sender,receiver,amount
2026-09-25 10:00:00,DEPOSIT,-,1001000001,100000.0
```

| Kolom | Keterangan |
|---|---|
| `date` | Waktu transaksi |
| `type` | Jenis transaksi: `DEPOSIT`, `WITHDRAW`, atau `TRANSFER` |
| `sender` | Nomor rekening pengirim |
| `receiver` | Nomor rekening penerima |
| `amount` | Jumlah transaksi dalam Rupiah |

---

## Fitur

- **Login** — autentikasi pengguna menggunakan nomor rekening dan PIN.
- **Cek Saldo** — menampilkan informasi akun dan saldo terkini.
- **Deposit** — menambahkan saldo akun.
- **Withdraw** — melakukan penarikan saldo.
- **Transfer** — memindahkan saldo ke akun lain.
- **Riwayat Transaksi** — melihat catatan transaksi masuk dan keluar.

---

## Cara Menjalankan

Jalankan perintah berikut dari direktori proyek yang berisi folder `python_csv`:

```bash
python3 -m python_csv.app.main
```

Pastikan Python 3.x sudah terpasang.

---

## Catatan Teknis

- File CSV digunakan sebagai media penyimpanan data tanpa database eksternal.
- Perubahan saldo disimpan ke `users.csv`.
- Transaksi yang berhasil dicatat ke `transactions.csv` beserta timestamp.

---

## Teknologi

- Python 3
- CSV File Handling
# python-csv
