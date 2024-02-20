class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def __init__(self, archivo):
        self.productos = []
        self.archivo = archivo
        self.cargar_inventario_desde_archivo()

    def agregar_producto(self, producto):
        for p in self.productos:
            if p.id == producto.id:
                print("Error: Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        self.guardar_inventario_en_archivo()
        print("Producto añadido con éxito.")

    def eliminar_producto(self, id):
        for i, producto in enumerate(self.productos):
            if producto.id == id:
                del self.productos[i]
                self.guardar_inventario_en_archivo()
                print("Producto eliminado.")
                return
        print("Error: Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.id == id:
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                self.guardar_inventario_en_archivo()
                print("Producto actualizado.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = []
        for producto in self.productos:
            if nombre.lower() in producto.nombre.lower():
                encontrados.append(producto)
        if encontrados:
            for p in encontrados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if self.productos:
            for producto in self.productos:
                print(producto)
        else:
            print("El inventario está vacío.")

    def cargar_inventario_desde_archivo(self):
        try:
            with open(self.archivo, 'r') as file:
                for line in file:
                    id, nombre, cantidad, precio = line.strip().split(',')
                    producto = Producto(id, nombre, int(cantidad), float(precio))
                    self.productos.append(producto)
        except FileNotFoundError:
            print(f"Archivo {self.archivo} no encontrado. Se creará uno nuevo.")
            self.guardar_inventario_en_archivo()

    def guardar_inventario_en_archivo(self):
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.productos:
                    file.write(f"{producto.id},{producto.nombre},{producto.cantidad},{producto.precio}\n")
        except PermissionError:
            print("Error: Permiso denegado para escribir en el archivo.")


def mostrar_menu():
    print("\nMenú:")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Mostrar todos los productos")
    print("6. Salir")


if __name__ == "__main__":
    archivo_inventario = "inventario.txt"
    inventario = Inventario(archivo_inventario)

    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id = input("Ingrese el ID del producto que desea eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = input("Ingrese el ID del producto que desea actualizar: ")
            cantidad = input("Ingrese la nueva cantidad del producto (deje en blanco para omitir): ")
            precio = input("Ingrese el nuevo precio del producto (deje en blanco para omitir): ")
            if cantidad:
                cantidad = int(cantidad)
            if precio:
                precio = float(precio)
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese el nombre (o parte del nombre) del producto que desea buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

