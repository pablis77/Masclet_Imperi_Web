import tkinter as tk
from tkinter import ttk
from tkinter import ttk, TclError

class MessageSystem:
    def __init__(self, parent_frame):
        """Inicializa el sistema de mensajes"""
        self.message_frame = None
        self.parent_frame = parent_frame
        self.current_message = None
        self.timer = None

    def show_message(self, message, message_type='info', duration=3000):
        """Muestra un mensaje en la interfaz
        message_type puede ser: 'success', 'error', 'info'
        duration en milisegundos"""
        # Si hay un mensaje previo, eliminarlo
        if self.message_frame:
            self.message_frame.destroy()
            if self.timer:
                self.parent_frame.after_cancel(self.timer)

        # Obtener la ventana principal
        top_window = self.parent_frame.winfo_toplevel()
        
        # Crear nuevo frame para el mensaje
        self.message_frame = tk.Frame(top_window, bg='white')
        
        # Usar place para posicionar el mensaje en el centro inferior
        self.message_frame.place(
            relx=0.5,
            rely=0.9,  # 90% desde arriba
            anchor='center'
        )

        # Definir colores según el tipo de mensaje
        colors = {
            'success': '#4CAF50',  # Verde
            'error': '#F44336',    # Rojo
            'info': '#2196F3'      # Azul
        }
        
        # Crear el mensaje con el estilo correspondiente
        message_label = tk.Label(
            self.message_frame,
            text=message,
            bg='white',
            fg=colors.get(message_type, colors['info']),
            font=('Arial', 14, 'bold')
        )
        message_label.pack(pady=10)

        # Levantar el frame del mensaje a la capa superior
        self.message_frame.lift()

        # Programar la eliminación del mensaje
        self.timer = self.parent_frame.after(duration, self.hide_message)

    def hide_message(self):
        """Oculta el mensaje actual"""
        try:
            if hasattr(self, 'timer') and self.timer:
                self.parent_frame.after_cancel(self.timer)
                self.timer = None
            if hasattr(self, 'message_frame') and self.message_frame and self.message_frame.winfo_exists():
                self.message_frame.destroy()
                self.message_frame = None
        except tk.TclError as e:
            print(f"Error al ocultar mensaje: {e}")