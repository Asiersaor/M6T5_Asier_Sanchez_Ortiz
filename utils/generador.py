import secrets
import string

# Este valor queda fijo por la especificación de la Fase 1.
LONGITUD_CONTRASENA = 12

# Conjunto de caracteres que se usan para generar la contraseña.
# Se incluye letras, números y signos para ofrecer una contraseña robusta
# sin añadir configuraciones avanzadas que no forman parte de esta fase.
CARACTERES_PERMITIDOS = string.ascii_letters + string.digits + string.punctuation


def generar_contrasena(longitud: int = LONGITUD_CONTRASENA) -> str:
    """Genera una contraseña aleatoria con la longitud indicada.

    Por defecto utiliza la longitud fija de 12 caracteres pedida en la Fase 1.
    La función usa secrets.choice para garantizar una aleatoriedad segura.
    """
    if longitud <= 0:
        raise ValueError("La longitud de la contraseña debe ser mayor que cero.")

    return "".join(secrets.choice(CARACTERES_PERMITIDOS) for _ in range(longitud))
