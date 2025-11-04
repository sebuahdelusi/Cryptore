# Simpan sebagai: ui/ui_auth_pages.py

import tkinter as tk
from tkinter import ttk

def create_login_ui(app_instance):
    """Membuat UI login yang stabil."""
    app_instance.clear_frame()
    
    # Import biometric module and check detailed status
    try:
        from modules.crypto_biometric import check_biometric_status
        biometric_available, status_message = check_biometric_status()
        app_instance.biometric_status = status_message
    except Exception as e:
        print(f"Error checking biometric availability: {e}")
        biometric_available = False
        app_instance.biometric_status = f"Error: {str(e)}"
    
    # Main container that fills the window
    container = ttk.Frame(app_instance.root, style="ContentWrapper.TFrame")
    container.pack(expand=True, fill='both')
    
    # Configure grid weights for both rows and columns to center the content
    container.grid_rowconfigure(0, weight=1)
    container.grid_rowconfigure(2, weight=1)
    container.grid_columnconfigure(0, weight=1)
    container.grid_columnconfigure(2, weight=1)
    
    # Modern frame with shadow effect
    frame = ttk.Frame(container, style="CryptoPage.TFrame", padding=40)
    frame.grid(row=1, column=1, sticky='nsew')
    
    # Always show the store name
    ttk.Label(frame, text="Toko Keren", style="PageTitle.TLabel").pack(pady=20)
    
    # Show logo if available
    try:
        if app_instance.image_cache["logo"]:
            logo_label = ttk.Label(frame, image=app_instance.image_cache["logo"], style="Crypto.TLabel")
            logo_label.pack(pady=(0, 20))
    except (KeyError, AttributeError):
        pass
    
    ttk.Label(frame, text="Selamat Datang! Silakan login.", font=("Arial", 14)).pack(pady=20)
    
    form_frame = ttk.Frame(frame)
    form_frame.pack(pady=10)

    # --- Ini adalah UI yang 100% stabil ---
    ttk.Label(form_frame, text="Username", font=("Arial", 11, "bold")).pack(anchor='w', padx=5)
    app_instance.login_username_entry = ttk.Entry(form_frame, width=40, font=("Arial", 12))
    app_instance.login_username_entry.pack(fill='x', padx=5, pady=(0, 10), ipady=5)

    ttk.Label(form_frame, text="Password", font=("Arial", 11, "bold")).pack(anchor='w', padx=5)
    app_instance.login_password_entry = ttk.Entry(form_frame, show='*', width=40, font=("Arial", 12))
    app_instance.login_password_entry.pack(fill='x', padx=5, pady=(0, 15), ipady=5)
    # --- Akhir UI Stabil ---

    # Add buttons frame for login options
    buttons_frame = ttk.Frame(form_frame)
    buttons_frame.pack(fill='x', padx=5, pady=20)

    # Regular login button
    ttk.Button(buttons_frame, text="Login", 
              command=app_instance.on_login_click, 
              style="Accent.TButton").pack(side='left', fill='x', expand=True, ipady=5, padx=(0,5))

    # Biometric login button (if available)
    if biometric_available:
        biometric_btn = ttk.Button(buttons_frame, text="🔐 Login dengan Windows Hello", 
                                command=app_instance.on_biometric_login_click, 
                                style="Accent.TButton")
        biometric_btn.pack(side='right', fill='x', expand=True, ipady=5, padx=(5,0))
        
        # Add tooltip hint for biometric login
        biometric_tooltip = ttk.Label(buttons_frame, 
                                   text="Masukkan username dan klik untuk login dengan Windows Hello", 
                                   style="Error.TLabel")
        biometric_tooltip.pack(side='bottom', pady=(5,0))
    else:
        # Show why biometric is not available
        status_frame = ttk.Frame(form_frame)
        status_frame.pack(fill='x', pady=(10,0))
        
        status_icon = ttk.Label(status_frame, text="ℹ️", font=("Arial", 12))
        status_icon.pack(side='left', padx=(5,0))
        
        status_label = ttk.Label(status_frame, 
                               text=f"Status Windows Hello: {app_instance.biometric_status}",
                               style="Error.TLabel",
                               wraplength=350)
        status_label.pack(side='left', padx=(5,0), fill='x', expand=True)

    ttk.Button(form_frame, text="Belum punya akun? Register di sini", 
              command=app_instance.create_register_ui, 
              style="Link.TButton").pack(pady=15)

def create_register_ui(app_instance):
    """Membuat UI register yang stabil."""
    app_instance.clear_frame()
    
    # Main container that fills the window
    container = ttk.Frame(app_instance.root, style="ContentWrapper.TFrame")
    container.pack(expand=True, fill='both')
    
    # Configure grid weights for both rows and columns to center the content
    container.grid_rowconfigure(0, weight=1)
    container.grid_rowconfigure(2, weight=1)
    container.grid_columnconfigure(0, weight=1)
    container.grid_columnconfigure(2, weight=1)
    
    # Modern frame with shadow effect
    frame = ttk.Frame(container, style="CryptoPage.TFrame", padding=40)
    frame.grid(row=1, column=1, sticky='nsew')
    
    try:
        logo_label = ttk.Label(frame, image=app_instance.image_cache["logo"], style="Crypto.TLabel")
        logo_label.pack(pady=(0, 20))
    except KeyError:
        ttk.Label(frame, text="Toko Keren", style="PageTitle.TLabel").pack(pady=20)
    
    ttk.Label(frame, text="Buat Akun Baru", font=("Arial", 16, "bold")).pack(pady=10)
    
    form_frame = ttk.Frame(frame)
    form_frame.pack(pady=10)
    
    # --- Ini adalah UI yang 100% stabil ---
    ttk.Label(form_frame, text="Username", font=("Arial", 11, "bold")).pack(anchor='w', padx=5)
    app_instance.reg_username_entry = ttk.Entry(form_frame, width=40, font=("Arial", 12))
    app_instance.reg_username_entry.pack(fill='x', padx=5, pady=(0, 10), ipady=5)

    ttk.Label(form_frame, text="Password", font=("Arial", 11, "bold")).pack(anchor='w', padx=5)
    app_instance.reg_password_entry = ttk.Entry(form_frame, show='*', width=40, font=("Arial", 12))
    app_instance.reg_password_entry.pack(fill='x', padx=5, pady=(0, 10), ipady=5)

    ttk.Label(form_frame, text="Konfirmasi Password", font=("Arial", 11, "bold")).pack(anchor='w', padx=5)
    app_instance.reg_confirm_entry = ttk.Entry(form_frame, show='*', width=40, font=("Arial", 12))
    app_instance.reg_confirm_entry.pack(fill='x', padx=5, pady=(0, 15), ipady=5)
    # --- Akhir UI Stabil ---
    
    app_instance.reg_error_label = ttk.Label(form_frame, text="", style="Error.TLabel")
    app_instance.reg_error_label.pack(pady=5)
    
    ttk.Button(form_frame, text="Buat Akun", command=app_instance.on_register_click, style="Accent.TButton").pack(pady=10, fill='x', padx=5, ipady=5)
    ttk.Button(form_frame, text="Sudah punya akun? Login", command=app_instance.create_login_ui, style="Link.TButton").pack(pady=15)