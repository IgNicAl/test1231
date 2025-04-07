import os
from pathlib import Path

# Get the project root directory
ROOT_DIR = Path(__file__).parent.parent.parent.parent

# Define paths for different types of files
LOGS_DIR = ROOT_DIR / "logs"
CONFIG_DIR = ROOT_DIR / "config"

# Ensure directories exist
LOGS_DIR.mkdir(exist_ok=True)
CONFIG_DIR.mkdir(exist_ok=True)

# Define specific file paths
LOG_FILE = LOGS_DIR / "app.log"
DEPENDENCY_LINKS_FILE = CONFIG_DIR / "dependency_links.txt"
SOURCES_FILE = CONFIG_DIR / "SOURCES.txt"
ENTRY_POINTS_FILE = CONFIG_DIR / "entry_points.txt"
REQUIRES_FILE = CONFIG_DIR / "requires.txt"
TOP_LEVEL_FILE = CONFIG_DIR / "top_level.txt" 