"""
Configuration settings for the OnlyFiles application.
"""

from .version import VERSION
from .paths import (
    ROOT_DIR,
    LOGS_DIR,
    CONFIG_DIR,
    LOG_FILE,
    DEPENDENCY_LINKS_FILE,
    SOURCES_FILE,
    ENTRY_POINTS_FILE,
    REQUIRES_FILE,
    TOP_LEVEL_FILE
)

__all__ = [
    'VERSION',
    'ROOT_DIR',
    'LOGS_DIR',
    'CONFIG_DIR',
    'LOG_FILE',
    'DEPENDENCY_LINKS_FILE',
    'SOURCES_FILE',
    'ENTRY_POINTS_FILE',
    'REQUIRES_FILE',
    'TOP_LEVEL_FILE'
] 