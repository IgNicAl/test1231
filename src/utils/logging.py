import os
from pathlib import Path
from datetime import datetime

class Logger:
    """Handles logging operations in a clean and organized way."""
    
    def __init__(self):
        self.log_dir = Path.home() / '.onlyfiles' / 'logs'
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.log_file = self.log_dir / f"onlyfiles_{datetime.now().strftime('%Y%m')}.log"
    
    def get_log_file(self) -> Path:
        """Returns the path of the current log file."""
        return self.log_file
    
    def info(self, message: str):
        """Logs an information message."""
        self._write_log('INFO', message)
    
    def error(self, message: str):
        """Logs an error message."""
        self._write_log('ERROR', message)
    
    def warning(self, message: str):
        """Logs a warning message."""
        self._write_log('WARNING', message)
    
    def _write_log(self, level: str, message: str):
        """Writes a message to the log file."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] {level}: {message}\n"
        
        try:
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(log_entry)
        except Exception as e:
            print(f"Error writing to log: {str(e)}")
    
    def clear_logs(self) -> bool:
        """Clears the current log file."""
        try:
            if self.log_file.exists():
                self.log_file.unlink()
                self.log_file.touch()
            return True
        except Exception:
            return False
    
    def get_logs(self) -> str:
        """Returns the content of the current log file."""
        try:
            if self.log_file.exists():
                with open(self.log_file, 'r', encoding='utf-8') as f:
                    return f.read()
            return ""
        except Exception:
            return "" 