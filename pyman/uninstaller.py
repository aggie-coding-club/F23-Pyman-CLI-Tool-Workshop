"""
uninstall script to remove pyman crap from your pc
"""
import os
from switcher import brancher, source
from rich.progress import track

def removePymanDir(path):
    """
    Removes the pyman directory created during initialization

    Args
        path (str): installation path for .pyman
    """
    if (os.path.isdir(path)):
        files = os.listdir(path)
        for file in track(files):
            os.remove(f"{path}/{file}")
        os.rmdir(path)
    else:
        print("Pyman directory not found...")
        exit("Exiting...")

def removeConfigChanges(path):
    """
    Deletes lines written in config files
    
    Args
        path (str): installation path for .pyman
    """
    shellPath = brancher()

    # first check if there's already something written
    shellConfig = []
    with open(shellPath) as f:
        shellConfig = f.readlines()
    # then fucking eat shit
    with open(shellPath, "w") as f:
        for line in shellConfig:
            if line == f"""export PATH="$PATH:{path}"\n""":
                continue
            f.write(line)

    source(shellPath)

def uninstall():
    try:
        dir = os.path.expanduser("~")+"/.pyman"
        removePymanDir(dir)
        
        try:
            removeConfigChanges(dir)
        except:
            print("Failed to remove .pyman from path; manual intervention required")
            
    except:
        raise
