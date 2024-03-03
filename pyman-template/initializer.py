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
    pass

def getPythonVersions(pythonPaths):
    """
    step(2): runs the pythonfile via the direct path to get the version then adds the version & path to dictionary 
    version should be in the format "Python x.x.x" if not well then ur fucked

    Args:
        pythonPaths [list (str)]: paths to the python executable/binary file

    Returns:
        dict {str: str}: dictionary with key being the version and value being the path
    """
    pass

def createCopies(pythonPaths):
    """
    step(3): creates copies of pythonfiles from parsed paths into ~/.pyman directory and renames the files as pyman[ver]

    Args:
        pythonPaths [dict {str:str}]: dictionary with key being the version and value being the path

    """
    pass

def initialize():
    """
    convientent initialization function that combines all the initialization steps
    
    Returns:
        dict {str: str}: dictionary with key being the version and value being the path
    """
    pass






