import os
import sys
import time
from datetime import datetime

# --- Paleta de colores Midnight Plasma ---
BG      = '\033[48;2;10;2;20m'       # Fondo ultra oscuro
RESET   = '\033[0m'

# --- Matriz del Reloj Digital (ANSI Shadow) ---
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

# --- ASCII Art del Logo (Basado en tu imagen) ---
LOGO_ART = [
    "          ███████████████████          ",
    "      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄     ",
    "    ▄█▀                         ▀█▄   ",
    "   ██             ███              ██  ",
    "   ██             ███              ██  ",
    "   ██            ██                ██  ",
    "   ██          ██                  ██  ",
    "   ██        ██                    ██  ",
    "    ▀█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▀   ",
    "      ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀     ",
    "          ███████████████████          ",
]

DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

def render_logo():
    """Genera el logo con un gradiente diagonal Cyan a Magenta (Midnight Plasma)."""
    lines = []
    height = len(LOGO_ART)
    width = max(len(line) for line in LOGO_ART)
    
    for y, line in enumerate(LOGO_ART):
        colored_line = ""
        for x, char in enumerate(line):
            if char == ' ':
                colored_line += char
                continue
            
            # Crear gradiente diagonal (Cyan arriba-izq -> Magenta abajo-der)
            factor = (x / width + y / height) / 2.0
            r = int(255 * factor)
            g = int(255 * (1 - factor))
            b = 255
            
            # Aplicar color TrueColor ANSI
            colored_line += f"\033[38;2;{r};{g};{b}m{char}"
        lines.append(colored_line + RESET)
    
    return '\n'.join(lines)

def render_time(now):
    """Renderiza la hora digital con el color Cian Eléctrico."""
    text = now.strftime('%H:%M:%S')
    rows = ['' for _ in range(6)]
    for ch in text:
        glyph = DIGITS.get(ch, ['     '] * 6)
        for i in range(6):
            rows[i] += glyph[i] + '  '
    # Color cyan brillante para el reloj
    return '\n'.join([f"\033[38;2;0;240;255m{row}{RESET}{BG}" for row in rows])

def frame(now):
    fecha = f"{DIAS[now.weekday()]}, {now.day} de {MESES[now.month - 1]} de {now.year}"
    
    return '\n'.join([
        f"{BG}",
        render_logo(),
        '',
        render_time(now),
        '',
        f"   \033[38;2;180;100;255m{fecha}{RESET}{BG}", # Violeta
        '',
        f"   \033[38;2;120;120;160mPresiona Ctrl+C para salir{RESET}{BG}", # Gris
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
