from ttkthemes import ThemedStyle
import tkinter as tk
from tkinter import ttk

class CustomTheme:
    def __init__(self, root):
        self.style = ThemedStyle(root)
        
        # Intentar cargar el tema forest primero
        try:
            self.style.set_theme("forest")
        except:
            # Si no está disponible, usar el tema por defecto
            print("Tema forest no disponible, usando tema por defecto")
        
        # Color verde lima del logo
        self.lima_color = "#8DC63F"
        
        # Personalizar elementos
        self.style.configure("TButton",
                           background=self.lima_color,
                           foreground="white")
        
        self.style.configure("TFrame",
                           background="white")
        
        self.style.configure("TLabel",
                           background="white",
                           font=('Arial', 11))
        
        self.style.configure("TEntry",
                           fieldbackground="white")
        
        self.style.configure("TCombobox",
                           fieldbackground="white",
                           background=self.lima_color)