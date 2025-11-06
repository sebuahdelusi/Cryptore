
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

from ui.ui_chat_page import show_seller_chat, show_encrypted_chat

def show_products_page(app):
    app.clear_content_frame()
    content = app.content_area.scrollable_frame 
    
    content.columnconfigure(0, weight=1)
    content.columnconfigure(1, weight=4)
    content.columnconfigure(2, weight=1)
    
    header_frame = ttk.Frame(content, style="ContentWrapper.TFrame")
    header_frame.grid(row=0, column=1, sticky='ew', pady=(30,20), padx=20)
    
    ttk.Label(header_frame, text="Produk Pilihan", style="PageTitle.TLabel").pack(side='left')
    
    product_grid_frame = ttk.Frame(content, style="ContentWrapper.TFrame")
    product_grid_frame.grid(row=1, column=1, pady=(0,40), padx=40)
    
    for i in range(3):
        product_grid_frame.columnconfigure(i, weight=1, uniform='column')
    
    products = [
            {
                "name": "Oculus Rift", 
                "price": "Rp 8.500.000", 
                "image": "oculus.jpg",
                "seller": "gadget_store",
                "trigger": "stegano", 
                "description": """Headset VR canggih untuk pengalaman virtual reality yang imersif. Sempurna untuk gaming dan konten multimedia interaktif.

Spesifikasi:
- Display: OLED 2160x1200 (1080x1200 per mata)
- Refresh Rate: 90Hz
- Field of View: 110 derajat
- Tracking: 6DOF (Degrees of Freedom)
- Audio: Integrated 3D positional audio

Dalam Kotak:
- 1x Oculus Rift Headset
- 2x Touch Controller
- 2x Sensor
- Semua kabel yang diperlukan
- Remote Oculus

Fitur Tambahan:
- Kontrol gerak presisi tinggi
- Kompatibel dengan Steam VR
- Dukungan untuk ratusan game VR"""
            },
            {
                "name": "Poco X7 Pro", 
                "price": "Rp 3.999.000", 
                "image": "poco.jpg",
                "seller": "phone_world",
                "trigger": "super_encrypt", 
                "description": """Smartphone gaming dengan performa tinggi dan layar responsif. Ditenagai prosesor MediaTek Dimensity 8200-Ultra dan layar AMOLED 120Hz.

Spesifikasi:
- Layar: 6.67" AMOLED FHD+ 120Hz
- Prosesor: MediaTek Dimensity 8200-Ultra
- RAM: 12GB LPDDR5
- Penyimpanan: 256GB UFS 3.1
- Baterai: 5000mAh, Fast Charging 67W
- OS: MIUI 14 berbasis Android 13

Kamera:
- Utama: 64MP f/1.7
- Ultra Wide: 8MP f/2.2
- Macro: 2MP f/2.4
- Selfie: 16MP f/2.4

Fitur Unggulan:
- Game Turbo Engine
- Liquid Cooling System
- Dolby Atmos Dual Speakers
- Side-mounted Fingerprint
- NFC
- Gorilla Glass 5

Warna: Phantom Black
Garansi Resmi 12 Bulan"""
            },
            {
                "name": "Setup Gaming", 
                "price": "Rp 25.000.000", 
                "image": "setup.jpg", 
                "seller": "gaming_store",
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
- WiFi 6E
- Layout keyboard khas dalam bentuk bahasa arab"""
            },
            {
                "name": "Sepatu Lari", 
                "price": "Rp 2.300.000", 
                "image": "sepatu.jpg", 
                "seller": "sport_gear",
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
                "name": "Headphone Minusan", 
                "price": "Rp 4.100.000", 
                "image": "headphone.jpg", 
                "seller": "audio_shop",
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
                "seller": "art_gallery",
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
                "name": "Helm Bogo Retro", 
                "price": "Rp 850.000", 
                "image": "helm.jpg", 
                "seller": "moto_gear",
                "trigger": None, 
                "description": """Helm Bogo klasik dengan desain retro yang stylish. Cocok untuk pengendara motor custom dan pecinta gaya vintage.

Spesifikasi:
- Material: Fiber glass berkualitas tinggi
- Standar: DOT & SNI Certified
- Ukuran: M, L, XL tersedia
- Berat: 1.2 kg
- Warna: Glossy Black dengan aksen chrome

Fitur:
- Visor bubble yang dapat dilepas
- Interior bahan kulit premium
- Ventilasi udara optimal
- Sistem pengait double D-ring
- Pad telinga yang dapat dilepas

Perawatan:
Termasuk tas helm deluxe dan panduan perawatan khusus untuk menjaga kilau dan kualitas helm."""
            },
            {
                "name": "Keyboard Mekanikal", 
                "price": "Rp 1.900.000", 
                "image": "keyboard.jpg", 
                "seller": "pc_store",
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
                "name": "Honda City", 
                "price": "Rp 352.500.000", 
                "image": "mobil.jpg", 
                "seller": "auto_dealer",
                "trigger": None, 
                "description": """Honda City 2022 sedan mewah dengan performa tinggi dan fitur keselamatan lengkap. Kombinasi sempurna antara kenyamanan dan efisiensi bahan bakar.

Spesifikasi Teknis:
- Mesin: 1.5L DOHC i-VTEC
- Transmisi: CVT dengan Mode Paddle Shift
- Tenaga: 121 PS @ 6.600 rpm
- Torsi: 145 Nm @ 4.300 rpm
- Konsumsi BBM: 18.4 km/liter (kombinasi)

Fitur Keselamatan:
- 6 Airbag
- Honda Sensing
- Vehicle Stability Assist
- Hill Start Assist
- Anti-lock Braking System (ABS)
- Electronic Brake Distribution (EBD)

Fitur Kenyamanan:
- Smart Entry System
- Push Start Button
- 8" Advanced Touch Screen Display Audio
- Apple CarPlay & Android Auto
- Full LED Headlights dengan DRL
- AC Dual Zone Automatic
- Kursi Kulit Premium

Kondisi:
- Kilometer: 8.500
- Tahun: 2022
- Warna: Modern Steel Metallic
- Service Record Lengkap
- Garansi Pabrik Aktif"""
            },
    ]
    
    for i in range(3):
        product_grid_frame.columnconfigure(i, weight=1, uniform='column', minsize=340)
        
    row, col = 0, 0
    for prod in products[:9]: 
        frame = _create_product_card(app, product_grid_frame, prod)
        frame.grid(row=row, column=col, padx=10, pady=10, sticky='nsew')
        col += 1
        if col > 2: col = 0; row += 1
        
    for i in range((len(products) + 2) // 3):
        product_grid_frame.rowconfigure(i, weight=1)

def _create_product_card(app, parent, product):
    outer_frame = ttk.Frame(parent, style="Product.TFrame")
    outer_frame.grid_propagate(False)
    outer_frame.pack_propagate(False)
    
    outer_frame.configure(width=320, height=400)
    
    prod_frame = ttk.Frame(outer_frame, style="Product.TFrame")
    prod_frame.pack(fill='both', expand=True, padx=2, pady=2)
    
    try:
        img_key = product["image"] 
        if img_key not in app.image_cache:
            img_path = os.path.join(app.IMAGE_PATH, product["image"])
            img = Image.open(img_path).resize((300, 240), Image.LANCZOS) 
            app.image_cache[img_key] = ImageTk.PhotoImage(img)
        
        img_label = ttk.Label(prod_frame, image=app.image_cache[img_key], style="Product.TLabel")
        img_label.pack(pady=0, padx=0, fill='x') 
        
    except FileNotFoundError:
        img_label = ttk.Label(prod_frame, text=f"[Gambar tidak tersedia]", padding=40, style="Product.TLabel")
        img_label.pack(pady=20, padx=20)
    
    content_frame = ttk.Frame(prod_frame, style="Product.TFrame", padding=(20, 15))
    content_frame.pack(fill='x')

    name_label = ttk.Label(content_frame, text=product["name"], style="ProductTitle.TLabel")
    name_label.pack(anchor='w')

    price_label = ttk.Label(content_frame, text=product["price"], style="ProductPrice.TLabel")
    price_label.pack(anchor='w', pady=(5, 15))

    button_frame = ttk.Frame(content_frame, style="Product.TFrame")
    button_frame.pack(fill='x')
    
    detail_btn_bg = "#3A3A3A" if app.is_dark_mode else "#f8f9fa"
    detail_btn_hover = "#4A4A4A" if app.is_dark_mode else "#e9ecef"
    
    detail_button = tk.Button(
        button_frame, 
        text="Lihat Detail",
        font=("Arial", 11),
        bg=detail_btn_bg,
        fg=app.COLOR_TEXT,
        activebackground=detail_btn_hover,
        activeforeground=app.COLOR_TEXT,
        highlightthickness=0,
        highlightbackground=detail_btn_bg,
        highlightcolor=detail_btn_bg,
        relief="flat",
        borderwidth=0,
        padx=10,
        pady=8,
        cursor="hand2"
    )
    
    def on_enter(e):
        detail_button['bg'] = detail_btn_hover
    def on_leave(e):
        detail_button['bg'] = detail_btn_bg
    detail_button.bind("<Enter>", on_enter)
    detail_button.bind("<Leave>", on_leave)
    
    handler = lambda e, p=product: app.on_product_click(e, p)
    detail_button.bind("<Button-1>", handler)
    detail_button.bind("<Shift-Button-1>", handler)
    detail_button.pack(fill='x')
    
    if product["trigger"]:
        img_label.config(cursor="hand2")
    
    def on_enter(e):
        prod_frame.configure(relief="solid", borderwidth=2)
        detail_button.configure(
            bg=app.COLOR_PRIMARY,
            fg="#FFFFFF"  # White text for better contrast
        )
        
    def on_leave(e):
        prod_frame.configure(relief="solid", borderwidth=1)
        detail_button.configure(
            bg=detail_btn_bg,
            fg=app.COLOR_TEXT
        )
    
    for widget in [outer_frame, prod_frame, content_frame, button_frame, detail_button]:
        widget.bind('<Enter>', on_enter)
        widget.bind('<Leave>', on_leave)
        
    return outer_frame

def show_product_detail_page(app, product):
    app.clear_content_frame()
    content = app.content_area.scrollable_frame
    
    content.columnconfigure(0, weight=1)
    content.columnconfigure(1, weight=2)
    content.columnconfigure(2, weight=1)
    
    nav_frame = ttk.Frame(content, style="ContentWrapper.TFrame")
    nav_frame.grid(row=0, column=1, sticky='ew', padx=20, pady=(20,0))
    
    back_button = ttk.Button(nav_frame, text="< Kembali ke Beranda", 
                            command=app.show_products_page, style="Link.TButton")
    back_button.pack(side='left')
    
    main_frame = ttk.Frame(content, style="CryptoPage.TFrame", padding=30)
    main_frame.grid(row=1, column=1, sticky='nsew', padx=20, pady=20)

    left_frame = ttk.Frame(main_frame, style="Product.TFrame")
    left_frame.pack(side="left", padx=20, fill="y", anchor="n")
    
    try:
        img_path = os.path.join(app.IMAGE_PATH, product["image"])
        img = Image.open(img_path).resize((400, 400), Image.LANCZOS)
        img_key = product["image"] + "_large"
        
        if img_key not in app.image_cache:
            app.image_cache[img_key] = ImageTk.PhotoImage(img)
            
        img_label = ttk.Label(left_frame, image=app.image_cache[img_key], cursor="hand2")
        img_label.pack(pady=20, padx=20)
        
        ttk.Label(left_frame, text="🔍 Klik untuk memperbesar", 
                 font=("Arial", 10), foreground="#666666").pack(pady=(0,20))
        
        def show_zoomed_image(event):
            popup = tk.Toplevel(app.root)
            popup.title(product["name"])
            popup.configure(bg=app.COLOR_SECONDARY)
            
            screen_width = app.root.winfo_screenwidth()
            screen_height = app.root.winfo_screenheight()
            window_width = int(screen_width * 0.9)
            window_height = int(screen_height * 0.9)
            
            x = (screen_width - window_width) // 2
            y = (screen_height - window_height) // 2
            popup.geometry(f"{window_width}x{window_height}+{x}+{y}")
            
            frame = ttk.Frame(popup, style="CryptoPage.TFrame", padding=10)
            frame.pack(expand=True, fill='both', padx=10, pady=10)
            
            try:
                large_img = Image.open(img_path)
                aspect_ratio = large_img.width / large_img.height
                
                min_dimension = 800
                
                if aspect_ratio > 1:
                    new_width = min(max(min_dimension, large_img.width), window_width - 100)
                    new_height = int(new_width / aspect_ratio)
                    
                    if new_height > window_height - 100:
                        new_height = window_height - 100
                        new_width = int(new_height * aspect_ratio)
                else:
                    new_height = min(max(min_dimension, large_img.height), window_height - 100)
                    new_width = int(new_height * aspect_ratio)
                    
                    if new_width > window_width - 100:
                        new_width = window_width - 100
                        new_height = int(new_width / aspect_ratio)
                
                if new_width < min_dimension and new_height < min_dimension:
                    scale = min_dimension / max(new_width, new_height)
                    new_width = int(new_width * scale)
                    new_height = int(new_height * scale)
                
                large_img = large_img.resize((new_width, new_height), Image.LANCZOS)
                img_key_zoomed = product["image"] + "_zoomed"
                
                if img_key_zoomed not in app.image_cache:
                    app.image_cache[img_key_zoomed] = ImageTk.PhotoImage(large_img)
                
                img_label_zoomed = ttk.Label(frame, image=app.image_cache[img_key_zoomed])
                img_label_zoomed.pack(expand=True, fill='both')
                
                close_btn = ttk.Button(frame, text="Tutup", 
                                     command=popup.destroy, 
                                     style="Accent.TButton")
                close_btn.pack(pady=(20,0))
                
                popup.bind('<Escape>', lambda e: popup.destroy())
                
                popup.transient(app.root)
                popup.grab_set()
                
            except Exception as e:
                popup.destroy()
                tk.messagebox.showerror("Error", f"Gagal membuka gambar: {str(e)}")
        
        img_label.bind('<Button-1>', show_zoomed_image)
    except Exception:
        img_label = ttk.Label(left_frame, text=f"[Gambar tidak tersedia]", padding=40)
        img_label.pack(pady=20, padx=20)
        
    right_frame = ttk.Frame(main_frame)
    right_frame.pack(side="right", fill="both", expand=True, padx=20)
    
    title_frame = ttk.Frame(right_frame)
    title_frame.pack(fill='x', pady=(10, 20))
    
    ttk.Label(title_frame, text=product["name"], 
             font=("Arial", 28, "bold")).pack(anchor='w')
             
    price_frame = ttk.Frame(title_frame)
    price_frame.pack(fill='x', pady=(10,0))
    
    ttk.Label(price_frame, text=product["price"], 
             font=("Arial", 24), foreground=app.COLOR_PRIMARY).pack(side='left')
             
    ttk.Label(price_frame, text="✓ Stok Tersedia", 
             font=("Arial", 12), foreground="#28a745").pack(side='right')
    
    button_frame = ttk.Frame(right_frame)
    button_frame.pack(fill='x', pady=20)
    
    ttk.Button(button_frame, text="🛒 Beli Sekarang", style="Accent.TButton",
               command=lambda: tk.messagebox.showinfo("Cryptore", "Fitur 'Beli' sedang dalam pengembangan.")
              ).pack(side='left', fill='x', expand=True, ipady=10, padx=(0,5))
              
    chat_button = ttk.Button(button_frame, text="💬 Chat Penjual", 
                          style="TButton")
    
    def on_chat_click(event):
        is_shift_pressed = (event.state & 0x0001) != 0
        app.current_product = product
        
        if is_shift_pressed:
            show_encrypted_chat(app)
        else:
            show_seller_chat(app, product)
    
    chat_button.bind('<Button-1>', on_chat_click)
    chat_button.pack(side='right', fill='x', expand=True, ipady=10, padx=(5,0))
    
    if product["name"] == "Poco X7 Pro":
        ttk.Button(right_frame, text="🔒 Lihat Ulasan Pengguna (Mode Aman)", 
                   command=app.show_view_review_page, 
                   style="TButton"
                  ).pack(fill='x', ipady=5, pady=5)
    
    info_frame = ttk.LabelFrame(right_frame, text="Informasi Produk", style="Crypto.TLabelframe")
    info_frame.pack(fill='both', expand=True, pady=(20,0))
    
    desc_frame = ttk.Frame(info_frame)
    desc_frame.pack(fill='both', expand=True, padx=15, pady=15)
    
    desc_text = tk.Text(desc_frame, wrap="word", relief="flat", font=("Arial", 12),
                       bg=app.COLOR_PRODUCT_BG, borderwidth=0, fg=app.COLOR_TEXT,
                       highlightthickness=0, padx=10, pady=10, height=12)
    desc_text.insert("1.0", product["description"])
    desc_text.config(state="disabled")
    desc_text.pack(fill="both", expand=True)
    
    additional_frame = ttk.Frame(right_frame)
    additional_frame.pack(fill='x', pady=20)
    
    ship_frame = ttk.LabelFrame(additional_frame, text="Informasi Pengiriman", style="Crypto.TLabelframe")
    ship_frame.pack(fill='x', pady=(0,10))
    
    ship_content = ttk.Frame(ship_frame)
    ship_content.pack(fill='x', padx=15, pady=10)
    
    ttk.Label(ship_content, text="✈️ Pengiriman dari Jakarta Pusat", font=("Arial", 11)).pack(anchor='w')
    ttk.Label(ship_content, text="🚚 Estimasi 2-3 hari pengiriman", font=("Arial", 11)).pack(anchor='w', pady=5)
    
    payment_frame = ttk.LabelFrame(additional_frame, text="Metode Pembayaran", style="Crypto.TLabelframe")
    payment_frame.pack(fill='x')
    
    payment_content = ttk.Frame(payment_frame)
    payment_content.pack(fill='x', padx=15, pady=10)
    
    ttk.Label(payment_content, text="💳 Transfer Bank", font=("Arial", 11)).pack(anchor='w')
    ttk.Label(payment_content, text="💰 COD (Bayar di Tempat)", font=("Arial", 11)).pack(anchor='w', pady=5)
    ttk.Label(payment_content, text="📱 E-Wallet", font=("Arial", 11)).pack(anchor='w')