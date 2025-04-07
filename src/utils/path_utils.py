import os
from typing import Tuple, Optional

class PathUtils:
    """Handles path-related operations in a clean and organized way."""
    
    @staticmethod
    def get_paths() -> Tuple[Optional[str], Optional[str]]:
        """
        Get source and destination paths from user input.
        
        Returns:
            Tuple[Optional[str], Optional[str]]: Source and destination paths
        """
        print("\nEnter paths (or 'cancel' to return to menu):")
        
        source = input("Source path: ").strip()
        if PathUtils._is_cancel_command(source):
            return None, None
            
        destination = input("Destination path: ").strip()
        if PathUtils._is_cancel_command(destination):
            return None, None
            
        if not os.path.exists(source):
            print(f"Error: Source path '{source}' does not exist.")
            return None, None
            
        if not os.path.exists(destination):
            print(f"Error: Destination path '{destination}' does not exist.")
            return None, None
            
        return source, destination
    
    @staticmethod
    def _is_cancel_command(command: str) -> bool:
        """
        Check if the command is a cancel command.
        
        Args:
            command: Command to check
            
        Returns:
            bool: True if command is a cancel command
        """
        return command.lower() in ['cancel', '-c']
    
    @staticmethod
    def get_file_extension(filename: str) -> str:
        """
        Get the extension of a file.
        
        Args:
            filename: Name of the file
            
        Returns:
            str: File extension with dot (e.g., '.txt')
        """
        return os.path.splitext(filename)[1].lower()
    
    @staticmethod
    def join_paths(*paths: str) -> str:
        """
        Join multiple path components.
        
        Args:
            *paths: Path components to join
            
        Returns:
            str: Joined path
        """
        return os.path.join(*paths) 