![image](https://berita-terkini.id/images/danguard-V3.1.png)

DANGUARD V3.1 - PANDUAN INSTALASI & PENGGUNAAN

Tools untuk mendeteksi dan verifikasi kerentanan Subdomain Takeover.

============================================================

1. PERSIAPAN

Pastikan komputer Anda sudah terinstall:
- Python 3.8 atau lebih baru
- Git

============================================================

2. INSTALASI

Buka terminal atau command prompt, lalu jalankan perintah berikut:

1. Clone repositori ini
   git clone https://github.com/forbidden403-lt/danguard-v3.1.git
   
   cd danguard-v3.1

2. Buat dan aktifkan virtual environment
 
   python -m venv venv

   Untuk Windows:
   
   venv\Scripts\activate

   Untuk macOS/Linux:
   
   source venv/bin/activate

3. Install semua library yang dibutuhkan

   pip install -r requirements.txt

============================================================

3. KONFIGURASI

Semua API key dan token disimpan di file .env.

1. Buat file .env dari file contoh:
   cp .env.example .env

2. Buka file .env dengan teks editor, lalu isi dengan kredensial Anda:

   # Vercel
   VERCEL_API_KEY="API_KEY_VERCEL_ANDA"
   
   # Azure
   AZURE_CLIENT_ID="ID_APLIKASI_AZURE_ANDA"
   AZURE_TENANT_ID="ID_DIREKTORI_AZURE_ANDA"
   AZURE_CLIENT_SECRET="SECRET_AZURE_ANDA"
   AZURE_SUBSCRIPTION_ID="ID_SUBSCRIPTION_AZURE_ANDA"
   
   ...dan seterusnya

PERINGATAN: File .env berisi data rahasia. Jangan pernah mengunggah file ini ke GitHub.

============================================================

4. CARA MENJALANKAN

1. Buat file bernama domains.txt di folder utama proyek.
2. Isi file tersebut dengan daftar domain yang ingin diperiksa, satu domain per baris.
   example.com
   sub.example.net
3. Jalankan tools:
   # Gunakan file domains.txt
   python main.py

   # Gunakan file kustom
   python main.py daftar-target-lain.txt
4. Masukkan username dan password Anda saat diminta.

============================================================

5. NOTIFIKASI TELEGRAM

Untuk menerima notifikasi, Anda harus didaftarkan oleh admin.

1. Chat bot tim di Telegram dan kirim pesan /start.
2. Dapatkan Chat ID Anda dari bot seperti @myidbot.
3. Berikan Chat ID tersebut kepada admin untuk ditambahkan ke database.

============================================================

6. STRUKTUR FOLDER

danguard-v3.1/
├── main.py
├── config.py
├── .env
├── domains.txt
├── auth/
│   ├── __init__.py
│   └── auth_manager.py
├── scanner/
│   ├── __init__.py
│   ├── dns_check.py
│   ├── vendor_fingerprint.py
│   └── analyzer.py
├── claimers/
│   ├── __init__.py
│   ├── base_claimer.py
│   └── vercel_claimer.py
└── notifications/
    ├── __init__.py
    └── telegram_notifier.py

============================================================

7. PERINGATAN KEAMANAN

Tools ini hanya boleh digunakan pada aset yang Anda miliki atau untuk mana Anda memiliki izin tertulis. Penggunaan tanpa izin adalah ilegal. Anda bertanggung jawab penuh atas tindakan Anda.
