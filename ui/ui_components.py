# Simpan sebagai: ui/ui_components.py

import tkinter as tk
from tkinter import ttk

COLOR_SECONDARY = "#F3F3F3"

class ScrollableFrame(ttk.Frame):
    """Frame yang bisa di-scroll secara vertikal."""
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        
        # Configure container to expand
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        canvas = tk.Canvas(self, bg=COLOR_SECONDARY, highlightthickness=0)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        
        # Create outer frame for centering
        outer_frame = ttk.Frame(canvas, style="ContentWrapper.TFrame")
        # Center frame configuration
        outer_frame.columnconfigure(0, weight=1)  # Left margin
        outer_frame.columnconfigure(1, weight=2)  # Content area
        outer_frame.columnconfigure(2, weight=1)  # Right margin
        
        # Create the actual scrollable frame in the center column
        self.scrollable_frame = ttk.Frame(outer_frame, style="TFrame")
        self.scrollable_frame.grid(row=0, column=1, sticky='nsew', padx=20)
        
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

        canvas.create_window((0, 0), window=outer_frame, anchor="nw", width=canvas.winfo_width())
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Configure canvas and scrollbar
        canvas.grid(row=0, column=0, sticky='nsew')
        scrollbar.grid(row=0, column=1, sticky='ns')
        
        # Make canvas expand to fill frame
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        # Update canvas width when window resizes
        def on_configure(event):
            canvas.itemconfig(canvas.find_withtag('all')[0], width=event.width)
            
        canvas.bind('<Configure>', on_configure)