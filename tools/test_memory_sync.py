#!/usr/bin/env python3
"""
Tests for the memory synchronization system.

---
ONBOARDING & USAGE
---
- Purpose: Verifies plug-and-play memory sync between file-based and SQLite/unified memory systems.
- How to Run (Manual):
    python -m unittest tools/test_memory_sync.py
- How to Run (PowerShell):
    python -m unittest tools/test_memory_sync.py
- How to Run (Bash):
    python3 -m unittest tools/test_memory_sync.py
- CI Integration:
    - Add to your CI pipeline to ensure memory sync logic is always validated.
    - Example (GitHub Actions):
        - name: Run Memory Sync Tests
          run: python -m unittest tools/test_memory_sync.py
- Multi-Agent/Workflow:
    - Validates core sync logic for all agent protocols (Architect, Coder, Reviewer, etc).
    - Reference: session_start_protocol.md, session_end_protocol.md, memory_system_guide.ps1
- Troubleshooting:
    - See troubleshooting tips at the end of this file.
    - Logs: See logs/ for output from sync/check scripts.
"""

import json
import os
import shutil
import tempfile
import unittest
from pathlib import Path
from typing import Dict, Any
from unittest.mock import patch, MagicMock

# Add the tools directory to the Python path
import sys
TOOLS_DIR = Path(__file__).parent.resolve()
sys.path.insert(0, str(TOOLS_DIR))

# Import the modules to test
from sync_memory import MemorySynchronizer
from check_memory_sync import MemorySyncChecker


class TestMemorySynchronization(unittest.TestCase):
    """Test cases for memory synchronization."""

    def setUp(self):
        """Set up test environment."""
        # Create a temporary directory
        self.test_dir = Path(tempfile.mkdtemp(prefix="memory_sync_test_"))
        
        # Set up test directories
        self.memory_bank_dir = self.test_dir / "memory-bank"
        self.logs_dir = self.test_dir / "logs"
        self.conflicts_dir = self.memory_bank_dir / "_conflicts"
        
        # Create directories
        self.memory_bank_dir.mkdir()
        self.logs_dir.mkdir()
        self.conflicts_dir.mkdir()
        
        # Initialize a test file
        self.test_file = self.memory_bank_dir / "test_file.md"
        self.test_file.write_text("# Test File\n\nThis is a test file.")
        

    
    def tearDown(self):
        """Clean up test environment."""
        # Stop all patches

        
        # Remove temporary directory
        shutil.rmtree(self.test_dir)
    
    def test_synchronizer_initialization(self):
        """Test MemorySynchronizer initialization."""
        sync = MemorySynchronizer()
        self.assertIsInstance(sync.sync_state, dict)
    
    def test_file_processing(self):
        """Test processing of a memory file."""
        sync = MemorySynchronizer()
        entity = sync.process_file(self.test_file)
        
        self.assertIsNotNone(entity)
        self.assertEqual(entity['name'], 'test_file')
        self.assertEqual(entity['entityType'], 'document')
        self.assertIn('This is a test file', entity['observations'][0])
    

    
    def test_sync_checker(self):
        """Test sync status checking."""
        # First, sync a file
        sync = MemorySynchronizer()

        
        # Now check status
        checker = MemorySyncChecker()
        checker.check_sync_status()
        
        # Verify status
        self.assertEqual(checker.status['total_files'], 1)
        self.assertEqual(checker.status['synced'], 1)
        self.assertEqual(checker.status['out_of_sync'], 0)
        self.assertEqual(checker.status['never_synced'], 0)


class TestConflictResolution(unittest.TestCase):
    """Test cases for conflict resolution."""
    
    def setUp(self):
        """Set up test environment."""
        # Create a temporary directory
        self.test_dir = Path(tempfile.mkdtemp(prefix="conflict_test_"))
        
        # Set up test directories
        self.memory_bank_dir = self.test_dir / "memory-bank"
        self.logs_dir = self.test_dir / "logs"
        self.conflicts_dir = self.memory_bank_dir / "_conflicts"
        
        # Create directories
        self.memory_bank_dir.mkdir()
        self.logs_dir.mkdir()
        self.conflicts_dir.mkdir()
        
        # Initialize a test file with a conflict
        self.conflict_file = self.memory_bank_dir / "conflict_file.md"
        conflict_content = """# Conflict Test

<<<<<<< HEAD
This is the local change.
=======
This is the remote change.
>>>>>>> abc123
"""
        self.conflict_file.write_text(conflict_content)
    
    def tearDown(self):
        """Clean up test environment."""
        shutil.rmtree(self.test_dir)
    
    def test_conflict_detection(self):
        """Test detection of merge conflicts."""
        sync = MemorySynchronizer()
        
        # Process the conflict file
        entity = sync.process_file(self.conflict_file)
        
        # Should not process files with conflicts
        self.assertIsNone(entity)
        
        # Verify conflict was moved to conflicts directory
        conflict_files = list(self.conflicts_dir.glob("*"))
        self.assertEqual(len(conflict_files), 1)
        self.assertIn("conflict_file", str(conflict_files[0]))


if __name__ == "__main__":
    unittest.main()

# ---
# TROUBLESHOOTING & ONBOARDING TIPS
# ---
# - If tests fail, check logs/ for memory_sync.log and review error output.
# - Ensure all dependencies are installed (requirements.txt, requirements-dev.txt).
# - For onboarding, see memory_system_guide.ps1 and protocol docs.
# - For CI failures, ensure temporary directories are writable and not locked by other processes.
# - These tests validate core memory sync for all agents and workflows—run regularly!
