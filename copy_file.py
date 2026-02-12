import os
import shutil
import sys
from datetime import datetime

def copy_file_to_repo(source_path):
    """Copy file to current repository directory"""
    
    if not os.path.exists(source_path):
        print(f"[ERROR] File not found: {source_path}")
        return False
    
    if not os.path.isfile(source_path):
        print(f"[ERROR] Path is not a file: {source_path}")
        return False
    
    filename = os.path.basename(source_path)
    dest_path = os.path.join(os.getcwd(), filename)
    
    if os.path.exists(dest_path):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        name, ext = os.path.splitext(filename)
        filename = f"{name}_{timestamp}{ext}"
        dest_path = os.path.join(os.getcwd(), filename)
        print(f"[WARNING] File already exists. Saved as: {filename}")
    
    try:
        shutil.copy2(source_path, dest_path)
        print(f"[SUCCESS] File copied: {filename}")
        print(f"Source: {source_path}")
        print(f"Destination: {dest_path}")
        return True
    except PermissionError:
        print("[ERROR] Permission denied")
        return False
    except Exception as e:
        print(f"[ERROR] Copy failed: {str(e)}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python copy_file.py <source_file_path>")
        print("Example: python copy_file.py C:\\Users\\student\\test.txt")
        sys.exit(1)
    
    source_file = sys.argv[1]
    success = copy_file_to_repo(source_file)
    sys.exit(0 if success else 1)