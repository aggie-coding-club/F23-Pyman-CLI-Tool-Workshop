"""
helper file for switching logic when switch command is called
"""
import sys
import os
import subprocess
import shutil

def brancher():
    """
    controls branching logic for pyman by sorting by os and then shell environment

    Returns:
        str: path to profile to be edited
    """
    unix = ["linux", "linux2", "darwin"]
    windows = ["win32", "win64", "cygwin", "msys"]
    opSys = sys.platform
    if (opSys in unix):
        shellPath = os.environ['HOME']+"/."+os.environ['SHELL'].split("/")[-1]+"rc"
    elif (opSys in windows):
        shellPath = subprocess.check_output("$PROFILE", shell = True, text=True)
    else:
        print(opSys, "is not supported by pyman")
        return None
    return shellPath

def writer(path):
    """
    writes the commands to switch python versions in dotfiles/profile

    Args:
        path (str): path to dotfile/profile
    """
    pymanDir = os.path.expanduser("~")+"/.pyman"

    # first check if there's already something written
    pathFound = False
    shellConfig = []
    with open(path) as f:
        shellConfig = f.readlines()
    for line in shellConfig:
        if line == f"""export PATH="$PATH:{pymanDir}"\n""":
            pathFound = True

    with open(path, "a") as f:
        if (not pathFound):
            f.write(f"""\nexport PATH="$PATH:{pymanDir}"\n""")


def source(path):
    """
    properly sources edited dotfiles

    Args:
        path (str): path to dotfile
    """
    try:
        os.system(f"source {path}")
    except:
        os.system(f". {path}")

def switcher(ver):
    """
    main function to switch python versions

    Args:
        ver (str): python version to switch to
    """
    try:
        # copy desired version as 'pie' executable
        dir = os.path.expanduser("~")+"/.pyman"
        shutil.copy(f"{dir}/pyman{ver}", f"{dir}/pie")
        
        # add .pyman directory to path
        try:
            path = brancher()
            writer(path)
            source(path)
        except:
            print("Failed to add .pyman to path; manual intervention required")
                    
    except:
        raise
    

