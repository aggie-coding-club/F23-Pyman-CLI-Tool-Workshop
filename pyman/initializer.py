"""
initialization script for pyman:
    1. find and return python binary file paths
        1a. search paths in path env var
        1b. recursively search default paths in os
    2. run binary file paths and return a dictionary of {ver: path}
    3. copy all binary files into ~/.pyman dir and rename them as pyman[ver]
"""
import subprocess
import os
import shutil
import re

def getPythonPaths():
    """
    step(1): find and return all python binary files found within the $PATH env var & default paths

    Returns:
        list (str): path to python binary files
    """
    pyPaths = []
    # get $PATH env var and get individual paths to search through
    paths = os.environ['PATH'].strip().split(":")

    # parse paths to see if python exists 
    for path in paths:
        files = os.listdir(path) if (os.path.isdir(path)) else []
        for file in files:
            if (re.search("^python(\d*\.*)+(exe)?$", file)):
                pyPaths.append(f"{path}/{file}")

    # recursively searches common python installation paths
    user = os.environ['USER']
    installPaths = [f"C:\\Users\\"+user+"\\AppData\\Local\\Programs\\Python"]
    def recursiveSearch(path):
        files = os.listdir(path) if (os.path.isdir(path)) else []
        for file in files:
            if (os.path.isdir(f"{path}/{file}")):
                recursiveSearch(f"{path}/{file}")
            if (re.search("^python(\d*\.*)+(exe)?$", file)):
                pyPaths.append(f"{path}/{file}")

    for installPath in installPaths:
        if (os.path.exists(installPath)):
            recursiveSearch(installPath)

    return pyPaths

def getPythonVersions(pythonPaths):
    """
    step(2): runs the pythonfile via the direct path to get the version then adds the version & path to dictionary 
    version should be in the format "Python x.x.x" if not well then ur fucked

    Args:
        pythonPaths [list (str)]: paths to the python executable/binary file

    Returns:
        dict {str: str}: dictionary with key being the version and value being the path
    """
    data = {}
    for pythonPath in pythonPaths:
        version = subprocess.check_output(f"{pythonPath} -V", shell=True, text=True)
        version = version.strip().split()[-1]
        data[version] = pythonPath
    return data

def createCopies(pythonPaths):
    """
    step(3): creates copies of pythonfiles from parsed paths into ~/.pyman directory and renames the files as pyman[ver]

    Args:
        pythonPaths [dict {str:str}]: dictionary with key being the version and value being the path

    """
    dir = os.path.expanduser("~")+"/.pyman"
    if (not os.path.isdir(dir)):
        os.makedirs(dir) # make .pyman folder if it doesn't exist
    for ver, path in pythonPaths.items():
        shutil.copy(path, f"{dir}/pyman{ver}") # using shutil because it's independent of shell

def initialize():
    """
    convientent initialization function that combines all the initialization steps
    
    Returns:
        dict {str: str}: dictionary with key being the version and value being the path
    """
    try:
        paths = getPythonPaths()
        pyman = getPythonVersions(paths)
        createCopies(pyman)
    except:
        raise
    
    return pyman






