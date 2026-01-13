Danguard v3.1 - Subdomain Takeover Suite
A fast, automated tool for identifying and verifying subdomain takeover vulnerabilities.

Danguard adalah sebuah command-line suite yang dirancang khusus untuk red team dan security researcher. Tool ini mengotomasi proses scanning untuk menemukan dangling DNS dan memverifikasi kerentanan subdomain takeover di berbagai layanan cloud. Jika Anda bisa arahkan CNAME ke sana, Danguard bisa mengujinya.

🎯 Fitur Utama
Multi-Vector Scanning: Dukungan penuh untuk Azure, Vercel, AWS, dan penyedia lainnya.
Automated Verification: Tidak hanya menunjukkan kerentanan, tapi secara aktif mencoba claim untuk mendapatkan bukti definitif.
Real-Time Comms: Dapatkan notifikasi instan di Telegram tim Anda saat sebuah target berhasil dikompromikan.
Team-Based Ops: Sistem autentikasi bawaan memastikan hanya operator yang berwenang yang bisa menjalankan operasi.
Structured Reporting: Semua temuan diekspor ke JSON yang rapi untuk memudahkan parsing dan integrasi dengan tool lain.
⚠️ Operational Security & Rules of Engagement
Ini adalah alat yang kuat. Dengan kekuatan datang tanggung jawab.

Authorization Only: Danggan hanya untuk digunakan pada aset yang Anda miliki atau untuk Anda uji dengan izin tertulis. Scanning atau takeover tanpa izin adalah ilegal.
Handle with Care: Anda bertanggung jawab penuh atas cara Anda menggunakan alat ini. Tim pengembang tidak bertanggung jawab atas penyalahgunaan.
Protect Your Keys: Jangan pernah, dalam kondisi apa pun, meng-commit file .env Anda atau membagikan API key Anda. Jika Anda curiga key Anda dikompromikan, revoke segera.
🚀 Setup & Deployment
1. Prerequisites
Python 3.8+
Git
2. Deployment
Clone repositori dan masuk ke direktori proyek.

bash

git clone https://github.com/your-team/danguard-v3.1.git
cd danguard-v3.1
3. Environment
Kami menggunakan virtual environment untuk menjaga dependensi tetap bersih dan terisolasi.

bash

# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
4. Install Dependencies
Install semua package Python yang dibutuhkan dari file requirements.txt.

bash

pip install -r requirements.txt
⚙️ Konfigurasi
API key dan token operasional Anda dikelola melalui file .env.

Salin template contoh untuk membuat file konfigurasi lokal Anda.
bash

cp .env.example .env
Buka file .env yang baru dibuat dengan editor pilihan Anda.
Isi setiap variabel dengan credentials Anda.
ini

# Contoh untuk Vercel
VERCEL_API_KEY="your_vercel_api_key_goes_here"

# ... dan seterusnya untuk semua penyedia lainnya
KRITIS: File .env berisi informasi sensitif. File ini ada di .gitignore dengan alasan. Jangan pernah meng-commit file ini ke repositori.

🏃 Menjalankan Operasi
1. Siapkan Target
Buat file bernama domains.txt di direktori utama proyek. Daftarkan setiap domain yang ingin Anda scan di baris baru.


example.com
sub.target.net
another-domain.org
2. Eksekusi
Jalankan script utama. Anda akan diminta kredensial operator.

bash

# Jalankan dengan daftar target default (domains.txt)
python main.py

# Jalankan dengan daftar target kustom
python main.py custom_targets.txt
Tool akan melakukan autentikasi, memindai setiap target, mencoba melakukan takeover, dan melaporkan statusnya secara real-time.

📢 Telegram Notifications
Untuk menerima notifikasi real-time, Anda perlu mendaftarkan Chat ID Anda ke team lead.

Temukan bot tim kami di Telegram dan kirim pesan /start.
Dapatkan Chat ID Anda dengan mengirim pesan ke bot seperti @myidbot atau yang sejenisnya.
Kirim Chat ID Anda ke team lead untuk ditambahkan ke database operator.
Setelah terdaftar, Anda akan mendapatkan notifikasi saat sebuah target berhasil diambil alih.

📊 Output
Danguard menyediakan dua bentuk output:

Console Log: Pembaruan status real-time untuk setiap target saat diproses.
JSON Report: Setelah selesai, laporan detail (misal: takeover_report_domains.txt.json) akan dihasilkan. File ini berisi status setiap target, termasuk takeover yang berhasil, percobaan yang gagal, dan alasan kegagalan.


