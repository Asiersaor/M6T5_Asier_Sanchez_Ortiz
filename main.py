import tkinter as tk

from utils.generador import generar_contrasena


def crear_ventana_principal() -> tk.Tk:
    """Crea la ventana principal de la aplicación."""
    ventana = tk.Tk()
    ventana.title("Generador de contraseñas")
    ventana.geometry("420x180")
    ventana.resizable(False, False)
    return ventana


def crear_interfaz(ventana: tk.Tk) -> None:
    """Construye la interfaz gráfica con un campo de texto y un botón."""
    titulo = tk.Label(
        ventana,
        text="Generador de contraseña",
        font=("Arial", 14, "bold"),
        pady=10,
    )
    titulo.pack()

    campo_contrasena = tk.Entry(
        ventana,
        width=32,
        font=("Arial", 12),
        justify="center",
        state="readonly",
    )
    campo_contrasena.pack(pady=8)

    def generar_y_mostrar() -> None:
        """Genera una contraseña de 12 caracteres y la muestra en pantalla."""
        contrasena = generar_contrasena()
        campo_contrasena.config(state="normal")
        campo_contrasena.delete(0, tk.END)
        campo_contrasena.insert(0, contrasena)
        campo_contrasena.config(state="readonly")

    boton_generar = tk.Button(
        ventana,
        text="Generar contraseña",
        command=generar_y_mostrar,
        width=20,
        height=2,
    )
    boton_generar.pack(pady=8)

    # Se genera una contraseña inicial al abrir la aplicación para que
    # la interfaz muestre un ejemplo desde el inicio.
    generar_y_mostrar()


def main() -> None:
    """Función principal que arranca la aplicación."""
    ventana = crear_ventana_principal()
    crear_interfaz(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()
