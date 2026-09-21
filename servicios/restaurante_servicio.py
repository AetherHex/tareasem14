import os

from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:
    def __init__(self):
        self.ruta_usuarios = os.path.join("datos", "usuarios.json")
        self.ruta_productos = os.path.join("datos", "productos.json")

    def autenticar(self, username, password):
        usuarios_data = ArchivoServicio.leer_json(self.ruta_usuarios)
        for u_data in usuarios_data:
            if str(u_data.get("username")) == str(username) and str(
                u_data.get("password")
            ) == str(password):
                return Usuario.from_dict(u_data)
        return None

    def obtener_usuarios(self):
        usuarios_data = ArchivoServicio.leer_json(self.ruta_usuarios)
        return [Usuario.from_dict(u) for u in usuarios_data]

    def obtener_productos(self):
        productos_data = ArchivoServicio.leer_json(self.ruta_productos)
        return [Producto.from_dict(p) for p in productos_data]

    def registrar_producto(self, id_producto, nombre, precio, categoria):
        productos = self.obtener_productos()
        for p in productos:
            if str(p.id_producto) == str(id_producto):
                raise ValueError("El ID del producto ya existe.")

        try:
            precio = float(precio)
        except ValueError:
            raise ValueError("El precio debe ser un valor numérico.")

        nuevo_producto = Producto(id_producto, nombre, precio, categoria)
        productos.append(nuevo_producto)
        self._guardar_productos(productos)

    def obtener_producto_por_id(self, id_producto):
        productos = self.obtener_productos()
        for p in productos:
            if str(p.id_producto) == str(id_producto):
                return p
        return None

    def actualizar_producto(self, id_producto, nombre, precio, categoria):
        productos = self.obtener_productos()
        actualizado = False

        try:
            precio = float(precio)
        except ValueError:
            raise ValueError("El precio debe ser un valor numérico.")

        for p in productos:
            if str(p.id_producto) == str(id_producto):
                p.nombre = nombre
                p.precio = precio
                p.categoria = categoria
                actualizado = True
                break

        if not actualizado:
            raise ValueError("Producto no encontrado para actualizar.")

        self._guardar_productos(productos)

    def eliminar_producto(self, id_producto):
        productos = self.obtener_productos()
        productos_filtrados = [
            p for p in productos if str(p.id_producto) != str(id_producto)
        ]

        if len(productos) == len(productos_filtrados):
            raise ValueError("Producto no encontrado.")

        self._guardar_productos(productos_filtrados)

    def _guardar_productos(self, productos):
        datos = [p.to_dict() for p in productos]
        ArchivoServicio.guardar_json(self.ruta_productos, datos)
