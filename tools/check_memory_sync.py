#!/usr/bin/env python3
"""
Memory Sync Status Checker
=========================

Checks the synchronization status between file-based memory bank and SQLite memory system.

References:
- Onboarding: README.md, docs/AGENT_GUIDE.md
- Sync/Protocols: tools/sync_memory.py, docs/memory-protocols.md, rules/session_management.rules.md
- CI Integration: See stub at end of file

Prerequisite: Run sync_memory.py before using this checker to generate the sync state file.
"""

import json
import logging
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime, timezone
import sys

# Configure logging
# Ensure log directory exists
LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(str(LOG_DIR / 'memory_sync.log')),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Constants
MEMORY_BANK_DIR = Path("memory-bank")
LOG_DIR = Path("logs")
SYNC_STATE_FILE = LOG_DIR / ".sync_state.json"

class MemorySyncChecker:
    """
    Checks synchronization status between file-based and SQLite memory systems.
    Methods can be used via CLI or imported as a module.
    """
    
    def __init__(self, verbose: bool = False):
        """
        Args:
            verbose (bool): If True, print detailed status to stdout.
        """
        self.verbose = verbose
        self.sync_state = self._load_sync_state()
        self.status = {
            'total_files': 0,
            'synced': 0,
            'out_of_sync': 0,
            'never_synced': 0,
            'last_sync': None,
            'details': []
        }
    
    def _load_sync_state(self) -> Dict:
        """Load the synchronization state from disk."""
        if not SYNC_STATE_FILE.exists():
            logger.warning("No sync state file found. Run sync_memory.py first.")
            return {}
            
        try:
            with open(SYNC_STATE_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            logger.error(f"Error loading sync state: {e}")
            return {}
    
    def check_sync_status(self) -> int:
        """
        Check synchronization status of all memory files.
        Returns an exit code: 0=all synced, 1=out-of-sync, 2=error/no sync state.
        """
        if not self.sync_state:
            logger.error("No sync state available. Please run sync_memory.py first.")
            return 2  # Fixed: Ensure function returns an int exit code for error state
        
        memory_files = list(MEMORY_BANK_DIR.glob("**/*.md"))
        self.status['total_files'] = len(memory_files)
        
        latest_sync = None
        
        for file_path in memory_files:
            rel_path = str(file_path.relative_to(MEMORY_BANK_DIR))
            file_stat = file_path.stat()
            
            if rel_path not in self.sync_state:
                self.status['never_synced'] += 1
                self.status['details'].append({
                    'file': rel_path,
                    'status': 'never_synced',
                    'last_modified': datetime.fromtimestamp(file_stat.st_mtime).isoformat()
                })
                continue
                
            sync_info = self.sync_state[rel_path]
            last_modified = datetime.fromtimestamp(file_stat.st_mtime)
            last_synced = datetime.fromisoformat(sync_info['last_synced'])
            
            # Track the most recent sync time
            if latest_sync is None or last_synced > latest_sync:
                latest_sync = last_synced
                
            if last_modified > last_synced.replace(tzinfo=timezone.utc).astimezone():
                self.status['out_of_sync'] += 1
                status = 'out_of_sync'
            else:
                self.status['synced'] += 1
                status = 'synced'
                
            self.status['details'].append({
                'file': rel_path,
                'status': status,
                'last_modified': datetime.fromtimestamp(file_stat.st_mtime).isoformat(),
                'last_synced': sync_info['last_synced']
            })  # Fixed: Added missing dictionary key/value pairs and closed brace
        
        # Protocol reference log
        logger.info("Checked according to Unified Memory System protocols (see docs/memory-protocols.md).")
        logger.info(f"Total files: {self.status['total_files']}")
        logger.info(f"Synced: {self.status['synced']}")
        logger.info(f"Out of sync: {self.status['out_of_sync']}")
        logger.info(f"Never synced: {self.status['never_synced']}")
        logger.info(f"Last sync: {self.status['last_sync']}")
        
        if self.verbose:
            print(json.dumps(self.status, indent=2))
        else:
            print(f"Sync Status: {self.status['synced']} synced, {self.status['out_of_sync']} out of sync, {self.status['never_synced']} never synced.")
        
        if self.status['out_of_sync'] == 0 and self.status['never_synced'] == 0:
            logger.info("All memory files are in sync.")
            return 0
        else:
            logger.warning("Some memory files are out of sync or never synced.")
            return 1

def main():
    """
    Main entry point for the sync checker.
    Usage:
        python tools/check_memory_sync.py [--verbose|--quiet]
    Returns exit code: 0=all synced, 1=out-of-sync, 2=error/no sync state.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Check memory sync status.")
    parser.add_argument('--verbose', action='store_true', help='Show full sync status JSON.')
    parser.add_argument('--quiet', action='store_true', help='Suppress all output except exit code.')
    args = parser.parse_args()

    checker = MemorySyncChecker(verbose=args.verbose)
    exit_code = checker.check_sync_status()
    if args.quiet:
        pass  # Suppress output
    return exit_code

# Example importable usage:
# from tools.check_memory_sync import MemorySyncChecker
# checker = MemorySyncChecker(verbose=True)
# code = checker.check_sync_status()

# CI Integration Stub:
# - Add the following to your CI pipeline to fail if memory is out of sync:
#   python tools/check_memory_sync.py --quiet
#   if [ $? -ne 0 ]; then echo "Memory out of sync!"; exit 1; fi
    checker = MemorySyncChecker()
    checker.check_sync_status()
    
    if args.json:
        import json
        print(json.dumps(checker.status, indent=2))
    else:
        print(checker.generate_report(detailed=args.detailed))
    
    # Return non-zero exit code if there are sync issues
    if checker.status.get('out_of_sync', 0) > 0 or checker.status.get('never_synced', 0) > 0:
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
