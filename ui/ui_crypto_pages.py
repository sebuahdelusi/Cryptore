# Simpan sebagai: ui/ui_crypto_pages.py

import tkinter as tk
from tkinter import ttk, messagebox
import os

def show_account_page(app):
    """Menggambar halaman Akun Saya (RSA)."""
    app.clear_content_frame()
    content = app.content_area.scrollable_frame
    
    back_button = ttk.Button(content, text="< Kembali ke Beranda", command=app.show_products_page, style="Link.TButton")
    back_button.pack(anchor='w', padx=10)
    ttk.Label(content, text="Manajemen Dokumen", style="PageTitle.TLabel").pack(anchor='w', pady=(5, 20), padx=20)
    
    wrapper = ttk.Frame(content, style="CryptoPage.TFrame", padding=20)
    wrapper.pack(fill='x', expand=True, padx=20, pady=10)
    
    if not (os.path.exists(app.KEY_PATH) and os.path.exists(os.path.join(app.KEY_PATH, "public_key.pem"))):
        ttk.Label(wrapper, text="Error: 'public_key.pem' atau 'private_key.pem' tidak ditemukan!", style="Error.TLabel").pack()
        ttk.Label(wrapper, text="Jalankan file 'generate_keys.py' satu kali.", style="Crypto.TLabel").pack()
        return
        
    enc_frame = ttk.LabelFrame(wrapper, text="Enkripsi Dokumen", padding=15)
    enc_frame.pack(fill='x', padx=10, pady=10)
    btn_enc_select = ttk.Button(enc_frame, text="1. Pilih Dokumen (PDF, TXT, dll)...", command=app.select_file_to_encrypt)
    btn_enc_select.pack(fill='x', pady=5)
    app.encrypt_file_path_var = tk.StringVar(value="Belum ada file dipilih.")
    lbl_enc = ttk.Label(enc_frame, textvariable=app.encrypt_file_path_var, style="Crypto.TLabel")
    lbl_enc.pack(fill='x', pady=5)
    btn_enc_run = ttk.Button(enc_frame, text="2. Amankan Dokumen", command=app.do_encrypt_file, style="Accent.TButton")
    btn_enc_run.pack(fill='x', pady=5)
    
    dec_frame = ttk.LabelFrame(wrapper, text="Buka Dokumen Aman", padding=15)
    dec_frame.pack(fill='x', padx=10, pady=10)
    btn_dec_select = ttk.Button(dec_frame, text="1. Pilih Dokumen (.enc)...", command=app.select_file_to_decrypt)
    btn_dec_select.pack(fill='x', pady=5)
    app.decrypt_file_path_var = tk.StringVar(value="Belum ada file dipilih.")
    lbl_dec = ttk.Label(dec_frame, textvariable=app.decrypt_file_path_var, style="Crypto.TLabel")
    lbl_dec.pack(fill='x', pady=5)
    btn_dec_run = ttk.Button(dec_frame, text="2. Buka Dokumen", command=app.do_decrypt_file)
    btn_dec_run.pack(fill='x', pady=5)

def show_reviews_page(app):
    """Menggambar halaman TULIS Ulasan (Super Encrypt)."""
    app.clear_content_frame()
    content = app.content_area.scrollable_frame
    
    back_button = ttk.Button(content, text="< Kembali ke Beranda", command=app.show_products_page, style="Link.TButton")
    back_button.pack(anchor='w', padx=10)
    ttk.Label(content, text="Tulis Ulasan Produk (Mode Aman)", style="PageTitle.TLabel").pack(anchor='w', pady=(5, 20), padx=20)
    
    wrapper = ttk.Frame(content, style="CryptoPage.TFrame", padding=20)
    wrapper.pack(fill='both', expand=True, padx=20, pady=10)
    
    ttk.Label(wrapper, text="Kode Verifikasi (e.g., DDCF)", style="Crypto.TLabel", font=("Arial", 11, "bold")).pack(anchor='w')
    app.hill_key_entry = ttk.Entry(wrapper, width=40, font=("Arial", 12))
    app.hill_key_entry.pack(fill='x', pady=(5, 10), ipady=5)
    
    ttk.Label(wrapper, text="Password Ulasan", style="Crypto.TLabel", font=("Arial", 11, "bold")).pack(anchor='w')
    app.blowfish_key_entry = ttk.Entry(wrapper, show="*", width=40, font=("Arial", 12))
    app.blowfish_key_entry.pack(fill='x', pady=(5, 15), ipady=5)

    ttk.Label(wrapper, text="Ulasan Kamu:", style="Crypto.TLabel", font=("Arial", 12, "bold")).pack(anchor='w', pady=(15,5))
    app.plaintext_text = tk.Text(wrapper, height=8, wrap='word', relief="solid", borderwidth=1, font=("Arial", 11))
    app.plaintext_text.pack(fill='x', pady=(0, 10))
    
    button_frame = ttk.Frame(wrapper, style="Crypto.TFrame")
    button_frame.pack(fill='x', pady=10)
    encrypt_button = ttk.Button(button_frame, text="Kirim Ulasan", command=app.do_super_encrypt, style="Accent.TButton")
    encrypt_button.pack(fill='x', padx=0, ipady=5)

def show_view_review_page(app):
    """Menggambar halaman LIHAT Ulasan (Super Decrypt)."""
    app.clear_content_frame()
    content = app.content_area.scrollable_frame
    
    back_button = ttk.Button(content, text="< Kembali ke Beranda", command=app.show_products_page, style="Link.TButton")
    back_button.pack(anchor='w', padx=10)
    ttk.Label(content, text="Lihat Ulasan (Mode Aman)", style="PageTitle.TLabel").pack(anchor='w', pady=(5, 20), padx=20)
    
    wrapper = ttk.Frame(content, style="CryptoPage.TFrame", padding=20)
    wrapper.pack(fill='both', expand=True, padx=20, pady=10)
    
    ttk.Label(wrapper, text="Kode Verifikasi (e.g., DDCF)", style="Crypto.TLabel", font=("Arial", 11, "bold")).pack(anchor='w')
    app.view_hill_key_entry = ttk.Entry(wrapper, width=40, font=("Arial", 12))
    app.view_hill_key_entry.pack(fill='x', pady=(5, 10), ipady=5)
    
    ttk.Label(wrapper, text="Password Ulasan", style="Crypto.TLabel", font=("Arial", 11, "bold")).pack(anchor='w')
    app.view_blowfish_key_entry = ttk.Entry(wrapper, show="*", width=40, font=("Arial", 12))
    app.view_blowfish_key_entry.pack(fill='x', pady=(5, 15), ipady=5)

    decrypt_button = ttk.Button(wrapper, text="Lihat Ulasan Saya", command=app.do_view_review, style="Accent.TButton")
    decrypt_button.pack(fill='x', ipady=5, pady=10)
    
    ttk.Label(wrapper, text="Ulasan Tersimpan (Terenkripsi):", style="Crypto.TLabel", font=("Arial", 12, "bold")).pack(anchor='w', pady=(15,5))
    app.view_ciphertext_text = tk.Text(wrapper, height=6, wrap='word', relief="solid", borderwidth=1, font=("Arial", 11), state='disabled')
    app.view_ciphertext_text.pack(fill='x', pady=(0, 10))
    
    ttk.Label(wrapper, text="Ulasan Kamu (Hasil Dekripsi):", style="Crypto.TLabel", font=("Arial", 12, "bold")).pack(anchor='w', pady=(5,5))
    app.view_plaintext_text = tk.Text(wrapper, height=6, wrap='word', relief="solid", borderwidth=1, font=("Arial", 11), state='disabled')
    app.view_plaintext_text.pack(fill='x', pady=(0, 10))
    
    # --- [MODIFIKASI] Otomatis muat SEMUA review tersimpan ---
    try:
        reviews_db = app.load_reviews_db()
        # 1. Ambil DAFTAR ulasan, atau list kosong
        saved_review_list = reviews_db.get(app.current_user, [])
        if saved_review_list:
            app.view_ciphertext_text.config(state='normal')
            # 2. Gabungkan semua ulasan dengan pemisah
            all_ciphertext = "\n\n".join(saved_review_list)
            app.view_ciphertext_text.insert("1.0", all_ciphertext)
            app.view_ciphertext_text.config(state='disabled')
    except Exception as e:
        print(f"Gagal memuat review tersimpan: {e}")
    # --- ----------------------------------------------- ---


def show_stegano_page(app, event=None):
    """Menggambar halaman Steganografi."""
    app.clear_content_frame()
    content = app.content_area.scrollable_frame
    
    back_button = ttk.Button(content, text="< Kembali ke Beranda", command=app.show_products_page, style="Link.TButton")
    back_button.pack(anchor='w', padx=10)
    ttk.Label(content, text="Detail Gambar (Mode Admin)", style="PageTitle.TLabel").pack(anchor='w', pady=(5, 20), padx=20)
    
    text_frame = ttk.Frame(content, style="TFrame")
    text_frame.pack(anchor='w', padx=20)

    ttk.Label(text_frame, text="Modul ini hanya untuk admin. Gunakan untuk ", style="TLabel").pack(side='left')
    
    trigger_label = ttk.Label(text_frame, text="menyisipkan", style="TLabel", foreground=app.COLOR_PRIMARY, cursor="hand2")
    trigger_label.pack(side='left')
    
    ttk.Label(text_frame, text=" atau mengekstrak metadata.", style="TLabel").pack(side='left')
    
    def on_trigger_click(event):
        is_shift_pressed = (event.state & 0x0001) != 0
        if is_shift_pressed:
            app.show_account_page()
        else:
            pass 
            
    trigger_label.bind("<Button-1>", on_trigger_click)
    trigger_label.bind("<Shift-Button-1>", on_trigger_click)
    
    wrapper = ttk.Frame(content, style="CryptoPage.TFrame", padding=20)
    wrapper.pack(fill='both', expand=True, padx=20, pady=10)
    
    app.steg_cover_path_var = tk.StringVar(value="Belum ada gambar dipilih.")
    app.steg_stego_path_var = tk.StringVar(value="Belum ada gambar dipilih.")
    
    hide_frame = ttk.LabelFrame(wrapper, text="Sisipkan Metadata", padding=15)
    hide_frame.pack(fill='x', padx=10, pady=10)
    btn_cover = ttk.Button(hide_frame, text="1. Pilih Gambar Asli", command=app.select_cover_image)
    btn_cover.pack(fill='x', pady=5)
    cover_label = ttk.Label(hide_frame, textvariable=app.steg_cover_path_var, style="Crypto.TLabel")
    cover_label.pack(fill='x', padx=5, pady=(0, 10))
    ttk.Label(hide_frame, text="2. Masukkan Metadata:", style="Crypto.TLabel").pack(anchor='w')
    app.steg_message_text = tk.Text(hide_frame, height=5, wrap='word', relief="solid", borderwidth=1, font=("Arial", 11))
    app.steg_message_text.pack(fill='x', pady=5)
    btn_hide = ttk.Button(hide_frame, text="3. Simpan Gambar", command=app.do_hide_stegano, style="Accent.TButton")
    btn_hide.pack(fill='x', pady=5)
    
    extract_frame = ttk.LabelFrame(wrapper, text="Ekstrak Metadata", padding=15)
    extract_frame.pack(fill='x', padx=10, pady=10)
    btn_stego = ttk.Button(extract_frame, text="1. Pilih Gambar", command=app.select_stego_image)
    btn_stego.pack(fill='x', pady=5)
    stego_label = ttk.Label(extract_frame, textvariable=app.steg_stego_path_var, style="Crypto.TLabel")
    stego_label.pack(fill='x', padx=5, pady=(0, 10))
    btn_extract = ttk.Button(extract_frame, text="2. Ekstrak Metadata", command=app.do_extract_stegano)
    btn_extract.pack(fill='x', pady=5)
    ttk.Label(extract_frame, text="Metadata Ditemukan:", style="Crypto.TLabel").pack(anchor='w', pady=(10, 0))
    app.steg_extracted_text = tk.Text(extract_frame, height=5, wrap='word', state='disabled', relief="solid", borderwidth=1, font=("Arial", 11))
    app.steg_extracted_text.pack(fill='x', pady=5)