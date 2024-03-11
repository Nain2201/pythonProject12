import tkinter as tk

class GUIApp:
    def __init__(self, master):
        self.master = master
        master.title("Aplicación de Interfaz Gráfica")

        self.label = tk.Label(master, text="Ingrese información:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.add_button = tk.Button(master, text="Agregar", command=self.add_info)
        self.add_button.pack()

        self.clear_button = tk.Button(master, text="Limpiar", command=self.clear_info)
        self.clear_button.pack()

        self.info_listbox = tk.Listbox(master)
        self.info_listbox.pack()

    def add_info(self):
        info_text = self.entry.get()
        if info_text:
            self.info_listbox.insert(tk.END, info_text)
            self.entry.delete(0, tk.END)  # Limpiar el campo de entrada después de agregar la información

    def clear_info(self):
        selected_indices = self.info_listbox.curselection()
        if selected_indices:
            for index in selected_indices[::-1]:
                self.info_listbox.delete(index)
        else:
            self.info_listbox.delete(0, tk.END)  # Limpiar toda la lista si no hay elementos seleccionados

def main():
    root = tk.Tk()
    app = GUIApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
