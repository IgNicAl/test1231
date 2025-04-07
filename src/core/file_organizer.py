import os
import shutil
from datetime import datetime
from typing import List, Dict, Optional
from pathlib import Path

class FileOrganizer:
    """Handles file organization operations in a clean and organized way."""
    
    @staticmethod
    def organize_by_extension(directory: str) -> Dict[str, List[str]]:
        """
        Organize files by their extensions into separate folders.
        
        Args:
            directory: Directory to organize
            
        Returns:
            Dict[str, List[str]]: Dictionary with extension as key and list of moved files as value
        """
        if not os.path.exists(directory):
            return {}
            
        organized_files = {}
        files = os.listdir(directory)
        
        for file in files:
            file_path = os.path.join(directory, file)
            if not os.path.isfile(file_path):
                continue
                
            # Get file extension without the dot
            extension = os.path.splitext(file)[1][1:].lower() or 'no_extension'
            
            # Create extension directory if it doesn't exist
            extension_dir = os.path.join(directory, extension)
            os.makedirs(extension_dir, exist_ok=True)
            
            # Move file to extension directory
            try:
                shutil.move(file_path, os.path.join(extension_dir, file))
                if extension not in organized_files:
                    organized_files[extension] = []
                organized_files[extension].append(file)
            except Exception:
                continue
                
        return organized_files
    
    @staticmethod
    def organize_by_date(directory: str) -> Dict[str, List[str]]:
        """
        Organize files by their creation date into year/month folders.
        
        Args:
            directory: Directory to organize
            
        Returns:
            Dict[str, List[str]]: Dictionary with date as key and list of moved files as value
        """
        if not os.path.exists(directory):
            return {}
            
        organized_files = {}
        files = os.listdir(directory)
        
        for file in files:
            file_path = os.path.join(directory, file)
            if not os.path.isfile(file_path):
                continue
                
            # Get file creation time
            creation_time = os.path.getctime(file_path)
            date = datetime.fromtimestamp(creation_time)
            
            # Create year/month directory structure
            year_dir = os.path.join(directory, str(date.year))
            month_dir = os.path.join(year_dir, str(date.month).zfill(2))
            os.makedirs(month_dir, exist_ok=True)
            
            # Move file to date directory
            try:
                shutil.move(file_path, os.path.join(month_dir, file))
                date_key = f"{date.year}/{date.month:02d}"
                if date_key not in organized_files:
                    organized_files[date_key] = []
                organized_files[date_key].append(file)
            except Exception:
                continue
                
        return organized_files
    
    @staticmethod
    def organize_by_size(directory: str) -> Dict[str, List[str]]:
        """
        Organize files by their size into categories (small, medium, large).
        
        Args:
            directory: Directory to organize
            
        Returns:
            Dict[str, List[str]]: Dictionary with size category as key and list of moved files as value
        """
        if not os.path.exists(directory):
            return {}
            
        organized_files = {
            'small': [],    # < 1MB
            'medium': [],   # 1MB - 10MB
            'large': []     # > 10MB
        }
        
        files = os.listdir(directory)
        
        for file in files:
            file_path = os.path.join(directory, file)
            if not os.path.isfile(file_path):
                continue
                
            # Get file size in bytes
            size_bytes = os.path.getsize(file_path)
            size_mb = size_bytes / (1024 * 1024)  # Convert to MB
            
            # Determine size category
            if size_mb < 1:
                category = 'small'
            elif size_mb < 10:
                category = 'medium'
            else:
                category = 'large'
            
            # Create category directory
            category_dir = os.path.join(directory, category)
            os.makedirs(category_dir, exist_ok=True)
            
            # Move file to category directory
            try:
                shutil.move(file_path, os.path.join(category_dir, file))
                organized_files[category].append(file)
            except Exception:
                continue
                
        return organized_files
    
    @staticmethod
    def organize_by_type(directory: str) -> Dict[str, List[str]]:
        """
        Organize files by their type (images, documents, audio, video, etc.).
        
        Args:
            directory: Directory to organize
            
        Returns:
            Dict[str, List[str]]: Dictionary with file type as key and list of moved files as value
        """
        if not os.path.exists(directory):
            return {}
            
        # Define file type categories and their extensions
        type_categories = {
            'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'],
            'documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx'],
            'audio': ['.mp3', '.wav', '.flac', '.m4a', '.aac', '.ogg'],
            'video': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv'],
            'archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
            'code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.h', '.php'],
            'others': []
        }
        
        organized_files = {category: [] for category in type_categories.keys()}
        files = os.listdir(directory)
        
        for file in files:
            file_path = os.path.join(directory, file)
            if not os.path.isfile(file_path):
                continue
                
            # Get file extension
            extension = os.path.splitext(file)[1].lower()
            
            # Determine file category
            category = 'others'
            for cat, extensions in type_categories.items():
                if extension in extensions:
                    category = cat
                    break
            
            # Create category directory
            category_dir = os.path.join(directory, category)
            os.makedirs(category_dir, exist_ok=True)
            
            # Move file to category directory
            try:
                shutil.move(file_path, os.path.join(category_dir, file))
                organized_files[category].append(file)
            except Exception:
                continue
                
        return organized_files
        
    @staticmethod
    def organize_directory(directory: str) -> Dict[str, List[str]]:
        """
        Organize files in a directory using multiple criteria.
        
        Args:
            directory: Directory to organize
            
        Returns:
            Dict[str, List[str]]: Dictionary with organization criteria as key and list of moved files as value
        """
        if not os.path.exists(directory):
            return {}
            
        # Organize by type (this is the default organization method)
        return FileOrganizer.organize_by_type(directory)
        
    @staticmethod
    def revert_last_organization(directory: Optional[str] = None) -> bool:
        """
        Revert the last organization operation by moving files back to their original locations.
        
        Args:
            directory: Directory to revert organization, defaults to current directory
            
        Returns:
            bool: True if reverted successfully, False otherwise
        """
        try:
            # Get the target directory
            target_dir = directory if directory and os.path.exists(directory) else os.getcwd()
            
            # Get all subdirectories in the target directory
            subdirs = [d for d in os.listdir(target_dir) if os.path.isdir(os.path.join(target_dir, d))]
            
            # Skip if no subdirectories (nothing to revert)
            if not subdirs:
                return False
            
            # Move files from each subdirectory back to the parent directory
            for subdir in subdirs:
                subdir_path = os.path.join(target_dir, subdir)
                files = os.listdir(subdir_path)
                
                for file in files:
                    source = os.path.join(subdir_path, file)
                    destination = os.path.join(target_dir, file)
                    
                    # Check if destination file already exists
                    if os.path.exists(destination):
                        # Append a unique identifier to avoid overwriting
                        base, ext = os.path.splitext(file)
                        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                        new_filename = f"{base}_{timestamp}{ext}"
                        destination = os.path.join(target_dir, new_filename)
                    
                    # Move file back to parent directory
                    shutil.move(source, destination)
                
                # Remove empty subdirectory
                os.rmdir(subdir_path)
            
            return True
            
        except Exception:
            return False 