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

---

## Fase 3: Copia, complejidad y guardado

### Descripción general

La aplicación de escritorio continúa evolucionando en Python 3.14 con Tkinter y mantiene el historial completo de las fases anteriores. En esta fase se añaden funciones útiles para la gestión diaria de la contraseña generada: copiarla al portapapeles, evaluar su nivel de complejidad y guardarla en un archivo TXT con fecha y hora.

### Objetivo de la fase

La aplicación debe cumplir con las siguientes funciones:

- Implementar un botón para copiar la contraseña generada al portapapeles.
- Mostrar un indicador de complejidad para la contraseña generada.
- Guardar la contraseña en un archivo `.txt` junto con la fecha y la hora exactas del guardado.
- Gestionar errores con `messagebox` para informar al usuario de forma clara.
- Mantener una interfaz limpia, intuitiva y funcional.

### Stack tecnológico

- Python 3.14
- Tkinter
- `datetime` para registrar la fecha y hora del guardado
- `messagebox` para errores y avisos

### Nuevas funcionalidades añadidas

#### 1. Copia al portapapeles

Se añade un botón llamado “Copiar” que toma el valor actual del campo de la contraseña y lo guarda en el portapapeles del sistema.

#### 2. Indicador de complejidad

La aplicación evalúa la contraseña generada en función de criterios como:

- longitud
- presencia de minúsculas
- presencia de mayúsculas
- presencia de números
- presencia de símbolos

El resultado se muestra como:

- Baja
- Media
- Alta
- Muy alta

#### 3. Guardado en archivo TXT

Se crea una carpeta llamada `passwords_guardadas` dentro del proyecto. Cada contraseña se guarda en un archivo con el formato:

- `password_YYYY-MM-DD_HH-MM-SS.txt`

El archivo incluye:

- la contraseña generada
- la fecha y hora del guardado

#### 4. Gestión de errores

Se usan `messagebox` para avisar al usuario en situaciones como:

- no hay contraseña generada
- error al copiar al portapapeles
- error al guardar en archivo
- configuración inválida

### Flujo de trabajo de la fase 3

1. El usuario ejecuta la aplicación.
2. La interfaz carga la configuración de las fases anteriores.
3. El usuario genera una contraseña.
4. La aplicación muestra la contraseña y calcula su complejidad.
5. El usuario puede copiar la contraseña al portapapeles.
6. El usuario puede guardar la contraseña en un archivo TXT con fecha y hora.
7. Si ocurre un error, se muestra un aviso con `messagebox`.

### Código principal

#### `main.py`

- `guardar_contrasena_archivo()`: crea la carpeta y guarda la contraseña con timestamp.
- `crear_ventana_principal()`: crea la ventana principal.Contenedor de la app.
- `crear_interfaz()`: define la interfaz con longitud, tipos, complejidad, botón generar, copiar y guardar.
- `copiar_al_portapapeles()`: copia la contraseña al sistema.
- `guardar_en_archivo()`: guarda la contraseña con fecha y hora.
- `main()`: arranca la aplicación.

#### `utils/generador.py`

- `evaluar_complejidad()`: calcula el nivel de complejidad de la contraseña.
- `generar_contrasena()`: mantiene la lógica de generación según la configuración activa.

### Restricciones de la fase 3

Esta fase incluye únicamente:

- copia al portapapeles
- indicador de complejidad
- guardado en `.txt` con fecha y hora
- gestión de errores con `messagebox`

No se implementan funcionalidades de fases posteriores, como:

- historial de contraseñas
- exportación en formato CSV
- autenticación o bloqueo
- ajustes avanzados del programa

### Cómo ejecutar la aplicación

Desde la carpeta del proyecto:

```bash
python main.py
```

### Estado actual de la Fase 3

La Fase 3 queda implementada con una interfaz clara, funcional y con validación de errores. La aplicación permite generar, copiar, evaluar y guardar la contraseña siguiendo el alcance solicitado.

---

## Resumen final del proyecto

El proyecto mantiene el historial completo de las fases anteriores y añade la Fase 3 sin alterar la documentación previa. La aplicación evoluciona de una base mínima a una herramienta más útil y práctica, siempre respetando los límites de cada etapa de desarrollo.

---

## Fase 4: Refactorización y optimización

### Descripción general

La aplicación de escritorio sigue manteniendo el historial completo de las fases anteriores y se centra en esta fase en la mejora del código y de la experiencia visual. La intención no es añadir nuevas funcionalidades, sino revisar nombres, limpiar la estructura y optimizar la parte gráfica para que el programa sea más claro, más legible y más intuitivo para un usuario.

### Objetivo de la fase

La aplicación debe cumplir con los siguientes puntos:

- Revisar nombres de variables y funciones para que sean más intuitivos.
- Mejorar la organización interna del código sin romper ninguna funcionalidad existente.
- Optimizar la apariencia visual para que la interfaz sea más limpia y profesional.
- Mantener la estructura modular y el historial completo del proyecto.
- Documentar los cambios en el README sin eliminar las fases anteriores.

### Qué se ha revisado y mejorado

#### 1. Nombres más intuitivos

Se han revisado los nombres de funciones y variables para que describan mejor su propósito. Por ejemplo, nombres más claros para acciones como generar, guardar, copiar e indicar complejidad hacen que el código sea más fácil de entender.

#### 2. Estructura más ordenada

Se ha reorganizado la lógica dentro de `main.py` para diferenciar mejor:

- creación de la ventana,
- configuración visual,
- generación de la contraseña,
- copia al portapapeles,
- guardado en archivo,
- actualización del indicador de complejidad.

#### 3. Optimización visual

Se ha mejorado la apariencia general de la interfaz para que sea más clara y agradable, manteniendo la funcionalidad que ya existía. La disposición de los elementos se ha ordenado para que resulte más natural a la vista.

### Flujo de trabajo de la fase 4

1. Se revisan los nombres existentes para detectar elementos poco claros.
2. Se refactoriza la estructura interna y la organización visual.
3. Se mantiene intacta la lógica de las fases anteriores.
4. Se valida que la aplicación sigue funcionando correctamente.
5. Se documenta el cambio en este README.

### Código principal

#### `main.py`

- `crear_ventana_principal()`: prepara la ventana principal.
- `crear_interfaz_principal()`: organiza la interfaz de forma más limpia.
- `generar_y_mostrar_contrasena()`: genera y muestra la contraseña en el campo principal.
- `copiar_contrasena_al_portapapeles()`: copia la contraseña al portapapeles.
- `guardar_contrasena_actual()`: guarda la contraseña con fecha y hora.
- `actualizar_indicador_complejidad()`: actualiza el nivel de seguridad visual.

#### `utils/generador.py`

- `evaluar_complejidad()`: mantiene la lógica de valoración de la contraseña.
- `generar_contrasena()`: sigue generando la contraseña según los tipos seleccionados.

### Restricciones de la fase 4

Esta fase incluye únicamente:

- refactorización de nombres
- mejora de la organización y la interfaz visual
- optimización estructural sin cambiar la lógica funcional del proyecto

No se implementan funcionalidades de fases posteriores, ni se añaden cambios que alteren el comportamiento ya validado de la aplicación.

### Cómo ejecutar la aplicación

Desde la carpeta del proyecto:

```bash
python main.py
```

### Estado actual de la Fase 4

La Fase 4 queda implementada como una mejora de calidad de la aplicación: nombres más claros, estructura más ordenada y una interfaz más limpia, sin romper ninguna funcionalidad existente.

---

## Resumen final del proyecto

El proyecto conserva todo el historial de las fases anteriores, y la Fase 4 aporta una mejora orientada a la claridad, la mantenibilidad y la experiencia visual. La aplicación sigue funcionando de forma consistente y autónoma, respetando el alcance de cada etapa de desarrollo.
