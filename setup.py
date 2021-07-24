import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"D:\Programs\Python\Python39\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"D:\Programs\Python\Python39\tcl\tk8.6"

executables = [cx_Freeze.Executable("ibk.py", base=base, icon="icon.ico")]


cx_Freeze.setup(
    name = "ibk Text Editor",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["icon.ico",'tcl86t.dll','tk86t.dll', 'icons2']}},
    version = "0.01",
    description = "Tkinter Application",
    executables = executables
    )