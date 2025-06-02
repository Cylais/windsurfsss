"""
Unified Memory Interface
=======================

---
ONBOARDING & USAGE
---
- Purpose: Provides a unified, plug-and-play memory API for all Windsurf agents and workflows.
- Quickstart:
    from unified_memory import memory
    doc = memory.create_entity({'type': 'document', 'name': 'Test', 'content': 'Hello'})
    found = memory.get_entity(doc['id'])
- Agent/Automation Integration:
    - Use as the main memory interface for all agents (Architect, Coder, Reviewer, etc.).
    - Compatible with multi-agent, protocol-driven, and CI/CD workflows.
- CI/Automation:
    - Add to your CI pipeline to validate memory logic and run syncs.
    - Example:
        python -m unittest tools/test_memory_sync.py
- Protocol References:
    - See session_start_protocol.md, session_end_protocol.md, memory_system_guide.ps1 for onboarding and integration.
- Troubleshooting:
    - See troubleshooting tips at the end of this file.
    - Logs: logs/memory_system.log
"""

import os
import logging
from pathlib import Path
from typing import Dict, List, Optional, Any, Union
import json
from datetime import datetime

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/memory_system.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('unified_memory')

# Import SQLite memory implementation
from sqlite_memory import SQLiteMemory

class UnifiedMemory:
    """
    Unified interface to the Windsurf memory system.
    Provides a consistent API for all agents to interact with the memory system.
    """
    
    def __init__(self, memory_bank_dir: str = None, db_path: str = None):
        """Initialize the unified memory system.
        
        Args:
            memory_bank_dir: Path to the memory bank directory (default: ../memory-bank)
            db_path: Path to the SQLite database (default: memory-bank/windsurf_memory.db)
        """
        # Set up paths
        self.base_dir = Path(__file__).parent.parent
        self.memory_bank_dir = Path(memory_bank_dir) if memory_bank_dir else self.base_dir / 'memory-bank'
        self.db_path = db_path if db_path else self.memory_bank_dir / 'windsurf_memory.db'
        
        # Ensure directories exist
        self.memory_bank_dir.mkdir(exist_ok=True)
        (self.base_dir / 'logs').mkdir(exist_ok=True)
        
        # Initialize SQLite memory
        self.db = SQLiteMemory(str(self.db_path))
        
        logger.info(f"Initialized UnifiedMemory with memory bank at {self.memory_bank_dir}")
    
    def create_entity(self, entity_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new entity in the memory system.
        
        Args:
            entity_data: Dictionary containing entity data
            
        Returns:
            Created entity with generated ID
        """
        # Add metadata
        entity_data['metadata'] = entity_data.get('metadata', {})
        entity_data['metadata']['created_at'] = datetime.utcnow().isoformat()
        entity_data['metadata']['updated_at'] = datetime.utcnow().isoformat()
        
        # Create in database
        result = self.db.create_entity(entity_data)
        
        logger.info(f"Created entity {result.get('id')} of type {entity_data.get('type', 'unknown')}")
        return result
    
    def get_entity(self, entity_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve an entity by ID.
        
        Args:
            entity_id: ID of the entity to retrieve
            
        Returns:
            Entity data or None if not found
        """
        return self.db.get_entity(entity_id)
    
    def update_entity(self, entity_id: str, updates: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Update an existing entity.
        
        Args:
            entity_id: ID of the entity to update
            updates: Dictionary of fields to update
            
        Returns:
            Updated entity or None if not found
        """
        # Update metadata
        updates['metadata'] = updates.get('metadata', {})
        updates['metadata']['updated_at'] = datetime.utcnow().isoformat()
        
        result = self.db.update_entity(entity_id, updates)
        if result:
            logger.info(f"Updated entity {entity_id}")
        else:
            logger.warning(f"Failed to update entity {entity_id}: not found")
        return result
    
    def delete_entity(self, entity_id: str) -> bool:
        """Delete an entity.
        
        Args:
            entity_id: ID of the entity to delete
            
        Returns:
            True if deleted, False otherwise
        """
        success = self.db.delete_entity(entity_id)
        if success:
            logger.info(f"Deleted entity {entity_id}")
        else:
            logger.warning(f"Failed to delete entity {entity_id}: not found")
        return success
    
    def search_entities(self, query: str, entity_type: str = None, limit: int = 10) -> List[Dict[str, Any]]:
        """Search for entities matching the query.
        
        Args:
            query: Search query string
            entity_type: Optional entity type filter
            limit: Maximum number of results to return
            
        Returns:
            List of matching entities
        """
        return self.db.search_entities(query, entity_type, limit)
    
    def create_relationship(self, from_id: str, to_id: str, rel_type: str, data: Dict = None) -> bool:
        """Create a relationship between two entities.
        
        Args:
            from_id: Source entity ID
            to_id: Target entity ID
            rel_type: Type of relationship
            data: Additional relationship data
            
        Returns:
            True if created, False otherwise
        """
        return self.db.create_relationship(from_id, to_id, rel_type, data or {})
    
    def get_relationships(self, entity_id: str, rel_type: str = None) -> List[Dict[str, Any]]:
        """Get relationships for an entity.
        
        Args:
            entity_id: Entity ID
            rel_type: Optional relationship type filter
            
        Returns:
            List of relationships
        """
        return self.db.get_relationships(entity_id, rel_type)
    
    def sync_from_files(self) -> Dict[str, Any]:
        """Synchronize the database with the file-based memory bank.
        
        Returns:
            Dictionary with sync statistics
        """
        from sync_memory import MemorySynchronizer
        
        syncer = MemorySynchronizer()
        success = syncer.sync_to_sqlite()
        
        return {
            'success': success,
            'processed': len(syncer.sync_state),
            'errors': syncer.error_count if hasattr(syncer, 'error_count') else 0
        }

# Singleton instance for easy importing
memory = UnifiedMemory()

# ---
# TROUBLESHOOTING & ONBOARDING TIPS
# ---
# - If you encounter errors, check logs/memory_system.log for details.
# - Ensure all dependencies are installed (requirements.txt, requirements-dev.txt).
# - For onboarding and advanced integration, see memory_system_guide.ps1 and protocol docs.
# - Use this interface for all agent and automation memory needs—no direct SQLite or file access required.
