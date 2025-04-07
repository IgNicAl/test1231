import platform
from typing import List
from ctypes import windll

class DriveOperations:
    """Handles drive-related operations in a clean and organized way."""
    
    @staticmethod
    def get_available_drives() -> List[str]:
        """
        Get list of available drives on the system.
        
        Returns:
            List[str]: List of available drive paths
        """
        if platform.system() == "Windows":
            return DriveOperations._get_windows_drives()
        return ["/"]  # For Unix-like systems
    
    @staticmethod
    def _get_windows_drives() -> List[str]:
        """Get available drives on Windows system."""
        drives = []
        bitmask = windll.kernel32.GetLogicalDrives()
        
        for letter in range(65, 91):  # A-Z
            if bitmask & (1 << (letter - 65)):
                drive = chr(letter) + ":\\"
                drives.append(drive)
        
        return drives 