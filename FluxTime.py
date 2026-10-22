import os
import sys
import time
from datetime import datetime

# --- Paleta de colores ---
BG      = '\033[48;2;10;2;20m'       # Fondo ultra oscuro (Medianoche)
RESET   = '\033[0m'

# --- Banner FLUXTIME (ANSI Shadow) ---
BANNER = r"""
███████╗██╗     ██╗   ██╗██╗  ██╗████████╗██╗███╗   ███╗███████╗
██╔════╝██║     ██║   ██║╚██╗██╔╝╚══██╔══╝██║████╗ ████║██╔════╝
█████╗  ██║     ██║   ██║ ╚███╔╝    ██║   ██║██╔████╔██║█████╗  
██╔══╝  ██║     ██║   ██║ ██╔██╗    ██║   ██║██║╚██╔╝██║██╔══╝  
██║     ███████╗╚██████╔╝██╔╝ ██╗   ██║   ██║██║ ╚═╝ ██║███████╗
╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝
"""

# --- Matriz del Reloj (ANSI Shadow) ---
DIGITS = {
    '0': ['██████╗ ', '██╔═████╗', '██║██╔██║', '████╔╝██║', '╚█████╔╝', ' ╚════╝ '],
    '1': [' ██╗', '███║', '╚██║', ' ██║', ' ██║', ' ╚═╝'],
    '2': ['██████╗ ', '╚════██╗', ' █████╔╝', '██╔═══╝ ', '███████╗', '╚══════╝'],
    '3': ['██████╗ ', '╚════██╗', ' █████╔╝', ' ╚═══██╗', '██████╔╝', '╚═════╝ '],
    '4': ['██╗  ██╗', '██║  ██║', '███████║', '╚════██║', '     ██║', '     ╚═╝'],
    '5': ['███████╗', '██╔════╝', '███████╗', '╚════██║', '███████║', '╚══════╝'],
    '6': [' ██████╗ ', '██╔════╝ ', '███████╗ ', '██╔══██╗ ', '╚██████╔╝', ' ╚═════╝ '],
    '7': ['███████╗', '╚════██║', '    ██╔╝', '   ██╔╝ ', '   ██║  ', '   ╚═╝  '],
    '8': [' █████╗ ', '██╔══██╗', '╚█████╔╝', '██╔══██╗', '╚█████╔╝', ' ╚════╝ '],
    '9': [' █████╗ ', '██╔══██╗', '╚██████║', ' ╚═══██║', ' █████╔╝', ' ╚════╝ '],
    ':': ['    ', '██╗ ', '╚═╝ ', '██╗ ', '╚═╝ ', '    '],
}

DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

def interpolate_color(start, end, factor):
    """Calcula el color RGB entre start y end basado en el factor (0.0 a 1.0)."""
    r = int(start[0] + (end[0] - start[0]) * factor)
    g = int(start[1] + (end[1] - start[1]) * factor)
    b = int(start[2] + (end[2] - start[2]) * factor)
    return f"\033[38;2;{r};{g};{b}m"

def apply_gradient(text, start_color=(0, 240, 255), end_color=(255, 0, 128)):
    """Aplica un gradiente diagonal (Cian a Magenta) a cualquier bloque de texto."""
    lines = text.split('\n')
    height = len(lines)
    width = max(len(line) for line in lines) if height > 0 else 1
    result = []
    
    for y, line in enumerate(lines):
        out_line = ""
        for x, char in enumerate(line):
            if char == ' ':
                out_line += char
                continue
            # El factor mezcla la posición X y Y para crear el gradiente diagonal
            factor = (x / width + y / height) / 2.0
            color_code = interpolate_color(start_color, end_color, factor)
            out_line += f"{color_code}{char}"
        result.append(out_line + RESET)
    return '\n'.join(result)

def render_time(now):
    """Construye la hora con los números ANSI Shadow."""
    text = now.strftime('%H:%M:%S')
    rows = ['' for _ in range(6)]
    for ch in text:
        glyph = DIGITS.get(ch, ['     '] * 6)
        for i in range(6):
            rows[i] += glyph[i] + '  '
    return '\n'.join(rows)

def frame(now):
    fecha = f"{DIAS[now.weekday()]}, {now.day} de {MESES[now.month - 1]} de {now.year}"
    
    # Aplicamos el gradiente al Banner
    banner_gradient = apply_gradient(BANNER)
    
    # Aplicamos el gradiente al Reloj (solo horizontal para que sea más legible)
    time_str = render_time(now)
    time_gradient = apply_gradient(time_str, start_color=(0, 255, 200), end_color=(255, 0, 200))
    
    return '\n'.join([
        f"{BG}",
        banner_gradient,
        '',
        time_gradient,
        '',
        f"   \033[38;2;180;100;255m{fecha}{RESET}{BG}", # Violeta
        '',
        f"   \033[38;2;120;120;160mPresiona Ctrl+C para salir{RESET}{BG}",
        ''
    ])

def main():
    if os.name == 'nt':
        os.system('')

    try:
        while True:
            ahora = datetime.now()
            sys.stdout.write('\033[H\033[J' + frame(ahora))
            sys.stdout.flush()
            time.sleep(0.1)
    except KeyboardInterrupt:
        print(f'{RESET}\n\n  ⏱  Reloj detenido. ¡Hasta pronto!\n')

if __name__ == '__main__':
    main()
