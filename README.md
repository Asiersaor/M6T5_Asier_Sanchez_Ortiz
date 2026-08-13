# Generador de contraseñas - Fase 1

## Descripción general

Este proyecto es una aplicación de escritorio desarrollada en Python con Tkinter para generar contraseñas aleatorias con una longitud fija de 12 caracteres. La Fase 1 se centra en crear una base funcional mínima, clara y documentada, sin incorporar configuraciones avanzadas ni funcionalidades de fases posteriores.

## Objetivo de la fase

La aplicación debe cumplir con los siguientes requisitos:

- Generar una contraseña aleatoria de 12 caracteres.
- Mostrar la contraseña en una interfaz gráfica sencilla.
- Mantener una estructura modular para una futura ampliación.
- Documentar el proyecto y el flujo de trabajo en este README.
- Comentar el código para facilitar su comprensión.

## Stack tecnológico

- Python 3.14 (orientado a esta versión del lenguaje)
- Tkinter para la interfaz gráfica
- Módulo `secrets` para una generación segura y aleatoria

## Estructura del proyecto

- `main.py`: archivo principal que crea la ventana y monta la interfaz.
- `utils/`: carpeta destinada a funciones reutilizables.
- `utils/generador.py`: archivo que contiene la lógica pura del generador de contraseñas.

## Flujo de trabajo

1. Se ejecuta `main.py`.
2. La función `crear_ventana_principal()` crea la ventana principal con Tkinter.
3. La función `crear_interfaz()` configura la interfaz con un campo de texto y un botón.
4. Al pulsar el botón, se llama a `generar_contrasena()` del módulo `utils/generador.py`.
5. La contraseña se muestra en el campo de texto.
6. La aplicación queda a la espera de nuevas interacciones del usuario.

## Lógica del generador

El módulo `utils/generador.py` define la constante `LONGITUD_CONTRASENA = 12`, que fija la cantidad de caracteres. La aleatoriedad se realiza con `secrets.choice()`, seleccionando elementos del conjunto de caracteres permitido:

- Letras minúsculas y mayúsculas
- Números
- Símbolos de puntuación

El uso de `secrets` garantiza una generación más segura que `random` para uso de contraseñas.

## Código principal

### `main.py`

- `crear_ventana_principal()`: crea la ventana raiz de Tkinter.
- `crear_interfaz()`: define el diseño visual de la aplicación.
- `generar_y_mostrar()`: genera la contraseña y la inserta en el campo de texto.
- `main()`: coordina la ejecución final del programa.

### `utils/generador.py`

- `generar_contrasena()`: función central que devuelve una contraseña aleatoria.
- Se valida que la longitud sea positiva antes de continuar.
- Si se recibe un valor inválido, lanza `ValueError` para evitar errores silenciosos.

## Reglas de la fase actual

Esta fase se limita estrictamente a lo siguiente:

- generación de contraseñas con longitud fija de 12 caracteres
- interfaz gráfica mínima con Tkinter
- lógica modular separada en `utils/generador.py`
- documentación y comentarios en el código

No se incluyen funcionalidades de fases posteriores, como:

- longitud configurable
- selección de tipos de caracteres
- guardado en archivo
- generación múltiple

## Cómo ejecutar la aplicación

Desde la carpeta del proyecto, ejecuta:

```bash
python main.py
```

Si la ejecución se realiza en un entorno con interfaz gráfica disponible, la ventana se mostrará y podrás generar una contraseña con un clic.

## Estado actual

La Fase 1 queda implementada con una base mínima funcional y documentada. El flujo principal es simple, legible y preparado para ampliaciones futuras sin alterar la estructura general del proyecto.
