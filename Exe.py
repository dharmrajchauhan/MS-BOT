# import cx_Freeze
# import sys
# import os
# base = None
# if sys.platform == 'win32':
#     base = "Win32GUI"

# # os.environ['TCL_LIBRARY'] = r"C:\Users\Gunjesh\AppData\Local\Programs\Python\Python37-32\tcl\tcl8.6"
# os.environ['TCL_LIBRARY'] = r"C:\Users\LENOVO\AppData\Local\Programs\Python\Python38\tcl\tcl8.6"
# # os.environ['TK_LIBRARY'] = r"C:\Users\Gunjesh\AppData\Local\Programs\Python\Python37-32\tcl\tk8.6"
# os.environ['TK_LIBRARY'] = r"C:\Users\LENOVO\AppData\Local\Programs\Python\Python38\tcl\tk8.6"

# executables = [cx_Freeze.Executable("main.py", base=base,icon="profile.ico")]

# cx_Freeze.setup(
#     name = "EPMS",
#     options = {"build_exe": {"packages":["PyQt5","pandas","sqlite3","selenium","datetime","os","sys"], "include_files":['tcl86t.dll','tk86t.dll','profile.ico',]}},
#     version = "1.00",
#     description = "Microsoft boat automation | Developed by Ubtohts ",
#     executables = executables
#     )
