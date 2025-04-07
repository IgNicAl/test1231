import click
from rich.console import Console
from rich.table import Table

from ..core.file_operations import FileOperations
from ..core.drive_operations import DriveOperations
from .interface import CustomHelp, display_menu
from ..config.version import VERSION

console = Console()

@click.group(cls=CustomHelp)
@click.version_option(version=VERSION, prog_name="OnlyFiles")
@click.option('-d', '--directory', help='Directory to work with')
@click.option('-e', '--extension', is_flag=True, help='Organize by extension')
@click.option('-t', '--date', is_flag=True, help='Organize by date')
@click.option('-s', '--size', is_flag=True, help='Organize by size')
@click.option('-y', '--type', is_flag=True, help='Organize by type')
@click.option('-b', '--backup', is_flag=True, help='Create backup of files')
@click.option('-r', '--revert', is_flag=True, help='Revert to last backup')
@click.option('-m', '--move', is_flag=True, help='Move files')
@click.option('-v', '--drives', is_flag=True, help='List available drives')
@click.option('-l', '--logs', is_flag=True, help='View operation logs')
@click.option('-c', '--clear-logs', is_flag=True, help='Clear operation logs')
def cli(**kwargs):
    """OnlyFiles - A powerful file management and backup CLI tool."""
    if kwargs.get('drives'):
        drives_cmd()
    elif kwargs.get('backup') and kwargs.get('directory'):
        backup_cmd(kwargs.get('directory'))
    elif kwargs.get('revert') and kwargs.get('directory'):
        revert_cmd(kwargs.get('directory'))
    else:
        display_menu()

def backup_cmd(file_path):
    """Create a backup of the specified file."""
    if FileOperations.create_backup(file_path):
        console.print(f"[green]Backup created successfully for {file_path}[/green]")
    else:
        console.print(f"[red]Failed to create backup for {file_path}[/red]")

@cli.command()
@click.argument('file_path', type=click.Path(exists=True))
def backup(file_path):
    """Create a backup of the specified file."""
    backup_cmd(file_path)

def revert_cmd(file_path):
    """Revert file to its most recent backup."""
    if FileOperations.revert_to_backup(file_path):
        console.print(f"[green]File {file_path} reverted successfully[/green]")
    else:
        console.print(f"[red]Failed to revert {file_path}[/red]")

@cli.command()
@click.argument('file_path', type=click.Path(exists=True))
def revert(file_path):
    """Revert a file to its most recent backup."""
    revert_cmd(file_path)

def drives_cmd():
    """List available drives."""
    drives = DriveOperations.get_available_drives()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Drive", style="dim")
    table.add_column("Status")
    
    for drive in drives:
        drive_info = DriveOperations.get_drive_info(drive)
        if "error" not in drive_info:
            status = f"[green]Available ({drive_info['free'] / (1024**3):.1f} GB free)[/green]"
        else:
            status = "[red]Unavailable[/red]"
        table.add_row(drive, status)
    
    console.print(table)

@cli.command()
def drives():
    """List available drives."""
    drives_cmd()

def interactive_mode():
    """Run the application in interactive mode."""
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == "1":
            file_path = input("Enter file path to backup: ")
            backup_cmd(file_path)
        elif choice == "2":
            file_path = input("Enter file path to revert: ")
            revert_cmd(file_path)
        elif choice == "3":
            drives_cmd()
        elif choice == "4":
            console.print("[yellow]Goodbye![/yellow]")
            break
        else:
            console.print("[red]Invalid choice. Please try again.[/red]")

@cli.command()
def interactive():
    """Run the application in interactive mode."""
    interactive_mode()

if __name__ == '__main__':
    cli() 