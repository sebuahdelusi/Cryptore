# Simpan sebagai: ui/ui_main_pages.py

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

def show_products_page(app):
    """Menggambar halaman daftar produk."""
    app.clear_content_frame()
    content = app.content_area.scrollable_frame 
    ttk.Label(content, text="Produk Pilihan", style="PageTitle.TLabel").pack(anchor='w', pady=20, padx=20)
    
    product_grid_frame = ttk.Frame(content)
    product_grid_frame.pack(anchor='center', pady=20, padx=20)
    
    products = [
            {
                "name": "Kamera Vintage", 
                "price": "Rp 5.000.000", 
                "image": "camera.png", 
                "trigger": "stegano", 
                "description": """Kamera film 35mm klasik yang direkondisi. Menghasilkan foto otentik dengan grain yang indah. Sempurna untuk penggemar fotografi analog.

Spesifikasi:
- Tipe: Analog 35mm SLR
- Lensa: 50mm f/1.8 (Termasuk)
- ISO Bawaan: 100-1600
- Kondisi: 9/10 (Direkondisi)
- Fitur: Light meter internal, self-timer

Dalam Kotak:
- 1x Body Kamera
- 1x Lensa 50mm
- 1x Strap Kulit
- 1x Baterai (untuk light meter)"""
            },
            {
                "name": "Buku Langka", 
                "price": "Rp 1.200.000", 
                "image": "book.png", 
                "trigger": "super_encrypt", 
                "description": """Edisi pertama dari 'Chronicles of Yore' yang sangat langka, dicetak pada tahun 1888. Sampul kulit asli dengan ukiran emas.

Detail:
- Penulis: A. B. C. Scribe
- Penerbit: Old World Press
- Tahun: 1888
- Bahasa: Inggris
- Kondisi: Baik, sedikit foxing pada halaman, sampul utuh.
- Halaman: 450 Halaman

Catatan Kolektor:
Ini adalah salah satu dari 500 cetakan pertama yang diketahui. Sangat dicari oleh kolektor sastra fantasi klasik."""
            },
            {
                "name": "Laptop Gaming", 
                "price": "Rp 25.000.000", 
                "image": "laptop.png", 
                "trigger": None, 
                "description": """Rasakan kekuatan gaming tertinggi dengan prosesor terbaru dan kartu grafis RTX seri 40. Layar 240Hz memastikan gameplay yang mulus.

Spesifikasi Teknis:
- CPU: Core i9 Gen-13
- GPU: NVIDIA GeForce RTX 4080 12GB
- RAM: 32GB DDR5 5200MHz
- Penyimpanan: 2TB NVMe SSD Gen4
- Layar: 16" QHD+ (2560x1600) 240Hz, 100% DCI-P3
- Keyboard: RGB Per-key
- OS: Windows 11 Pro

Fitur Tambahan:
- Sistem Pendingin Vapor Chamber
- Port Thunderbolt 4
- WiFi 6E"""
            },
            {
                "name": "Sepatu Lari", 
                "price": "Rp 2.300.000", 
                "image": "sepatu.png", 
                "trigger": None, 
                "description": """Sepatu lari ultra-ringan dengan bantalan busa reaktif. Didesain untuk pelari maraton dan harian. Memberikan kenyamanan maksimal.

Fitur Utama:
- Bahan: Jaring Sintetis (Mesh)
- Sol: Busa Reaktif Karbon
- Berat: 210g (Ukuran 42)
- Drop: 8mm
- Warna: Biru Neon

Teknologi:
Upper mesh yang 'breathable' menjaga kaki tetap sejuk. Pelat karbon di midsole memberikan tolakan responsif untuk setiap langkah."""
            },
            {
                "name": "Headphone Pro", 
                "price": "Rp 4.100.000", 
                "image": "headphone.png", 
                "trigger": None, 
                "description": """Headphone peredam bising (noise-cancelling) terbaik di kelasnya. Dengarkan musik tanpa gangguan dengan kualitas suara studio.

Spesifikasi:
- Koneksi: Bluetooth 5.2 (Multi-device)
- Daya Tahan Baterai: 30 Jam (ANC On)
- Fitur: ANC Adaptif, Mode Transparansi
- Driver: 40mm Kustom
- Charging: USB-C (Fast Charge 10 menit untuk 5 jam)

Fitur Cerdas:
- Deteksi pemakaian (musik otomatis pause/play).
- Equalizer kustom via aplikasi."""
            },
            {
                "name": "Lukisan Abstrak", 
                "price": "Rp 12.000.000", 
                "image": "lukisan.png", 
                "trigger": None, 
                "description": """Lukisan cat minyak di atas kanvas oleh seniman lokal ternama, 'Artisto'. Berjudul 'Urban Dreamscape'.

Detail Karya:
- Ukuran: 120cm x 80cm
- Media: Cat Minyak di atas Kanvas
- Tahun: 2023
- Bingkai: Termasuk (Kayu Jati Minimalis)

Catatan Kurator:
Karya ini mengeksplorasi kontras antara alam dan struktur perkotaan. Sapuan kuas yang dinamis menciptakan rasa gerakan yang kuat. Dilengkapi sertifikat keaslian."""
            },
            {
                "name": "Jam Tangan Pintar", 
                "price": "Rp 3.800.000", 
                "image": "smartwatch.png", 
                "trigger": None, 
                "description": """Tetap terhubung dan sehat dengan jam tangan pintar generasi terbaru. Monitor detak jantung 24/7 dan GPS internal.

Spesifikasi:
- Layar: 1.4" AMOLED (Resolusi 454x454)
- Baterai: Hingga 7 hari pemakaian
- Koneksi: Bluetooth 5.0, Wi-Fi, NFC
- Sensor: GPS, Detak Jantung, SpO2, Barometer
- Tahan Air: 5 ATM

Fitur:
Pelacak tidur, monitor stres, lebih dari 100 mode olahraga, pembayaran NFC, dan notifikasi smartphone."""
            },
            {
                "name": "Keyboard Mekanikal", 
                "price": "Rp 1.900.000", 
                "image": "keyboard.png", 
                "trigger": None, 
                "description": """Rasakan pengalaman mengetik terbaik dengan keyboard mekanikal full-size. Dilengkapi RGB yang dapat dikustomisasi.

Spesifikasi:
- Layout: 104 Tombol (Full-size)
- Switch: Blue Mechanical (Clicky & Tactile)
- Koneksi: USB-C (Kabel) & Bluetooth 5.1 (Wireless)
- Baterai: 4000 mAh
- Keycaps: PBT Double-shot

Fitur:
- Full N-Key Rollover
- Kustomisasi RGB per tombol
- Kompatibel dengan Windows & macOS"""
            },
            {
                "name": "Kopi Arabika Premium", 
                "price": "Rp 350.000", 
                "image": "kopi.png", 
                "trigger": None, 
                "description": """Biji kopi single-origin 500g pilihan dari dataran tinggi Gayo, Aceh.

Detail:
- Asal: Gayo, Aceh, Indonesia
- Varietas: Arabika Ateng
- Proses: Natural
- Ketinggian: 1500 MDPL
- Berat Bersih: 500g

Catatan Rasa:
Aroma floral yang kuat dengan cita rasa cokelat hitam, jeruk, dan sedikit rempah. Keasaman (acidity) medium yang seimbang."""
            },
    ]
    
    row, col = 0, 0
    for prod in products[:9]: 
        frame = _create_product_card(app, product_grid_frame, prod)
        frame.grid(row=row, column=col, padx=15, pady=15)
        col += 1
        if col > 2: col = 0; row += 1

def _create_product_card(app, parent, product):
    """Helper internal untuk membuat satu kartu produk."""
    prod_frame = ttk.Frame(parent, style="Product.TFrame")
    
    try:
        img_key = product["image"] 
        if img_key not in app.image_cache:
            img_path = os.path.join(app.IMAGE_PATH, product["image"])
            img = Image.open(img_path).resize((260, 200), Image.LANCZOS) 
            app.image_cache[img_key] = ImageTk.PhotoImage(img)
        
        img_label = ttk.Label(prod_frame, image=app.image_cache[img_key], style="Product.TLabel")
        img_label.pack(pady=0, padx=0, fill='x') 
        
    except FileNotFoundError:
        img_label = ttk.Label(prod_frame, text=f"[Gagal muat {product['image']}]", padding=40, style="Product.TLabel")
        img_label.pack(pady=20, padx=20)
    
    text_frame = ttk.Frame(prod_frame, style="Product.TFrame", padding=(15, 10))
    text_frame.pack(fill='x')

    ttk.Label(text_frame, text=product["name"], style="ProductTitle.TLabel").pack(anchor='w')
    ttk.Label(text_frame, text=product["price"], style="ProductPrice.TLabel").pack(anchor='w', pady=(2, 10))

    detail_button = ttk.Button(prod_frame, text="Lihat Detail")
    handler = lambda e, p=product: app.on_product_click(e, p)
    detail_button.bind("<Button-1>", handler)
    detail_button.bind("<Shift-Button-1>", handler)
    
    detail_button.pack(pady=(0, 15), padx=15, fill='x')
    
    if product["trigger"]:
        img_label.config(cursor="hand2")
        
    return prod_frame

def show_product_detail_page(app, product):
    """Menggambar halaman detail produk (decoy)."""
    app.clear_content_frame()
    content = app.content_area.scrollable_frame
    
    back_button = ttk.Button(content, text="< Kembali ke Beranda", 
                             command=app.show_products_page, style="Link.TButton")
    back_button.pack(anchor='w', padx=10, pady=(10,0))
    
    main_frame = ttk.Frame(content)
    main_frame.pack(fill='both', expand=True, padx=20, pady=10)

    left_frame = ttk.Frame(main_frame)
    left_frame.pack(side="left", padx=20, fill="y", anchor="n")
    try:
        img_path = os.path.join(app.IMAGE_PATH, product["image"])
        img = Image.open(img_path).resize((350, 350), Image.LANCZOS)
        img_key = product["image"] + "_large"
        
        if img_key not in app.image_cache:
            app.image_cache[img_key] = ImageTk.PhotoImage(img)
            
        img_label = ttk.Label(left_frame, image=app.image_cache[img_key])
        img_label.pack(pady=20, padx=20)
    except Exception:
        img_label = ttk.Label(left_frame, text=f"[Gagal muat {product['image']}]", padding=40)
        img_label.pack(pady=20, padx=20)
        
    right_frame = ttk.Frame(main_frame)
    right_frame.pack(side="right", fill="both", expand=True, padx=20)
    
    ttk.Label(right_frame, text=product["name"], font=("Arial", 24, "bold")).pack(anchor='w', pady=(10, 5))
    ttk.Label(right_frame, text=product["price"], font=("Arial", 18), foreground=app.COLOR_PRIMARY).pack(anchor='w', pady=10)
    
    ttk.Button(right_frame, text="Beli Sekarang", style="Accent.TButton", 
               command=lambda: tk.messagebox.showinfo("Toko Keren", "Fitur 'Beli' sedang dalam pengembangan.")
              ).pack(fill='x', ipady=10, pady=20)
    
    # --- [MODIFIKASI] Tombol 'Lihat Ulasan' ditambahkan di sini ---
    if product["name"] == "Buku Langka":
        ttk.Button(right_frame, text="Lihat Ulasan Pengguna (Mode Aman)", 
                   command=app.show_view_review_page, 
                   style="TButton" # Style tombol biasa
                  ).pack(fill='x', ipady=5, pady=5)
    # --- ---------------------------------------------------- ---
    
    ttk.Label(right_frame, text="Deskripsi Produk", font=("Arial", 14, "bold")).pack(anchor='w', pady=(20, 10))
    
    desc_text = tk.Text(right_frame, height=15, wrap="word", relief="flat", font=("Arial", 11), 
                        bg=app.COLOR_SECONDARY, borderwidth=0, fg=app.COLOR_TEXT, highlightthickness=0)
    desc_text.insert("1.0", product["description"])
    desc_text.config(state="disabled")
    desc_text.pack(fill="both", expand=True)