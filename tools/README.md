# Memory Management Tools

This directory contains tools for managing the Windsurf project's memory system, which uses SQLite for efficient storage and retrieval of project knowledge.

## Tools

### sync_memory.py

Synchronizes content between the file-based memory bank and the SQLite database.

**Usage:**

```bash
python tools/sync_memory.py
```

**Features:**

- Detects changes in memory bank files
- Creates/updates corresponding entities in the SQLite database
- Maintains sync state in `.sync_state.json`
- Handles conflicts by preserving file-based changes
- Logs all operations to `logs/memory_sync.log`
- Automatically creates the SQLite database if it doesn't exist

### check_memory_sync.py

Checks the synchronization status between the file-based memory bank and the SQLite database.

**Usage:**

```bash
# Basic status
python tools/check_memory_sync.py

# Detailed status
python tools/check_memory_sync.py --detailed

# JSON output
python tools/check_memory_sync.py --json
```

**Exit Codes:**

- `0`: All files are in sync
- `1`: Some files are out of sync or have never been synced

## Memory System Architecture

The memory system uses a dual-layer architecture for optimal performance and maintainability:

1. **File-based Memory Layer** (`memory-bank/`)
   - Human-readable markdown files
   - Version-controlled history
   - Primary source of truth
   - Easy to edit and review

2. **SQLite Database Layer** (`memory-bank/windsurf_memory.db`)
   - Efficient storage and querying
   - Automatic indexing for fast lookups
   - Transaction support for data integrity
   - No server required - runs locally

## Workflow

1. **During Development**
   - Edit files in `memory-bank/`
   - Run `sync_memory.py` to update the SQLite database
   - Use `check_memory_sync.py` to verify sync status

2. **Automated Sync**
   - The system automatically syncs on session start/end
   - Changes are tracked using file hashes
   - Conflicts are logged and can be reviewed

3. **Backup and Recovery**
   - The SQLite database is a single file that can be easily backed up
   - To restore, simply replace the database file and run `sync_memory.py`

## Best Practices

1. **File Naming**
   - Use kebab-case for file names
   - Keep file names descriptive but concise
   - Group related files in subdirectories

2. **Metadata**
   - Use YAML frontmatter for metadata
   - Include relevant tags and categories
   - Add timestamps for important changes

3. **Synchronization**
   - Run sync after making significant changes
   - Check sync status before important operations
   - Review and resolve any conflicts promptly

## Troubleshooting

### Common Issues

1. **Sync Failures**
   - Check `logs/memory_sync.log` for errors
   - Verify write permissions in the `memory-bank` directory
   - Ensure files have valid markdown syntax

2. **Database Locked**
   - Ensure no other process is accessing the database
   - Delete the lock file if the previous process was terminated unexpectedly

3. **Corrupted Database**
   - Restore from backup if available
   - Or delete the database file and let the system recreate it on next sync
   - Verify disk space is available

4. **Conflict Resolution**
   - Review files in `memory-bank/_conflicts/`
   - Manually merge changes if needed
   - Update the sync state after resolution
