from io import BytesIO
import win32clipboard
from PIL import Image
import os
import random

class ResimKopyalama:
    def __init__(self):
        self.file_paths = []

    def send_to_clipboard(self, clip_type, filepath):
        image = Image.open(filepath)

        output = BytesIO()
        image.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]
        output.close()

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(clip_type, data)
        win32clipboard.CloseClipboard()

    def get_file_paths(self, folder_path):
        self.file_paths = []

        for root, dirs, files in os.walk(folder_path):
            for file in files:
                self.file_paths.append(os.path.relpath(os.path.join(root, file), folder_path))

        return self.file_paths

resimci = ResimKopyalama()
file_paths = resimci.get_file_paths("resimler")
random_file_path = random.choice(file_paths)
resimci.send_to_clipboard(win32clipboard.CF_DIB, os.path.join("resimler", random_file_path))