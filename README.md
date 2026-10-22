# 💗 FluxTime

<p align="center">
  <strong>Un reloj digital futurista para tu terminal, hecho con Python.</strong><br>
  Rosa neón, cian eléctrico y violeta sobre un fondo Midnight Plasma. 🩷🩵💜
</p>

---

## ✨ Características

- 🕒 Reloj digital en tiempo real con formato de 24 horas.
- 🔢 Números grandes dibujados con caracteres de estilo **ANSI Shadow**.
- 🎨 Paleta neón con colores ANSI TrueColor (24 bits).
- 📅 Fecha actual en español.
- 🐍 Utiliza módulos de la biblioteca estándar de Python; no requiere paquetes externos.
- ⌨️ Salida sencilla con `Ctrl+C`.

## 🖥️ Vista previa

FluxTime muestra un banner grande, la hora en cian eléctrico y la fecha en violeta. Su fondo oscuro y el rosa neón completan la estética **Midnight Plasma**.

> Puedes añadir aquí una captura del programa cuando subas la imagen al repositorio.

## 🚀 Cómo ejecutarlo

Necesitas tener Python 3 instalado.

1. Clona el repositorio o descarga `FluxTime.py`.
2. Abre una terminal en la carpeta del archivo.
3. Ejecuta:

```bash
python3 FluxTime.py
```

En algunos sistemas, el comando puede ser:

```bash
python FluxTime.py
```

Presiona `Ctrl+C` para cerrar el reloj.

## 🎨 Paleta de colores

| Elemento | Color |
| --- | --- |
| Banner | Rosa neón |
| Hora | Cian eléctrico |
| Fecha | Violeta |
| Texto secundario | Gris azulado |
| Fondo | Azul/morado muy oscuro |

Los colores usan secuencias ANSI TrueColor. Para ver el diseño como fue pensado, utiliza una terminal compatible con colores de 24 bits y secuencias ANSI.

## 📦 Dependencias

FluxTime usa únicamente módulos incluidos con Python:

```python
import os
import sys
import time
from datetime import datetime
```

No hace falta instalar dependencias adicionales.

## 📄 Licencia

Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo `LICENSE` del repositorio para ver sus términos.

---

Hecho con Python. ¡Gracias por visitar FluxTime! 💗🩵
