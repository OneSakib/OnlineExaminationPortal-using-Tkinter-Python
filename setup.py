import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Sakib Malik\AppData\Local\Programs\Python\Python39\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Sakib Malik\AppData\Local\Programs\Python\Python39\tcl\tk8.6"

executables = [cx_Freeze.Executable("Online Examination System.py", base=base, icon="logo.ico")]


cx_Freeze.setup(
    name = "Online Examination Portal",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["papers",'tcl86t.dll','tk86t.dll', 'adminlogin.json','background.png','dev.png','login.json','logo.png','paper.json']}},
    version = "0.01",
    description = "Tkinter Application",
    executables = executables
    )
