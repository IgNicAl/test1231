import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from typing import Optional

from ..core.file_operations import FileOperations
from ..core.drive_operations import DriveOperations
from ..core.file_organizer import FileOrganizer
from ..utils.logging import Logger
from ..utils.path_utils import PathUtils
from .cli_app import print_help

# Initialize console and logger
console = Console()
logger = Logger()

@click.group()
@click.version_option(version="1.0.0", prog_name="OnlyFiles")
@click.option('--directory', '-d', type=click.Path(exists=True, file_okay=False, dir_okay=True), help='Directory to work with')
@click.option('--extension', '-e', is_flag=True, help='Organize by extension')
@click.option('--date', '-t', is_flag=True, help='Organize by date')
@click.option('--size', '-s', is_flag=True, help='Organize by size')
@click.option('--type', '-y', is_flag=True, help='Organize by type')
@click.option('--backup', '-b', is_flag=True, help='Create backup of files')
@click.option('--revert', '-r', is_flag=True, help='Revert to last backup')
@click.option('--move', '-m', is_flag=True, help='Move files')
@click.option('--drives', '-v', is_flag=True, help='List available drives')
@click.option('--logs', '-l', is_flag=True, help='View operation logs')
@click.option('--clear-logs', '-c', is_flag=True, help='Clear operation logs')
def cli(directory: str, extension: bool, date: bool, size: bool, type: bool, 
        backup: bool, revert: bool, move: bool, drives: bool, logs: bool, clear_logs: bool):
    """
    Main CLI command group for OnlyFiles.
    
    This function handles all the main operations of the application:
    
    - File organization (by extension, date, size, type)
    - File backup and restore
    - File movement
    - Drive listing
    - Log management
    """
    if not any([extension, date, size, type, backup, revert, move, drives, logs, clear_logs]):
        print_help()
        return

    # Handle file organization operations
    if extension or date or size or type:
        if not directory:
            console.print("[red]Directory (-d) is required for organization operations[/red]")
            return
        organize_files(directory, extension, date, size, type)

    # Handle backup operations
    if backup:
        if not directory:
            console.print("[red]Directory (-d) is required for backup operation[/red]")
            return
        if FileOperations.create_backup(directory):
            console.print(f"[green]Backup created successfully for {directory}[/green]")
            logger.info(f"Backup created for {directory}")
        else:
            console.print(f"[red]Failed to create backup for {directory}[/red]")
            logger.error(f"Failed to create backup for {directory}")

    # Handle revert operations
    if revert:
        if not directory:
            console.print("[red]Directory (-d) is required for revert operation[/red]")
            return
        if FileOperations.revert_to_backup(directory):
            console.print(f"[green]File {directory} reverted successfully[/green]")
            logger.info(f"File {directory} reverted to backup")
        else:
            console.print(f"[red]Failed to revert {directory}[/red]")
            logger.error(f"Failed to revert {directory}")

    # Handle file movement operations
    if move:
        if not directory:
            console.print("[red]Directory (-d) is required for move operation[/red]")
            return
        source, destination = PathUtils.get_paths()
        if not source or not destination:
            return
        moved_files = FileOperations.move_files(source, destination)
        if moved_files:
            console.print(f"[green]Successfully moved {len(moved_files)} files[/green]")
            for file in moved_files:
                logger.info(f"Moved file: {file}")
        else:
            console.print("[yellow]No files were moved[/yellow]")
            logger.info("No files were moved")

    # Handle drive listing operations
    if drives:
        drives_list = DriveOperations.get_available_drives()
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Drive", style="dim")
        table.add_column("Status")
        
        for drive in drives_list:
            table.add_row(drive, "[green]Available[/green]")
        
        console.print(Panel(table, title="Available Drives", border_style="blue"))

    # Handle log viewing operations
    if logs:
        log_entries = logger.get_logs()
        if log_entries:
            console.print("\n=== Operation Logs ===\n")
            for entry in log_entries:
                console.print(entry.strip())
            console.print("\n=== End of Logs ===\n")
        else:
            console.print("[yellow]No logs found[/yellow]")

    # Handle log clearing operations
    if clear_logs:
        if logger.clear_logs():
            console.print("[green]Logs cleared successfully[/green]")
        else:
            console.print("[red]Failed to clear logs[/red]")

def _display_organization_results(title: str, organized_files: dict):
    """
    Helper function to display organization results in a table.
    
    Args:
        title: Title for the results table
        organized_files: Dictionary with organization results
    """
    if not any(organized_files.values()):
        console.print(f"[yellow]No files were organized by {title.lower()}[/yellow]")
        return

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column(title, style="dim")
    table.add_column("Files Moved")
    
    for key, files in organized_files.items():
        if files:  # Only show categories that have files
            table.add_row(key, str(len(files)))
    
    console.print(Panel(table, title=f"Files Organized by {title}", border_style="blue"))
    logger.info(f"Organized files by {title.lower()}")

def organize_files(directory: str, extension: bool, date: bool, size: bool, type: bool):
    """
    Helper function to organize files based on specified criteria.
    
    Args:
        directory: Directory to organize
        extension: Whether to organize by extension
        date: Whether to organize by date
        size: Whether to organize by size
        type: Whether to organize by type
    """
    if extension:
        organized_files = FileOrganizer.organize_by_extension(directory)
        _display_organization_results("Extension", organized_files)
    
    if date:
        organized_files = FileOrganizer.organize_by_date(directory)
        _display_organization_results("Date", organized_files)
    
    if size:
        organized_files = FileOrganizer.organize_by_size(directory)
        _display_organization_results("Size Category", organized_files)
    
    if type:
        organized_files = FileOrganizer.organize_by_type(directory)
        _display_organization_results("File Type", organized_files) 