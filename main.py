import tkinter as tk
from datetime import datetime
from pathlib import Path
from tkinter import messagebox

from utils.generador import (
    LONGITUD_CONTRASENA,
    LOTE_MINIMO,
    LOTE_MAXIMO,
    evaluar_complejidad,
    generar_contrasena,
    generar_lote_contrasenas,
)

RUTA_GUARDADO = Path(__file__).resolve().parent / "passwords_guardadas"


def guardar_contrasena_en_archivo(contrasena: str) -> str:
    """Guarda la contraseña en un archivo TXT con la fecha y la hora del guardado."""
    if not contrasena:
        raise ValueError("No hay ninguna contraseña para guardar.")

    # Se crea una carpeta específica para guardar las contraseñas de forma ordenada.
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


# Mantenemos un alias para no romper la compatibilidad con nombres anteriores.
def guardar_contrasena_archivo(contrasena: str) -> str:
    """Alias para mantener compatibilidad con versiones previas."""
    return guardar_contrasena_en_archivo(contrasena)


def guardar_lote_contrasenas_en_archivo(lista_contrasenas: list[str]) -> str:
    """Fase 5: Guarda un lote de contraseñas en un archivo con fecha y hora."""
    if not lista_contrasenas:
        raise ValueError("No hay ningún lote de contraseñas para guardar.")

    RUTA_GUARDADO.mkdir(exist_ok=True)

    fecha_hora_actual = datetime.now()
    nombre_archivo = f"lote_{fecha_hora_actual.strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    ruta_archivo = RUTA_GUARDADO / nombre_archivo

    with ruta_archivo.open("w", encoding="utf-8") as archivo:
        archivo.write(f"Lote de contraseñas generado: {len(lista_contrasenas)} contraseñas\n")
        archivo.write(
            f"Fecha y hora de guardado: {fecha_hora_actual.strftime('%d/%m/%Y %H:%M:%S')}\n"
        )
        archivo.write("=" * 50 + "\n")
        for i, contrasena in enumerate(lista_contrasenas, 1):
            archivo.write(f"{i}. {contrasena}\n")

    return str(ruta_archivo)


def crear_ventana_principal() -> tk.Tk:
    """Crea la ventana principal de la aplicación."""
    ventana = tk.Tk()
    ventana.title("Generador de contraseñas")
    ventana.geometry("720x650")
    ventana.minsize(600, 550)
    ventana.configure(bg="#f2f5fb")
    ventana.resizable(True, True)
    return ventana


def crear_interfaz_principal(ventana: tk.Tk) -> None:
    """Construye la interfaz gráfica principal de la aplicación."""
    contenedor_principal = tk.Frame(ventana, bg="#f2f5fb", padx=18, pady=18)
    contenedor_principal.pack(fill="both", expand=True)

    # Encabezado principal para mantener la interfaz clara y visualmente ordenada.
    titulo = tk.Label(
        contenedor_principal,
        text="Generador de contraseña",
        font=("Arial", 15, "bold"),
        bg="#f2f5fb",
        fg="#1f2937",
        pady=8,
    )
    titulo.pack(anchor="center")

    panel_configuracion = tk.Frame(contenedor_principal, bg="#ffffff", bd=1, relief="solid")
    panel_configuracion.pack(fill="x", pady=(0, 12), padx=4)

    # Control de longitud con una interfaz más limpia y organizada.
    frame_longitud = tk.Frame(panel_configuracion, bg="#ffffff", padx=12, pady=12)
    frame_longitud.pack(fill="x")

    tk.Label(frame_longitud, text="Longitud:", font=("Arial", 10, "bold"), bg="#ffffff").pack(
        side="left"
    )

    spinbox_longitud = tk.Spinbox(
        frame_longitud,
        from_=8,
        to=64,
        width=6,
        justify="center",
        font=("Arial", 10),
    )
    spinbox_longitud.delete(0, tk.END)
    spinbox_longitud.insert(0, str(LONGITUD_CONTRASENA))
    spinbox_longitud.pack(side="left", padx=(10, 0))

    # Checkbox agrupados para una mejor lectura del usuario y un mejor uso visual.
    frame_tipos = tk.Frame(panel_configuracion, bg="#ffffff", padx=12, pady=12)
    frame_tipos.pack(fill="x")

    variables_tipos = {
        "minusculas": tk.BooleanVar(value=True),
        "mayusculas": tk.BooleanVar(value=True),
        "numeros": tk.BooleanVar(value=True),
        "simbolos": tk.BooleanVar(value=True),
    }

    for nombre, variable in variables_tipos.items():
        texto = {
            "minusculas": "Minúsculas",
            "mayusculas": "Mayúsculas",
            "numeros": "Números",
            "simbolos": "Símbolos",
        }[nombre]
        tk.Checkbutton(frame_tipos, text=texto, variable=variable, bg="#ffffff").pack(
            side="left", padx=8
        )

    # Indicador de complejidad para mostrar el nivel de seguridad de la contraseña.
    etiqueta_complejidad = tk.Label(
        contenedor_principal,
        text="Complejidad: --",
        font=("Arial", 10, "bold"),
        fg="#4b5563",
        bg="#f2f5fb",
    )
    etiqueta_complejidad.pack(anchor="center", pady=(0, 8))

    campo_contrasena = tk.Entry(
        contenedor_principal,
        width=40,
        font=("Arial", 12),
        justify="center",
        state="readonly",
        bd=2,
        relief="sunken",
    )
    campo_contrasena.pack(fill="x", padx=8)

    # Fase 5: Panel de generación en lote con Spinbox (5-10 contraseñas).
    panel_lotes = tk.Frame(contenedor_principal, bg="#f0f0f0", bd=1, relief="solid")
    panel_lotes.pack(fill="x", pady=(10, 0), padx=4)

    frame_lotes = tk.Frame(panel_lotes, bg="#f0f0f0", padx=12, pady=10)
    frame_lotes.pack(fill="x")

    tk.Label(frame_lotes, text="Generar lote:", font=("Arial", 10, "bold"), bg="#f0f0f0").pack(
        side="left"
    )

    spinbox_cantidad_lote = tk.Spinbox(
        frame_lotes,
        from_=LOTE_MINIMO,
        to=LOTE_MAXIMO,
        width=6,
        justify="center",
        font=("Arial", 10),
    )
    spinbox_cantidad_lote.delete(0, tk.END)
    spinbox_cantidad_lote.insert(0, str(LOTE_MINIMO))
    spinbox_cantidad_lote.pack(side="left", padx=(10, 0))

    tk.Label(frame_lotes, text=f"contraseñas (mín: {LOTE_MINIMO}, máx: {LOTE_MAXIMO})", 
             font=("Arial", 9), bg="#f0f0f0").pack(side="left", padx=(8, 0))

    # Fase 5: Panel de resumen de criterios aplicados.
    panel_resumen = tk.Frame(contenedor_principal, bg="#e8f4f8", bd=1, relief="solid")
    panel_resumen.pack(fill="x", pady=(8, 0), padx=4)

    frame_resumen = tk.Frame(panel_resumen, bg="#e8f4f8", padx=12, pady=8)
    frame_resumen.pack(fill="x")

    etiqueta_resumen = tk.Label(
        frame_resumen,
        text="Criterios: Longitud | Tipos | Complejidad | Sin ambiguos",
        font=("Arial", 9, "italic"),
        bg="#e8f4f8",
        fg="#2c5282",
    )
    etiqueta_resumen.pack(anchor="w")

    def actualizar_resumen_criterios() -> None:
        """Actualiza el panel de resumen de criterios aplicados."""
        try:
            longitud = int(spinbox_longitud.get())
            tipos_activos = [t for t, v in variables_tipos.items() if v.get()]
            texto_tipos = ", ".join([t.capitalize() for t in tipos_activos]) or "Ninguno"
            resumen = f"Criterios: Longitud {longitud} | Tipos: {texto_tipos} | Complejidad | Sin caracteres ambiguos"
            etiqueta_resumen.config(text=resumen)
        except Exception:
            pass

    def generar_lote_contrasenas_interfaz() -> None:
        """Genera un lote de contraseñas según la configuración."""
        try:
            cantidad = int(spinbox_cantidad_lote.get())
            longitud = int(spinbox_longitud.get())
            tipos_seleccionados = {
                nombre: variable.get() for nombre, variable in variables_tipos.items()
            }
            lote = generar_lote_contrasenas(cantidad, longitud, tipos_seleccionados)
            
            # Mostrar el lote en una ventana emergente
            ventana_lote = tk.Toplevel(ventana)
            ventana_lote.title(f"Lote de {cantidad} contraseñas")
            ventana_lote.geometry("500x400")

            frame_lote_content = tk.Frame(ventana_lote, bg="#f2f5fb", padx=12, pady=12)
            frame_lote_content.pack(fill="both", expand=True)

            tk.Label(
                frame_lote_content, 
                text=f"Lote de {cantidad} contraseñas generadas:",
                font=("Arial", 11, "bold"),
                bg="#f2f5fb"
            ).pack(anchor="w", pady=(0, 8))

            frame_scrollable = tk.Frame(frame_lote_content, bg="#ffffff", bd=1, relief="sunken")
            frame_scrollable.pack(fill="both", expand=True, pady=(0, 10))

            scrollbar = tk.Scrollbar(frame_scrollable)
            scrollbar.pack(side="right", fill="y")

            text_lote = tk.Text(
                frame_scrollable,
                height=15,
                width=50,
                font=("Courier", 10),
                yscrollcommand=scrollbar.set,
                state="normal"
            )
            text_lote.pack(side="left", fill="both", expand=True)
            scrollbar.config(command=text_lote.yview)

            for i, pwd in enumerate(lote, 1):
                text_lote.insert(tk.END, f"{i}. {pwd}\n")
            text_lote.config(state="disabled")

            frame_botones_lote = tk.Frame(frame_lote_content, bg="#f2f5fb")
            frame_botones_lote.pack(fill="x", pady=(10, 0))

            def copiar_lote():
                """Copia el lote completo al portapapeles."""
                try:
                    texto_completo = "\n".join([f"{i}. {pwd}" for i, pwd in enumerate(lote, 1)])
                    ventana.clipboard_clear()
                    ventana.clipboard_append(texto_completo)
                    messagebox.showinfo("Lote copiado", f"Se copiaron {cantidad} contraseñas al portapapeles.")
                except Exception as error:
                    messagebox.showerror("Error", f"No se pudo copiar: {error}")

            def guardar_lote():
                """Guarda el lote en un archivo."""
                try:
                    ruta = guardar_lote_contrasenas_en_archivo(lote)
                    messagebox.showinfo("Lote guardado", f"Guardado en:\n{ruta}")
                except Exception as error:
                    messagebox.showerror("Error", f"No se pudo guardar: {error}")

            boton_copiar_lote = tk.Button(
                frame_botones_lote,
                text="Copiar lote",
                command=copiar_lote,
                width=20,
                bg="#dbeafe",
                fg="#1e3a8a",
                font=("Arial", 9, "bold"),
            )
            boton_copiar_lote.pack(side="left", padx=(0, 8))

            boton_guardar_lote = tk.Button(
                frame_botones_lote,
                text="Guardar lote",
                command=guardar_lote,
                width=20,
                bg="#dcfce7",
                fg="#166534",
                font=("Arial", 9, "bold"),
            )
            boton_guardar_lote.pack(side="left")

        except (TypeError, ValueError) as error:
            messagebox.showerror("Configuración no válida", str(error))
        except Exception as error:
            messagebox.showerror("Error inesperado", f"No se pudo generar el lote: {error}")

    campo_contrasena.pack(fill="x", padx=8)

    def actualizar_indicador_complejidad(contrasena: str) -> None:
        """Actualiza el texto visible y el color del indicador de complejidad."""
        nivel = evaluar_complejidad(contrasena)
        colores = {
            "Baja": "#b91c1c",
            "Media": "#d97706",
            "Alta": "#15803d",
            "Muy alta": "#065f46",
        }
        etiqueta_complejidad.config(text=f"Complejidad: {nivel}", fg=colores.get(nivel, "#4b5563"))

    def generar_y_mostrar_contrasena() -> None:
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
        actualizar_indicador_complejidad(contrasena)
        actualizar_resumen_criterios()

    def copiar_contrasena_al_portapapeles() -> None:
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

    def guardar_contrasena_actual() -> None:
        """Guarda la contraseña actual en un archivo TXT con fecha y hora."""
        contrasena = campo_contrasena.get()
        if not contrasena:
            messagebox.showwarning("Sin contraseña", "Primero genera una contraseña antes de guardarla.")
            return

        try:
            ruta_archivo = guardar_contrasena_en_archivo(contrasena)
            messagebox.showinfo(
                "Contraseña guardada",
                f"La contraseña se ha guardado correctamente en:\n{ruta_archivo}",
            )
        except Exception as error:
            messagebox.showerror("Error al guardar", f"No se pudo guardar la contraseña: {error}")

    frame_botones = tk.Frame(contenedor_principal, bg="#f2f5fb", pady=12)
    frame_botones.pack()

    boton_generar = tk.Button(
        frame_botones,
        text="Generar contraseña",
        command=generar_y_mostrar_contrasena,
        width=15,
        height=2,
        bg="#2563eb",
        fg="white",
        font=("Arial", 9, "bold"),
    )
    boton_generar.pack(side="left", padx=4)

    boton_copiar = tk.Button(
        frame_botones,
        text="Copiar",
        command=copiar_contrasena_al_portapapeles,
        width=10,
        height=2,
        bg="#dbeafe",
        fg="#1e3a8a",
        font=("Arial", 9, "bold"),
    )
    boton_copiar.pack(side="left", padx=4)

    boton_guardar = tk.Button(
        frame_botones,
        text="Guardar",
        command=guardar_contrasena_actual,
        width=10,
        height=2,
        bg="#dcfce7",
        fg="#166534",
        font=("Arial", 9, "bold"),
    )
    boton_guardar.pack(side="left", padx=4)

    # Fase 5: Botón para generar lotes.
    boton_generar_lote = tk.Button(
        frame_botones,
        text="Generar lote",
        command=generar_lote_contrasenas_interfaz,
        width=12,
        height=2,
        bg="#f59e0b",
        fg="white",
        font=("Arial", 9, "bold"),
    )
    boton_generar_lote.pack(side="left", padx=4)

    # Carga inicial para que la app ya muestre una contraseña al abrirse.
    generar_y_mostrar_contrasena()


def crear_interfaz(ventana: tk.Tk) -> None:
    """Alias para mantener compatibilidad con nombres previos."""
    crear_interfaz_principal(ventana)


def main() -> None:
    """Función principal que arranca la aplicación."""
    ventana = crear_ventana_principal()
    crear_interfaz_principal(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()
