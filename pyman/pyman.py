from initializer import initialize 
from switcher import switcher
from uninstaller import uninstall

from typer import Typer
from typing import Optional
from typing_extensions import Annotated
from inquirer import prompt, List
from rich.console import Console
from rich.table import Table
from rich.text import Text

app = Typer()
console = Console()

@app.command()
def list():
    # search for all python files with initialization script & get data
    try:
        pymanData = initialize()
    except Exception as e:
        print("Exception occurred while running initialization script:\n", e)
        exit("Exiting...")
    
    # create & add to rich table, then print out table
    try:
        table = Table(title="Pyman Versions")
        table.add_column("Version")
        table.add_column("Path", style="magenta")
        for k, v in pymanData.items():
            table.add_row(k, v)
        console.print(table)
    except Exception as e:
        print("Exception occurred while creating & printing table:\n", e)
        exit("Exiting...")
    

@app.command()
def switch(version: Annotated[Optional[str], "version to switch to"] = None):
    # search for all python files with initialization script & get data
    try:
        pymanData = initialize()
    except Exception as e:
        print("Exception occurred while running initialization script:\n", e)
        exit("Exiting...")
    
    # switching logic
    try:
        # if no version is passed in, then create select interface for user
        if (version == None):
            question = List("version", message="Select a version to switch to", choices=pymanData.keys())
            selectedVersion = prompt([question])["version"]
            switcher(selectedVersion)
        # if version is passed in, set main pyman file to pyman[ver] 
        else:
            switcher(version)
        console.print(Text.assemble((f"Successfully switched to version {selectedVersion if (version == None) else version}\n", "bold green")))
    except Exception as e:
        print("Exception occurred while switching versions:\n", e)
        exit("Exiting...")
    
@app.command()
def clean():
    try:
        uninstall()
        console.print(Text.assemble((f"Successfully removed pyman\n", "bold red")))
    except Exception as e:
        print("Error ocurred while cleaning:", e)
        exit("Exiting....")

if __name__ == "__main__":
    app()
