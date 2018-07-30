import cx_Freeze

#os.environ['TCL_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Pyton35-32\tcl\tcl8.6"
##os.environ['TK_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Pyton35-32\tcl\tk8.6"

Executables = [cx_Freeze.Executable("BoatyTheGame.py")]

cx_Freeze.setup(
    name="Boaty_The_Game",
    options={"build_exe": {"packages":["pygame"],"include_files":["boaty.png"]}},
    executables = Executables,
    version = "1.0.0"
)