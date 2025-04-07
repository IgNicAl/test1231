# OnlyFiles

A powerful command-line tool for file management and backup operations.

## Features

- Create backups of files with timestamps
- Revert files to their most recent backup
- List available drives on the system
- Interactive mode for easy operation

## Installation

```bash
pip install -e .
```

## Usage

### Command Line Interface

```bash
# Show help
onlyfiles --help

# Show version
onlyfiles --version

# Create a backup
onlyfiles backup <file_path>

# Revert a file
onlyfiles revert <file_path>

# List available drives
onlyfiles drives

# Start interactive mode
onlyfiles interactive
```

### Interactive Mode

The interactive mode provides a user-friendly menu interface for all operations.

## Requirements

- Python 3.6 or higher
- click
- rich 