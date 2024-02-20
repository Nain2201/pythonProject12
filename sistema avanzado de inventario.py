import json

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.id] = producto

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            print("Producto eliminado.")
        else:
            print("El producto no existe en el inventario.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].cantidad = cantidad
            if precio is not None:
                self.productos[id].precio = precio
            print("Producto actualizado.")
        else:
            print("El producto no existe en el inventario.")

    def buscar_producto_por_nombre(self, nombre):
        for producto in self.productos.values():
            if producto.nombre == nombre:
                print(producto)
                return
        print("Producto no encontrado.")

    def mostrar_inventario(self):
        for producto in self.productos.values():
            print(producto)

    def guardar_inventario(self, filename):
        with open(filename, 'w') as file:
            json.dump([vars(p) for p in self.productos.values()], file)

    def cargar_inventario(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            for item in data:
                producto = Producto(**item)
                self.agregar_producto(producto)

def menu():
    print("\nMenú:")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar inventario")
    print("6. Guardar inventario")
    print("7. Cargar inventario")
    print("8. Salir")

def main():
    inventario = Inventario()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad del producto: "))
            precio = float(input("Ingrese precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == '2':
            id = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == '3':
            id = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Ingrese nueva cantidad (deje vacío para mantener): ")
            precio = input("Ingrese nuevo precio (deje vacío para mantener): ")
            if cantidad:
                cantidad = int(cantidad)
            if precio:
                precio = float(precio)
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == '4':
            nombre = input("Ingrese nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == '5':
            inventario.mostrar_inventario()

        elif opcion == '6':
            filename = input("Ingrese el nombre del archivo para guardar: ")
            inventario.guardar_inventario(filename)

        elif opcion == '7':
            filename = input("Ingrese el nombre del archivo para cargar: ")
            inventario.cargar_inventario(filename)

        elif opcion == '8':
            print("Saliendo del programa.")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
