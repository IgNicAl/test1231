import sys
import os
from pathlib import Path
from src.cli.terminal_interface import TerminalInterface

def print_help():
    """
    Print a formatted help message.
    
    This function displays the main help text with all available commands and options.
    The text is loaded from a separate file for easier maintenance.
    """
    # Determinar o caminho do arquivo de ajuda
    help_file_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
        "resources", 
        "help_text.txt"
    )
    
    try:
        # Tentar ler o arquivo de ajuda
        with open(help_file_path, "r", encoding="utf-8") as help_file:
            help_text = help_file.read()
        print(help_text)
    except Exception as e:
        # Fallback para o caso do arquivo não existir ou não puder ser lido
        print(f"Erro ao carregar o arquivo de ajuda: {str(e)}")
        print("Para mais informações, visite: https://github.com/MichaelBittencourt/OnlyFiles")

def main():
    """
    Main entry point for the OnlyFiles CLI application.
    
    This function handles the main program flow and command parsing.
    """
    if len(sys.argv) == 1 or "--help" in sys.argv or "-h" in sys.argv:
        print_help()
        sys.exit(0)
    elif "--version" in sys.argv:
        try:
            from src import __version__
        except ImportError:
            __version__ = "unknown"
        print(f"OnlyFiles version {__version__}")
        sys.exit(0)
    elif len(sys.argv) > 1 and sys.argv[1] == "start":
        interface = TerminalInterface()
        interface.start()
    else:
        print("Error: Unknown command or option")
        print_help()
        sys.exit(1)

if __name__ == "__main__":
    main() 