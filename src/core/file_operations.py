import os
import shutil
from datetime import datetime
from typing import Tuple, List, Optional

class FileOperations:
    """Handles all file-related operations in a clean and organized way."""
    
    @staticmethod
    def create_backup(path: str) -> bool:
        """
        Create a backup of the specified file or directory with timestamp.
        
        Args:
            path: Path to the file or directory to backup
            
        Returns:
            bool: True if backup was successful, False otherwise
        """
        if not os.path.exists(path):
            return False
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = f"{path}.backup_{timestamp}"
        
        try:
            if os.path.isfile(path):
                shutil.copy2(path, backup_path)
            else:
                shutil.copytree(path, backup_path)
            return True
        except Exception:
            return False
    
    @staticmethod
    def revert_to_backup(path: str) -> bool:
        """
        Revert file or directory to its most recent backup.
        
        Args:
            path: Path to the file or directory to revert
            
        Returns:
            bool: True if revert was successful, False otherwise
        """
        if not os.path.exists(path):
            return False
        
        backups = FileOperations._get_backup_files(path)
        if not backups:
            return False
        
        latest_backup = max(backups, key=lambda x: os.path.getctime(x))
        
        try:
            if os.path.isfile(path):
                shutil.copy2(latest_backup, path)
            else:
                # Remove existing directory and replace with backup
                shutil.rmtree(path)
                shutil.copytree(latest_backup, path)
            return True
        except Exception:
            return False
    
    @staticmethod
    def move_files(source_path: str, destination_path: str, file_pattern: Optional[str] = None) -> List[str]:
        """
        Move files from source to destination, optionally filtering by pattern.
        
        Args:
            source_path: Source directory path
            destination_path: Destination directory path
            file_pattern: Optional pattern to filter files (e.g., "*.txt")
            
        Returns:
            List[str]: List of successfully moved files
        """
        if not os.path.exists(source_path) or not os.path.exists(destination_path):
            return []
        
        moved_files = []
        files = os.listdir(source_path)
        
        for file in files:
            if file_pattern and not file.endswith(file_pattern):
                continue
                
            source = os.path.join(source_path, file)
            destination = os.path.join(destination_path, file)
            
            if os.path.isfile(source):
                try:
                    shutil.move(source, destination)
                    moved_files.append(file)
                except Exception:
                    continue
        
        return moved_files
    
    @staticmethod
    def _get_backup_files(path: str) -> List[str]:
        """
        Get list of backup files for a given file or directory path.
        
        Args:
            path: Path to the file or directory
            
        Returns:
            List[str]: List of backup file/directory paths
        """
        directory = os.path.dirname(path)
        name = os.path.basename(path)
        return [
            os.path.join(directory, f) 
            for f in os.listdir(directory) 
            if f.startswith(name + ".backup_")
        ] 