import os
import shutil


class FileManagerVZ:
    def __init__(self, path):
        self.path = path

    def list_files_vz(self):
        """A könyvtár tartalmának listázása."""
        try:
            return os.listdir(self.path)
        except FileNotFoundError:
            return ["Hibás elérési út!"]

    def create_folder_vz(self, folder_name):
        """Új mappa létrehozása."""
        os.makedirs(os.path.join(self.path, folder_name), exist_ok=True)

    def delete_item_vz(self, name):
        """Fájl vagy mappa törlése."""
        target = os.path.join(self.path, name)
        if os.path.isfile(target):
            os.remove(target)
        elif os.path.isdir(target):
            shutil.rmtree(target)