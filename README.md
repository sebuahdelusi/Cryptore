------



👥 Tim Pengembang



**Universitas Pembangunan Nasional "Veteran" Yogyakarta (UPNYK)**  **Universitas Pembangunan Nasional "Veteran" Yogyakarta (UPNYK)**  

**Mata Kuliah:** Kriptografi - Semester 5**Mata Kuliah:** Kriptografi - Semester 5



- **Gorbi Ello Pasaribu** - 123230083 - IF-H- **Gorbi Ello Pasaribu** - 123230083 - IF-H

- **Athallah Joyoningrat** - 123230230 - IF-H- **Athallah Joyoningrat** - 123230230 - IF-H



------



# Cryptore - Secure Cryptographic E-commerce Application# Cryptore - Secure Cryptographic E-commerce Application



> **📥 Download aplikasi:** [Releases](https://github.com/sebuahdelusi/Cryptore/releases)> **📥 Ingin langsung download aplikasi?** Kunjungi halaman **[Releases](https://github.com/sebuahdelusi/Cryptore/releases)** untuk download executable siap pakai.  

> Dokumentasi lengkap ada di bawah.

Aplikasi e-commerce yang mengimplementasikan berbagai teknik kriptografi untuk keamanan pesan, enkripsi file, dan steganografi.

**Cryptore** adalah aplikasi e-commerce yang mengimplementasikan berbagai teknik kriptografi untuk keamanan pesan, enkripsi file, dan steganografi. Dibangun dengan Python dan Tkinter, aplikasi ini menyediakan antarmuka yang user-friendly dengan fitur keamanan yang robust.

## 📖 Daftar Isi

- [Teknologi Kriptografi](#-teknologi-kriptografi)## 📖 Daftar Isi

- [Fitur Utama](#-fitur-utama)- [Tentang Cryptore](#-tentang-cryptore)

- [Instalasi & Penggunaan](#-instalasi--penggunaan)- [Teknologi Kriptografi](#-teknologi-kriptografi-yang-digunakan)

- [Fitur Tersembunyi](#-fitur-tersembunyi-easter-eggs)- [Fitur Lengkap](#-fitur-lengkap)

- [Struktur Proyek](#-struktur-proyek)- [Persyaratan Sistem](#-persyaratan-sistem)

- [Keamanan](#-keamanan)- [Instalasi](#-instalasi)

- [Cara Menggunakan](#-cara-menggunakan)

## 🔐 Teknologi Kriptografi- [Fitur Tersembunyi (Easter Eggs)](#-fitur-tersembunyi-easter-eggs)

- [Struktur Proyek](#-struktur-proyek)

### 1. Hill Cipher (Klasik)- [Build Executable](#-build-executable-exe)

- Cipher substitusi poligrafik berbasis aljabar linear matriks 3x3- [Catatan Keamanan](#-catatan-keamanan)

- Digunakan sebagai lapisan pertama super encryption

- Resistant terhadap frequency analysis## 🔐 Tentang Cryptore



### 2. Blowfish (Modern)Cryptore adalah aplikasi keamanan komprehensif yang menggabungkan berbagai algoritma kriptografi klasik dan modern untuk melindungi data pengguna. Aplikasi ini dikembangkan sebagai studi kasus implementasi kriptografi dalam skenario e-commerce yang aman.

- Symmetric-key block cipher (64-bit block, 32-448 bit key)

- Mode CBC dengan 16 putaran Feistel network## � Teknologi Kriptografi yang Digunakan

- Lapisan kedua super encryption untuk keamanan maksimal

### 1. **Hill Cipher (Kriptografi Klasik)**

### 3. RSA 2048-bit (Asimetris)**Lokasi Implementasi:** `modules/crypto_super_encrypt.py`

- Public-key cryptography dengan OAEP padding

- Enkripsi/dekripsi file dengan key pair (public + private)**Deskripsi:**

- Implementasi: `assets/keys/*.pem`- Algoritma cipher klasik berbasis aljabar linear

- Menggunakan matriks kunci untuk enkripsi/dekripsi

### 4. LSB Steganography- Merupakan cipher substitusi poligrafik yang beroperasi pada blok plaintext

- Sembunyikan pesan dalam gambar (PNG/JPG/BMP)

- Least Significant Bit replacement pada pixel RGB**Cara Kerja:**

- Tidak terlihat mata manusia, dapat dikombinasi dengan enkripsi1. Plaintext dikonversi menjadi vektor numerik (A=0, B=1, ..., Z=25)

2. Vektor dikalikan dengan matriks kunci menggunakan modulo 26

### 5. Super Encryption (Hybrid)3. Hasil perkalian dikonversi kembali menjadi ciphertext

- Kombinasi Hill Cipher + Blowfish secara cascade

- Defense in depth: dua lapisan algoritma independen**Implementasi di Cryptore:**

- Digunakan untuk chat terenkripsi dan reviews- Digunakan sebagai lapisan enkripsi pertama pada sistem chat terenkripsi

- Matriks kunci dibangkitkan dari verification code yang dimasukkan user

### 6. Password Hashing- Ukuran matriks: 3x3 untuk blok plaintext 3 karakter

- SHA-256 dengan salt unik per user

- Mencegah rainbow table attacks**Kelebihan:**

- Password tidak pernah disimpan plaintext- Resistant terhadap frequency analysis sederhana

- Enkripsi blok meningkatkan keamanan

### 7. Windows Hello Biometric

- Integrasi API Windows Hello (PIN/Fingerprint/Face)**Kelemahan:**

- Credential storage via Windows Credential Manager- Vulnerable terhadap known-plaintext attack

- Biometric data dikelola sistem, bukan aplikasi- Memerlukan matriks yang invertible



## 🚀 Fitur Utama### 2. **Blowfish (Kriptografi Modern)**

**Lokasi Implementasi:** `modules/crypto_super_encrypt.py`

### 🔑 Autentikasi

- **Login/Register** dengan password hashing (SHA-256 + salt)**Deskripsi:**

- **Windows Hello** untuk login biometric (PIN/Face/Fingerprint)- Symmetric-key block cipher yang dikembangkan oleh Bruce Schneier

- Data user tersimpan aman di `data/users.json`- Ukuran blok: 64-bit

- Panjang kunci: variable (32-448 bits)

### 💬 Chat Terenkripsi- Menggunakan struktur Feistel network dengan 16 putaran

- **Super Encryption** (Hill Cipher + Blowfish) untuk end-to-end encryption

- **Chat Penjual** tanpa enkripsi untuk komunikasi biasa**Cara Kerja:**

- WhatsApp-style UI dengan bubble messages dan timestamp1. Key expansion: Kunci user diperluas menjadi subkeys (18 P-array + 4 S-boxes)

- Verification code (3 digit) + password sebagai kunci enkripsi2. Data encryption: Plaintext dienkripsi melalui 16 putaran Feistel

3. Setiap putaran menggunakan XOR dan substitusi melalui S-boxes

### 📁 File Encryption (RSA)

- Enkripsi/dekripsi file apapun (dokumen, gambar, video)**Implementasi di Cryptore:**

- RSA 2048-bit dengan OAEP padding- Digunakan sebagai lapisan enkripsi kedua (super encryption)

- Output format: `.enc`- Mode operasi: CBC (Cipher Block Chaining) untuk keamanan tambahan

- Kunci dihasilkan dari password chat yang dimasukkan user

### 🖼️ Steganografi

- **Sembunyikan** pesan dalam gambar (LSB method)**Kelebihan:**

- **Ekstrak** pesan tersembunyi dari gambar- Sangat cepat dan efisien

- Support: PNG, JPG, JPEG, BMP- Tidak ada kelemahan kriptografi yang ditemukan hingga saat ini

- Public domain (free untuk digunakan)

### ⭐ Review Terenkripsi

- Submit review produk dengan super encryption**Kelemahan:**

- Dekripsi dengan verification code + password yang sama- Ukuran blok 64-bit dianggap kecil untuk standar modern

- Vulnerable terhadap birthday attack pada data besar

### 🎨 Light/Dark Mode

- Toggle tema dari menu profil### 3. **RSA (Rivest-Shamir-Adleman)**

- Preferensi tersimpan otomatis**Lokasi Implementasi:** `modules/crypto_rsa_file.py`, `generate_keys.py`

- Semua UI ter-theme (backgrounds, buttons, inputs)

**Deskripsi:**

### 🛍️ Katalog Produk- Algoritma kriptografi asimetris (public-key cryptography)

- Grid display produk dengan gambar dan detail- Berbasis pada kesulitan faktorial bilangan prima besar

- Tombol chat (normal/encrypted) terintegrasi- Ukuran kunci: 2048-bit (default dalam Cryptore)



## 🛠️ Instalasi & Penggunaan**Cara Kerja:**

1. **Key Generation:**

### Metode 1: Executable (Recommended)   - Pilih dua bilangan prima besar p dan q

1. Download `Cryptore.exe` dari [Releases](https://github.com/sebuahdelusi/Cryptore/releases)   - Hitung n = p × q (modulus)

2. Jalankan langsung (tidak perlu instalasi)   - Hitung φ(n) = (p-1)(q-1)

3. Register akun → Login → Gunakan fitur   - Pilih e (public exponent) yang coprime dengan φ(n)

   - Hitung d (private exponent) dimana d × e ≡ 1 (mod φ(n))

### Metode 2: Source Code

```bash2. **Enkripsi:** C = M^e mod n (menggunakan public key)

# Clone repository3. **Dekripsi:** M = C^d mod n (menggunakan private key)

git clone https://github.com/sebuahdelusi/Cryptore.git

cd Cryptore**Implementasi di Cryptore:**

- Digunakan untuk enkripsi/dekripsi file

# Install dependencies- Public key: `assets/keys/public_key.pem`

pip install -r requirements.txt- Private key: `assets/keys/private_key.pem`

- Padding: OAEP (Optimal Asymmetric Encryption Padding) untuk keamanan

# Generate RSA keys (pertama kali)

python generate_keys.py**Kelebihan:**

- Tidak perlu pertukaran kunci rahasia

# Jalankan aplikasi- Mendukung digital signature

python main.py- Widely adopted dan well-tested

```

**Kelemahan:**

### Persyaratan Sistem- Sangat lambat untuk data besar

- **OS:** Windows 10/11 (64-bit)- Memerlukan manajemen kunci yang kompleks

- **RAM:** 4 GB minimum

- **Storage:** 500 MB### 4. **Steganografi LSB (Least Significant Bit)**

- **Python:** 3.8+ (untuk development)**Lokasi Implementasi:** `modules/crypto_steganography.py`



### Quick Start Guide**Deskripsi:**

- Teknik menyembunyikan data dalam media digital (image)

**1. Register & Login**- Menggunakan metode LSB replacement pada pixel image

- Klik "Register" → Masukkan username & password- Tidak terlihat oleh mata manusia karena perubahan minimal

- Login dengan kredensial atau aktifkan Windows Hello dari menu profil

**Cara Kerja:**

**2. Chat Terenkripsi**1. **Embedding (Menyembunyikan Pesan):**

- Pilih produk → "💬🔒 Chat Terenkripsi"   - Konversi pesan menjadi binary string

- Pilih user → Ketik pesan → Klik "Kirim"   - Tambahkan delimiter "####END####" untuk menandai akhir pesan

- Masukkan Verification Code (3 digit) + Password   - Ganti bit terakhir (LSB) dari setiap byte pixel dengan bit pesan

- **Penting:** Bagikan code via jalur terpisah (WhatsApp/telepon)   - Proses dilakukan pada channel RGB secara sequential

- Klik pesan 🔒 untuk dekripsi dengan code yang sama

2. **Extraction (Mengekstrak Pesan):**

**3. Enkripsi File**   - Ambil LSB dari setiap byte pixel

- Menu "🔐 Enkripsi Dokumen"   - Gabungkan bits menjadi string

- **Enkripsi:** Pilih file → "Amankan Dokumen" → Save sebagai `.enc`   - Baca hingga menemukan delimiter

- **Dekripsi:** Pilih file `.enc` → "Pulihkan Dokumen" → Restore original   - Konversi binary kembali menjadi text



**4. Steganografi****Implementasi di Cryptore:**

- Menu "🖼️ Sembunyikan Metadata"- Mendukung format: PNG, JPG, JPEG, BMP

- **Sembunyikan:** Pilih gambar → Ketik pesan → "Simpan Gambar" (PNG)- Output format: PNG (untuk preservasi data)

- **Ekstrak:** Pilih gambar stego → "Ekstrak Metadata"- Kapasitas: Tergantung ukuran gambar (1 byte pesan per 3 pixels RGB)



**5. Review Terenkripsi****Kelebihan:**

- Menu "⭐ Kirim Ulasan" → Pilih produk → Tulis review- Sederhana dan mudah diimplementasikan

- Masukkan Verification Code + Password → "Kirim Ulasan"- Perubahan tidak terdeteksi visual

- Lihat review: "👁️ Lihat Ulasan" → Masukkan code yang sama- Dapat dikombinasikan dengan enkripsi



## 🎯 Fitur Tersembunyi (Easter Eggs)**Kelemahan:**

- Vulnerable terhadap steganalysis

Akses dengan **Shift + Click**:- Mudah rusak jika gambar di-compress atau di-resize

- Kapasitas terbatas

| Lokasi | Shortcut | Fungsi |

|--------|----------|--------|### 5. **Super Encryption (Hybrid Approach)**

| Product Card → "Lihat Detail" | **Shift + Click** | Debug Crypto Panel (log enkripsi real-time) |**Lokasi Implementasi:** `modules/crypto_super_encrypt.py`

| Detail Produk → "💬 Chat Penjual" | **Shift + Click** | Encrypted Chat Mode (end-to-end encryption) |

| Halaman Steganografi → Label "Cryptore" | **Shift + Click** | Easter Egg Image (surprise!) |**Deskripsi:**

Cryptore mengimplementasikan "super encryption" dengan menggabungkan Hill Cipher dan Blowfish secara cascade untuk mencapai keamanan berlapis.

**Tips:** Tahan Shift terlebih dahulu, baru klik. Tidak ada indikator visual.

**Proses Enkripsi:**

## 📁 Struktur Proyek```

Plaintext → Hill Cipher → Intermediate Ciphertext → Blowfish → Final Ciphertext

``````

Cryptore/

├── main.py                      # Entry point & window manager**Proses Dekripsi:**

├── generate_keys.py             # RSA key generator```

├── build_exe.py                 # PyInstaller build scriptFinal Ciphertext → Blowfish → Intermediate Ciphertext → Hill Cipher → Plaintext

├── requirements.txt             # Dependencies```

│

├── assets/**Keuntungan Hybrid:**

│   ├── images/                  # Product images & UI assets- Defense in depth: Jika satu algoritma berhasil dipecahkan, lapisan lain masih melindungi

│   └── keys/                    # RSA key pair (public_key.pem, private_key.pem)- Hill Cipher menyulitkan pattern analysis

│- Blowfish memberikan enkripsi modern yang kuat

├── data/                        # JSON storage- Kombinasi kunci independen (verification code + password)

│   ├── users.json               # User database (hashed passwords)

│   ├── chats.json               # Encrypted chat messages### 6. **Password Hashing dengan Salt**

│   ├── reviews.json             # Encrypted product reviews**Lokasi Implementasi:** `modules/crypto_login.py`

│   └── theme.json               # Theme preferences

│**Deskripsi:**

├── modules/                     # Crypto logic- Menggunakan SHA-256 untuk hashing password

│   ├── crypto_login.py          # Authentication & hashing- Salt unik untuk setiap user mencegah rainbow table attacks

│   ├── crypto_super_encrypt.py  # Hill Cipher + Blowfish- Password tidak pernah disimpan dalam plaintext

│   ├── crypto_chat.py           # Chat encryption

│   ├── crypto_rsa_file.py       # RSA file encryption**Cara Kerja:**

│   ├── crypto_steganography.py  # LSB steganography1. User registrasi: Salt random dibangkitkan → Hash = SHA256(password + salt)

│   ├── crypto_biometric.py      # Windows Hello integration2. Verifikasi login: Hash ulang password input dengan salt tersimpan → Bandingkan hash

│   └── crypto_debug.py          # Debug utilities

│### 7. **Windows Hello Biometric Authentication**

└── ui/                          # User interface**Lokasi Implementasi:** `modules/crypto_biometric.py`

    ├── ui_auth_pages.py         # Login & Register

    ├── ui_main_pages.py         # Home & Products**Deskripsi:**

    ├── ui_chat_page.py          # Chat interface- Integrasi dengan Windows Hello API

    ├── ui_crypto_pages.py       # Crypto features- Mendukung: PIN, Fingerprint, Face Recognition

    └── ui_components.py         # Reusable components- Menggunakan Windows Credential Manager untuk storage

```

**Keamanan:**

## 🔒 Keamanan- Biometric data tidak disimpan dalam aplikasi

- Managed oleh Windows Security

### Best Practices- Per-user configuration dengan keyring

✅ **Passwords:** Minimal 12 karakter, kombinasi huruf/angka/simbol  

✅ **Private Key:** Backup ke storage offline, jangan commit ke Git  ## 🚀 Fitur Lengkap

✅ **Verification Code:** Komunikasikan via jalur terpisah (jangan di chat)  

✅ **File Backup:** Simpan original sebelum enkripsi  ### 1. 🔑 Sistem Autentikasi Aman

✅ **Windows Hello:** Aktifkan untuk two-factor authentication  **File:** `ui/ui_auth_pages.py`, `modules/crypto_login.py`



### Limitasi**Fitur:**

⚠️ **Local Storage:** Data tersimpan lokal (encrypt hard drive dengan BitLocker)  - **Login Tradisional:**

⚠️ **No Key Rotation:** RSA keys static (generate ulang manual secara berkala)    - Username dan password

⚠️ **No Remote Wipe:** Tidak ada remote delete jika device hilang    - Password hashing dengan SHA-256 + salt

  - Validasi real-time

### PENTING: Private Key  

❌ JANGAN: Commit ke Git, share via email/cloud, simpan di lokasi tidak aman  - **Windows Hello Login:**

✅ WAJIB: Backup offline, simpan terenkripsi, generate ulang jika exposed    - Autentikasi biometrik (PIN/Fingerprint/Face)

  - Per-user configuration

## 🔨 Build Executable  - Secure credential storage dengan keyring

  - Visual feedback saat menunggu autentikasi

```bash

# Install PyInstaller- **Registrasi User:**

pip install pyinstaller  - Validasi username unik

  - Password strength requirement

# Build  - Automatic salt generation

python build_exe.py  - Secure storage dalam `data/users.json`



# Output: dist/Cryptore.exe (~35 MB)**Cara Menggunakan:**

```1. Pertama kali: Klik "Register" untuk membuat akun baru

2. Login dengan username dan password

**Distribusi:** Bundle `Cryptore.exe` + folder `assets/` (HANYA public_key.pem, BUKAN private_key.pem!)3. Opsional: Aktifkan Windows Hello dari menu profil setelah login

4. Selanjutnya: Gunakan tombol "🔐 Windows Hello" untuk login cepat

## 📄 Lisensi & Disclaimer

### 2. 🎨 Light/Dark Mode Theme

**Academic Use Only** - Project untuk keperluan akademik mata kuliah Kriptografi.**File:** `main.py`, `data/theme.json`



⚠️ **Disclaimer:** Dibuat untuk tujuan edukasi. Tidak untuk production use tanpa security audit. Penulis tidak bertanggung jawab atas kerugian data atau security breach.**Fitur:**

- Toggle theme dari menu profil

🎓 **Academic Integrity:** Hasil karya original untuk tugas kuliah. Plagiarisme melanggar kode etik akademik.- Tema tersimpan otomatis (persistent)

- Semua elemen UI ter-theme:

## 📞 Contact  - Backgrounds (header, content, chat, products)

  - Buttons (normal, hover, active states)

- **Repository:** [github.com/sebuahdelusi/Cryptore](https://github.com/sebuahdelusi/Cryptore)  - Input fields (entries, text boxes)

- **Issues:** [Report bugs](https://github.com/sebuahdelusi/Cryptore/issues)  - Chat bubbles (own messages, received messages)

  - Scrollbars dan borders

---

**Warna:**

*Version: 2.0 | Last Updated: 2024*- **Light Mode:** 

  - Primary: #0078D4 (Microsoft Blue)
  - Secondary: #F3F3F3 (Light Gray)
  - Text: #222222 (Dark Gray)
  
- **Dark Mode:**
  - Primary: #4A9EFF (Light Blue)
  - Secondary: #1E1E1E (Dark Gray)
  - Text: #E0E0E0 (Light Gray)

**Cara Menggunakan:**
1. Login ke aplikasi
2. Klik nama profil di kanan atas
3. Pilih "☀️ Light Mode" atau "🌙 Dark Mode"
4. Tema langsung berubah dan tersimpan

### 3. 💬 Sistem Chat Terenkripsi
**File:** `ui/ui_chat_page.py`, `modules/crypto_chat.py`, `modules/crypto_super_encrypt.py`

**Fitur:**
- **Chat Terenkripsi (Super Encryption):**
  - Enkripsi berlapis: Hill Cipher + Blowfish
  - End-to-end encryption
  - Setiap pesan dapat didekripsi independen
  - Indikator enkripsi (🔒/🔓)
  
- **Chat Penjual Produk:**
  - Chat langsung dengan penjual
  - Terintegrasi dengan halaman detail produk
  - History chat tersimpan per produk

- **UI/UX:**
  - WhatsApp-style interface
  - Message bubbles berwarna (hijau: user, biru: lawan)
  - Timestamp pada setiap pesan
  - Mousewheel scrolling
  - Auto-refresh chat

**Algoritma Enkripsi Chat:**
```
1. Input: Plaintext, Verification Code, Password
2. Hill Cipher Encryption:
   - Generate matriks 3x3 dari verification code
   - Enkripsi plaintext → Ciphertext1
3. Blowfish Encryption:
   - Generate kunci dari password
   - Enkripsi Ciphertext1 → Ciphertext2 (final)
4. Store: Ciphertext2 di data/chats.json
```

**Cara Menggunakan:**
1. **Chat Terenkripsi:**
   - Pilih "Beranda" → Klik produk → "💬🔒 Chat Terenkripsi"
   - Atau dari menu kiri: Chat Terenkripsi
   - Pilih user lawan chat
   - Tulis pesan, klik "Kirim"
   - Masukkan Verification Code (3 digit) dan Password
   - Pesan terenkripsi dan terkirim

2. **Dekripsi Pesan:**
   - Klik pesan terenkripsi (bertanda 🔒)
   - Masukkan Verification Code dan Password yang SAMA dengan pengirim
   - Pesan terdekripsi dan muncul (🔓)

3. **Chat Penjual:**
   - Buka halaman detail produk
   - Klik "💬 Chat Penjual"
   - Chat langsung tanpa enkripsi
   - Untuk komunikasi sederhana dengan penjual

### 4. 📁 Enkripsi File (RSA)
**File:** `ui/ui_crypto_pages.py`, `modules/crypto_rsa_file.py`

**Fitur:**
- Enkripsi file dengan RSA 2048-bit
- Mendukung SEMUA tipe file (dokumen, gambar, video, dll)
- Public/Private key pair
- OAEP padding untuk keamanan
- File terenkripsi dengan ekstensi `.enc`

**Cara Kerja:**
1. **Key Generation:**
   - Jalankan `python generate_keys.py` (otomatis saat pertama kali)
   - Menghasilkan `public_key.pem` dan `private_key.pem` di `assets/keys/`

2. **Enkripsi:**
   - File dibaca → Encrypted dengan public key → Simpan sebagai .enc
   - File original tetap ada (tidak terhapus)

3. **Dekripsi:**
   - File .enc dibaca → Decrypted dengan private key → Restore file original

**Cara Menggunakan:**
1. **Enkripsi File:**
   - Menu kiri: "🔐 Enkripsi Dokumen"
   - Langkah 1: Klik "1. Pilih File untuk Dienkripsi"
   - Pilih file apapun dari komputer
   - Langkah 2: Klik "2. Amankan Dokumen"
   - Pilih lokasi penyimpanan untuk file .enc
   - File terenkripsi dan disimpan

2. **Dekripsi File:**
   - Klik tab "Dekripsi File"
   - Langkah 1: Klik "1. Pilih File .enc untuk Didekripsi"
   - Pilih file .enc yang sudah dienkripsi
   - Langkah 2: Klik "2. Pulihkan Dokumen"
   - Pilih lokasi untuk menyimpan file original
   - File terdekripsi dan tersimpan

**⚠️ Catatan Penting:**
- Backup `private_key.pem` dengan aman
- Jika private key hilang, file .enc TIDAK BISA didekripsi
- Jangan bagikan private key ke siapapun

### 5. 🖼️ Steganografi (Sembunyikan Pesan dalam Gambar)
**File:** `ui/ui_crypto_pages.py`, `modules/crypto_steganography.py`

**Fitur:**
- Sembunyikan teks dalam gambar (LSB Steganography)
- Format support: PNG, JPG, JPEG, BMP
- Output: PNG (lossless)
- Tidak terlihat oleh mata manusia
- Ekstraksi pesan dari gambar

**Cara Kerja Teknis:**
```
Embedding:
1. Konversi pesan → binary
2. Tambah delimiter "####END####"
3. Untuk setiap bit pesan:
   - Ambil pixel dari gambar
   - Ganti LSB pixel dengan bit pesan
4. Save modified image

Extraction:
1. Baca LSB dari setiap pixel
2. Gabungkan bits → string
3. Stop saat temukan delimiter
4. Konversi binary → text
```

**Cara Menggunakan:**
1. **Menyembunyikan Pesan:**
   - Menu kiri: "🖼️ Sembunyikan Metadata"
   - Tab: "Sembunyikan Metadata"
   - Langkah 1: Klik "1. Pilih Gambar Asli"
   - Pilih gambar cover (PNG/JPG)
   - Langkah 2: Ketik metadata/pesan di text box
   - Langkah 3: Klik "3. Simpan Gambar"
   - Pilih lokasi dan nama untuk gambar baru
   - Pesan tersembunyi dalam gambar!

2. **Mengekstrak Pesan:**
   - Tab: "Gerak Metadata"
   - Langkah 1: Klik "1. Pilih Gambar"
   - Pilih gambar yang mengandung pesan tersembunyi
   - Langkah 2: Klik "2. Ekstrak Metadata"
   - Pesan ter-extract dan ditampilkan di text box

**Contoh Penggunaan:**
- Sembunyikan password dalam foto profil
- Kirim pesan rahasia via gambar di social media
- Watermarking digital

### 6. ⭐ Sistem Review Produk (Terenkripsi)
**File:** `ui/ui_crypto_pages.py`, `modules/crypto_super_encrypt.py`

**Fitur:**
- Submit review terenkripsi untuk produk
- View reviews dengan dekripsi
- Enkripsi sama seperti chat (Hill + Blowfish)
- History review tersimpan

**Cara Menggunakan:**
1. **Kirim Review:**
   - Menu kiri: "⭐ Kirim Ulasan"
   - Pilih produk dari dropdown
   - Tulis ulasan di text box
   - Masukkan Verification Code dan Password
   - Klik "Kirim Ulasan"
   - Review terenkripsi dan tersimpan

2. **Lihat Review:**
   - Menu kiri: "👁️ Lihat Ulasan"
   - Klik "Lihat Ulasan Saya"
   - Masukkan Verification Code dan Password
   - Review terdekripsi dan ditampilkan

### 7. 🛍️ Katalog Produk
**File:** `ui/ui_main_pages.py`

**Fitur:**
- Grid display produk dengan gambar
- Halaman detail produk
- Informasi harga dan stok
- Tombol chat penjual
- Hover effects

**Cara Menggunakan:**
- Browse produk di halaman "Beranda"
- Klik "Lihat Detail" untuk info lengkap
- Klik "💬 Chat Penjual" untuk chat
- Klik "💬🔒 Chat Terenkripsi" untuk chat aman

## 📋 Persyaratan Sistem

### Hardware
- **Processor:** Intel Core i3 atau AMD equivalent (minimum)
- **RAM:** 4 GB (minimum), 8 GB (recommended)
- **Storage:** 500 MB free space
- **Display:** 1280x720 resolution (minimum)

### Software
- **Operating System:** Windows 10/11 (64-bit)
  - Windows Hello memerlukan hardware yang compatible (optional)
- **Python:** 3.8 atau lebih tinggi (untuk development)
- **Internet:** Untuk instalasi dependencies

### Dependencies Python
```
tkinter          # GUI framework (built-in dengan Python)
Pillow>=10.0.0   # Image processing untuk steganografi
cryptography>=41.0.0  # RSA dan Blowfish encryption
numpy>=1.24.0    # Matrix operations untuk Hill Cipher
keyring>=24.0.0  # Secure credential storage
winrt>=2.0.0     # Windows Hello API (Windows only)
```

## 🛠️ Instalasi

### Metode 1: Menggunakan Executable (Recommended untuk User)

1. **Download Executable:**
   ```bash
   # Clone repository
   git clone https://github.com/sebuahdelusi/Cryptore.git
   cd Cryptore
   ```

2. **Download dari Release:**
   - Buka halaman [Releases](https://github.com/sebuahdelusi/Cryptore/releases)
   - Download `Cryptore.exe` terbaru
   - Jalankan langsung tanpa instalasi

3. **Atau Build Sendiri:**
   ```bash
   # Install PyInstaller
   pip install pyinstaller
   
   # Build executable
   python build_exe.py
   
   # Executable akan ada di folder 'dist/'
   ```

### Metode 2: Instalasi dari Source Code (Untuk Development)

1. **Clone Repository:**
   ```bash
   git clone https://github.com/sebuahdelusi/Cryptore.git
   cd Cryptore
   ```

2. **Buat Virtual Environment (Recommended):**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   
   Atau install manual:
   ```bash
   pip install pillow cryptography numpy keyring winrt
   ```

4. **Generate RSA Keys (Pertama Kali):**
   ```bash
   python generate_keys.py
   ```
   
   Ini akan membuat:
   - `assets/keys/public_key.pem`
   - `assets/keys/private_key.pem`

5. **Jalankan Aplikasi:**
   ```bash
   python main.py
   ```

### Troubleshooting Instalasi

**Error: No module named 'tkinter'**
```bash
# Windows
pip install tk

# Linux (Ubuntu/Debian)
sudo apt-get install python3-tk

# macOS
brew install python-tk
```

**Error: winrt module not found**
```bash
# Install winrt untuk Windows Hello
pip install winrt
```

**Error: Failed to create RSA keys**
```bash
# Pastikan folder assets/keys/ ada
mkdir -p assets/keys

# Generate ulang keys
python generate_keys.py
```

## � Cara Menggunakan (Panduan Lengkap)

### Pertama Kali Menggunakan

1. **Launch Aplikasi:**
   - Double-click `Cryptore.exe` atau
   - Run `python main.py`

2. **Register Akun Baru:**
   - Klik tombol "Register" di halaman login
   - Masukkan username (unik)
   - Masukkan password (minimal 6 karakter)
   - Klik "Register"
   - Akun berhasil dibuat!

3. **Login:**
   - Masukkan username dan password
   - Klik "Login"
   - Anda masuk ke halaman utama

### Setup Windows Hello (Optional tapi Recommended)

1. **Pastikan Windows Hello tersedia:**
   - Buka Settings → Accounts → Sign-in options
   - Setup PIN/Fingerprint/Face recognition di Windows

2. **Aktifkan di Cryptore:**
   - Login dengan password
   - Klik nama profil (kanan atas)
   - Pilih "🔐 Aktifkan Windows Hello"
   - Ikuti prompt autentikasi Windows Hello
   - Setelah berhasil, Windows Hello aktif untuk akun Anda

3. **Login dengan Windows Hello:**
   - Di halaman login, pilih username dari dropdown
   - Klik tombol "🔐 Windows Hello"
   - Autentikasi dengan PIN/Fingerprint/Face
   - Login otomatis tanpa password!

### Menggunakan Chat Terenkripsi

**Scenario 1: Chat dengan User Lain**

1. Buka menu "💬🔒 Chat Terenkripsi"
2. Pilih user tujuan dari dropdown "Chat dengan:"
3. Ketik pesan di kotak input
4. Klik "Kirim"
5. **Popup akan muncul:**
   - Verification Code: Masukkan 3 digit angka (contoh: 123)
   - Password Chat: Masukkan password (contoh: rahasia123)
   - Ingat: **Beritahu kode ini ke lawan chat via jalur lain (WhatsApp, telepon, dll)**
6. Pesan terenkripsi dan terkirim!

**Membaca Pesan Terenkripsi:**
1. Pesan masuk tampil dengan ikon 🔒
2. Klik pada pesan tersebut
3. Masukkan Verification Code dan Password yang SAMA
4. Pesan terdekripsi dan tampil (ikon berubah 🔓)

**Tips:**
- Verification Code + Password = kunci enkripsi
- Harus dikomunikasikan secara aman ke lawan chat
- Setiap pesan bisa pakai kode berbeda
- Jika lupa kode, pesan tidak bisa didekripsi (by design)

### Mengenkripsi File

**Enkripsi Dokumen Penting:**

1. Menu kiri: "🔐 Enkripsi Dokumen"
2. Tab "Enkripsi File"
3. **Langkah 1:** Klik "1. Pilih File untuk Dienkripsi"
   - Contoh: Pilih file `rahasia.pdf`
4. **Langkah 2:** Klik "2. Amankan Dokumen"
   - Pilih lokasi save (contoh: `Desktop/rahasia.pdf.enc`)
5. File terenkripsi! File original tetap ada.

**Dekripsi File:**

1. Tab "Dekripsi File"
2. **Langkah 1:** Klik "1. Pilih File .enc untuk Didekripsi"
   - Pilih file `rahasia.pdf.enc`
3. **Langkah 2:** Klik "2. Pulihkan Dokumen"
   - Pilih lokasi save (contoh: `Desktop/rahasia_restored.pdf`)
4. File terdekripsi dan kembali normal!

**Use Cases:**
- Enkripsi file sebelum upload ke cloud
- Proteksi dokumen rahasia di laptop
- Backup encrypted untuk data sensitif

### Steganografi - Sembunyikan Pesan

**Menyembunyikan Pesan:**

1. Menu kiri: "🖼️ Sembunyikan Metadata"
2. Tab "Sembunyikan Metadata"
3. **Langkah 1:** Klik "1. Pilih Gambar Asli"
   - Contoh: Pilih foto `vacation.jpg`
4. **Langkah 2:** Ketik pesan rahasia
   - Contoh: "Password vault: MySecret123!"
5. **Langkah 3:** Klik "3. Simpan Gambar"
   - Save sebagai `vacation_steg.png`
6. Gambar terlihat sama, tapi berisi pesan tersembunyi!

**Mengekstrak Pesan:**

1. Tab "Gerak Metadata"
2. **Langkah 1:** Klik "1. Pilih Gambar"
   - Pilih `vacation_steg.png`
3. **Langkah 2:** Klik "2. Ekstrak Metadata"
4. Pesan rahasia muncul di text box!

**Use Cases:**
- Sembunyikan password recovery hints
- Kirim pesan rahasia via foto social media
- Digital watermarking
- Steganography challenge/CTF

### Review Produk Terenkripsi

**Kirim Review:**

1. Menu: "⭐ Kirim Ulasan"
2. Pilih produk dari dropdown
3. Tulis review (contoh: "Produk bagus, fast delivery!")
4. Masukkan Verification Code: 456
5. Masukkan Password: review2024
6. Klik "Kirim Ulasan"

**Lihat Review:**

1. Menu: "👁️ Lihat Ulasan"
2. Klik "Lihat Ulasan Saya"
3. Masukkan Code: 456, Password: review2024
4. Semua review Anda terdekripsi dan tampil

### Switch Theme (Light/Dark Mode)

1. Klik nama profil (kanan atas)
2. Pilih "🌙 Dark Mode" atau "☀️ Light Mode"
3. Tema langsung berubah
4. Preferensi tersimpan otomatis

## 🎯 Fitur Tersembunyi (Easter Eggs)

Cryptore memiliki beberapa fitur tersembunyi yang hanya bisa diakses dengan kombinasi tombol khusus!

### 🔑 Cara Akses Fitur Tersembunyi

**1. Debug Kriptografi (Shift + Click)**

**Lokasi:** Halaman Utama → Klik Product Card
- **Cara Akses:** Tahan tombol **Shift** + Klik pada tombol "Lihat Detail" produk
- **Fungsi:** Membuka panel debug yang menampilkan:
  - Log operasi kriptografi terkini
  - Detail enkripsi/dekripsi yang dilakukan
  - Hash plaintext dan ciphertext
  - Timestamp setiap operasi crypto
- **Untuk Apa:** Berguna untuk troubleshooting atau memahami proses enkripsi yang terjadi di balik layar

**Contoh Penggunaan:**
```
1. Login ke aplikasi
2. Buka halaman "🏪 Belanja"
3. Tahan tombol Shift
4. Sambil menahan Shift, klik "Lihat Detail" pada produk mana saja
5. Panel debug akan muncul menampilkan aktivitas kriptografi
```

**2. Chat Terenkripsi User-to-User (Shift + Click)**

**Lokasi:** Detail Produk → Tombol "Chat Penjual"
- **Cara Akses:** Tahan tombol **Shift** + Klik pada tombol "💬 Chat Penjual"
- **Fungsi:** Membuka **Encrypted Chat** (end-to-end encryption) alih-alih chat biasa
- **Perbedaan:**
  - **Chat Biasa:** Pesan tersimpan dalam bentuk plaintext
  - **Encrypted Chat:** Pesan dienkripsi dengan Hill Cipher + Blowfish (Super Encryption)
- **Untuk Apa:** Komunikasi yang benar-benar aman untuk transaksi sensitif

**Contoh Penggunaan:**
```
1. Buka detail produk
2. Tahan tombol Shift
3. Sambil menahan Shift, klik "💬 Chat Penjual"
4. Masukkan Verification Code (3 digit) dan Password
5. Kirim pesan terenkripsi yang hanya bisa dibaca dengan kode yang sama
```

**3. Easter Egg Image (Shift + Click)**

**Lokasi:** Halaman Steganografi → Label "Cryptore"
- **Cara Akses:** Tahan tombol **Shift** + Klik pada label "Cryptore" di halaman Steganografi
- **Fungsi:** Menampilkan gambar easter egg tersembunyi (ualmelet.png)
- **Untuk Apa:** Fun feature, apresiasi untuk users yang eksplorasi aplikasi dengan teliti!

**Contoh Penggunaan:**
```
1. Buka menu "🖼️ Sembunyikan Metadata"
2. Tahan tombol Shift
3. Sambil menahan Shift, klik pada label "Cryptore" di bagian header
4. Gambar easter egg akan muncul sebagai surprise!
```

### 💡 Tips Menggunakan Shift + Click

- **Tahan Shift terlebih dahulu**, baru klik (jangan dibalik)
- Fitur ini bekerja pada **klik kiri** (left mouse button)
- Tidak ada indikator visual bahwa fitur tersembunyi ada, jadi explore!
- Shift + Click adalah **shortcut power user** untuk fitur advanced

### 🎮 Kombinasi Keyboard Lainnya

| Kombinasi | Fungsi | Lokasi |
|-----------|---------|--------|
| **Shift + Click** (Lihat Detail) | Debug Crypto Panel | Halaman Belanja |
| **Shift + Click** (Chat Penjual) | Encrypted Chat Mode | Detail Produk |
| **Shift + Click** (Label Cryptore) | Easter Egg Image | Halaman Steganografi |
| **Enter** | Kirim Pesan | Chat Interface |
| **Escape** | Tutup Zoom | Product Image Zoom |

## 📁 Struktur Proyek

```
Cryptore/
│
├── main.py                      # Entry point aplikasi & window manager
│
├── generate_keys.py             # Script generator RSA key pair
│
├── build_exe.py                 # Script build executable dengan PyInstaller
│
├── requirements.txt             # Python dependencies
│
├── README.md                    # Dokumentasi lengkap (file ini)
│
├── assets/                      # Asset gambar dan keys
│   ├── images/                  # Gambar produk dan UI
│   │   ├── product1.jpg         # Sample gambar produk
│   │   ├── product2.jpg
│   │   └── ualmelet.png         # Easter egg image
│   │
│   └── keys/                    # RSA key pair (JANGAN COMMIT KE GIT!)
│       ├── public_key.pem       # Public key untuk enkripsi
│       └── private_key.pem      # Private key untuk dekripsi (RAHASIA!)
│
├── data/                        # Data storage JSON files
│   ├── users.json               # Database user (username & hashed password)
│   ├── chats.json               # Chat history terenkripsi
│   ├── reviews.json             # Product reviews terenkripsi
│   ├── theme.json               # User theme preferences
│   └── crypto_debug.json        # Debug log untuk cryptography operations
│
├── modules/                     # Core cryptography modules
│   ├── crypto_login.py          # Authentication & password hashing
│   ├── crypto_chat.py           # Chat encryption/decryption logic
│   ├── crypto_super_encrypt.py  # Super Encryption (Hill + Blowfish)
│   ├── crypto_rsa_file.py       # RSA file encryption
│   ├── crypto_steganography.py  # LSB steganography implementation
│   ├── crypto_biometric.py      # Windows Hello integration
│   └── crypto_debug.py          # Debug utilities & logging
│
└── ui/                          # User interface components
    ├── __init__.py              # Package initializer
    ├── ui_components.py         # Reusable UI components (ScrollableFrame, etc)
    ├── ui_auth_pages.py         # Login & Register pages
    ├── ui_main_pages.py         # Home, Products, Reviews pages
    └── ui_chat_page.py          # Chat interface
```

### Penjelasan File Penting

**Main Application Files:**
- `main.py`: Window manager utama, theme system, routing antar pages
- `generate_keys.py`: Generate RSA 2048-bit key pair untuk file encryption
- `build_exe.py`: Build configuration untuk PyInstaller (create executable)

**Modules (Logic Layer):**
- `crypto_login.py`: Handles login/register, SHA-256 password hashing
- `crypto_super_encrypt.py`: Hill Cipher (3x3 matrix) + Blowfish (CBC mode)
- `crypto_chat.py`: Chat encryption orchestration, menggunakan super encryption
- `crypto_rsa_file.py`: RSA-OAEP file encryption/decryption
- `crypto_steganography.py`: LSB steganography dengan PNG/JPG support
- `crypto_biometric.py`: Windows Hello API wrapper (WinRT)
- `crypto_debug.py`: Logging untuk troubleshooting crypto operations

**UI Layer:**
- `ui_auth_pages.py`: Login & register interface
- `ui_main_pages.py`: Home dashboard, product catalog, reviews list
- `ui_chat_page.py`: WhatsApp-style chat UI dengan encryption controls
- `ui_components.py`: Reusable components (ScrollableFrame, themed buttons)

**Data Files (JSON):**
- `users.json`: User database dengan hashed passwords
- `chats.json`: Encrypted chat messages dengan metadata
- `reviews.json`: Encrypted product reviews
- `theme.json`: Per-user theme preferences (light/dark)
- `crypto_debug.json`: Debug logs untuk tracing crypto operations

## 🔒 Catatan Keamanan

### ⚠️ PENTING - Private Key Security

**JANGAN PERNAH:**
- ❌ Commit `private_key.pem` ke Git/GitHub
- ❌ Share private key via email/chat/cloud
- ❌ Upload ke public repository
- ❌ Simpan di lokasi tidak aman

**WAJIB:**
- ✅ Simpan `private_key.pem` di lokasi aman dan terenkripsi
- ✅ Backup private key ke storage offline
- ✅ Generate ulang keys jika private key exposed
- ✅ Add `private_key.pem` ke `.gitignore`

### Best Practices

**Password Management:**
- Gunakan password minimal 12 karakter
- Kombinasi huruf besar, kecil, angka, dan simbol
- Jangan reuse password dari aplikasi lain
- Aktifkan Windows Hello untuk login lebih aman

**File Encryption:**
- Backup file original sebelum enkripsi
- Simpan file `.enc` di lokasi terpisah
- Test dekripsi setelah enkripsi
- Jangan hapus file original sampai yakin enkripsi berhasil

**Chat Security:**
- Verification code dan password harus dikomunikasikan via kanal terpisah
- Jangan simpan verification code di plaintext
- Use unique code untuk setiap pesan penting
- Decrypt message segera, jangan biarkan encrypted too long

**Steganography:**
- Gunakan gambar dengan banyak detail/noise (lebih aman)
- Jangan embed pesan terlalu panjang (deteksi lebih mudah)
- Compress image sebelum upload bisa merusak hidden message
- Test ekstraksi sebelum delete gambar original

### Limitasi Keamanan

**Known Limitations:**
1. **Local Storage:** Data encrypted disimpan lokal, jika device hilang/dicuri, data bisa diakses
2. **No Key Rotation:** RSA keys bersifat static, tidak ada auto-rotation
3. **Single Factor:** Tanpa Windows Hello, hanya password-based (single factor)
4. **No Remote Wipe:** Tidak ada mekanisme remote delete jika device hilang

**Mitigasi:**
- Enable Windows Hello (adds biometric factor)
- Encrypt hard drive dengan BitLocker
- Regular backup ke secure location
- Generate ulang RSA keys secara berkala (manual)

## 🔨 Build Executable

### Build dengan PyInstaller

**Langkah-Langkah:**

1. **Install PyInstaller:**
   ```bash
   pip install pyinstaller
   ```

2. **Run Build Script:**
   ```bash
   python build_exe.py
   ```

3. **Temukan Executable:**
   - Lokasi: `dist/Cryptore.exe`
   - Size: ~50-80 MB (includes Python interpreter + libraries)
   - Type: Standalone executable (tidak perlu Python install)

4. **Test Executable:**
   ```bash
   cd dist
   ./Cryptore.exe
   ```

### Build Configuration

Script `build_exe.py` menggunakan settings:
- `--onefile`: Single executable file
- `--windowed`: No console window (GUI only)
- `--icon`: Custom icon (optional)
- `--add-data`: Includes assets, modules, ui folders
- `--hidden-import`: Ensures PIL, winrt, keyring, cryptography included

### Distribusi

**Untuk distribusi ke user lain:**

1. **Bundle yang diperlukan:**
   ```
   Cryptore.exe
   assets/
   ├── images/
   └── keys/
       └── public_key.pem (ONLY public key!)
   ```

2. **JANGAN include:**
   - ❌ `private_key.pem` (security risk!)
   - ❌ `data/users.json` (user privacy)
   - ❌ `data/chats.json` (encrypted messages)
   - ❌ Source code `.py` files

3. **Instruksi untuk user:**
   - Extract zip ke folder
   - Double-click `Cryptore.exe`
   - Register akun baru
   - Setup Windows Hello (optional)

### Build Troubleshooting

**Error: "Failed to execute script"**
- Pastikan semua dependencies installed
- Check missing modules dengan `--debug` flag
- Add missing imports ke `hidden_imports` di `build_exe.py`

**Error: "Could not find assets/keys"**
- Verify `--add-data` paths correct
- Use absolute paths di build script
- Ensure assets folder structure intact

**Executable size terlalu besar:**
- Normal untuk Python apps (50-100 MB)
- Use `--onefile` untuk single file
- Atau gunakan `--onedir` untuk folder-based (smaller dll footprint)

## 🤝 Kontribusi

Contributions welcome! Untuk kontribusi:

1. Fork repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

**Areas for Contribution:**
- 🔐 Additional encryption algorithms
- 🌐 Multi-language support
- 📱 Cross-platform compatibility (Linux/macOS)
- 🎨 UI/UX improvements
- 🐛 Bug fixes
- 📚 Documentation improvements

## 📄 Lisensi

Project ini dibuat untuk keperluan akademik (Tugas Kriptografi, Semester 5).

**Academic Use Only** - Tidak untuk produksi commercial tanpa review security lengkap.

##  Acknowledgments

- Terima kasih kepada dosen pengampu mata kuliah Kriptografi
- Python Cryptography Community
- Tkinter & CustomTkinter contributors
- Windows Hello API documentation
- Open source libraries: Pillow, cryptography, numpy, keyring

## 📞 Contact & Support

- **Repository:** [github.com/sebuahdelusi/Cryptore](https://github.com/sebuahdelusi/Cryptore)
- **Issues:** [Report bugs here](https://github.com/sebuahdelusi/Cryptore/issues)

---

**⚠️ Disclaimer:** Aplikasi ini dibuat untuk tujuan edukasi dan penelitian kriptografi. Tidak direkomendasikan untuk production use tanpa security audit menyeluruh. Penulis tidak bertanggung jawab atas kerugian data atau security breach yang terjadi dari penggunaan aplikasi ini.

**🎓 Academic Integrity:** Project ini adalah hasil karya original untuk tugas kuliah. Plagiarisme atau penggunaan tanpa atribusi yang proper melanggar kode etik akademik.

---

*Last Updated: 2024*
*Version: 2.0 (dengan Light/Dark Mode & Windows Hello)*
