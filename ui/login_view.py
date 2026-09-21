import tkinter as tk
from tkinter import messagebox, ttk

from servicios.restaurante_servicio import RestauranteServicio


class LoginView(tk.Frame):
    def __init__(self, parent, on_success):
        super().__init__(parent)
        self.parent = parent
        self.on_success = on_success
        self.servicio = RestauranteServicio()
        self.configurar_ui()

    def configurar_ui(self):
        self.parent.title("Inicio de Sesión")
        self.parent.geometry("300x350")
        self.pack(expand=True, fill="both", padx=20, pady=20)

        ttk.Label(self, text="Restaurante App", font=("Arial", 16, "bold")).pack(
            pady=15
        )

        ttk.Label(self, text="Usuario:").pack(anchor="w")
        self.entry_usuario = ttk.Entry(self)
        self.entry_usuario.pack(fill="x", pady=5)

        ttk.Label(self, text="Contraseña:").pack(anchor="w")
        self.entry_password = ttk.Entry(self, show="*")
        self.entry_password.pack(fill="x", pady=5)

        ttk.Button(self, text="Ingresar", command=self.validar_login).pack(pady=20)

    def validar_login(self):
        usuario = self.entry_usuario.get()
        password = self.entry_password.get()

        if not usuario or not password:
            messagebox.showerror("Error", "Llene todos los campos requeridos.")
            return

        usuario_valido = self.servicio.autenticar(usuario, password)
        if usuario_valido:
            self.on_success(usuario_valido)
        else:
            messagebox.showerror("Error", "Credenciales incorrectas.")
