import os
import shutil
from datetime import datetime
from typing import Optional, List, Tuple

class FileOperations:
    @staticmethod
    def create_backup(file_path: str) -> bool:
        """
        Create a backup of the specified file with timestamp.
        
        Args:
            file_path (str): Path to the file to backup
            
        Returns:
            bool: True if backup was successful, False otherwise
        """
        if not os.path.exists(file_path):
            return False
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = f"{file_path}.backup_{timestamp}"
        
        try:
            shutil.copy2(file_path, backup_path)
            return True
        except Exception:
            return False

    @staticmethod
    def revert_to_backup(file_path: str) -> bool:
        """
        Revert a file to its most recent backup.
        
        Args:
            file_path (str): Path to the file to revert
            
        Returns:
            bool: True if revert was successful, False otherwise
        """
        if not os.path.exists(file_path):
            return False
        
        backups = [f for f in os.listdir(os.path.dirname(file_path)) 
                  if f.startswith(os.path.basename(file_path) + ".backup_")]
        
        if not backups:
            return False
        
        latest_backup = max(backups, key=lambda x: os.path.getctime(
            os.path.join(os.path.dirname(file_path), x)))
        backup_path = os.path.join(os.path.dirname(file_path), latest_backup)
        
        try:
            shutil.copy2(backup_path, file_path)
            return True
        except Exception:
            return False

    @staticmethod
    def get_file_info(file_path: str) -> Optional[Tuple[str, int, datetime]]:
        """
        Get basic information about a file.
        
        Args:
            file_path (str): Path to the file
            
        Returns:
            Optional[Tuple[str, int, datetime]]: Tuple of (extension, size, creation_time)
                                                or None if file doesn't exist
        """
        if not os.path.exists(file_path):
            return None
            
        return (
            os.path.splitext(file_path)[1],
            os.path.getsize(file_path),
            datetime.fromtimestamp(os.path.getctime(file_path))
        ) 