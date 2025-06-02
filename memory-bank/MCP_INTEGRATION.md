# SQLite Memory System Integration

## Version: 1.0.0 (Last updated: 2025-05-25)

This document explains how the SQLite-based memory system works in the Windsurf Project.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Using the Memory System](#using-the-memory-system)
- [Troubleshooting](#troubleshooting)
- [Advanced Configuration](#advanced-configuration)

## Overview

The SQLite-based memory system provides a lightweight, file-based knowledge graph that integrates with the Windsurf Project's file-based memory bank. It enables:

- Semantic search across all project knowledge
- Entity-relationship modeling
- Cross-session memory persistence
- Advanced querying capabilities

## Prerequisites

- Python 3.8+
- No additional servers or services required

## Installation

The memory system requires no additional installation beyond the standard Python environment. The SQLite database will be created automatically when you first use the system.

## Using the Memory System

### Syncing Files to the Memory System

To sync your memory bank files with the SQLite database:

```bash
python tools/sync_memory.py
```

This will:

1. Scan all markdown files in the `memory-bank` directory
2. Create or update corresponding entities in the SQLite database
3. Maintain relationships between entities based on file structure and content

### Available Scripts

- `sync_memory.py` - Syncs memory bank with SQLite database
- `sqlite_memory.py` - Core SQLite memory implementation

## Troubleshooting

### Database Location

The SQLite database is stored at `memory-bank/windsurf_memory.db` by default.

Check the `logs` directory for detailed error messages if you encounter issues.

### Common Issues

- **Database is locked**: Ensure no other process is accessing the database
- **Permission errors**: Verify write permissions in the `memory-bank` directory
- **Corrupted database**: Delete the database file and let the system recreate it

## Advanced Configuration

### Customizing the Database Location

You can specify a custom database path when initializing the `SQLiteMemory` class:

```python
from sqlite_memory import SQLiteMemory

# Use a custom database path
memory = SQLiteMemory("path/to/custom_database.db")
```

### Extending the Schema

To add custom fields or modify the schema, edit the `_ensure_db_exists` method in `sqlite_memory.py`.

### Backing Up the Database

Since the database is a single file, you can back it up by simply copying `memory-bank/windsurf_memory.db` to a safe location.

## Next Steps

- [ ] Set up automatic syncing on file changes
- [ ] Implement scheduled backups
- [ ] Add web interface for browsing the knowledge graph
