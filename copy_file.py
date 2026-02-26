import os
import shutil
import sys
from datetime import datetime

def safe_copy(src, dst_name=None):
    """Копирует файл с проверкой и защитой от перезаписи"""
    if not os.path.exists(src):
        print(f"[ERROR] Файл не найден: {src}")
        return False
    if not os.path.isfile(src):
        print(f"[ERROR] Это не файл: {src}")
        return False

    # Определяем имя назначения
    if dst_name is None:
        dst_name = os.path.basename(src)
    
    dst = dst_name
    if os.path.exists(dst):
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        name, ext = os.path.splitext(dst)
        dst = f"{name}_{ts}{ext}"
        print(f"[ПРЕДУПРЕЖДЕНИЕ] Файл существует → сохранено как: {dst}")

    try:
        shutil.copy2(src, dst)
        print(f"[УСПЕХ] Скопировано: {dst}")
        return True
    except PermissionError:
        print("[ОШИБКА] Нет прав на запись")
        return False
    except Exception as e:
        print(f"[ОШИБКА] {e}")
        return False

def main():
    print("\n=== СКРИПТ КОПИРОВАНИЯ ФАЙЛОВ ===")
    print("1. Скопировать один файл")
    print("2. Выход")
    
    while True:
        choice = input("\nВыберите действие (1/2): ").strip()
        if choice == "1":
            path = input("Введите полный путь к файлу: ").strip()
            if path:
                safe_copy(path)
            else:
                print("[ИНФО] Пустой путь.")
        elif choice == "2":
            print("Завершение работы.")
            break
        else:
            print("[ИНФО] Неверный выбор. Повторите.")

if __name__ == "__main__":
    main()
