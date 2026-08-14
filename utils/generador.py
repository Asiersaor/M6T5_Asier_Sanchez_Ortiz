import secrets
import string

# Fase 2: la longitud y los tipos de caracteres dejan de estar fijos.
LONGITUD_CONTRASENA = 12
LONGITUD_MINIMA = 8
LONGITUD_MAXIMA = 64

# Diccionario que agrupa los tipos de caracteres permitidos en la aplicación.
# Cada clave representa un tipo y su valor es el conjunto de caracteres asociado.
TIPOS_CARACTERES = {
    "minusculas": string.ascii_lowercase,
    "mayusculas": string.ascii_uppercase,
    "numeros": string.digits,
    "simbolos": string.punctuation,
}


def validar_configuracion(longitud: int, tipos_seleccionados: dict[str, bool]) -> None:
    """Valida que la longitud y la selección de tipos sean correctas."""
    if not isinstance(longitud, int):
        raise ValueError("La longitud debe ser un número entero.")

    if longitud < LONGITUD_MINIMA or longitud > LONGITUD_MAXIMA:
        raise ValueError(
            f"La longitud debe estar entre {LONGITUD_MINIMA} y {LONGITUD_MAXIMA} caracteres."
        )

    if not tipos_seleccionados or not any(tipos_seleccionados.values()):
        raise ValueError("Debes seleccionar al menos un tipo de caracteres.")


def generar_contrasena(
    longitud: int = LONGITUD_CONTRASENA,
    tipos_seleccionados: dict[str, bool] | None = None,
) -> str:
    """Genera una contraseña segura usando los tipos seleccionados por el usuario.

    La contraseña siempre se crea con una longitud válida y con una selección
    no vacía. Si no se indica ningún conjunto, se usa la configuración completa.
    """
    if tipos_seleccionados is None:
        tipos_seleccionados = {nombre: True for nombre in TIPOS_CARACTERES}

    validar_configuracion(longitud, tipos_seleccionados)

    caracteres_disponibles = "".join(
        caracteres
        for tipo, caracteres in TIPOS_CARACTERES.items()
        if tipos_seleccionados.get(tipo, False)
    )

    # Para asegurar que la contraseña incluya al menos un carácter de cada tipo
    # seleccionado, se añaden primero esos caracteres y luego se rellena el resto.
    tipos_activos = [
        tipo for tipo, activo in tipos_seleccionados.items() if activo
    ]

    password = [
        secrets.choice(TIPOS_CARACTERES[tipo])
        for tipo in tipos_activos
    ]

    while len(password) < longitud:
        password.append(secrets.choice(caracteres_disponibles))

    # Se mezcla la lista para que la posición de los caracteres no siga un patrón
    # predecible y para evitar que siempre aparezcan primero los del mismo tipo.
    secrets.SystemRandom().shuffle(password)
    return "".join(password)[:longitud]
