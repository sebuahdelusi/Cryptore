# Simpan sebagai: ui/ui_components.py

import tkinter as tk
from tkinter import ttk

COLOR_SECONDARY = "#F3F3F3"

class ScrollableFrame(ttk.Frame):
    """Frame yang bisa di-scroll secara vertikal."""
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        
        canvas = tk.Canvas(self, bg=COLOR_SECONDARY, highlightthickness=0)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        
        # style="TFrame" penting agar background-nya konsisten
        self.scrollable_frame = ttk.Frame(canvas, style="TFrame") 
        
        self.scrollable_frame.bind("<Configure>", 
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
        def _on_mousewheel(event):
            delta = 0
            if hasattr(event, 'delta') and event.delta != 0:
                delta = event.delta
            elif event.num == 5:
                delta = -120 # Scroll ke bawah
            elif event.num == 4:
                delta = 120 # Scroll ke atas
            
            if delta != 0:
                canvas.yview_scroll(int(-1*(delta/120)), "units")
        
        self.bind_all("<MouseWheel>", _on_mousewheel)
        self.bind_all("<Button-4>", _on_mousewheel)
        self.bind_all("<Button-5>", _on_mousewheel)

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")