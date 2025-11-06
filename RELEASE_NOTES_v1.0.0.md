# 🎉 Cryptore v1.0.0 - Release Notes

## 📦 Download
Download file **Cryptore.exe** dari bagian Assets di bawah.

## 🚀 Cara Menggunakan

1. **Download** file `Cryptore.exe` dari release ini
2. **Jalankan** `Cryptore.exe` (tidak perlu instalasi)
3. **Login/Register** untuk mulai menggunakan aplikasi
4. **Nikmati** semua fitur kriptografi yang tersedia!

## ✨ Fitur Utama

### 🔐 Keamanan & Autentikasi
- **Login System** dengan password hashing (Salt + SHA-256)
- **Windows Hello Integration** - Login menggunakan biometric (PIN/Face/Fingerprint)
- **RSA 2048-bit** untuk enkripsi file
- **Blowfish** untuk enkripsi data
- **Hill Cipher** untuk enkripsi klasik

### 💬 Komunikasi Terenkripsi
- **Encrypted Chat** - Chat end-to-end encryption dengan Hill Cipher + Blowfish
- **Normal Chat** - Chat biasa untuk komunikasi sehari-hari
- **Real-time Messaging** - Pesan tersimpan secara aman

### 🖼️ Steganografi
- **Hide Message** - Sembunyikan pesan dalam gambar (LSB Steganography)
- **Extract Message** - Ekstrak pesan tersembunyi dari gambar
- Support format: PNG, JPG, JPEG, BMP

### 📝 Product Reviews
- **Super Encryption** - Review terenkripsi dengan Hill Cipher + Blowfish
- **Secure Storage** - Review disimpan dalam format terenkripsi
- **Multi-user Support** - Setiap user punya review sendiri

### 🎯 Fitur Tersembunyi (Easter Eggs)
Untuk power users! Gunakan **Shift + Click** pada:
- **Lihat Detail** (Product Card) → Debug Crypto Panel
- **Chat Penjual** (Detail Produk) → Encrypted Chat Mode
- **Label Cryptore** (Halaman Steganografi) → Easter Egg Image

### 🎨 User Interface
- **Light/Dark Mode** - Toggle tema sesuai preferensi
- **Responsive Design** - UI yang clean dan modern
- **Easy Navigation** - Interface intuitif dan mudah digunakan

## 🔧 Persyaratan Sistem

### Sistem Operasi
- **Windows 10/11** (64-bit) - **WAJIB**
- Windows Hello compatible (untuk fitur biometric)

### Hardware
- **RAM:** Minimal 2 GB
- **Storage:** Minimal 100 MB free space
- **Display:** Resolusi minimal 1200x800

### Windows Hello (Opsional)
Untuk menggunakan fitur biometric login:
- Device dengan Windows Hello support
- PIN/Face recognition/Fingerprint reader telah dikonfigurasi di Windows

## 📂 Struktur File Setelah Dijalankan

Setelah menjalankan `Cryptore.exe`, aplikasi akan otomatis membuat folder berikut:

```
Cryptore.exe
├── data/
│   ├── users.json       (Data login user)
│   ├── chats.json       (Pesan chat terenkripsi)
│   ├── reviews.json     (Review terenkripsi)
│   └── theme.json       (Preferensi tema)
└── assets/
    ├── images/          (Gambar produk)
    └── keys/            (RSA keys)
        ├── public_key.pem
        └── private_key.pem
```

**⚠️ PENTING:** Jangan hapus folder `data` jika ingin menyimpan data user dan chat!

## 🛡️ Keamanan

### Enkripsi Data
- **Passwords:** Salt + SHA-256 hashing (tidak disimpan plain text)
- **Chat Messages:** Hill Cipher + Blowfish encryption
- **Reviews:** Super Encryption (Hill + Blowfish)
- **Files:** RSA 2048-bit encryption

### Windows Hello
- Kredensial disimpan di **Windows Credential Manager** (bukan di file)
- Biometric data tidak disimpan oleh aplikasi
- Menggunakan Windows Security API resmi

## 🐛 Known Issues & Solutions

### Windows Hello "Tidak Tersedia"
**Solusi:**
1. Pastikan Windows Hello sudah dikonfigurasi di Windows Settings
2. Login dengan password terlebih dahulu
3. Aktifkan Windows Hello dari menu profil

### Permission Error saat Membuka File
**Solusi:**
1. Pastikan file tidak sedang dibuka di aplikasi lain
2. Run as Administrator jika diperlukan
3. Check file permissions

### Gambar Tidak Muncul
**Solusi:**
1. Pastikan folder `assets/images/` ada di folder yang sama dengan exe
2. Re-download aplikasi jika diperlukan

## 📖 Dokumentasi Lengkap

Untuk dokumentasi lengkap, fitur tersembunyi, dan tutorial:
👉 **[Baca README.md di GitHub](https://github.com/sebuahdelusi/Cryptore)**

## 🎓 Informasi Proyek

**Mata Kuliah:** Kriptografi  
**Semester:** 5  
**Teknologi:**
- Python 3.13.3
- Tkinter (GUI)
- Cryptography Library
- WinRT (Windows Hello API)
- Pillow (Image Processing)

## 🔄 Changelog v1.0.0

### ✨ Features
- ✅ Login/Register system dengan password hashing
- ✅ Windows Hello biometric authentication
- ✅ Encrypted chat dengan Super Encryption
- ✅ Steganografi (hide/extract messages)
- ✅ RSA file encryption/decryption
- ✅ Product review dengan encryption
- ✅ Light/Dark mode toggle
- ✅ Debug crypto panel (Shift + Click)
- ✅ Easter eggs untuk power users

### 🐛 Bug Fixes
- ✅ Fixed Windows Hello error code 99 di executable
- ✅ Fixed subprocess issues di frozen app
- ✅ Fixed biometric availability detection

### 📚 Documentation
- ✅ Complete README dengan fitur tersembunyi
- ✅ Keyboard shortcuts documentation
- ✅ System requirements guide
- ✅ Installation & usage instructions

## 👨‍💻 Developer

**GitHub:** [@sebuahdelusi](https://github.com/sebuahdelusi)  
**Repository:** [Cryptore](https://github.com/sebuahdelusi/Cryptore)

## 📝 License

Proyek ini dibuat untuk keperluan akademik - Mata Kuliah Kriptografi.

---

**🎉 Terima kasih telah menggunakan Cryptore! 🎉**

*Untuk bug reports atau pertanyaan, silakan buka Issue di GitHub.*
