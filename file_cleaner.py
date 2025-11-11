import os
import shutil
import stat
import time
from pathlib import Path
from tempfile import NamedTemporaryFile, TemporaryDirectory

def delete_file(file_path, type):
    """Basic file deletion function"""
    os.chmod(file_path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
    try:
        if type=='file':
            os.remove(file_path)
        else:
            shutil.rmtree(file_path)
        print(f"Successfully deleted: {file_path}")
        return True
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return False
    except PermissionError:
        print(f"Permission denied: {file_path}")
        time.sleep(5)
        delete_file(file_path)
        return False
    except Exception as e:
        print(f"Error deleting {file_path}: {e}")
        os.remove(file_path)
        return False