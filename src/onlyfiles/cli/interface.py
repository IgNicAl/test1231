import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.box import ROUNDED
from rich.layout import Layout
from rich.text import Text
from rich.style import Style
from rich.syntax import Syntax

from ..core.file_operations import FileOperations
from ..core.drive_operations import DriveOperations
from ..config.version import VERSION

console = Console()

class CustomHelp(click.Group):
    """Custom help formatter for the CLI"""
    def format_help(self, ctx, formatter):
        help_console = Console(highlight=False)
        
        # Header
        header_text = f"[bold blue]OnlyFiles v{VERSION}[/bold blue]"
        description = "[italic]A powerful file management and backup CLI tool[/italic]"
        header = Panel(
            f"{header_text}\n{description}",
            border_style="blue",
            box=ROUNDED
        )
        help_console.print(header)

        # Organization options
        org_table = Table(box=ROUNDED, title="📁 [bold cyan]ORGANIZATION OPTIONS[/bold cyan]")
        org_table.add_column("Option", style="bold yellow")
        org_table.add_column("Description")
        org_table.add_row("-e, --extension", "Organize by extension (.txt, .pdf, etc)")
        org_table.add_row("-t, --date", "Organize by creation date (year/month)")
        org_table.add_row("-s, --size", "Organize by size (small/medium/large)")
        org_table.add_row("-y, --type", "Organize by type (images/docs/audio)")
        help_console.print(org_table)

        # File operations
        file_table = Table(box=ROUNDED, title="🔄 [bold magenta]FILE OPERATIONS[/bold magenta]")
        file_table.add_column("Option", style="bold yellow")
        file_table.add_column("Description")
        file_table.add_row("-b, --backup", "Create backup of specified file")
        file_table.add_row("-r, --revert", "Revert to last backup")
        file_table.add_row("-m, --move", "Move files between locations")
        help_console.print(file_table)

        # System operations
        sys_table = Table(box=ROUNDED, title="⚙️ [bold green]SYSTEM OPERATIONS[/bold green]")
        sys_table.add_column("Option", style="bold yellow")
        sys_table.add_column("Description")
        sys_table.add_row("-v, --drives", "List available drives")
        sys_table.add_row("-l, --logs", "View operation logs")
        sys_table.add_row("-c, --clear-logs", "Clear operation logs")
        help_console.print(sys_table)

        # Examples
        examples = Text("\n📋 USAGE EXAMPLES", style="bold blue")
        help_console.print(examples)
        help_console.print("""
[bold]▪ Organize files:[/bold]
  [yellow]onlyfiles -d /path/to/dir -e[/yellow]         # By extension
  [yellow]onlyfiles -d /path/to/dir -t[/yellow]         # By date
  [yellow]onlyfiles -d /path/to/dir -s[/yellow]         # By size
  [yellow]onlyfiles -d /path/to/dir -y[/yellow]         # By type

[bold]▪ File operations:[/bold]
  [yellow]onlyfiles -d /path/to/file -b[/yellow]        # Create backup
  [yellow]onlyfiles -d /path/to/file -r[/yellow]        # Revert to backup
  [yellow]onlyfiles -d /path/to/dir -m[/yellow]         # Move files

[bold]▪ System operations:[/bold]
  [yellow]onlyfiles -v[/yellow]                         # List drives
  [yellow]onlyfiles -l[/yellow]                         # View logs
  [yellow]onlyfiles -c[/yellow]                         # Clear logs
""")

        # Notes
        notes = Text("\n📝 NOTES", style="bold blue")
        help_console.print(notes)
        help_console.print("""
[bold]▪[/bold] -d/--directory is required for most operations
[bold]▪[/bold] Multiple organization criteria can be combined
[bold]▪[/bold] All operations are logged automatically
""")

        # Command options
        help_console.print("\n[bold]OPTIONS:[/bold]")
        # Format options manually instead of using formatter.write_dl
        options_table = Table(box=None, show_header=False, padding=(0, 2))
        options_table.add_column("Option", style="bold yellow")
        options_table.add_column("Description")
        
        for param in ctx.command.get_params(ctx):
            opts = "/".join(param.opts)
            if param.help:
                options_table.add_row(opts, param.help)
            
        help_console.print(options_table)

def display_menu():
    """Display the main menu using rich formatting"""
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Option", style="dim")
    table.add_column("Description")
    
    table.add_row("1", "Create backup")
    table.add_row("2", "Revert to last backup")
    table.add_row("3", "List available drives")
    table.add_row("4", "Exit")
    
    console.print(Panel(table, title="File Management System", border_style="blue")) 