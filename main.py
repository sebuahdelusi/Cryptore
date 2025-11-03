# Simpan sebagai: main.py

import tkinter as tk
from tkinter import ttk, messagebox, filedialog, END
from PIL import Image, ImageTk
import json
import os

# --- Impor dari folder modules/ ---
from modules import crypto_login, crypto_steganography, crypto_super_encrypt, crypto_rsa_file
from modules.crypto_super_encrypt import create_key_matrix

# --- Impor dari folder ui/ ---
from ui.ui_components import ScrollableFrame
from ui.ui_auth_pages import create_login_ui, create_register_ui
from ui.ui_main_pages import show_products_page, show_product_detail_page
from ui.ui_crypto_pages import show_account_page, show_reviews_page, show_stegano_page, show_view_review_page

# --- Setup Path ---
BASE_PATH = os.path.dirname(__file__)
ASSETS_PATH = os.path.join(BASE_PATH, "assets")
IMAGE_PATH = os.path.join(ASSETS_PATH, "images")
KEY_PATH = os.path.join(ASSETS_PATH, "keys")
DATA_PATH = os.path.join(BASE_PATH, "data")
USER_DB_FILE = os.path.join(DATA_PATH, "users.json")
REVIEWS_DB_FILE = os.path.join(DATA_PATH, "reviews.json")

# Buat folder jika belum ada
os.makedirs(DATA_PATH, exist_ok=True)
os.makedirs(IMAGE_PATH, exist_ok=True)
os.makedirs(KEY_PATH, exist_ok=True)

# Palet Warna (didefinisikan di sini agar bisa diakses global oleh App)
COLOR_PRIMARY = "#0078D4"
COLOR_SECONDARY = "#F3F3F3"
COLOR_HEADER = "#FFFFFF"
COLOR_TEXT = "#222222"
COLOR_PRODUCT_BG = "#FFFFFF"
COLOR_ERROR = "#D83B01"

# --- Kelas Aplikasi Utama ---
class DecoyEStoreApp:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Toko Keren - Aplikasi Belanja")
        self.root.geometry("1200x800")
        self.root.configure(bg=COLOR_SECONDARY)
        
        self.COLOR_PRIMARY = COLOR_PRIMARY
        self.COLOR_SECONDARY = COLOR_SECONDARY
        self.COLOR_TEXT = COLOR_TEXT 
        self.COLOR_HEADER = COLOR_HEADER
        self.COLOR_PRODUCT_BG = COLOR_PRODUCT_BG
        
        self.is_logged_in = False
        self.current_user = None
        
        self.header_frame = None
        self.content_area = None
        self.image_cache = {}

        self.IMAGE_PATH = IMAGE_PATH
        self.KEY_PATH = KEY_PATH

        self.user_db = self.load_user_db()
        self.setup_styles()
        
        try:
            logo_image = Image.open(os.path.join(IMAGE_PATH, "logo.png")).resize((150, 150), Image.LANCZOS)
            self.image_cache["logo"] = ImageTk.PhotoImage(logo_image)
        except FileNotFoundError:
            self.image_cache["logo"] = None

        self.create_splash_screen()
        
        self.root.after(1500, self.on_splash_faded_out)

    def setup_styles(self):
        style = ttk.Style(self.root)
        style.theme_use('clam')
        
        style.configure("TFrame", background=COLOR_SECONDARY)
        style.configure("Header.TFrame", background=COLOR_HEADER, borderwidth=1, relief="solid")
        
        # Modern product card styles
        style.configure("Product.TFrame", 
                        background=COLOR_PRODUCT_BG, 
                        relief="solid", 
                        borderwidth=1)
                        
        style.configure("Shadow.TFrame",
                        background=COLOR_SECONDARY)
                        
        # Modern style for all pages
        style.configure("CryptoPage.TFrame", 
                    background=COLOR_PRODUCT_BG,
                    relief="solid", 
                    borderwidth=1,
                    padding=20)
        
        # Add subtle shadow effect
        style.configure("ModernFrame.TFrame",
                    background=COLOR_PRODUCT_BG,
                    relief="solid",
                    borderwidth=1)

        # Modern splash screen styles with transparency support
        style.configure("Splash.TFrame", 
                    background=COLOR_PRODUCT_BG)
        style.configure("Splash.TLabel", 
                    background=COLOR_PRODUCT_BG,
                    foreground=COLOR_TEXT,
                    font=("Arial", 28, "bold"))
        
        # Update CryptoPage frame for splash
        style.configure("CryptoPage.TFrame",
                    background=COLOR_PRODUCT_BG,
                    relief="solid",
                    borderwidth=1,
                    padding=20)

        # Content wrapper style for centering
        style.configure("ContentWrapper.TFrame", background=COLOR_SECONDARY)
        
        style.configure("TLabel", background=COLOR_SECONDARY, foreground=COLOR_TEXT, font=("Arial", 11))
        style.configure("Header.TLabel", background=COLOR_HEADER, foreground=COLOR_TEXT)
        style.configure("Product.TLabel", background=COLOR_PRODUCT_BG, foreground=COLOR_TEXT)
        style.configure("ProductTitle.TLabel", 
                        background=COLOR_PRODUCT_BG, 
                        foreground=COLOR_TEXT, 
                        font=("Arial", 16, "bold"))
        
        style.configure("ProductPrice.TLabel", 
                        background=COLOR_PRODUCT_BG, 
                        foreground=COLOR_PRIMARY,
                        font=("Arial", 14, "bold"))
                        
        style.configure("Error.TLabel", background=COLOR_SECONDARY, foreground=COLOR_ERROR, font=("Arial", 10, "italic"))
        style.configure("Splash.TLabel", background=COLOR_SECONDARY, foreground=COLOR_TEXT, font=("Arial", 28, "bold"))
        style.configure("PageTitle.TLabel", background=COLOR_SECONDARY, foreground=COLOR_TEXT, font=("Arial", 20, "bold"))
        style.configure("Crypto.TLabel", background=COLOR_PRODUCT_BG, foreground=COLOR_TEXT, font=("Arial", 11))
        
        style.configure("TButton", font=("Arial", 11), padding=10, relief="flat", background="#E1E1E1", foreground=COLOR_TEXT)
        style.map("TButton", 
                  background=[('active', '#CFCFCF'), ('hover', '#EAEAEA')],
                  foreground=[('hover', COLOR_PRIMARY)])
                  
        style.configure("Accent.TButton", font=("Arial", 12, "bold"), padding=10, relief="flat", background=COLOR_PRIMARY, foreground=COLOR_HEADER)
        style.map("Accent.TButton", 
                  background=[('active', '#005a9e'), ('hover', '#006ac1')])
        
        style.configure("Link.TButton", 
                        font=("Arial", 10), 
                        padding=5, 
                        borderwidth=0, 
                        relief="flat",
                        background=COLOR_SECONDARY, 
                        foreground=COLOR_PRIMARY)
        style.map("Link.TButton", 
                  background=[('active', COLOR_SECONDARY)], 
                  foreground=[('active', '#005a9e'), ('hover', '#005a9e')],
                  underline=[('hover', 1)])
        
        style.configure("TEntry", 
                        font=("Arial", 12),
                        padding=10,
                        fieldbackground="white",
                        borderwidth=1,
                        relief="flat",
                        foreground=COLOR_TEXT
                       )
        style.map("TEntry",
                  bordercolor=[('focus', COLOR_PRIMARY)],
                  relief=[('focus', 'solid')]
                 )
        
        style.configure("TLabelFrame", background=COLOR_SECONDARY, font=("Arial", 11))
        style.configure("TLabelFrame.Label", background=COLOR_SECONDARY, foreground=COLOR_TEXT, font=("Arial", 12, "bold"))
        
        # --- Modern LabelFrame Styles ---
        style.configure("TLabelframe", 
                        background=COLOR_PRODUCT_BG)
        style.configure("TLabelframe.Label", 
                        background=COLOR_PRODUCT_BG,
                        foreground=COLOR_TEXT,
                        font=("Arial", 12, "bold"))
                        
        style.configure("Crypto.TLabelframe", 
                        background=COLOR_PRODUCT_BG,
                        relief="solid",
                        borderwidth=1)
        style.configure("Crypto.TLabelframe.Label", 
                        background=COLOR_PRODUCT_BG,
                        foreground=COLOR_TEXT,
                        font=("Arial", 14, "bold"),
                        padding=(10, 5))
        # --- -------------------------------------------- ---

        style.configure("Nav.TButton", 
                        font=("Arial", 11, "bold"), 
                        padding=(12, 8), 
                        relief="flat", 
                        background=COLOR_HEADER, 
                        foreground=COLOR_TEXT)
        style.map("Nav.TButton", 
                  background=[('active', '#EAEAEA'), ('hover', '#F0F0F0')],
                  foreground=[('hover', COLOR_PRIMARY)])

        style.configure("Nav.Logout.TButton", 
                        font=("Arial", 10), 
                        padding=8, 
                        relief="solid", 
                        borderwidth=1,
                        bordercolor="#CCCCCC",
                        background="#FAFAFA", 
                        foreground=COLOR_TEXT)
        style.map("Nav.Logout.TButton", 
                  background=[('active', '#E0E0E0'), ('hover', '#F0F0F0')])


    # --- Fungsi Animasi & DB ---
    def create_splash_screen(self):
        self.clear_frame()
        
        # Create simple splash frame
        splash_frame = ttk.Frame(self.root)
        splash_frame.pack(expand=True)
        
        if self.image_cache["logo"]:
            logo_label = ttk.Label(splash_frame, image=self.image_cache["logo"])
            logo_label.pack(pady=20)
        else:
            ttk.Label(splash_frame, text="Toko Keren", font=("Arial", 28, "bold")).pack(pady=20)
            
        # Version text
        ttk.Label(splash_frame, text="CryptoVault", font=("Arial", 16, "bold")).pack()
        ttk.Label(splash_frame, text="v1.0", font=("Arial", 14)).pack(pady=10)
    
    def fade_out_splash(self):
        self.clear_frame()
        self.create_login_ui()
    
    def on_splash_faded_out(self):
        # Show splash for 1.5 seconds then switch to login
        self.root.after(1500, self.fade_out_splash)
    
    def load_user_db(self):
        if not os.path.exists(USER_DB_FILE): return {}
        try:
            with open(USER_DB_FILE, "r") as f: return json.load(f)
        except json.JSONDecodeError: return {}
    
    def save_user_db(self):
        try:
            with open(USER_DB_FILE, "w") as f: json.dump(self.user_db, f, indent=4)
        except Exception as e: print(f"Gagal menyimpan DB: {e}")

    def load_reviews_db(self):
        if not os.path.exists(REVIEWS_DB_FILE): return {}
        try:
            with open(REVIEWS_DB_FILE, "r") as f: return json.load(f)
        except json.JSONDecodeError: return {}
    
    def save_reviews_db(self, db_data):
        try:
            with open(REVIEWS_DB_FILE, "w") as f: json.dump(db_data, f, indent=4)
        except Exception as e: print(f"Gagal menyimpan DB Review: {e}")
    
    def clear_frame(self):
        for widget in self.root.winfo_children(): widget.destroy()
    
    def clear_content_frame(self):
        if hasattr(self, 'content_area') and self.content_area:
            self.content_area.destroy()
        self.content_area = ScrollableFrame(self.root)
        self.content_area.pack(expand=True, fill='both')

    # --- Panggilan ke UI Halaman ---
    def create_login_ui(self):
        create_login_ui(self)
    
    def create_register_ui(self):
        create_register_ui(self)

    def create_main_app_ui(self):
        self.clear_frame()
        
        self.header_frame = ttk.Frame(self.root, padding=10, style="Header.TFrame")
        self.header_frame.pack(fill='x')
        
        ttk.Label(self.header_frame, text="Toko Keren", font=("Arial", 18, "bold"), style="Header.TLabel").pack(side='left', padx=10)
        
        ttk.Button(self.header_frame, text="Beranda", command=self.show_products_page, style="Nav.TButton").pack(side='left', padx=5)
        
        user_frame = ttk.Frame(self.header_frame, style="Header.TFrame")
        user_frame.pack(side='right', padx=10)

        logout_button = ttk.Button(user_frame, text="Logout", command=self.do_logout, style="Nav.Logout.TButton")
        logout_button.pack(side='right', padx=10)
        
        status_label = ttk.Label(user_frame, text=f"Logged in as: {self.current_user}", font=("Arial", 10), style="Header.TLabel")
        status_label.pack(side='right', padx=10)
        
        self.content_area = ScrollableFrame(self.root)
        self.content_area.pack(expand=True, fill='both')
        self.show_products_page()

    def show_products_page(self):
        show_products_page(self)

    def show_product_detail_page(self, product):
        show_product_detail_page(self, product)

    def show_account_page(self):
        show_account_page(self)

    def show_reviews_page(self):
        show_reviews_page(self)
        
    def show_stegano_page(self, event=None):
        show_stegano_page(self)

    def show_view_review_page(self):
        show_view_review_page(self)

    # --- Handler Logika (Bisnis) ---
    
    def on_register_click(self):
        username = self.reg_username_entry.get()
        password = self.reg_password_entry.get()
        confirm = self.reg_confirm_entry.get()
        if not username or not password or not confirm: self.reg_error_label.config(text="Semua field harus diisi!"); return
        if password != confirm: self.reg_error_label.config(text="Password dan konfirmasi tidak cocok!"); return
        if username in self.user_db: self.reg_error_label.config(text=f"Username '{username}' sudah ada!"); return
        salt_b64, hash_b64 = crypto_login.hash_password(password)
        self.user_db[username] = { "salt": salt_b64, "hash": hash_b64 }
        self.save_user_db()
        messagebox.showinfo("Sukses", f"Pengguna '{username}' berhasil didaftarkan. Silakan login.")
        self.create_login_ui()
    
    def on_login_click(self):
        username = self.login_username_entry.get()
        password = self.login_password_entry.get()
        if not username or not password: messagebox.showerror("Gagal", "Username dan password harus diisi."); return
        if username not in self.user_db: messagebox.showerror("Gagal", "Username atau password salah."); return
        user_data = self.user_db[username]
        if crypto_login.verify_password(user_data["salt"], user_data["hash"], password):
            self.is_logged_in = True; self.current_user = username
            self.create_main_app_ui()
        else:
            messagebox.showerror("Gagal", "Username atau password salah.")
            
    def do_logout(self):
        self.is_logged_in = False
        self.current_user = None
        self.image_cache = {}
        self.create_login_ui()

    def on_product_click(self, event, product):
        is_shift_pressed = (event.state & 0x0001) != 0
        if is_shift_pressed and product["trigger"]:
            if product["trigger"] == "stegano":
                self.show_stegano_page()
            elif product["trigger"] == "super_encrypt":
                self.show_reviews_page()
        else:
            self.show_product_detail_page(product)

    # --- Handler Kripto ---
    def select_file_to_encrypt(self):
        path = filedialog.askopenfilename(title="Pilih file APAPUN untuk dienkripsi")
        if path: self.encrypt_file_path_var.set(path)
    def select_file_to_decrypt(self):
        path = filedialog.askopenfilename(title="Pilih file .enc", filetypes=[("Encrypted Files", "*.enc")])
        if path: self.decrypt_file_path_var.set(path)
    def do_encrypt_file(self):
        file_path = self.encrypt_file_path_var.get()
        if file_path == "Belum ada file dipilih.": messagebox.showwarning("Input Kurang", "Pilih file untuk dienkripsi."); return
        try:
            crypto_rsa_file.rsa_encrypt_file(file_path)
            messagebox.showinfo("Sukses", f"File berhasil diamankan ke {file_path}.enc")
            self.encrypt_file_path_var.set("Belum ada file dipilih.")
        except Exception as e: messagebox.showerror("Error", f"Gagal: {e}")
    def do_decrypt_file(self):
        file_path = self.decrypt_file_path_var.get()
        if file_path == "Belum ada file dipilih.": messagebox.showwarning("Input Kurang", "Pilih file .enc untuk dibuka."); return
        try:
            crypto_rsa_file.rsa_decrypt_file(file_path)
            messagebox.showinfo("Sukses", "Dokumen berhasil dibuka!")
            self.decrypt_file_path_var.set("Belim ada file dipilih.")
        except Exception as e: messagebox.showerror("Error", f"Gagal: {e}")

    def do_super_encrypt(self):
        plaintext = self.plaintext_text.get("1.0", END).strip()
        hill_key = self.hill_key_entry.get()
        blowfish_key = self.blowfish_key_entry.get()
        if not (plaintext and hill_key and blowfish_key): messagebox.showwarning("Input Kurang", "Semua field harus diisi!"); return
        try: create_key_matrix(hill_key) 
        except ValueError as e: messagebox.showerror("Kode Verifikasi Error", f"Kode Verifikasi tidak valid: {e}"); return
        
        result_ciphertext = crypto_super_encrypt.super_encrypt(plaintext, hill_key, blowfish_key)
        
        if result_ciphertext:
            reviews_db = self.load_reviews_db()
            user_reviews_list = reviews_db.get(self.current_user, [])
            user_reviews_list.append(result_ciphertext)
            reviews_db[self.current_user] = user_reviews_list
            self.save_reviews_db(reviews_db)
            self.plaintext_text.delete("1.0", END)
            messagebox.showinfo("Sukses", "Ulasan berhasil dikirim (disimpan dengan aman)!")

    def do_view_review(self):
        hill_key = self.view_hill_key_entry.get()
        blowfish_key = self.view_blowfish_key_entry.get()
        if not (hill_key and blowfish_key): messagebox.showwarning("Input Kurang", "Kode Verifikasi dan Password harus diisi!"); return
        
        reviews_db = self.load_reviews_db()
        user_reviews_list = reviews_db.get(self.current_user, [])
        
        if not user_reviews_list:
            messagebox.showerror("Gagal", "Tidak ada ulasan tersimpan untuk pengguna ini.")
            return

        self.view_ciphertext_text.config(state='normal')
        self.view_ciphertext_text.delete("1.0", END)
        all_ciphertext = "\n\n".join(user_reviews_list)
        self.view_ciphertext_text.insert("1.0", all_ciphertext)
        self.view_ciphertext_text.config(state='disabled')

        try: create_key_matrix(hill_key)
        except ValueError as e: messagebox.showerror("Kode Verifikasi Error", f"Kode Verifikasi tidak valid: {e}"); return
        
        all_plaintext = []
        for i, ciphertext in enumerate(user_reviews_list):
            result_plaintext = crypto_super_encrypt.super_decrypt(ciphertext, hill_key, blowfish_key)
            
            if result_plaintext:
                all_plaintext.append(f"--- Ulasan #{i+1} ---\n{result_plaintext}")
            else:
                all_plaintext.append(f"--- Ulasan #{i+1} ---\n[DEKRIPSI GAGAL. Cek kunci.]")
        
        self.view_plaintext_text.config(state='normal')
        self.view_plaintext_text.delete("1.0", END)
        self.view_plaintext_text.insert("1.0", "\n\n".join(all_plaintext))
        self.view_plaintext_text.config(state='disabled')
        
        if any("[DEKRIPSI GAGAL" in s for s in all_plaintext):
             messagebox.showwarning("Selesai", f"Berhasil memuat {len(user_reviews_list)} ulasan. Beberapa ulasan gagal didekripsi (kunci salah).")
        else:
            messagebox.showinfo("Sukses", f"Berhasil memuat dan mendekripsi {len(user_reviews_list)} ulasan!")

    def select_cover_image(self):
        path = filedialog.askopenfilename(title="Pilih Gambar Asli", filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")])
        if path: self.steg_cover_path_var.set(path)
    def select_stego_image(self):
        path = filedialog.askopenfilename(title="Pilih Gambar", filetypes=[("PNG Image", "*.png")])
        if path: self.steg_stego_path_var.set(path)
    def do_hide_stegano(self):
        cover_path = self.steg_cover_path_var.get()
        message = self.steg_message_text.get("1.0", END).strip()
        if not (cover_path and message) or cover_path == "Belum ada gambar dipilih.": messagebox.showwarning("Input Kurang", "Pilih gambar dan isi metadata."); return
        output_path = filedialog.asksaveasfilename(title="Simpan Gambar Baru...", defaultextension=".png", filetypes=[("PNG Image", "*.png")])
        if not output_path: return
        try:
            crypto_steganography.hide_message_in_image(cover_path, message, output_path)
            messagebox.showinfo("Sukses", f"Metadata berhasil disisipkan ke {output_path}")
            self.steg_message_text.delete("1.0", END)
        except Exception as e: messagebox.showerror("Error", f"Gagal: {e}")
    def do_extract_stegano(self):
        stego_path = self.steg_stego_path_var.get()
        if not stego_path or stego_path == "Belum ada gambar dipilih.": messagebox.showwarning("Input Kurang", "Pilih gambar untuk diekstrak."); return
        try:
            extracted_message = crypto_steganography.extract_message_from_image(stego_path)
            self.steg_extracted_text.config(state='normal')
            self.steg_extracted_text.delete("1.0", END)
            self.steg_extracted_text.insert("1.0", extracted_message)
            self.steg_extracted_text.config(state='disabled')
            messagebox.showinfo("Sukses", "Ekstraksi metadata selesai.")
        except Exception as e: messagebox.showerror("Error", f"Gagal: {e}")

# --- Jalankan Aplikasi ---
if __name__ == "__main__":
    root = tk.Tk()
    try:
        style = ttk.Style(root)
        style.theme_use('clam') 
    except tk.TclError:
        print("Theme 'clam' tidak tersedia, menggunakan default.")
    
    app = DecoyEStoreApp(root)
    root.mainloop()