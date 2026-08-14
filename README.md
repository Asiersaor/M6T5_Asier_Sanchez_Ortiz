# Generador de contraseñas - Fase 1 y Fase 2

## Fase 1: Esqueleto mínimo

### Descripción general

Este proyecto es una aplicación de escritorio desarrollada en Python con Tkinter para generar contraseñas aleatorias con una longitud fija de 12 caracteres. La Fase 1 se centra en crear una base funcional mínima, clara y documentada, sin incorporar configuraciones avanzadas ni funcionalidades de fases posteriores.

### Objetivo de la fase

La aplicación debe cumplir con los siguientes requisitos:

- Generar una contraseña aleatoria de 12 caracteres.
- Mostrar la contraseña en una interfaz gráfica sencilla.
- Mantener una estructura modular para una futura ampliación.
- Documentar el proyecto y el flujo de trabajo en este README.
- Comentar el código para facilitar su comprensión.

### Stack tecnológico

- Python 3.14
- Tkinter para la interfaz gráfica
- Módulo `secrets` para una generación segura y aleatoria

### Estructura del proyecto

- `main.py`: archivo principal que crea la ventana y monta la interfaz.
- `utils/`: carpeta destinada a funciones reutilizables.
- `utils/generador.py`: archivo que contiene la lógica pura del generador de contraseñas.

### Flujo de trabajo

1. Se ejecuta `main.py`.
2. La función `crear_ventana_principal()` crea la ventana principal con Tkinter.
3. La función `crear_interfaz()` configura la interfaz con un campo de texto y un botón.
4. Al pulsar el botón, se llama a `generar_contrasena()` del módulo `utils/generador.py`.
5. La contraseña se muestra en el campo de texto.
6. La aplicación queda a la espera de nuevas interacciones del usuario.

### Lógica del generador

El módulo `utils/generador.py` define la constante `LONGITUD_CONTRASENA = 12`, que fija la cantidad de caracteres. La aleatoriedad se realiza con `secrets.choice()`, seleccionando elementos del conjunto de caracteres permitido:

- Letras minúsculas y mayúsculas
- Números
- Símbolos de puntuación

El uso de `secrets` garantiza una generación más segura que `random` para uso de contraseñas.

### Código principal

#### `main.py`

- `crear_ventana_principal()`: crea la ventana raíz de Tkinter.
- `crear_interfaz()`: define el diseño visual de la aplicación.
- `generar_y_mostrar()`: genera la contraseña y la inserta en el campo de texto.
- `main()`: coordina la ejecución final del programa.

#### `utils/generador.py`

- `generar_contrasena()`: función central que devuelve una contraseña aleatoria.
- Se valida que la longitud sea positiva antes de continuar.
- Si se recibe un valor inválido, lanza `ValueError` para evitar errores silenciosos.

### Reglas de la fase actual

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

### Cómo ejecutar la aplicación

Desde la carpeta del proyecto, ejecuta:

```bash
python main.py
```

Si la ejecución se realiza en un entorno con interfaz gráfica disponible, la ventana se mostrará y podrás generar una contraseña con un clic.

### Estado actual de la Fase 1

La Fase 1 queda implementada con una base mínima funcional y documentada. El flujo principal es simple, legible y preparado para ampliaciones futuras sin alterar la estructura general del proyecto.

---

## Fase 2: Longitud y tipos de caracteres

### Descripción general

La aplicación de escritorio sigue desarrollándose en Python 3.14 con Tkinter y mantiene la estructura modular de la Fase 1. En esta fase se amplía la lógica del generador para permitir la selección de tipos de caracteres y controlar la longitud desde la interfaz.

### Objetivo de la fase

La aplicación debe cumplir con las siguientes funciones:

- Generar contraseñas con longitud configurable desde un control de interfaz.
- Permitir seleccionar qué tipos de caracteres se incluyen.
- Validar entradas para evitar combinaciones no válidas.
- Mantener la arquitectura modular y legible.
- Documentar el cambio en el README y comentar el código importante.

### Stack tecnológico

- Python 3.14
- Tkinter
- Módulo `secrets` para generación segura

### Estructura del proyecto

- `main.py`: archivo principal que construye la ventana y conecta la interfaz con la lógica.
- `utils/`: carpeta de utilidades.
- `utils/generador.py`: lógica del generador con validación y selección activa de tipos.

### Cambios respecto a la Fase 1

#### 1. Generador con tipos de caracteres

La función `generar_contrasena()` ya no usa un conjunto fijo. Ahora recibe:

- una longitud entera,
- un diccionario con los tipos activos.

Los tipos disponibles son:

- minúsculas
- mayúsculas
- números
- símbolos

#### 2. Control de longitud en Tkinter

Se añade un `Spinbox` para elegir la longitud de la contraseña. El rango permitido queda definido como:

- mínimo: 8 caracteres
- máximo: 64 caracteres

#### 3. Selección de tipos mediante checkboxes

Se incorporan checkbox para activar o desactivar cad
 caracteres. Si no se marca ninguna opción, la generación se rechaza con un mensaje de e

#### 4. Validación de la configuración

La aplicación controla estas situaciones:

- longitud 0 o negativa
- longitud demasiado larga
- longitud no numérica
- ninguna opción de caracteres activa

### Flujo de trabajo de la fase 2

1. El usuario ejecuta `main.py`.
2. La ventana carga una configuración inicial con todos los tipos activos y longitud 12.
3. El usuario puede modificar la longitud con el `Spinbox`.
4. El usuario activa o desactiva los checkbox de cada tipo.
5. Al pulsar el botón, la interfaz extrae los valores actuales.
6. Se valida la configuración antes de generar la contraseña.
7. Si la configuración es correcta, se llama a `generar_contrasena()`.
8. La contraseña se muestra en el campo de texto.
9. En caso de error, se muestra un mensaje con la causa.

### Lógica del generador

La lógica central está en `utils/generador.py` y realiza estas tareas:

- valida la longitud
- valida que haya al menos un tipo de carácter seleccionado
- compone la lista de caracteres disponibles según los tipos activos
- añade al menos un carácter de cada tipo seleccionado
- rellena el resto de la longitud con caracteres aleatorios
- mezcla la contraseña para evitar patrones predecibles

### Código principal

#### `main.py`

- `crear_ventana_principal()`: crea la ventana principal.
- `crear_interfaz()`: define el diseño con longitud, checkbox y campo para mostrar la contraseña.
- `generar_y_mostrar()`: recoge los valores de la interfaz y llama a la lógica del generador.
- `main()`: lanza la aplicación.

#### `utils/generador.py`

- `validar_configuracion()`: comprueba la longitud y los tipos activos.
- `generar_contrasena()`: genera la contraseña con la configuración indicada.

### Restricciones de la fase 2

Esta fase incluye únicamente:

- longitud configurable
- selección de tipos de caracteres
- validación de combinaciones inválidas
- interfaz gráfica con Tkinter

No se implementan funcionalidades de fases posteriores, como:

- guardado en archivo
- generación múltiple
- longitud personalizada ilimitada
- selección de perfiles o presets

### Cómo ejecutar la aplicación

Desde la carpeta del proyecto:

```bash
python main.py
```

### Estado actual de la Fase 2

La Fase 2 queda implementada con una base funcional y validada. La aplicación permite definir la longitud y los tipos de caracteres sin introducir elementos extra fuera del alcance solicitado.

---

## Resumen final

El proyecto mantiene la estructura modular de la Fase 1 y amplía la funcionalidad en la Fase 2 sin perder la documentación previa. Ambas fases quedan reflejadas en este README para mantener un historial claro del desarrollo y del flujo de trabajo del proyecto.
