import os
import sys
import time
from datetime import datetime

# Forzar UTF-8
if sys.version_info >= (3, 7):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

RESET = '\033[H'  # Volver al inicio
CLEAR = '\033[2J' # Limpiar pantalla
ALT_SCREEN_ON = '\033[?1049h'
ALT_SCREEN_OFF = '\033[?1049l'
HIDE_CURSOR = '\033[?25l'
SHOW_CURSOR = '\033[?25h'

BANNER = r"""
███████╗██╗     ██╗   ██╗██╗  ██╗████████╗██╗███╗   ███╗███████╗
██╔════╝██║     ██║   ██║╚██╗██╔╝╚══██╔══╝██║████╗ ████║██╔════╝
█████╗  ██║     ██║   ██║ ╚███╔╝    ██║   ██║██╔████╔██║█████╗  
██╔══╝  ██║     ██║   ██║ ██╔██╗    ██║   ██║██║╚██╔╝██║██╔══╝  
██║     ███████╗╚██████╔╝██╔╝ ██╗   ██║   ██║██║ ╚═╝ ██║███████╗
╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝
""".strip('\n')

# ¡AQUÍ ESTABA EL ERROR! Ahora TODOS los números miden exactamente 9 caracteres de ancho.
DIGITS = {
    '0': [' ██████╗ ', '██╔═████╗', '██║██╔██║', '████╔╝██║', '╚█████╔╝ ', ' ╚════╝  '],
    '1': [' ██╗     ', '███║     ', '╚██║     ', ' ██║     ', ' ██║     ', ' ╚═╝     '],
    '2': ['██████╗  ', '╚════██╗ ', ' █████╔╝ ', '██╔═══╝  ', '███████╗ ', '╚══════╝ '],
    '3': ['██████╗  ', '╚════██╗ ', ' █████╔╝ ', ' ╚═══██╗ ', '██████╔╝ ', '╚═════╝  '],
    '4': ['██╗  ██╗ ', '██║  ██║ ', '███████║ ', '╚════██║ ', '     ██║ ', '     ╚═╝ '],
    '5': ['███████╗ ', '██╔════╝ ', '███████╗ ', '╚════██║ ', '███████║ ', '╚══════╝ '],
    '6': [' ██████╗ ', '██╔════╝ ', '███████╗ ', '██╔══██╗ ', '╚██████╔╝', ' ╚═════╝ '],
    '7': ['███████╗ ', '╚════██║ ', '    ██╔╝ ', '   ██╔╝  ', '   ██║   ', '   ╚═╝   '],
    '8': [' █████╗  ', '██╔══██╗ ', '╚█████╔╝ ', '██╔══██╗ ', '╚█████╔╝ ', ' ╚════╝  '],
    '9': [' █████╗  ', '██╔══██╗ ', '╚██████║ ', ' ╚═══██║ ', ' █████╔╝ ', ' ╚════╝  '],
    ':': ['         ', '   ██╗   ', '   ╚═╝   ', '   ██╗   ', '   ╚═╝   ', '         '],
}

DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

def apply_gradient(text, start_color=(0, 240, 255), end_color=(255, 0, 128)):
    lines = text.split('\n')
    height = max(1, len(lines) - 1)
    width = max(len(line) for line in lines) if lines else 1
    result = []
    
    for y, line in enumerate(lines):
        out_line = ""
        for x, char in enumerate(line):
            if char == ' ':
                out_line += char
                continue
            factor = (x / width + y / height) / 2.0
            r = int(start_color[0] + (end_color[0] - start_color[0]) * factor)
            g = int(start_color[1] + (end_color[1] - start_color[1]) * factor)
            b = int(start_color[2] + (end_color[2] - start_color[2]) * factor)
            out_line += f"\033[38;2;{r};{g};{b}m{char}"
        result.append(out_line + '\033[0m')
    return '\n'.join(result)

def render_time(now):
    text = now.strftime('%H:%M:%S')
    rows = ['' for _ in range(6)]
    for ch in text:
        glyph = DIGITS.get(ch, ['         '] * 6)
        for i in range(6):
            rows[i] += glyph[i] # Sin espacios extra, ya miden 9
    return '\n'.join(rows)

def frame(now):
    fecha = f"{DIAS[now.weekday()]}, {now.day} de {MESES[now.month - 1]} de {now.year}"
    banner_gradient = apply_gradient(BANNER)
    time_gradient = apply_gradient(render_time(now))
    
    return '\n'.join([
        banner_gradient,
        '',
        time_gradient,
        '',
        f"   \033[38;2;180;100;255m{fecha}\033[0m",
        '',
        f"   \033[38;2;120;120;160mPresiona Ctrl+C para salir\033[0m",
        ''
    ])

def main():
    if os.name == 'nt':
        os.system('')
    
    sys.stdout.write(ALT_SCREEN_ON + HIDE_CURSOR + CLEAR)
    sys.stdout.flush()
    
    try:
        while True:
            ahora = datetime.now()
            sys.stdout.write(RESET + frame(ahora))
            sys.stdout.flush()
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write(SHOW_CURSOR + ALT_SCREEN_OFF)
        sys.stdout.flush()
        print('\n  ⏱  Reloj detenido. ¡Hasta pronto!\n')

if __name__ == '__main__':
    main()
