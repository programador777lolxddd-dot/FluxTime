# Guía de uso de FluxTime

## Inicio rápido

Desde la carpeta donde se encuentra `FluxTime.py`, ejecuta:

```bash
python3 FluxTime.py
```

Si tu sistema utiliza el comando `python` para Python 3:

```bash
python FluxTime.py
```

## Qué aparece en pantalla

- **Banner:** nombre de FluxTime en caracteres ASCII grandes.
- **Hora:** horas, minutos y segundos en formato de 24 horas.
- **Fecha:** día de la semana y fecha local del sistema, en español.
- **Mensaje de salida:** recordatorio para detener el reloj con Ctrl+C.

## Personalización

La paleta se define al principio de `FluxTime.py` mediante códigos ANSI TrueColor. Los valores de color siguen el formato RGB. Cambia estos valores solo si deseas personalizar el tema.

Los caracteres grandes se guardan en el diccionario `DIGITS`, y el banner se almacena en `BANNER`. Si modificas sus dimensiones, revisa la alineación en tu terminal.

## Diagnóstico rápido

1. Confirma que Python 3 está instalado.
2. Abre una terminal compatible con secuencias ANSI.
3. Ejecuta el archivo desde la carpeta correcta.
4. Si se corta la salida o no se ve completa, amplía la terminal.
5. Detén el programa con Ctrl+C.
