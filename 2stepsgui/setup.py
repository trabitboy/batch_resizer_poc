## works
import cx_Freeze
import os.path

#no idea what I am doing , comes from stack overflow (other wise simple pygame fails)
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

executables = [cx_Freeze.Executable("batchresizedndwrkrnd.py")]

#copied from wx python wiki, no idea why it s needed
excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
            'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
            'Tkconstants', 'Tkinter']

cx_Freeze.setup(
    name="make an exe",
    options={"build_exe": {"packages":["pygame"
##                                       ,"wxPython"
                                       ],
                           "include_files":[
##                               "ship.png",
                               os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
                               os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
                               ],
                           "excludes":excludes,
                           }},
                            
    executables = executables

    )
