# Generador de Contraseñas - Proyecto Completo (5 Fases)

## Descripción General
Aplicación de escritorio en Python 3.14 con Tkinter para generar contraseñas de forma segura, con soporte para generación simple, lotes masivos, y evaluación de complejidad.

---

## Fase 1: Esqueleto Mínimo
- **Funcionalidades**: Generación fija de 12 caracteres, interfaz básica con Tkinter.
- **Decisión técnica**: Uso de `secrets` para aleatoriedad criptográfica segura.
- **Archivo principal**: `utils/generador.py` con lógica modular.

---

## Fase 2: Longitud y Tipos de Caracteres
- **Funcionalidades**: Spinbox para elegir longitud (8-64), checkboxes para minúsculas/mayúsculas/números/símbolos, validación de configuración.
- **Decisión técnica**: Diccionario `TIPOS_CARACTERES` para gestión flexible de conjuntos de caracteres.
- **Mejora**: Cada tipo seleccionado se garantiza en la contraseña generada.

---

## Fase 3: Copia, Complejidad y Guardado
- **Funcionalidades**: Botón "Copiar" al portapapeles, indicador de complejidad (Baja/Media/Alta/Muy alta), guardado en `.txt` con fecha/hora.
- **Decisión técnica**: `datetime` para timestamp, `messagebox` para notificaciones de usuario.
- **Gestiónde errores**: Try-except específico para TypeError/ValueError separado de excepciones genéricas.
- **Carpeta**: `passwords_guardadas/` con archivos `password_YYYY-MM-DD_HH-MM-SS.txt`.

---

## Fase 4: Refactorización y Optimización
- **Funcionalidades**: Renombrado de funciones (ej. `generar_contrasena_en_archivo`), mejora visual con colores y Frames anidados, interfaz redimensionable.
- **Decisión técnica**: Frames anidados (`contenedor_principal`, `panel_configuracion`) para mejor organización y adaptabilidad.
- **Alias**: Se mantienen alias (`guardar_contrasena_archivo`, `crear_interfaz`) para compatibilidad hacia atrás.

---

## Fase 5: Caracteres Ambiguos, Lotes y Panel de Criterios
- **Funcionalidades**:
  1. **Evitar ambiguos**: Filtra caracteres confusos (0/O, 1/l/I, etc.) para mayor legibilidad.
  2. **Generación en lote**: 5-10 contraseñas simultáneamente.
  3. **Guardar lotes**: Archivo `lote_YYYY-MM-DD_HH-MM-SS.txt` con todas las contraseñas numeradas.
  4. **Panel de criterios**: Resumen visible de la configuración aplicada (longitud, tipos, complejidad, sin ambiguos).
  5. **Ventana emergente**: Muestra el lote con botones para copiar y guardar.

- **Decisión técnica**: 
  - Parámetro `evitar_ambiguos=True` por defecto en `generar_contrasena()`.
  - Función `_filtrar_caracteres_ambiguos()` privada reutilizable.
  - `generar_lote_contrasenas()` devuelve `list[str]`.
  - Constantes `LOTE_MINIMO=5`, `LOTE_MAXIMO=10`.

- **UI**: Spinbox para cantidad de lotes, panel con fondo `#e8f4f8` para criterios, botón "Generar lote" en color naranja.

---

## Stack Tecnológico (Todas las Fases)
- Python 3.14
- Tkinter para GUI
- `secrets` para generación segura
- `datetime` para timestamps
- `pathlib` para gestión de rutas

---

## Estructura del Proyecto
```
M6T5_Asier_Sanchez_Ortiz/
├── main.py                          # Interfaz y orquestación
├── utils/
│   └── generador.py                 # Lógica de generación
├── passwords_guardadas/              # Contraseñas individuales guardadas
└── README.md
```

---

## Ejecución
```bash
python main.py
```

---

## Restricciones por Fase
- **Fase 1-4**: Solo lo especificado, sin adicionales.
- **Fase 5 (última)**: Incluye caracteres ambiguos, generación en lote, panel de criterios. No incluye: historial persistente, exportación CSV, autenticación.

---

## Notas Técnicas Clave
1. **Compatibilidad hacia atrás**: Alias mantienen nombres antiguos para tests previos.
2. **Validación robusta**: Errores específicos vs. genéricos diferenciados.
3. **`readonly` vs. `disabled`**: Campo de contraseña usa `readonly` para permitir copiar.
4. **Frames anidados**: Permite ventana redimensionable sin desajustes.
5. **Caracteres ambiguos**: Lista centralizada `CARACTERES_AMBIGUOS` para fácil actualización.
