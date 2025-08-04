import os
from desafio1.app.config import UPLOAD_DIR

def save_file(file, filename: str):
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_path = os.path.join(UPLOAD_DIR, filename)
    with open(file_path, "wb") as buffer:
        buffer.write(file)
    return file_path
