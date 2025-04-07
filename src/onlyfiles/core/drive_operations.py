import platform
from typing import List

class DriveOperations:
    @staticmethod
    def get_available_drives() -> List[str]:
        """
        Get list of available drives on the system.
        
        Returns:
            List[str]: List of available drive paths
        """
        if platform.system() == "Windows":
            from ctypes import windll
            drives = []
            bitmask = windll.kernel32.GetLogicalDrives()
            for letter in range(65, 91):  # A-Z
                if bitmask & (1 << (letter - 65)):
                    drive = chr(letter) + ":\\"
                    drives.append(drive)
            return drives
        else:
            return ["/"]  # For Unix-like systems

    @staticmethod
    def get_drive_info(drive_path: str) -> dict:
        """
        Get information about a specific drive.
        
        Args:
            drive_path (str): Path to the drive
            
        Returns:
            dict: Dictionary containing drive information
        """
        import os
        import shutil
        
        try:
            total, used, free = shutil.disk_usage(drive_path)
            return {
                "total": total,
                "used": used,
                "free": free,
                "path": drive_path
            }
        except Exception:
            return {
                "total": 0,
                "used": 0,
                "free": 0,
                "path": drive_path,
                "error": "Unable to access drive"
            } 