import os
import shutil
import sys
from datetime import datetime

def safe_copy(src):
    if not os.path.exists(src):
        print(f"[ERROR] Файл не найден: {src}")
        return False
    if not os.path.isfile(src):
        print(f"[ERROR] Это не файл: {src}")
        return False

    dst = os.path.basename(src)
    if os.path.exists(dst):
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        name, ext = os.path.splitext(dst)
        dst = f"{name}_{ts}{ext}"
        print(f"[ПРЕДУПРЕЖДЕНИЕ] Файл существует → сохранено как: {dst}")

    try:
        shutil.copy2(src, dst)
        print(f"[УСПЕХ] Скопировано: {dst}")
        return True
    except Exception as e:
        print(f"[ОШИБКА] {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python copy_file.py <путь_к_файлу>")
        sys.exit(1)
    safe_copy(sys.argv[1])