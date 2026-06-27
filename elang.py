#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

TERMUX_DIR = Path.home() / ".termux"
CONFIG_FILE = TERMUX_DIR / "termux.properties"
BACKUP_FILE = TERMUX_DIR / "termux.properties.bak.elang"

CONFIG_CONTENT = 'extra-keys = [["ESC","|","/","HOME","UP","END","PGUP","DEL"],["TAB","CTRL","BKSP","LEFT","DOWN","RIGHT","PGDN","~"],["ls","cd ","clear","exit","pkg ","ENTER"]]'

def main():
    print("[+] Elang Keyboard Installer v1.1")
    print("[+] Format: 1 baris JSON aman anti error")

    TERMUX_DIR.mkdir(exist_ok=True)

    if CONFIG_FILE.exists():
        shutil.move(CONFIG_FILE, BACKUP_FILE)
        print(f"[+] Backup config lama: {BACKUP_FILE}")

    with open(CONFIG_FILE, "w") as f:
        f.write(CONFIG_CONTENT)
    print(f"[+] Config Elang Keyboard ditulis: {CONFIG_FILE}")

    os.system("termux-reload-settings")
    print("[+] Selesai! Exit Termux > Buka lagi.")

if __name__ == "__main__":
    main()
