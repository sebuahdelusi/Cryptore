
import tkinter as tk
from tkinter import ttk

def create_login_ui(app_instance):
    app_instance.clear_frame()
    
    container = ttk.Frame(app_instance.root, style="ContentWrapper.TFrame")
    container.pack(expand=True, fill='both')
    
    container.grid_rowconfigure(0, weight=1)
    container.grid_rowconfigure(2, weight=1)
    container.grid_columnconfigure(0, weight=1)
    container.grid_columnconfigure(2, weight=1)
    
    frame = ttk.Frame(container, style="CryptoPage.TFrame", padding=40)
    frame.grid(row=1, column=1, sticky='nsew')
    
    ttk.Label(frame, text="Cryptore", style="PageTitle.TLabel").pack(pady=20)
    
    try:
        if app_instance.image_cache["logo"]:
            logo_label = ttk.Label(frame, image=app_instance.image_cache["logo"], style="Crypto.TLabel")
            logo_label.pack(pady=(0, 20))
    except (KeyError, AttributeError):
        pass
    
    ttk.Label(frame, text="Selamat Datang! Silakan login.", font=("Arial", 14)).pack(pady=20)
    
    form_frame = ttk.Frame(frame)
    form_frame.pack(pady=10)

    ttk.Label(form_frame, text="Username", font=("Arial", 11, "bold")).pack(anchor='w', padx=5)
    app_instance.login_username_entry = ttk.Entry(form_frame, width=40, font=("Arial", 12))
    app_instance.login_username_entry.pack(fill='x', padx=5, pady=(0, 10), ipady=5)

    ttk.Label(form_frame, text="Password", font=("Arial", 11, "bold")).pack(anchor='w', padx=5)
    app_instance.login_password_entry = ttk.Entry(form_frame, show='*', width=40, font=("Arial", 12))
    app_instance.login_password_entry.pack(fill='x', padx=5, pady=(0, 15), ipady=5)

    buttons_frame = ttk.Frame(form_frame)
    buttons_frame.pack(fill='x', padx=5, pady=20)

    login_btn = ttk.Button(buttons_frame, text="Login", 
                          command=app_instance.on_login_click, 
                          style="Accent.TButton")
    login_btn.pack(fill='x', expand=True, ipady=8, pady=(0, 10))

    biometric_btn = ttk.Button(buttons_frame, text="🔐 Windows Hello", 
                               command=app_instance.on_biometric_login_click, 
                               style="Accent.TButton")
    biometric_btn.pack(fill='x', expand=True, ipady=8)
    
    try:
        from modules.crypto_biometric import check_biometric_availability as check_biometric_status
        biometric_available, status_message = check_biometric_status()
        app_instance.biometric_status = status_message
    except Exception as e:
        biometric_available = False
        app_instance.biometric_status = f"Error: {str(e)}"

    if biometric_available:
        tooltip_text = "Masukkan username dan klik untuk login dengan biometrik"
    else:
        tooltip_text = f"{app_instance.biometric_status}"

    biometric_tooltip = ttk.Label(buttons_frame, 
                                  text=tooltip_text, 
                                  style="Error.TLabel",
                                  wraplength=380,
                                  justify='center')
    biometric_tooltip.pack(pady=(5,0))

    ttk.Button(form_frame, text="Belum punya akun? Register di sini", 
              command=app_instance.create_register_ui, 
              style="Link.TButton").pack(pady=15)

def create_register_ui(app_instance):
    app_instance.clear_frame()
    
    container = ttk.Frame(app_instance.root, style="ContentWrapper.TFrame")
    container.pack(expand=True, fill='both')
    
    container.grid_rowconfigure(0, weight=1)
    container.grid_rowconfigure(2, weight=1)
    container.grid_columnconfigure(0, weight=1)
    container.grid_columnconfigure(2, weight=1)
    
    frame = ttk.Frame(container, style="CryptoPage.TFrame", padding=40)
    frame.grid(row=1, column=1, sticky='nsew')
    
    try:
        logo_label = ttk.Label(frame, image=app_instance.image_cache["logo"], style="Crypto.TLabel")
        logo_label.pack(pady=(0, 20))
    except KeyError:
        ttk.Label(frame, text="Cryptore", style="PageTitle.TLabel").pack(pady=20)
    
    ttk.Label(frame, text="Buat Akun Baru", font=("Arial", 16, "bold")).pack(pady=10)
    
    form_frame = ttk.Frame(frame)
    form_frame.pack(pady=10)
    
    ttk.Label(form_frame, text="Username", font=("Arial", 11, "bold")).pack(anchor='w', padx=5)
    app_instance.reg_username_entry = ttk.Entry(form_frame, width=40, font=("Arial", 12))
    app_instance.reg_username_entry.pack(fill='x', padx=5, pady=(0, 10), ipady=5)

    ttk.Label(form_frame, text="Password", font=("Arial", 11, "bold")).pack(anchor='w', padx=5)
    app_instance.reg_password_entry = ttk.Entry(form_frame, show='*', width=40, font=("Arial", 12))
    app_instance.reg_password_entry.pack(fill='x', padx=5, pady=(0, 10), ipady=5)

    ttk.Label(form_frame, text="Konfirmasi Password", font=("Arial", 11, "bold")).pack(anchor='w', padx=5)
    app_instance.reg_confirm_entry = ttk.Entry(form_frame, show='*', width=40, font=("Arial", 12))
    app_instance.reg_confirm_entry.pack(fill='x', padx=5, pady=(0, 15), ipady=5)
    
    app_instance.reg_error_label = ttk.Label(form_frame, text="", style="Error.TLabel")
    app_instance.reg_error_label.pack(pady=5)
    
    ttk.Button(form_frame, text="Buat Akun", command=app_instance.on_register_click, style="Accent.TButton").pack(pady=10, fill='x', padx=5, ipady=5)
    ttk.Button(form_frame, text="Sudah punya akun? Login", command=app_instance.create_login_ui, style="Link.TButton").pack(pady=15)