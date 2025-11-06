
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, END
from PIL import Image, ImageTk
import json
import os
import sys
import keyring

from modules import crypto_login, crypto_steganography, crypto_super_encrypt, crypto_rsa_file, crypto_chat
from modules.crypto_super_encrypt import create_key_matrix

from ui.ui_components import ScrollableFrame
from ui.ui_auth_pages import create_login_ui, create_register_ui
from ui.ui_main_pages import show_products_page, show_product_detail_page
from ui.ui_chat_page import show_chat_page
from ui.ui_crypto_pages import show_account_page, show_reviews_page, show_stegano_page, show_view_review_page

BASE_PATH = os.path.dirname(__file__)
ASSETS_PATH = os.path.join(BASE_PATH, "assets")
IMAGE_PATH = os.path.join(ASSETS_PATH, "images")
KEY_PATH = os.path.join(ASSETS_PATH, "keys")
DATA_PATH = os.path.join(BASE_PATH, "data")
USER_DB_FILE = os.path.join(DATA_PATH, "users.json")
REVIEWS_DB_FILE = os.path.join(DATA_PATH, "reviews.json")
CHATS_DB_FILE = os.path.join(DATA_PATH, "chats.json")

os.makedirs(DATA_PATH, exist_ok=True)
os.makedirs(IMAGE_PATH, exist_ok=True)
os.makedirs(KEY_PATH, exist_ok=True)

COLOR_PRIMARY = "#0078D4"
COLOR_SECONDARY = "#F3F3F3"
COLOR_HEADER = "#FFFFFF"
COLOR_TEXT = "#222222"
COLOR_PRODUCT_BG = "#FFFFFF"
COLOR_ERROR = "#D83B01"

class DecoyEStoreApp:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Cryptore - Secure Application")
        self.root.geometry("1200x800")
        
        self.is_dark_mode = False
        self.load_theme_preference()
        self.apply_theme()
        
        self.root.configure(bg=self.COLOR_SECONDARY)
        
        self.chat_system = crypto_chat.SecureChat(CHATS_DB_FILE)
        
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
    
    def load_theme_preference(self):
        theme_file = os.path.join(DATA_PATH, "theme.json")
        try:
            if os.path.exists(theme_file):
                with open(theme_file, "r") as f:
                    data = json.load(f)
                    self.is_dark_mode = data.get("dark_mode", False)
            else:
                self.is_dark_mode = False
        except:
            self.is_dark_mode = False
    
    def save_theme_preference(self):
        theme_file = os.path.join(DATA_PATH, "theme.json")
        try:
            with open(theme_file, "w") as f:
                json.dump({"dark_mode": self.is_dark_mode}, f)
        except Exception as e:
            print(f"Failed to save theme: {e}")
    
    def apply_theme(self):
        if self.is_dark_mode:
            self.COLOR_PRIMARY = "#4A9EFF"
            self.COLOR_SECONDARY = "#1E1E1E"
            self.COLOR_HEADER = "#2D2D2D"
            self.COLOR_TEXT = "#E0E0E0"
            self.COLOR_PRODUCT_BG = "#252525"
            self.COLOR_ERROR = "#FF6B6B"
        else:
            self.COLOR_PRIMARY = "#0078D4"
            self.COLOR_SECONDARY = "#F3F3F3"
            self.COLOR_HEADER = "#FFFFFF"
            self.COLOR_TEXT = "#222222"
            self.COLOR_PRODUCT_BG = "#FFFFFF"
            self.COLOR_ERROR = "#D83B01"
        
        self.root.configure(bg=self.COLOR_SECONDARY)
    
    def toggle_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        self.save_theme_preference()
        self.apply_theme()
        self.setup_styles()
        
        if self.is_logged_in:
            self.create_main_app_ui()
        else:
            self.create_login_ui()

    def setup_styles(self):
        style = ttk.Style(self.root)
        style.theme_use('clam')
        
        style.configure("TFrame", background=self.COLOR_SECONDARY)
        style.configure("Header.TFrame", background=self.COLOR_HEADER, borderwidth=1, relief="solid")
        
        style.configure("Product.TFrame", 
                        background=self.COLOR_PRODUCT_BG, 
                        relief="solid", 
                        borderwidth=1)
                        
        style.configure("Shadow.TFrame",
                        background=self.COLOR_SECONDARY)
                        
        style.configure("CryptoPage.TFrame", 
                    background=self.COLOR_PRODUCT_BG,
                    relief="solid", 
                    borderwidth=1,
                    padding=20)
        
        style.configure("ModernFrame.TFrame",
                    background=self.COLOR_PRODUCT_BG,
                    relief="solid",
                    borderwidth=1)

        style.configure("Splash.TFrame", 
                    background=self.COLOR_PRODUCT_BG)
        style.configure("Splash.TLabel", 
                    background=self.COLOR_PRODUCT_BG,
                    foreground=self.COLOR_TEXT,
                    font=("Arial", 28, "bold"))
        
        style.configure("CryptoPage.TFrame",
                    background=self.COLOR_PRODUCT_BG,
                    relief="solid",
                    borderwidth=1,
                    padding=20)

        style.configure("ContentWrapper.TFrame", background=self.COLOR_SECONDARY)
        
        style.configure("TLabel", background=self.COLOR_SECONDARY, foreground=self.COLOR_TEXT, font=("Arial", 11))
        style.configure("Header.TLabel", background=self.COLOR_HEADER, foreground=self.COLOR_TEXT)
        style.configure("Product.TLabel", background=self.COLOR_PRODUCT_BG, foreground=self.COLOR_TEXT)
        style.configure("ProductTitle.TLabel", 
                        background=self.COLOR_PRODUCT_BG, 
                        foreground=self.COLOR_TEXT, 
                        font=("Arial", 16, "bold"))
        
        style.configure("ProductPrice.TLabel", 
                        background=self.COLOR_PRODUCT_BG, 
                        foreground=self.COLOR_PRIMARY,
                        font=("Arial", 14, "bold"))
                        
        style.configure("Error.TLabel", background=self.COLOR_SECONDARY, foreground=self.COLOR_ERROR, font=("Arial", 10, "italic"))
        style.configure("Splash.TLabel", background=self.COLOR_SECONDARY, foreground=self.COLOR_TEXT, font=("Arial", 28, "bold"))
        style.configure("PageTitle.TLabel", background=self.COLOR_SECONDARY, foreground=self.COLOR_TEXT, font=("Arial", 20, "bold"))
        style.configure("Crypto.TLabel", background=self.COLOR_PRODUCT_BG, foreground=self.COLOR_TEXT, font=("Arial", 11))
        
        button_bg = "#3A3A3A" if self.is_dark_mode else "#E1E1E1"
        button_hover = "#4A4A4A" if self.is_dark_mode else "#EAEAEA"
        button_active = "#2A2A2A" if self.is_dark_mode else "#CFCFCF"
        
        style.configure("TButton", font=("Arial", 11), padding=10, relief="flat", background=button_bg, foreground=self.COLOR_TEXT)
        style.map("TButton", 
                  background=[('active', button_active), ('hover', button_hover)],
                  foreground=[('hover', self.COLOR_PRIMARY)])
                  
        accent_hover = "#3A8AE8" if self.is_dark_mode else "#006ac1"
        accent_active = "#2A7AD8" if self.is_dark_mode else "#005a9e"
        accent_fg = "#FFFFFF" if self.is_dark_mode else self.COLOR_HEADER
        
        style.configure("Accent.TButton", 
                    font=("Arial", 12, "bold"),
                    padding=10,
                    width=15,
                    background=self.COLOR_PRIMARY,
                    foreground=accent_fg)
        style.map("Accent.TButton",
                 background=[('active', accent_active), ('hover', accent_hover)],
                 foreground=[('active', accent_fg), ('hover', accent_fg)])
                    
        style.configure("Submit.TButton", 
                    font=("Arial", 12, "bold"),
                    padding=10,
                    width=15,
                    background=self.COLOR_PRIMARY,
                    foreground=accent_fg)
        style.map("Submit.TButton",
                 background=[('active', accent_active), ('hover', accent_hover)],
                 foreground=[('active', accent_fg), ('hover', accent_fg)])
        
        link_hover = "#3A8AE8" if self.is_dark_mode else "#005a9e"
        link_active = "#3A8AE8" if self.is_dark_mode else "#005a9e"
        
        style.configure("Link.TButton", 
                        font=("Arial", 10), 
                        padding=5, 
                        borderwidth=0, 
                        relief="flat",
                        background=self.COLOR_SECONDARY, 
                        foreground=self.COLOR_PRIMARY)
        style.map("Link.TButton", 
                  background=[('active', self.COLOR_SECONDARY)], 
                  foreground=[('active', link_active), ('hover', link_hover)],
                  underline=[('hover', 1)])
        
        entry_bg = "#2A2A2A" if self.is_dark_mode else "white"
        entry_fg = "#E0E0E0" if self.is_dark_mode else "#222222"
        
        style.configure("TEntry", 
                        font=("Arial", 12),
                        padding=10,
                        fieldbackground=entry_bg,
                        borderwidth=1,
                        relief="flat",
                        foreground=entry_fg
                       )
        style.map("TEntry",
                  bordercolor=[('focus', self.COLOR_PRIMARY)],
                  relief=[('focus', 'solid')]
                 )
        
        style.configure("TLabelFrame", background=self.COLOR_SECONDARY, font=("Arial", 11))
        style.configure("TLabelFrame.Label", background=self.COLOR_SECONDARY, foreground=self.COLOR_TEXT, font=("Arial", 12, "bold"))
        
        style.configure("TLabelframe", 
                        background=self.COLOR_PRODUCT_BG)
        style.configure("TLabelframe.Label", 
                        background=self.COLOR_PRODUCT_BG,
                        foreground=self.COLOR_TEXT,
                        font=("Arial", 12, "bold"))
                        
        style.configure("Crypto.TLabelframe", 
                        background=self.COLOR_PRODUCT_BG,
                        relief="solid",
                        borderwidth=1)
        style.configure("Crypto.TLabelframe.Label", 
                        background=self.COLOR_PRODUCT_BG,
                        foreground=self.COLOR_TEXT,
                        font=("Arial", 14, "bold"),
                        padding=(10, 5))

        style.configure("Nav.TButton", 
                        font=("Arial", 11, "bold"), 
                        padding=(12, 8), 
                        relief="flat", 
                        background=self.COLOR_HEADER, 
                        foreground=self.COLOR_TEXT)
        style.map("Nav.TButton", 
                  background=[('active', '#EAEAEA'), ('hover', '#F0F0F0')],
                  foreground=[('hover', self.COLOR_PRIMARY)])

        logout_bg = "#3A3A3A" if self.is_dark_mode else "#FAFAFA"
        logout_hover = "#4A4A4A" if self.is_dark_mode else "#F0F0F0"
        logout_active = "#2A2A2A" if self.is_dark_mode else "#E0E0E0"
        logout_border = "#555555" if self.is_dark_mode else "#CCCCCC"
        
        style.configure("Nav.Logout.TButton", 
                        font=("Arial", 10), 
                        padding=8, 
                        relief="solid", 
                        borderwidth=1,
                        bordercolor=logout_border,
                        background=logout_bg, 
                        foreground=self.COLOR_TEXT)
        style.map("Nav.Logout.TButton", 
                  background=[('active', logout_active), ('hover', logout_hover)])
        
        style.configure("Profile.TMenubutton",
                       font=("Arial", 10),
                       padding=(8, 6),
                       relief="flat",
                       background=self.COLOR_HEADER,
                       foreground=self.COLOR_TEXT)
        style.map("Profile.TMenubutton",
                 background=[('active', '#EAEAEA'), ('hover', '#F0F0F0')],
                 foreground=[('hover', self.COLOR_PRIMARY)])


    def create_splash_screen(self):
        self.clear_frame()
        
        splash_frame = ttk.Frame(self.root)
        splash_frame.pack(expand=True)
        
        if self.image_cache["logo"]:
            logo_label = ttk.Label(splash_frame, image=self.image_cache["logo"])
            logo_label.pack(pady=20)
        else:
            ttk.Label(splash_frame, text="Cryptore", font=("Arial", 28, "bold")).pack(pady=20)
            
        ttk.Label(splash_frame, text="CryptoVault", font=("Arial", 16, "bold")).pack()
        ttk.Label(splash_frame, text="v1.0", font=("Arial", 14)).pack(pady=10)
    
    def fade_out_splash(self):
        self.clear_frame()
        self.create_login_ui()
    
    def on_splash_faded_out(self):
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
        self.content_area = ScrollableFrame(self.root, bg_color=self.COLOR_SECONDARY)
        self.content_area.pack(expand=True, fill='both')

    def create_login_ui(self):
        create_login_ui(self)
    
    def create_register_ui(self):
        create_register_ui(self)

    def create_main_app_ui(self):
        self.clear_frame()
        
        self.header_frame = ttk.Frame(self.root, padding=10, style="Header.TFrame")
        self.header_frame.pack(fill='x')
        
        ttk.Label(self.header_frame, text="Cryptore", font=("Arial", 18, "bold"), style="Header.TLabel").pack(side='left', padx=10)
        
        ttk.Button(self.header_frame, text="Beranda",   
                 command=self.show_products_page, 
                 style="Nav.TButton").pack(side='left', padx=5)
        
        user_frame = ttk.Frame(self.header_frame, style="Header.TFrame")
        user_frame.pack(side='right', padx=10)

        logout_button = ttk.Button(user_frame, text="Logout", command=self.do_logout, style="Nav.Logout.TButton")
        logout_button.pack(side='right', padx=10)
        
        profile_button = ttk.Menubutton(user_frame, text=f"👤 {self.current_user}", style="Profile.TMenubutton")
        profile_button.pack(side='right', padx=5)
        
        profile_menu = tk.Menu(profile_button, tearoff=0, font=("Arial", 10))
        profile_button['menu'] = profile_menu
        
        from modules.crypto_biometric import check_biometric_availability
        wh_available, wh_status = check_biometric_availability()
        
        try:
            wh_enabled = keyring.get_password("CryptoreApp_WH", self.current_user)
            wh_configured = (wh_enabled == "enabled")
        except:
            wh_configured = False
        
        if wh_available:
            if wh_configured:
                profile_menu.add_command(label="✓ Windows Hello Aktif", command=self.show_windows_hello_settings)
            else:
                profile_menu.add_command(label="🔐 Aktifkan Windows Hello", command=self.enable_windows_hello)
        else:
            profile_menu.add_command(label="🔐 Windows Hello (Tidak Tersedia)", state='disabled')
        
        theme_label = "🌙 Dark Mode" if not self.is_dark_mode else "☀️ Light Mode"
        profile_menu.add_command(label=theme_label, command=self.toggle_theme)
        
        profile_menu.add_separator()
        profile_menu.add_command(label="Logout", command=self.do_logout)
        
        self.content_area = ScrollableFrame(self.root, bg_color=self.COLOR_SECONDARY)
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
        if not username or not password: 
            messagebox.showerror("Gagal", "Username dan password harus diisi."); return
        if username not in self.user_db: 
            messagebox.showerror("Gagal", "Username atau password salah."); return
        
        user_data = self.user_db[username]
        
        if crypto_login.verify_password(user_data["salt"], user_data["hash"], password):
            self.is_logged_in = True
            self.current_user = username
            self.create_main_app_ui()
        else:
            messagebox.showerror("Gagal", "Username atau password salah.")
            
    def on_biometric_login_click(self):
        from modules.crypto_biometric import verify_biometric_with_prompt
        
        username_from_box = self.login_username_entry.get()
        if not username_from_box:
            messagebox.showerror("Gagal", "Masukkan username Anda terlebih dahulu.")
            return
            
        if username_from_box not in self.user_db:
            messagebox.showerror("Gagal", "Username tidak ditemukan.")
            return
        
        try:
            wh_enabled = keyring.get_password("CryptoreApp_WH", username_from_box)
            if wh_enabled != "enabled":
                messagebox.showerror("Gagal", 
                    f"Windows Hello belum diaktifkan untuk '{username_from_box}'.\n\n"
                    f"Silakan login dengan password terlebih dahulu, lalu aktifkan Windows Hello dari menu profil."
                )
                return
        except Exception as e:
            messagebox.showerror("Gagal", 
                f"Windows Hello belum diaktifkan untuk '{username_from_box}'.\n\n"
                f"Silakan login dengan password terlebih dahulu, lalu aktifkan Windows Hello dari menu profil."
            )
            return
            
        self.root.lift()
        self.root.attributes('-topmost', True)
        self.root.after(100, lambda: self.root.attributes('-topmost', False))
        
        messagebox.showinfo(
            "Windows Hello",
            "Jendela Windows Hello akan muncul.\n"
            "Silakan cek layar Anda untuk mengautentikasi."
        )
        
        verification_success = verify_biometric_with_prompt()
        
        if verification_success:
            self.is_logged_in = True
            self.current_user = username_from_box
            self.create_main_app_ui()
        else:
            messagebox.showwarning("Gagal", "Verifikasi biometrik gagal atau dibatalkan.")
    
    def enable_windows_hello(self):
        from modules.crypto_biometric import verify_biometric_with_prompt
        
        response = messagebox.askyesno(
            "Aktifkan Windows Hello",
            f"Aktifkan Windows Hello untuk login cepat sebagai '{self.current_user}'?\n\n"
            f"Setelah diaktifkan, Anda dapat login menggunakan PIN, sidik jari, atau face recognition."
        )
        
        if not response:
            return
        
        self.root.lift()
        self.root.attributes('-topmost', True)
        self.root.after(100, lambda: self.root.attributes('-topmost', False))
        
        messagebox.showinfo(
            "Windows Hello",
            "Jendela Windows Hello akan muncul.\n"
            "Silakan cek layar Anda untuk mengautentikasi."
        )
        
        if verify_biometric_with_prompt():
            try:
                keyring.set_password("CryptoreApp_WH", self.current_user, "enabled")
                messagebox.showinfo(
                    "Berhasil",
                    f"Windows Hello berhasil diaktifkan untuk '{self.current_user}'!\n\n"
                    f"Sekarang Anda dapat login menggunakan Windows Hello di halaman login."
                )
                self.create_main_app_ui()
            except Exception as e:
                messagebox.showerror("Error", f"Gagal menyimpan ke keyring: {e}")
        else:
            messagebox.showwarning("Gagal", "Verifikasi Windows Hello gagal atau dibatalkan.")
    
    def show_windows_hello_settings(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Pengaturan Windows Hello")
        dialog.geometry("400x250")
        dialog.transient(self.root)
        dialog.grab_set()
        
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (dialog.winfo_width() // 2)
        y = (dialog.winfo_screenheight() // 2) - (dialog.winfo_height() // 2)
        dialog.geometry(f"+{x}+{y}")
        
        frame = ttk.Frame(dialog, padding=20)
        frame.pack(expand=True, fill='both')
        
        ttk.Label(frame, text="🔐 Windows Hello", font=("Arial", 16, "bold")).pack(pady=10)
        ttk.Label(frame, text=f"Status: Aktif untuk '{self.current_user}'", font=("Arial", 11)).pack(pady=5)
        ttk.Label(frame, text="Anda dapat login menggunakan Windows Hello\ndi halaman login.", 
                 font=("Arial", 10), justify='center').pack(pady=10)
        
        button_frame = ttk.Frame(frame)
        button_frame.pack(pady=20)
        
        ttk.Button(button_frame, text="Nonaktifkan", command=lambda: self.disable_windows_hello(dialog), 
                  style="Accent.TButton").pack(side='left', padx=5)
        ttk.Button(button_frame, text="Tutup", command=dialog.destroy, 
                  style="Link.TButton").pack(side='left', padx=5)
    
    def disable_windows_hello(self, dialog=None):
        response = messagebox.askyesno(
            "Nonaktifkan Windows Hello",
            f"Nonaktifkan Windows Hello untuk '{self.current_user}'?\n\n"
            f"Anda masih dapat login menggunakan password."
        )
        
        if not response:
            return
        
        try:
            wh_enabled = keyring.get_password("CryptoreApp_WH", self.current_user)
            if wh_enabled == "enabled":
                keyring.delete_password("CryptoreApp_WH", self.current_user)
                messagebox.showinfo("Berhasil", "Windows Hello berhasil dinonaktifkan.")
                if dialog:
                    dialog.destroy()
                self.create_main_app_ui()
            else:
                messagebox.showwarning("Perhatian", "Windows Hello tidak aktif untuk user ini.")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menonaktifkan: {e}")
            
    def do_logout(self):
        if hasattr(self, 'chat_system') and self.chat_system:
            self.chat_system.load_chats()
            
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
        if not (cover_path and message) or cover_path == "Belum ada file dipilih.": messagebox.showwarning("Input Kurang", "Pilih gambar dan isi metadata."); return
        output_path = filedialog.asksaveasfilename(title="Simpan Gambar Baru...", defaultextension=".png", filetypes=[("PNG Image", "*.png")])
        if not output_path: return
        try:
            crypto_steganography.hide_message_in_image(cover_path, message, output_path)
            messagebox.showinfo("Sukses", f"Metadata berhasil disisipkan ke {output_path}")
            self.steg_message_text.delete("1.0", END)
        except Exception as e: messagebox.showerror("Error", f"Gagal: {e}")
    def do_extract_stegano(self):
        stego_path = self.steg_stego_path_var.get()
        if not stego_path or stego_path == "Belum ada file dipilih.": messagebox.showwarning("Input Kurang", "Pilih gambar untuk diekstrak."); return
        try:
            extracted_message = crypto_steganography.extract_message_from_image(stego_path)
            self.steg_extracted_text.config(state='normal')
            self.steg_extracted_text.delete("1.0", END)
            self.steg_extracted_text.insert("1.0", extracted_message)
            self.steg_extracted_text.config(state='disabled')
            messagebox.showinfo("Sukses", "Ekstraksi metadata selesai.")
        except Exception as e: messagebox.showerror("Error", f"Gagal: {e}")

if __name__ == "__main__":
    
    if "--hello-available" in sys.argv or "--hello-verify" in sys.argv:
        try:
            from modules.crypto_biometric import _hello_helper_main
            flag = sys.argv[1]
            message = sys.argv[2] if len(sys.argv) > 2 else None
            _hello_helper_main(flag, message)
        except Exception as e:
            sys.exit(98)

    root = tk.Tk()
    try:
        style = ttk.Style(root)
        style.theme_use('clam') 
    except tk.TclError:
        print("Theme 'clam' tidak tersedia, menggunakan default.")
    
    app = DecoyEStoreApp(root)
    root.mainloop()