
import tkinter as tk
from tkinter import ttk

COLOR_SECONDARY = "#F3F3F3"

class CryptoKeyPopup(tk.Toplevel):
    def __init__(self, parent, title="Enter Keys", on_submit=None):
        super().__init__(parent)
        self.title(title)
        self.resizable(False, False)
        
        window_width = 500
        window_height = 350
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.minsize(500, 350)
        
        frame = ttk.Frame(self, padding="20", style="Product.TFrame")
        frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(frame, text="Verification Code:", font=("Arial", 11, "bold"), style="Product.TLabel").pack(pady=(0, 5))
        self.hill_key = ttk.Entry(frame, width=40, font=("Arial", 12))
        self.hill_key.pack(fill=tk.X, pady=(0, 15), ipady=5)
        
        ttk.Label(frame, text="Password:", font=("Arial", 11, "bold"), style="Product.TLabel").pack(pady=(0, 5))
        self.bf_key = ttk.Entry(frame, show="*", width=40, font=("Arial", 12))
        self.bf_key.pack(fill=tk.X, pady=(0, 15), ipady=5)
        
        button_frame = ttk.Frame(frame, style="Product.TFrame")
        button_frame.pack(fill=tk.X, pady=20, padx=50)
        
        submit_btn = tk.Button(button_frame, 
                             text="Submit",
                             command=self._on_submit,
                             font=("Arial", 12, "bold"),
                             bg="#0078D4",
                             fg="white",
                             width=20,
                             height=2,
                             relief="raised",
                             borderwidth=1)
        submit_btn.pack(fill=tk.X)
        
        submit_btn.bind("<Enter>", lambda e: submit_btn.configure(bg="#006ac1"))
        submit_btn.bind("<Leave>", lambda e: submit_btn.configure(bg="#0078D4"))
        
        self.on_submit_callback = on_submit
        
        self.transient(parent)
        self.grab_set()
        self.hill_key.focus_set()
        
    def _on_submit(self):
        if self.on_submit_callback:
            self.on_submit_callback(self.hill_key.get().strip(), self.bf_key.get().strip())
        self.destroy()

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, bg_color=None, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        canvas_bg = bg_color if bg_color else COLOR_SECONDARY
        canvas = tk.Canvas(self, bg=canvas_bg, highlightthickness=0)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        
        outer_frame = ttk.Frame(canvas, style="ContentWrapper.TFrame")
        outer_frame.columnconfigure(0, weight=1)
        outer_frame.columnconfigure(1, weight=2)
        outer_frame.columnconfigure(2, weight=1)
        
        self.scrollable_frame = ttk.Frame(outer_frame, style="TFrame")
        self.scrollable_frame.grid(row=0, column=1, sticky='nsew', padx=20)
        
        self.scrollable_frame.bind("<Configure>", 
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
        def _on_mousewheel(event):
            delta = 0
            if hasattr(event, 'delta') and event.delta != 0:
                delta = event.delta
            elif event.num == 5:
                delta = -120
            elif event.num == 4:
                delta = 120
            
            if delta != 0:
                canvas.yview_scroll(int(-1*(delta/120)), "units")
        
        self.bind_all("<MouseWheel>", _on_mousewheel)
        self.bind_all("<Button-4>", _on_mousewheel)
        self.bind_all("<Button-5>", _on_mousewheel)

        canvas.create_window((0, 0), window=outer_frame, anchor="nw", width=canvas.winfo_width())
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.grid(row=0, column=0, sticky='nsew')
        scrollbar.grid(row=0, column=1, sticky='ns')
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        def on_configure(event):
            canvas.itemconfig(canvas.find_withtag('all')[0], width=event.width)
            
        canvas.bind('<Configure>', on_configure)