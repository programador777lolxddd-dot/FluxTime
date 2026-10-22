import os
import sys
import time
from datetime import datetime

# --- Paleta de colores Midnight Plasma (TrueColor ANSI) ---
BG      = '\033[48;2;10;2;20m'       # Fondo: Azul/Morado ultra oscuro (Medianoche)
PINK    = '\033[38;2;255;0;128m'     # Banner: Rosa Neón / Plasma
CYAN    = '\033[38;2;0;240;255m'     # Reloj: Cian Eléctrico
PURPLE  = '\033[38;2;180;100;255m'   # Fecha: Violeta Brillante
TEXT    = '\033[38;2;120;120;160m'   # Texto secundario: Gris azulado
RESET   = '\033[0m'                  # Reset de color

# Números en estilo ANSI Shadow (6 filas)
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

BANNER = r"""
███████╗██╗     ██╗   ██╗██╗  ██╗████████╗██╗███╗   ███╗███████╗
██╔════╝██║     ██║   ██║╚██╗██╔╝╚══██╔══╝██║████╗ ████║██╔════╝
█████╗  ██║     ██║   ██║ ╚███╔╝    ██║   ██║██╔████╔██║█████╗  
██╔══╝  ██║     ██║   ██║ ██╔██╗    ██║   ██║██║╚██╔╝██║██╔══╝  
██║     ███████╗╚██████╔╝██╔╝ ██╗   ██║   ██║██║ ╚═╝ ██║███████╗
╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝
"""

DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

def render_time(now):
    """Renderiza la hora con los bloques."""
    text = now.strftime('%H:%M:%S')
    rows = ['' for _ in range(6)]
    for ch in text:
        glyph = DIGITS.get(ch, ['     '] * 6)
        for i in range(6):
            rows[i] += glyph[i] + '  '  # Doble espacio
    return '\n'.join(rows)

def frame(now):
    fecha = f"{DIAS[now.weekday()]}, {now.day} de {MESES[now.month - 1]} de {now.year}"
    
    # El BG (fondo) se aplica al principio para teñir toda la pantalla
    return '\n'.join([
        f"{BG}{PINK}{BANNER}{RESET}{BG}",
        '',
        f"{CYAN}{render_time(now)}{RESET}{BG}",
        '',
        f"   {PURPLE}{fecha}{RESET}{BG}",
        '',
        f"   {TEXT}Presiona Ctrl+C para salir{RESET}{BG}",
        ''
    ])

def main():
    if os.name == 'nt':
        os.system('')

    try:
        while True:
            ahora = datetime.now()
            # \033[H mueve el cursor arriba, \033[J limpia la pantalla
            sys.stdout.write('\033[H\033[J' + frame(ahora))
            sys.stdout.flush()
            time.sleep(0.1)
    except KeyboardInterrupt:
        print(f'{RESET}\n\n  ⏱  Reloj detenido. ¡Hasta pronto!\n')

if __name__ == '__main__':
    main()