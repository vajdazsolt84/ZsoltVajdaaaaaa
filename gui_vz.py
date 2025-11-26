import tkinter as tk
from tkinter import messagebox
from filemanager_vz import FileManagerVZ


class FileManagerGUIVZ:
    def __init__(self, root):
        self.root = root
        self.root.title("VZ File Manager")

        self.fm = FileManagerVZ(".")

        self.listbox = tk.Listbox(root, width=50, height=15)
        self.listbox.pack(pady=10)

        tk.Button(root, text="Frissítés", command=self.refresh_vz).pack(pady=2)

        self.new_folder_entry = tk.Entry(root)
        self.new_folder_entry.pack(pady=2)
        tk.Button(root, text="Új mappa", command=self.create_folder_vz).pack(pady=2)

        tk.Button(root, text="Kijelölt törlése", command=self.delete_selected_vz).pack(pady=2)

        self.refresh_vz()

    def refresh_vz(self):
        """Lista frissítése."""
        self.listbox.delete(0, tk.END)
        for item in self.fm.list_files_vz():
            self.listbox.insert(tk.END, item)

    def create_folder_vz(self):
        """Új mappa létrehozása a beírt névvel."""
        name = self.new_folder_entry.get()
        if not name.strip():
            messagebox.showerror("Hiba", "Adj meg egy mappanevet!")
            return
        self.fm.create_folder_vz(name)
        self.new_folder_entry.delete(0, tk.END)
        self.refresh_vz()

    def delete_selected_vz(self):
        """A listában kijelölt elem törlése."""
        selected = self.listbox.get(tk.ACTIVE)
        if not selected:
            messagebox.showwarning("Figyelem", "Nincs kijelölve elem!")
            return

        answer = messagebox.askyesno("Megerősítés", f"Biztosan törlöd: {selected}?")
        if not answer:
            return

        self.fm.delete_item_vz(selected)
        self.refresh_vz()
