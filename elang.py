#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

TERMUX_DIR = Path.home() / ".termux"
CONFIG_FILE = TERMUX_DIR / "termux.properties"
BACKUP_FILE = TERMUX_DIR / "termux.properties.bak.elang"

CONFIG_CONTENT = """# Elang Keyboard - Termux Custom 3 Baris
# https://github.com/elmy711/elang_keyboard

terminal-transcript-colors = true
terminal-font = monospace

# Layout 3 baris
extra-keys = [
  ['ESC','|','/','HOME','UP','END','PGUP','DEL'],
  ['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN','~'],
  ['ls -la','cd ','clear','exit','pkg ','python','nano ','vim ']
"""

def main():
    print("[+] Elang Keyboard Installer v1.0")

    TERMUX_DIR.mkdir(exist_ok=True)

    if CONFIG_FILE.exists():
        shutil.move(CONFIG_FILE, BACKUP_FILE)
        print(f"[+] Backup config lama: {BACKUP_FILE}")

    with open(CONFIG_FILE, "w") as f:
        f.write(CONFIG_CONTENT)
    print(f"[+] Elang Keyboard aktif di: {CONFIG_FILE}")

    os.system("termux-reload-settings")
    print("[+] Selesai! Buka tutup Termux.")

if __name__ == "__main__":
    main()
