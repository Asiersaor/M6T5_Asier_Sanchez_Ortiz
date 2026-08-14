import tkinter as tk
from tkinter import messagebox

from utils.generador import LONGITUD_CONTRASENA, generar_contrasena


def crear_ventana_principal() -> tk.Tk:
    """Crea la ventana principal de la aplicación."""
    ventana = tk.Tk()
    ventana.title("Generador de contraseñas")
    ventana.geometry("520x300")
    ventana.resizable(False, False)
    return ventana


def crear_interfaz(ventana: tk.Tk) -> None:
    """Construye la interfaz gráfica con controles para longitud y tipos."""
    titulo = tk.Label(
        ventana,
        text="Generador de contraseña",
        font=("Arial", 14, "bold"),
        pady=10,
    )
    titulo.pack()

    # Control de longitud con Spinbox para fijar la cantidad de caracteres.
    frame_longitud = tk.Frame(ventana)
    frame_longitud.pack(pady=(0, 8))

    tk.Label(frame_longitud, text="Longitud:", font=("Arial", 10)).pack(side="left")

    spinbox_longitud = tk.Spinbox(
        frame_longitud,
        from_=8,
        to=64,
        width=5,
        justify="center",
        font=("Arial", 10),
    )
    spinbox_longitud.delete(0, tk.END)
    spinbox_longitud.insert(0, str(LONGITUD_CONTRASENA))
    spinbox_longitud.pack(side="left", padx=(8, 0))

    # Checkboxes para decidir qué tipos de caracteres se incluyen.
    variables_tipos = {
        "minusculas": tk.BooleanVar(value=True),
        "mayusculas": tk.BooleanVar(value=True),
        "numeros": tk.BooleanVar(value=True),
        "simbolos": tk.BooleanVar(value=True),
    }

    frame_tipos = tk.Frame(ventana)
    frame_tipos.pack(pady=4)

    for nombre, variable in variables_tipos.items():
        texto = {
            "minusculas": "Minúsculas",
            "mayusculas": "Mayúsculas",
            "numeros": "Números",
            "simbolos": "Símbolos",
        }[nombre]
        tk.Checkbutton(frame_tipos, text=texto, variable=variable).pack(side="left", padx=8)

    campo_contrasena = tk.Entry(
        ventana,
        width=40,
        font=("Arial", 12),
        justify="center",
        state="readonly",
    )
    campo_contrasena.pack(pady=10)

    def generar_y_mostrar() -> None:
        """Genera la contraseña según la configuración visible en la interfaz."""
        try:
            longitud = int(spinbox_longitud.get())
            tipos_seleccionados = {
                nombre: variable.get() for nombre, variable in variables_tipos.items()
            }
            contrasena = generar_contrasena(longitud, tipos_seleccionados)
        except ValueError as error:
            messagebox.showerror("Configuración no válida", str(error))
            return

        campo_contrasena.config(state="normal")
        campo_contrasena.delete(0, tk.END)
        campo_contrasena.insert(0, contrasena)
        campo_contrasena.config(state="readonly")

    boton_generar = tk.Button(
        ventana,
        text="Generar contraseña",
        command=generar_y_mostrar,
        width=22,
        height=2,
    )
    boton_generar.pack(pady=(0, 10))

    # Genera una contraseña inicial con la configuración por defecto al abrir la app.
    generar_y_mostrar()


def main() -> None:
    """Función principal que arranca la aplicación."""
    ventana = crear_ventana_principal()
    crear_interfaz(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()
