import tkinter as tk
from tkinter import messagebox, ttk

from servicios.restaurante_servicio import RestauranteServicio


class MainView(tk.Frame):
    def __init__(self, parent, usuario_actual):
        super().__init__(parent)
        self.parent = parent
        self.usuario_actual = usuario_actual
        self.servicio = RestauranteServicio()

        self.parent.title("Sistema de Gestión - Restaurante")
        self.parent.geometry("850x450")
        self.pack(expand=True, fill="both")

        self.crear_interfaz()

    def crear_interfaz(self):
        top_frame = ttk.Frame(self)
        top_frame.pack(fill="x", padx=10, pady=5)
        ttk.Label(
            top_frame,
            text=f"Bienvenido: {self.usuario_actual.username} | Rol: {self.usuario_actual.rol}",
            font=("Arial", 11, "bold"),
        ).pack(side="left")

        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill="both", padx=10, pady=10)

        self.tab_productos = ttk.Frame(notebook)
        self.tab_usuarios = ttk.Frame(notebook)

        notebook.add(self.tab_productos, text="Gestión de Productos")
        notebook.add(self.tab_usuarios, text="Consulta de Usuarios")

        self.configurar_tab_productos()
        self.configurar_tab_usuarios()

    def configurar_tab_productos(self):
        left_frame = ttk.Frame(self.tab_productos)
        left_frame.pack(side="left", fill="y", padx=10, pady=10)

        form_frame = ttk.LabelFrame(left_frame, text="Datos del Producto")
        form_frame.pack(fill="x", pady=5)

        ttk.Label(form_frame, text="ID / Código:").grid(
            row=0, column=0, padx=5, pady=5, sticky="e"
        )
        self.ent_id = ttk.Entry(form_frame)
        self.ent_id.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Nombre:").grid(
            row=1, column=0, padx=5, pady=5, sticky="e"
        )
        self.ent_nombre = ttk.Entry(form_frame)
        self.ent_nombre.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Precio:").grid(
            row=2, column=0, padx=5, pady=5, sticky="e"
        )
        self.ent_precio = ttk.Entry(form_frame)
        self.ent_precio.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Categoría:").grid(
            row=3, column=0, padx=5, pady=5, sticky="e"
        )
        self.cbx_categoria = ttk.Combobox(
            form_frame,
            values=["Bebida", "Plato Fuerte", "Postre", "Entrada"],
            state="readonly",
        )
        self.cbx_categoria.grid(row=3, column=1, padx=5, pady=5)

        btn_frame = ttk.Frame(left_frame)
        btn_frame.pack(fill="x", pady=10)

        ttk.Button(btn_frame, text="Registrar", command=self.registrar_producto).grid(
            row=0, column=0, padx=3, pady=3, sticky="ew"
        )
        ttk.Button(
            btn_frame, text="Cargar/Consultar", command=self.cargar_producto
        ).grid(row=0, column=1, padx=3, pady=3, sticky="ew")
        ttk.Button(btn_frame, text="Actualizar", command=self.actualizar_producto).grid(
            row=1, column=0, padx=3, pady=3, sticky="ew"
        )
        ttk.Button(btn_frame, text="Eliminar", command=self.eliminar_producto).grid(
            row=1, column=1, padx=3, pady=3, sticky="ew"
        )
        ttk.Button(
            btn_frame, text="Limpiar Formulario", command=self.limpiar_campos
        ).grid(row=2, column=0, columnspan=2, padx=3, pady=10, sticky="ew")

        btn_frame.columnconfigure(0, weight=1)
        btn_frame.columnconfigure(1, weight=1)

        right_frame = ttk.Frame(self.tab_productos)
        right_frame.pack(side="right", expand=True, fill="both", padx=10, pady=10)

        scroll = ttk.Scrollbar(right_frame)
        scroll.pack(side="right", fill="y")

        self.tree_productos = ttk.Treeview(
            right_frame,
            columns=("id", "nombre", "precio", "categoria"),
            show="headings",
            yscrollcommand=scroll.set,
        )
        scroll.config(command=self.tree_productos.yview)

        self.tree_productos.heading("id", text="ID")
        self.tree_productos.heading("nombre", text="Nombre")
        self.tree_productos.heading("precio", text="Precio ($)")
        self.tree_productos.heading("categoria", text="Categoría")

        self.tree_productos.column("id", width=80, anchor="center")
        self.tree_productos.column("precio", width=100, anchor="center")
        self.tree_productos.column("categoria", width=120, anchor="center")

        self.tree_productos.pack(expand=True, fill="both")
        self.actualizar_tabla_productos()

    def configurar_tab_usuarios(self):
        frame = ttk.Frame(self.tab_usuarios)
        frame.pack(expand=True, fill="both", padx=10, pady=10)

        self.tree_usuarios = ttk.Treeview(
            frame, columns=("id", "username", "rol"), show="headings"
        )
        self.tree_usuarios.heading("id", text="ID")
        self.tree_usuarios.heading("username", text="Nombre de Usuario")
        self.tree_usuarios.heading("rol", text="Rol del Sistema")

        self.tree_usuarios.column("id", width=50, anchor="center")

        self.tree_usuarios.pack(expand=True, fill="both")
        self.actualizar_tabla_usuarios()

    def actualizar_tabla_productos(self):
        for item in self.tree_productos.get_children():
            self.tree_productos.delete(item)
        productos = self.servicio.obtener_productos()
        for p in productos:
            self.tree_productos.insert(
                "",
                "end",
                values=(p.id_producto, p.nombre, f"{p.precio:.2f}", p.categoria),
            )

    def actualizar_tabla_usuarios(self):
        for item in self.tree_usuarios.get_children():
            self.tree_usuarios.delete(item)
        usuarios = self.servicio.obtener_usuarios()
        for u in usuarios:
            self.tree_usuarios.insert("", "end", values=(u.id, u.username, u.rol))

    def limpiar_campos(self):
        self.ent_id.delete(0, tk.END)
        self.ent_nombre.delete(0, tk.END)
        self.ent_precio.delete(0, tk.END)
        self.cbx_categoria.set("")

    def registrar_producto(self):
        id_prod = self.ent_id.get().strip()
        nom = self.ent_nombre.get().strip()
        pre = self.ent_precio.get().strip()
        cat = self.cbx_categoria.get().strip()

        if not (id_prod and nom and pre and cat):
            messagebox.showwarning(
                "Advertencia", "Debe completar todos los campos del formulario."
            )
            return

        try:
            self.servicio.registrar_producto(id_prod, nom, pre, cat)
            self.actualizar_tabla_productos()
            self.limpiar_campos()
            messagebox.showinfo("Éxito", "Producto registrado correctamente.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def cargar_producto(self):
        id_prod = self.ent_id.get().strip()
        if not id_prod:
            messagebox.showwarning(
                "Advertencia", "Ingrese el ID del producto que desea consultar."
            )
            return

        producto = self.servicio.obtener_producto_por_id(id_prod)
        if producto:
            self.limpiar_campos()
            self.ent_id.insert(0, producto.id_producto)
            self.ent_nombre.insert(0, producto.nombre)
            self.ent_precio.insert(0, str(producto.precio))
            self.cbx_categoria.set(producto.categoria)
        else:
            messagebox.showerror(
                "No encontrado", "No existe un producto con el ID especificado."
            )

    def actualizar_producto(self):
        id_prod = self.ent_id.get().strip()
        nom = self.ent_nombre.get().strip()
        pre = self.ent_precio.get().strip()
        cat = self.cbx_categoria.get().strip()

        if not (id_prod and nom and pre and cat):
            messagebox.showwarning(
                "Advertencia", "Debe completar todos los campos para actualizar."
            )
            return

        try:
            self.servicio.actualizar_producto(id_prod, nom, pre, cat)
            self.actualizar_tabla_productos()
            self.limpiar_campos()
            messagebox.showinfo("Éxito", "Información del producto actualizada.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def eliminar_producto(self):
        id_prod = self.ent_id.get().strip()
        if not id_prod:
            messagebox.showwarning(
                "Advertencia", "Ingrese el ID del producto que desea eliminar."
            )
            return

        if messagebox.askyesno(
            "Confirmación", f"¿Está seguro de eliminar el producto con ID '{id_prod}'?"
        ):
            try:
                self.servicio.eliminar_producto(id_prod)
                self.actualizar_tabla_productos()
                self.limpiar_campos()
                messagebox.showinfo("Éxito", "Producto eliminado del sistema.")
            except ValueError as e:
                messagebox.showerror("Error", str(e))
