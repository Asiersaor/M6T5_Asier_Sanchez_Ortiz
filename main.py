import tkinter as tk
from datetime import datetime
from pathlib import Path
from tkinter import messagebox

from utils.generador import LONGITUD_CONTRASENA, evaluar_complejidad, generar_contrasena

RUTA_GUARDADO = Path(__file__).resolve().parent / "passwords_guardadas"


def guardar_contrasena_archivo(contrasena: str) -> str:
    """Guarda la contraseña en un archivo TXT con la fecha y hora del guardado."""
    if not contrasena:
        raise ValueError("No hay ninguna contraseña para guardar.")

    # Se crea una carpeta específica para almacenar las contraseñas guardadas.
    RUTA_GUARDADO.mkdir(exist_ok=True)

    fecha_hora_actual = datetime.now()
    nombre_archivo = f"password_{fecha_hora_actual.strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    ruta_archivo = RUTA_GUARDADO / nombre_archivo

    with ruta_archivo.open("w", encoding="utf-8") as archivo:
        archivo.write(f"Contraseña generada: {contrasena}\n")
        archivo.write(
            f"Fecha y hora de guardado: {fecha_hora_actual.strftime('%d/%m/%Y %H:%M:%S')}\n"
        )

    return str(ruta_archivo)


def crear_ventana_principal() -> tk.Tk:
    """Crea la ventana principal de la aplicación."""
    ventana = tk.Tk()
    ventana.title("Generador de contraseñas")
    ventana.geometry("560x360")
    ventana.resizable(False, False)
    return ventana


def crear_interfaz(ventana: tk.Tk) -> None:
    """Construye la interfaz gráfica con controles para longitud, tipos y opciones."""
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

    # Indicador de complejidad para mostrar el nivel de seguridad de la contraseña.
    label_complejidad = tk.Label(
        ventana,
        text="Complejidad: --",
        font=("Arial", 10, "bold"),
        fg="gray",
    )
    label_complejidad.pack(pady=(0, 6))

    campo_contrasena = tk.Entry(
        ventana,
        width=40,
        font=("Arial", 12),
        justify="center",
        state="readonly",
    )
    campo_contrasena.pack(pady=10)

    def actualizar_complejidad(contrasena: str) -> None:
        """Actualiza el texto visible y el color del indicador de complejidad."""
        nivel = evaluar_complejidad(contrasena)
        colores = {
            "Baja": "#b22222",
            "Media": "#d97706",
            "Alta": "#15803d",
            "Muy alta": "#166534",
        }
        label_complejidad.config(text=f"Complejidad: {nivel}", fg=colores.get(nivel, "gray"))

    def generar_y_mostrar() -> None:
        """Genera la contraseña según la configuración visible en la interfaz."""
        try:
            longitud = int(spinbox_longitud.get())
            tipos_seleccionados = {
                nombre: variable.get() for nombre, variable in variables_tipos.items()
            }
            contrasena = generar_contrasena(longitud, tipos_seleccionados)
        except (TypeError, ValueError) as error:
            messagebox.showerror("Configuración no válida", str(error))
            return
        except Exception as error:
            messagebox.showerror("Error inesperado", f"No se pudo generar la contraseña: {error}")
            return

        campo_contrasena.config(state="normal")
        campo_contrasena.delete(0, tk.END)
        campo_contrasena.insert(0, contrasena)
        campo_contrasena.config(state="readonly")
        actualizar_complejidad(contrasena)

    def copiar_al_portapapeles() -> None:
        """Copia la contraseña actual al portapapeles del sistema."""
        contrasena = campo_contrasena.get()
        if not contrasena:
            messagebox.showwarning("Sin contraseña", "Primero genera una contraseña antes de copiarla.")
            return

        try:
            ventana.clipboard_clear()
            ventana.clipboard_append(contrasena)
            messagebox.showinfo("Copia completada", "La contraseña se ha copiado al portapapeles.")
        except Exception as error:
            messagebox.showerror("Error al copiar", f"No se pudo copiar al portapapeles: {error}")

    def guardar_en_archivo() -> None:
        """Guarda la contraseña actual en un archivo TXT con fecha y hora."""
        contrasena = campo_contrasena.get()
        if not contrasena:
            messagebox.showwarning("Sin contraseña", "Primero genera una contraseña antes de guardarla.")
            return

        try:
            ruta_archivo = guardar_contrasena_archivo(contrasena)
            messagebox.showinfo(
                "Contraseña guardada",
                f"La contraseña se ha guardado correctamente en:\n{ruta_archivo}",
            )
        except Exception as error:
            messagebox.showerror("Error al guardar", f"No se pudo guardar la contraseña: {error}")

    # Se agrupan botones de acción para mantener la interfaz clara y usable.
    frame_botones = tk.Frame(ventana)
    frame_botones.pack(pady=(0, 10))

    boton_generar = tk.Button(
        frame_botones,
        text="Generar contraseña",
        command=generar_y_mostrar,
        width=18,
        height=2,
    )
    boton_generar.pack(side="left", padx=8)

    boton_copiar = tk.Button(
        frame_botones,
        text="Copiar",
        command=copiar_al_portapapeles,
        width=12,
        height=2,
    )
    boton_copiar.pack(side="left", padx=8)

    boton_guardar = tk.Button(
        frame_botones,
        text="Guardar",
        command=guardar_en_archivo,
        width=12,
        height=2,
    )
    boton_guardar.pack(side="left", padx=8)

    # Genera una contraseña inicial con la configuración por defecto al abrir la app.
    generar_y_mostrar()


def main() -> None:
    """Función principal que arranca la aplicación."""
    ventana = crear_ventana_principal()
    crear_interfaz(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()
