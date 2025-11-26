from tkinter import Tk
from gui_vz import FileManagerGUIVZ


def main_vz():
    root = Tk()
    app = FileManagerGUIVZ(root)
    root.mainloop()


if __name__ == "__main__":
    main_vz()
