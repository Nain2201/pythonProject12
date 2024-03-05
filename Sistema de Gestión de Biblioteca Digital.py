class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo_autor = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}
        self.usuarios_registrados = set()

    def agregar_libro(self, libro):
        self.libros_disponibles[libro.isbn] = libro

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]

    def registrar_usuario(self, usuario):
        self.usuarios_registrados.add(usuario.id_usuario)

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            self.usuarios_registrados.remove(id_usuario)

    def prestar_libro(self, isbn, usuario):
        if isbn in self.libros_disponibles:
            libro = self.libros_disponibles[isbn]
            if libro not in usuario.libros_prestados:
                usuario.libros_prestados.append(libro)
                del self.libros_disponibles[isbn]
                print(f"Libro '{libro.titulo_autor}' prestado a {usuario.nombre}.")
            else:
                print(f"El usuario ya tiene prestado el libro '{libro.titulo_autor}'.")
        else:
            print("El libro no está disponible en la biblioteca.")

    def devolver_libro(self, isbn, usuario):
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                self.agregar_libro(libro)
                usuario.libros_prestados.remove(libro)
                print(f"Libro '{libro.titulo_autor}' devuelto.")
                return
        print("El usuario no tiene prestado este libro.")

    def buscar_libros_por_titulo(self, titulo):
        libros_encontrados = [libro for libro in self.libros_disponibles.values() if titulo.lower() in libro.titulo_autor[0].lower()]
        if libros_encontrados:
            return libros_encontrados
        else:
            return "No se encontraron libros con ese título."

    def buscar_libros_por_autor(self, autor):
        libros_encontrados = [libro for libro in self.libros_disponibles.values() if autor.lower() in libro.titulo_autor[1].lower()]
        if libros_encontrados:
            return libros_encontrados
        else:
            return "No se encontraron libros de ese autor."

    def buscar_libros_por_categoria(self, categoria):
        libros_encontrados = [libro for libro in self.libros_disponibles.values() if categoria.lower() == libro.categoria.lower()]
        if libros_encontrados:
            return libros_encontrados
        else:
            return "No se encontraron libros en esa categoría."

    def listar_libros_prestados(self, usuario):
        if usuario.libros_prestados:
            return [libro.titulo_autor for libro in usuario.libros_prestados]
        else:
            return "El usuario no tiene libros prestados."


# Prueba del sistema
if __name__ == "__main__":
    # Crear algunos libros
    libro1 = Libro("La sombra del viento", "Carlos Ruiz Zafón", "Ficción", "9788408043640")
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", "9780307350431")
    libro3 = Libro("Python for Data Science For Dummies", "John Paul Mueller", "Informática", "9781119547624")

    # Crear algunos usuarios
    usuario1 = Usuario("Juan", 1)
    usuario2 = Usuario("María", 2)

    # Crear biblioteca
    biblioteca = Biblioteca()

    # Agregar libros a la biblioteca
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    # Registrar usuarios
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Préstamo de libros
    biblioteca.prestar_libro("9788408043640", usuario1)
    biblioteca.prestar_libro("9780307350431", usuario2)

    # Listar libros prestados por usuario
    print(biblioteca.listar_libros_prestados(usuario1))
    print(biblioteca.listar_libros_prestados(usuario2))

    # Búsqueda de libros
    print(biblioteca.buscar_libros_por_titulo("cien"))
    print(biblioteca.buscar_libros_por_autor("Carlos Ruiz Zafón"))
    print(biblioteca.buscar_libros_por_categoria("informática"))

    # Devolución de libros
    biblioteca.devolver_libro("9788408043640", usuario1)
    biblioteca.devolver_libro("9780307350431", usuario2)

    # Lista de libros disponibles después de devoluciones
    print(biblioteca.libros_disponibles)

