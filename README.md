# Danguard v3.1 - Panduan Instalasi & Penggunaan

Tools untuk mendeteksi dan verifikasi kerentanan Subdomain Takeover.

---

## 1. Persiapan

Pastikan komputer Anda sudah terinstall:
-   Python 3.8 atau lebih baru
-   Git

---

## 2. Instalasi

Buka terminal atau command prompt, lalu jalankan perintah berikut:

```bash
# 1. Clone repositori ini
git clone https://github.com/username-anda/danguard-v3.1.git
cd danguard-v3.1

# 2. Buat dan aktifkan virtual environment
python -m venv venv

# Untuk Windows
venv\Scripts\activate

# Untuk macOS/Linux
source venv/bin/activate

# 3. Install semua library yang dibutuhkan
pip install -r requirements.txt

3. Konfigurasi
Semua API key dan token disimpan di file .env.

1. Buat file .env dari file contoh :
cp .env.example .env

2. Buka file .env dengan teks editor, lalu isi dengan kredensial Anda :
# Vercel
VERCEL_API_KEY="API_KEY_VERCEL_ANDA"

# Azure
AZURE_CLIENT_ID="ID_APLIKASI_AZURE_ANDA"
AZURE_TENANT_ID="ID_DIREKTORI_AZURE_ANDA"
AZURE_CLIENT_SECRET="SECRET_AZURE_ANDA"
AZURE_SUBSCRIPTION_ID="ID_SUBSCRIPTION_AZURE_ANDA"

# Telegram
TELEGRAM_BOT_TOKEN="TOKEN_BOT_TELEGRAM_ANDA"

# ...dan seterusnya

PERINGATAN: File .env berisi data rahasia. Jangan pernah mengunggah file ini ke GitHub.

4. Cara Menjalankan
1. Buat file bernama domains.txt di folder utama proyek.
2. Isi file tersebut dengan daftar domain yang ingin diperiksa, satu domain per baris.

example.com
sub.example.net

3. Jalankan tools :
# Gunakan file domains.txt
python main.py

# Gunakan file kustom
python main.py daftar-target-lain.txt

4. Masukkan username dan password Anda saat diminta.

5. Notifikasi Telegram
Untuk menerima notifikasi, Anda harus didaftarkan oleh admin.

1. Chat bot tim di Telegram dan kirim pesan /start.
2. Dapatkan Chat ID Anda dari bot seperti @myidbot.
3. Berikan Chat ID tersebut kepada admin untuk ditambahkan ke database.

6. Struktur Folder
danguard-v3.1/
├── main.py              # Script utama untuk dijalankan
├── config.py            # Pengaturan kredensial
├── .env                 # File rahasia (buat sendiri)
├── domains.txt          # Daftar target (buat sendiri)
├── auth/                # Folder sistem login
├── scanner/             # Folder pemindai domain
├── claimers/            # Folder modul takeover
└── notifications/       # Folder notifikasi

Peringatan Keamanan
Tools ini hanya boleh digunakan pada aset yang Anda miliki atau untuk mana Anda memiliki izin tertulis. Penggunaan tanpa izin adalah ilegal. Anda bertanggung jawab penuh atas tindakan Anda.
```
