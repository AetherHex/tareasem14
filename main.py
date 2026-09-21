import ctypes
import json
import os
import tkinter as tk

from ui.login_view import LoginView
from ui.main_view import MainView


class RestauranteApp:
    def __init__(self):
        self.configurar_dpi()
        self.root = tk.Tk()
        self.vista_actual = None
        self.preparar_entorno()
        self.iniciar_login()

    def configurar_dpi(self):
        try:
            # Habilita el soporte para alta resolución (DPI awareness) en Windows
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except Exception:
            pass

    def preparar_entorno(self):
        if not os.path.exists("datos"):
            os.makedirs("datos")

        ruta_usuarios = os.path.join("datos", "usuarios.json")
        if not os.path.exists(ruta_usuarios):
            datos_iniciales = [
                {
                    "id": 1,
                    "username": "admin",
                    "password": "123",
                    "rol": "administrador",
                }
            ]
            with open(ruta_usuarios, "w", encoding="utf-8") as f:
                json.dump(datos_iniciales, f, indent=4)

        ruta_productos = os.path.join("datos", "productos.json")
        if not os.path.exists(ruta_productos):
            with open(ruta_productos, "w", encoding="utf-8") as f:
                json.dump([], f)

    def iniciar_login(self):
        # Corrección para el linter: verificación explícita de que no sea None
        if self.vista_actual is not None:
            self.vista_actual.destroy()
        self.vista_actual = LoginView(self.root, self.acceso_concedido)

    def acceso_concedido(self, usuario):
        # Corrección para el linter: verificación explícita de que no sea None
        if self.vista_actual is not None:
            self.vista_actual.destroy()
        self.vista_actual = MainView(self.root, usuario)

    def ejecutar(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = RestauranteApp()
    app.ejecutar()
