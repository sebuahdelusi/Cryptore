import tkinter as tk
from tkinter import ttk, messagebox, TclError
from modules.crypto_super_encrypt import super_decrypt

def show_seller_chat(app, product):
    return show_chat_page(app, target_user=product['seller'], return_to_product=True)

def show_encrypted_chat(app):
    return show_chat_page(app, is_secure=True)

def show_chat_page(app, target_user=None, return_to_product=False, is_secure=False):
    app.clear_content_frame()
    content = app.content_area.scrollable_frame
    
    style = ttk.Style()
    
    if app.is_dark_mode:
        others_msg_bg = "#2A4A5A"  # Dark blue-gray for other's messages
        own_msg_bg = "#2A4A2A"     # Dark green for own messages
        sender_color = "#999999"   # Lighter gray for sender text
        msg_text_color = "#E0E0E0" # Light text for dark bubbles
    else:
        others_msg_bg = "#E3F2FD"  # Light blue for other's messages
        own_msg_bg = "#DCF8C6"     # Light green for own messages
        sender_color = "#666666"   # Dark gray for sender text
        msg_text_color = "#222222" # Dark text for light bubbles
    
    style.configure("ChatMsg.TFrame", 
                   background=others_msg_bg,
                   relief="flat",
                   borderwidth=0)
    style.configure("ChatMsg.Own.TFrame",
                   background=own_msg_bg,
                   relief="flat", 
                   borderwidth=0)
    
    style.configure("ChatMsg.TLabel",
                   background=others_msg_bg,
                   foreground=msg_text_color)
    style.configure("ChatMsg.Own.TLabel",
                   background=own_msg_bg,
                   foreground=msg_text_color)
    
    content.columnconfigure(0, weight=1)
    content.columnconfigure(1, weight=2)
    content.columnconfigure(2, weight=1)
    
    main_frame = ttk.Frame(content, style="CryptoPage.TFrame", padding=30)
    main_frame.grid(row=0, column=1, sticky='nsew', padx=20, pady=20)
    
    header_frame = ttk.Frame(main_frame, style="Product.TFrame")
    header_frame.pack(fill='x', pady=(0, 20))
    
    if return_to_product:
        back_cmd = lambda: app.show_product_detail_page(app.current_product)
        back_text = "← Kembali ke Produk"
    else:
        back_cmd = app.show_products_page
        back_text = "← Kembali ke Beranda"
        
    back_btn = ttk.Button(header_frame, text=back_text, 
                         command=back_cmd, 
                         style="Link.TButton")
    back_btn.pack(side='left')
    
    user_frame = ttk.Frame(header_frame, style="Product.TFrame")
    user_frame.pack(side='right', fill='x')
    
    selected_user = tk.StringVar()
    
    if return_to_product:
        seller_name = f"Penjual {app.current_product['name']}"
        ttk.Label(user_frame, 
                 text=f"Chat dengan {seller_name}", 
                 font=("Arial", 11)).pack(side='left')
        selected_user.set(target_user)
    else:
        ttk.Label(user_frame, text="Chat dengan:", 
                 font=("Arial", 11, "bold")).pack(side='left', padx=(0, 10))
                 
        users = list(app.user_db.keys())
        users.remove(app.current_user)
        
        user_combo = ttk.Combobox(user_frame, 
                                 textvariable=selected_user,
                                 values=users,
                                 state='readonly',
                                 width=30)
        user_combo.pack(side='left')
        
        def on_user_change(event):
            for widget in messages_frame.winfo_children():
                widget.destroy()
            refresh_messages()
            
        user_combo.bind('<<ComboboxSelected>>', on_user_change)
        
        if target_user and target_user in users:
            user_combo.set(target_user)
        elif users:
            user_combo.set(users[0])
    
    if return_to_product:
        title = f"💬 Chat Penjual {app.current_product['name']}"
        ttk.Label(header_frame, text=title, 
                 font=("Arial", 16)).pack(side='right')
    elif is_secure:
        title = "💬🔒 Chat Terenkripsi"
        ttk.Label(header_frame, text=title, 
                 font=("Arial", 16, "bold")).pack(side='right')
    else:
        title = "💬 Chat"
        ttk.Label(header_frame, text=title, 
                 font=("Arial", 16)).pack(side='right')
    
    chat_frame = ttk.Frame(main_frame, style="Product.TFrame")
    chat_frame.pack(fill='both', expand=True, pady=(0, 10))
    
    canvas = tk.Canvas(chat_frame, bg=app.COLOR_PRODUCT_BG, highlightthickness=0)
    scrollbar = ttk.Scrollbar(chat_frame, orient="vertical", command=canvas.yview)
    messages_frame = ttk.Frame(canvas, style="Product.TFrame")
    
    messages_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    
    canvas.create_window((0, 0), window=messages_frame, anchor="nw", width=canvas.winfo_reqwidth())
    canvas.configure(yscrollcommand=scrollbar.set)
    
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    canvas.bind("<Enter>", lambda e: canvas.bind_all("<MouseWheel>", _on_mousewheel))
    canvas.bind("<Leave>", lambda e: canvas.unbind_all("<MouseWheel>"))
    messages_frame.bind("<Enter>", lambda e: canvas.bind_all("<MouseWheel>", _on_mousewheel))
    messages_frame.bind("<Leave>", lambda e: canvas.unbind_all("<MouseWheel>"))
    
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    input_frame = ttk.Frame(main_frame, style="Product.TFrame")
    input_frame.pack(fill='x', pady=(10, 0))
    
    message_var = tk.StringVar()
    message_entry = ttk.Entry(input_frame, textvariable=message_var, 
                            font=("Arial", 12))
    message_entry.pack(side='left', fill='x', expand=True, padx=(0, 10))
    
    def send_message():
        message = message_var.get().strip()
        if not message:
            return
            
        if is_secure:
            def on_key_submit(hill_key, bf_key):
                if not hill_key or not bf_key:
                    messagebox.showwarning(
                        "Input Kurang", 
                        "Masukkan Kode Verifikasi dan Password Chat untuk mengirim pesan terenkripsi."
                    )
                    return
                
                try:
                    chat_target = target_user if return_to_product else selected_user.get()
                    if not chat_target:
                        messagebox.showwarning("Pilih Pengguna", "Pilih pengguna untuk chat terlebih dahulu.")
                        return
                        
                    app.chat_system.send_message(
                        app.current_user, chat_target, message,
                        hill_key=hill_key, blowfish_key=bf_key
                    )
                    
                    message_var.set("")
                    refresh_messages()
                except Exception as e:
                    messagebox.showerror("Error", f"Gagal mengirim pesan: {str(e)}")
            
            from ui.ui_components import CryptoKeyPopup
            popup = CryptoKeyPopup(app.root, title="Enter Encryption Keys", on_submit=on_key_submit)
        else:
            chat_target = target_user if return_to_product else selected_user.get()
            if not chat_target:
                messagebox.showwarning("Pilih Pengguna", "Pilih pengguna untuk chat terlebih dahulu.")
                return
            
            app.chat_system.send_message(app.current_user, chat_target, message)
            message_var.set("")
            refresh_messages()
    
    def refresh_messages(force_refresh=False):
        try:
            if messages_frame.winfo_exists():
                for widget in messages_frame.winfo_children():
                    widget.destroy()
                    
            chat_target = target_user if return_to_product else selected_user.get()
            if not chat_target:
                return
                
            chat_key = app.chat_system.get_chat_key(app.current_user, chat_target)
            messages = app.chat_system.chats.get(chat_key, [])
            
            placeholder_color = "#999999" if app.is_dark_mode else "#666666"
            if not messages:
                placeholder = ttk.Label(messages_frame,
                                     text="Belum ada percakapan. Mulai chat dengan mengirim pesan.",
                                     font=("Arial", 11),
                                     foreground=placeholder_color,
                                     wraplength=400,
                                     justify='center')
                placeholder.pack(pady=20)
                
                if not selected_user.get() and not return_to_product:
                    message_entry.configure(state='disabled')
                    send_btn.configure(state='disabled')
                else:
                    message_entry.configure(state='normal')
                    send_btn.configure(state='normal')
                return
            
            message_entry.configure(state='normal')
            send_btn.configure(state='normal')
            
            for msg in messages:
                is_own_message = msg["sender"].strip().lower() == app.current_user.strip().lower()
                
                msg_wrapper = ttk.Frame(messages_frame, style="Product.TFrame")
                msg_wrapper.pack(fill='x', pady=5, padx=10)
                
                inner_frame = ttk.Frame(msg_wrapper, style="Product.TFrame")
                inner_frame.pack(fill='x', expand=True)
                
                align_side = 'e' if is_own_message else 'w'
                
                if return_to_product:
                    seller_name = f"Penjual {app.current_product['name']}"
                else:
                    seller_name = msg["sender"]
                    
                sender = "Anda" if is_own_message else seller_name
                sender_label = ttk.Label(inner_frame, 
                         text=f"{sender} • {msg['timestamp']}",
                         font=("Arial", 8),
                         foreground=sender_color,
                         background=app.COLOR_PRODUCT_BG)
                sender_label.pack(anchor=align_side)
                
                if msg["encrypted"]:
                    if "decrypted_content" in msg:
                        content_text = msg["decrypted_content"]
                        lock_text = "🔓"
                    else:
                        content_text = "[Pesan Terenkripsi - Klik untuk memasukkan kunci]"
                        lock_text = "🔒"
                else:
                    content_text = msg["content"]
                    lock_text = ""
                
                text_frame = ttk.Frame(inner_frame, 
                                    style="ChatMsg.Own.TFrame" if is_own_message else "ChatMsg.TFrame")
                text_frame.pack(fill='x', pady=(2, 0))
                
                msg_label = ttk.Label(text_frame, 
                                    text=content_text,
                                    wraplength=500,
                                    justify='left',
                                    font=("Arial", 11),
                                    style="ChatMsg.Own.TLabel" if is_own_message else "ChatMsg.TLabel")
                msg_label.pack(padx=10, pady=5)
                
                if lock_text:
                    status_frame = ttk.Frame(inner_frame, style="Product.TFrame")
                    status_frame.pack(anchor=align_side, pady=(2, 0))
                    
                    lock_label = ttk.Label(status_frame,
                                         text=lock_text,
                                         font=("Arial", 8),
                                         foreground=sender_color,
                                         background=app.COLOR_PRODUCT_BG)
                    lock_label.pack(side='right' if is_own_message else 'left', padx=5)
                    
                    if msg["encrypted"] and not "decrypted_content" in msg:
                        hint_label = ttk.Label(status_frame,
                                             text="Gunakan Kode Verifikasi & Password yang sama dengan pengirim untuk membaca pesan",
                                             font=("Arial", 8),
                                             foreground=sender_color,
                                             background=app.COLOR_PRODUCT_BG)
                        hint_label.pack(side='right' if is_own_message else 'left', padx=5)
                
                if msg["encrypted"] and not "decrypted_content" in msg:
                    def create_click_handler(msg_ref, msg_label_ref, lock_label_ref):
                        def on_message_click(event):
                            def on_key_submit(hill_key, bf_key):
                                try:
                                    if not hill_key or not bf_key:
                                        messagebox.showwarning("Input Required", "Please enter both verification code and password.")
                                        return
                                        
                                    message_text = msg_ref["content"]
                                    if not message_text or not ':' in message_text:
                                        messagebox.showerror("Invalid Message", "This message cannot be decrypted.")
                                        return
                                        
                                    decrypted = super_decrypt(message_text, hill_key, bf_key)
                                    
                                    if decrypted:
                                        msg_ref["decrypted_content"] = decrypted
                                        msg_ref["is_decrypted"] = True
                                        
                                        if msg_label_ref and msg_label_ref.winfo_exists():
                                            msg_label_ref.configure(text=decrypted)
                                        if lock_label_ref and lock_label_ref.winfo_exists():
                                            lock_label_ref.configure(text="🔓")
                                        
                                        messagebox.showinfo("Success", "Message decrypted successfully!")
                                    else:
                                        messagebox.showerror(
                                            "Decryption Failed", 
                                            "Could not decrypt the message. Please check your verification code and password."
                                        )
                                except ValueError as ve:
                                    messagebox.showerror("Key Error", f"Invalid verification code format: {str(ve)}")
                                except Exception as e:
                                    messagebox.showerror("Decryption Error", f"An error occurred: {str(e)}")
                            
                            from ui.ui_components import CryptoKeyPopup
                            popup = CryptoKeyPopup(app.root, title="Enter Decryption Keys", on_submit=on_key_submit)
                        return on_message_click
                    
                    msg_label.bind('<Button-1>', create_click_handler(msg, msg_label, lock_label))
                    msg_label.configure(cursor="hand2")  # Show hand cursor on hover
            
            canvas.update_idletasks()
            canvas.yview_moveto(1.0)
                
        except tk.TclError:
            return
    
    send_btn = ttk.Button(input_frame, text="Kirim", 
                         command=send_message,
                         style="Submit.TButton")
    send_btn.pack(side='right', padx=10)
    
    message_entry.bind('<Return>', lambda e: send_message())
    
    refresh_messages()
    
    periodic_refresh_id = None
    
    def periodic_refresh():
        nonlocal periodic_refresh_id
        try:
            if main_frame.winfo_exists():
                refresh_messages()
                periodic_refresh_id = main_frame.after(5000, periodic_refresh)
        except tk.TclError:
            return
    
    periodic_refresh()