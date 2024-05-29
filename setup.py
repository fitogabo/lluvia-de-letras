from cx_Freeze import setup, Executable
import os
import sys

os.environ['TCL_LIBRARY'] = r'C:\Users\gabri\AppData\Local\Programs\Python\Python39\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\gabri\AppData\Local\Programs\Python\Python39\tcl\tk8.6'

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["pygame", "random", "string", "turtle", "freegames"],
    "include_files": ["sonidos/"],
    "excludes": []
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Lluvia de Letras",
    version="0.1",
    description="Juego para practicar la mecanografía",
    options={"build_exe": build_exe_options},
    executables=[Executable("lluvia-de-letras.py", base=base)]
)
