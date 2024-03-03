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
    pass
    # search for all python files with initialization script & get data
    
    # create & add to rich table, then print out table
    
@app.command()
def switch(version: Annotated[Optional[str], "version to switch to"] = None):
    pass
    # search for all python files with initialization script & get data

    # switching logic
        # if no version is passed in, then create select interface for user
        # if version is passed in, set main pyman file to pyman[ver] 
    
@app.command()
def clean():
    pass

if __name__ == "__main__":
    app()
