# Restaurante App - Gestión de Productos y Usuarios

## Propósito de la Semana 14
La presente actividad corresponde a la Semana 14 de la asignatura Programación Orientada a Objetos. El objetivo principal de esta entrega es la evolución de la interfaz gráfica de usuario mediante el uso adecuado de **componentes, contenedores y gestores de geometría** de la biblioteca Tkinter. Se busca ofrecer una experiencia más clara y amigable para el usuario, incorporando formularios, botones, contenedores y áreas de visualización (tablas) para gestionar productos, todo ello manteniendo estrictamente la arquitectura modular, la separación de responsabilidades y la persistencia en archivos JSON.

## Estructura del Proyecto
El proyecto mantiene la siguiente arquitectura modular:

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md
```

## Componentes y Contenedores Utilizados

Para estructurar y organizar la interfaz visual, se utilizaron los siguientes elementos de `tkinter` y `tkinter.ttk`:

* **Contenedores:** `tk.Tk` (ventana principal), `tk.Frame` / `ttk.Frame` (paneles de agrupación), `ttk.Notebook` (sistema de pestañas para separar Productos y Usuarios), `ttk.LabelFrame` (formulario de entrada con título).
* **Componentes de entrada y control:** `ttk.Entry` (campos de texto), `ttk.Combobox` (listas desplegables para categorías de productos), `ttk.Button` (botones de acción vinculados a funciones mediante `command=`).
* **Componentes de visualización y texto:** `ttk.Label` (etiquetas de texto), `ttk.Treeview` (tablas para mostrar el listado estructurado de productos y usuarios), `ttk.Scrollbar` (barra de desplazamiento vertical para la tabla de productos).
* **Gestores de geometría:** `pack()` para el diseño general de flujo y `grid()` para el alineamiento preciso dentro de los formularios.


## Operaciones Implementadas sobre Productos

La pestaña "Gestión de Productos" permite realizar las siguientes acciones vinculadas directamente al servicio de negocio (`RestauranteServicio`):

* **Registrar:** Agrega un nuevo producto validando que el ID no exista previamente en el sistema y que el formato del precio sea numérico.
* **Cargar/Consultar:** Busca un producto por su ID y rellena automáticamente los campos del formulario para su revisión.
* **Actualizar:** Modifica y guarda la información (nombre, precio, categoría) de un producto previamente consultado.
* **Eliminar:** Borra permanentemente el producto seleccionado del sistema mediante su ID.

## Persistencia Utilizada

La aplicación conserva los datos de manera local y permanente a través de archivos en formato **JSON** (`datos/productos.json` y `datos/usuarios.json`).
La capa de interfaz gráfica (`ui/`) está programada para interactuar exclusivamente con la capa de servicios. De este modo, delega todas las validaciones de dominio y operaciones de lectura/escritura a `RestauranteServicio`, que a su vez se apoya en `ArchivoServicio`, respetando la separación de responsabilidades y evitando la manipulación directa de datos desde los botones.

## Instrucciones de Ejecución

Para iniciar la aplicación:

1. Asegúrese de tener **Python 3.x** instalado en su sistema.
2. Abra una terminal o línea de comandos.
3. Navegue hasta la carpeta raíz del proyecto (`restaurante_app`).
4. Ejecute el siguiente comando para lanzar la aplicación:
```bash
python main.py

```


5. En la ventana de "Inicio de Sesión", ingrese con las credenciales registradas por defecto:
* **Usuario:** `admin`
* **Contraseña:** `123`



```

```
