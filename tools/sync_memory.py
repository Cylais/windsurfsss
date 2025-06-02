#!/usr/bin/env python3
"""
Memory Synchronization Tool for Windsurf Project

Synchronizes content between file-based memory bank and the SQLite memory system.

---
ONBOARDING & USAGE
---
- Purpose: Keeps the file-based memory-bank and the SQLite memory backend in sync for all agents and workflows.
- Quickstart:
    python tools/sync_memory.py
- Automation/CI:
    - Add this script to your CI pipeline or agent startup/end protocols to ensure memory is always synchronized.
    - Example (PowerShell):
        python tools/sync_memory.py
    - Example (Bash):
        python3 tools/sync_memory.py
- Multi-Agent Workflows:
    - Safe for use by multiple agents (Architect, Coder, Reviewer, etc.) as part of session protocols.
    - Integrates with check_memory_sync.py for validation and troubleshooting.
- Troubleshooting:
    - See troubleshooting tips at the end of this script.
    - Logs are written to logs/memory_sync.log for review.
- Related Protocols & Docs:
    - See session_start_protocol.md, session_end_protocol.md, and memory_system_guide.ps1 for full onboarding and workflow integration.
"""

import os
import hashlib
import logging
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
from datetime import datetime
import json
import sys

# Add the tools directory to the path so we can import our modules
sys.path.append(str(Path(__file__).parent))

# Import our SQLite memory module
from sqlite_memory import SQLiteMemory



# Configure logging
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_DIR / 'memory_sync.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Constants
MEMORY_BANK_DIR = Path("memory-bank")
CONFLICT_DIR = MEMORY_BANK_DIR / "_conflicts"
SYNC_STATE_FILE = LOG_DIR / ".sync_state.json"

# Ensure directories exist
for directory in [MEMORY_BANK_DIR, CONFLICT_DIR, LOG_DIR]:
    directory.mkdir(exist_ok=True)

# Ensure directories exist
for directory in [MEMORY_BANK_DIR, CONFLICT_DIR, LOG_DIR]:
    directory.mkdir(exist_ok=True)

class MemorySynchronizer:
    """Handles synchronization between file-based and SQLite memory systems."""
    
    def __init__(self):
        self.sync_state = self._load_sync_state()
    
    def _load_sync_state(self) -> Dict:
        """Load the synchronization state from disk."""
        if SYNC_STATE_FILE.exists():
            try:
                with open(SYNC_STATE_FILE, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                logger.warning("Corrupted sync state file, starting fresh")
        return {}
    
    def _save_sync_state(self):
        """Save the current synchronization state to disk."""
        with open(SYNC_STATE_FILE, 'w') as f:
            json.dump(self.sync_state, f, indent=2)
    
    def calculate_file_hash(self, file_path: Path) -> str:
        """Calculate a hash of the file's content."""
        hasher = hashlib.sha256()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    
    def has_changes(self, file_path: Path) -> bool:
        """Check if a file has changed since last sync."""
        file_str = str(file_path.relative_to(MEMORY_BANK_DIR))
        current_hash = self.calculate_file_hash(file_path)
        
        if file_str not in self.sync_state:
            return True
            
        return self.sync_state[file_str].get('hash') != current_hash
    
    def update_sync_state(self, file_path: Path, entity_id: str):
        """Update the sync state after processing a file."""
        file_str = str(file_path.relative_to(MEMORY_BANK_DIR))
        self.sync_state[file_str] = {
            'hash': self.calculate_file_hash(file_path),
            'last_synced': datetime.utcnow().isoformat(),
            'entity_id': entity_id
        }
    
    def process_file(self, file_path: Path) -> Optional[dict]:
        """Process a single memory bank file and return parsed entity data."""
        if not self.has_changes(file_path):
            logger.debug(f"No changes detected in {file_path}")
            return None
            
        logger.info(f"Processing {file_path}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Parse metadata from frontmatter if present
            metadata = {}
            if content.startswith('---'):
                try:
                    _, frontmatter, content = content.split('---', 2)
                    import yaml
                    metadata = yaml.safe_load(frontmatter) or {}
                except Exception as e:
                    logger.warning(f"Error parsing frontmatter in {file_path}: {e}")
            
            # Create entity data
            entity = {
                'name': file_path.stem,
                'entityType': metadata.get('type', 'document'),
                'observations': [content.strip()],
                'metadata': {
                    'source': 'file_based',
                    'file_path': str(file_path.relative_to(MEMORY_BANK_DIR)),
                    'last_updated': datetime.utcnow().isoformat(),
                    **metadata.get('metadata', {})
                }
            }
            
            return entity
            
        except Exception as e:
            logger.error(f"Error processing {file_path}: {e}", exc_info=True)
            return None
    
    def sync_to_sqlite(self) -> bool:
        """Synchronize all memory bank files with the SQLite database."""
        logger.info("Starting memory synchronization with SQLite database")
        
        # Initialize the memory system
        memory = SQLiteMemory()
        
        # Process all markdown files in memory bank
        memory_files = list(MEMORY_BANK_DIR.glob("**/*.md"))
        memory_files = [f for f in memory_files if f.is_file() and f.parent != CONFLICT_DIR]
        
        success_count = 0
        error_count = 0
        
        for file_path in memory_files:
            entity_data = self.process_file(file_path)
            if not entity_data:
                continue
                
            try:
                file_str = str(file_path.relative_to(MEMORY_BANK_DIR))
                entity_id = self.sync_state.get(file_str, {}).get('entity_id')
                
                # Prepare entity data for the database
                entity = {
                    'type': entity_data.get('entityType', 'document'),
                    'name': entity_data.get('name', file_path.stem),
                    'content': '\n'.join(entity_data.get('observations', [])),
                    'metadata': {
                        'source': 'file_based',
                        'file_path': file_str,
                        'last_updated': datetime.utcnow().isoformat(),
                        **entity_data.get('metadata', {})
                    }
                }
                
                # Create or update entity in the database
                if entity_id:
                    # Try to update existing entity
                    existing_entity = memory.get_entity(entity_id)
                    if existing_entity:
                        # Update the existing entity
                        updated_entity = memory.update_entity(entity_id, entity)
                        logger.info(f"Updated entity {entity_id} from {file_path}")
                        success_count += 1
                    else:
                        # If entity not found, create a new one
                        logger.warning(f"Entity {entity_id} not found, creating new entity")
                        created_entity = memory.create_entity({
                            'id': entity_id,  # Keep the same ID
                            **entity
                        })
                        entity_id = created_entity['id']
                        logger.info(f"Created new entity {entity_id} from {file_path}")
                        success_count += 1
                else:
                    # Create new entity
                    created_entity = memory.create_entity(entity)
                    entity_id = created_entity['id']
                    logger.info(f"Created new entity {entity_id} from {file_path}")
                    success_count += 1
                
                # Update sync state
                self.update_sync_state(file_path, entity_id)
                
            except Exception as e:
                error_count += 1
                logger.error(f"Error syncing {file_path} to SQLite: {e}", exc_info=True)
        
        # Save the updated sync state
        self._save_sync_state()
        
        # Log summary
        logger.info(f"Memory synchronization complete: {success_count} files synced, {error_count} errors")
        return error_count == 0

def main():
    """Main entry point for the sync script."""
    try:
        logger.info("Starting memory synchronization with SQLite database")
        logger.info(f"Memory bank directory: {MEMORY_BANK_DIR.absolute()}")
        
        synchronizer = MemorySynchronizer()
        success = synchronizer.sync_to_sqlite()
        
        if success:
            logger.info("Memory synchronization completed successfully")
            return 0
        else:
            logger.error("Memory synchronization completed with errors")
            return 1
            
    except Exception as e:
        logger.critical(f"Fatal error during synchronization: {e}", exc_info=True)
        return 2

if __name__ == "__main__":
    sys.exit(main())

# ---
# TROUBLESHOOTING & MULTI-AGENT WORKFLOW NOTES
# ---
# - If you see 'database is locked', ensure no agent or tool is holding a long transaction.
# - For sync errors, review logs/memory_sync.log and use tools/check_memory_sync.py for diagnostics.
# - This script is designed for safe use in multi-agent and CI/CD workflows—always run before and after major memory changes.
# - For onboarding and advanced usage, see memory_system_guide.ps1 and session protocol docs.
