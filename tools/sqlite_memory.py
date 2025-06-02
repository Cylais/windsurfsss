"""
SQLite-based Memory System for Windsurf Project

A robust, file-based memory backend using SQLite for persistence.

---
ONBOARDING & USAGE
---
- Purpose: Provides persistent, queryable memory for agents and tools (entities, relations, search, etc).
- Quickstart:
    from sqlite_memory import memory
    doc = memory.create_entity({'type': 'document', 'name': 'Test', 'content': 'Hello'})
    found = memory.get_entity(doc['id'])
- Agent/Automation Integration:
    - Use as a backend for AgentMemoryInterface or any agent needing persistent memory.
    - Compatible with multi-agent workflows and memory sync protocols.
- Logging:
    - All operations are logged to 'logs/sqlite_memory.log'.
    - Adjust logging config at the top of this file if needed.
- Troubleshooting:
    - See troubleshooting tips at the end of this file.
    - For memory sync issues, see tools/check_memory_sync.py and session protocols.

---
For more onboarding help, see memory_system_guide.ps1, session_start_protocol.md, and session_end_protocol.md.
"""

import sqlite3
import json
import os
from pathlib import Path
from typing import Dict, List, Optional, Any, Union
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(Path(__file__).parent.parent / 'logs' / 'sqlite_memory.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class SQLiteMemory:
    """A simple SQLite-based memory system for the Windsurf Project."""
    
    def __init__(self, db_path: str = None):
        """Initialize the SQLite memory system.
        
        Args:
            db_path: Path to the SQLite database file. If not provided, 
                    uses 'memory-bank/windsurf_memory.db'.
        """
        if db_path is None:
            db_path = str(Path(__file__).parent.parent / 'memory-bank' / 'windsurf_memory.db')
        
        self.db_path = db_path
        self._ensure_db_exists()
    
    def _get_connection(self) -> sqlite3.Connection:
        """Get a database connection."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Enable dictionary-style access
        return conn
    
    def _ensure_db_exists(self):
        """Ensure the database and tables exist."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            
            # Create entities table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS entities (
                    id TEXT PRIMARY KEY,
                    type TEXT NOT NULL,
                    name TEXT NOT NULL,
                    content TEXT,
                    metadata TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Create relations table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS relations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    source_id TEXT NOT NULL,
                    target_id TEXT NOT NULL,
                    type TEXT NOT NULL,
                    properties TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (source_id) REFERENCES entities(id),
                    FOREIGN KEY (target_id) REFERENCES entities(id),
                    UNIQUE(source_id, target_id, type)
                )
            ''')
            
            # Create indices for better performance
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_entities_type ON entities(type)')
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_relations_source ON relations(source_id)')
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_relations_target ON relations(target_id)')
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_relations_type ON relations(type)')
            
            conn.commit()
    
    def create_entity(self, entity_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new entity in the memory system.
        
        Args:
            entity_data: Dictionary containing entity data with keys:
                        - id: Unique identifier (optional, will be generated if not provided)
                        - type: Entity type (e.g., 'document', 'person', 'concept')
                        - name: Display name for the entity
                        - content: Main content or description
                        - metadata: Additional metadata as a dictionary
                        
        Returns:
            Dictionary containing the created entity data
        """
        # Generate an ID if not provided
        entity_id = entity_data.get('id', f"ent_{int(datetime.utcnow().timestamp() * 1000)}")
        
        # Prepare the entity data
        entity = {
            'id': entity_id,
            'type': entity_data.get('type', 'document'),
            'name': entity_data.get('name', 'Unnamed Entity'),
            'content': entity_data.get('content', ''),
            'metadata': json.dumps(entity_data.get('metadata', {})),
            'created_at': datetime.utcnow().isoformat(),
            'updated_at': datetime.utcnow().isoformat()
        }
        
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO entities (id, type, name, content, metadata, created_at, updated_at)
                VALUES (:id, :type, :name, :content, :metadata, :created_at, :updated_at)
            ''', entity)
            conn.commit()
        
        # Return the created entity with metadata as a dictionary
        entity['metadata'] = json.loads(entity['metadata'])
        return entity
    
    def get_entity(self, entity_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve an entity by its ID.
        
        Args:
            entity_id: ID of the entity to retrieve
            
        Returns:
            Dictionary containing the entity data, or None if not found
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM entities WHERE id = ?', (entity_id,))
            row = cursor.fetchone()
            
            if not row:
                return None
            
            # Convert row to dictionary
            entity = dict(row)
            entity['metadata'] = json.loads(entity['metadata']) if entity['metadata'] else {}
            return entity
    
    def update_entity(self, entity_id: str, updates: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Update an existing entity.
        
        Args:
            entity_id: ID of the entity to update
            updates: Dictionary of fields to update
            
        Returns:
            Dictionary containing the updated entity, or None if not found
        """
        # Get the existing entity
        entity = self.get_entity(entity_id)
        if not entity:
            return None
        
        # Update fields
        for key, value in updates.items():
            if key == 'metadata' and isinstance(value, dict):
                # Merge metadata dictionaries
                entity['metadata'].update(value)
                entity['metadata'] = json.dumps(entity['metadata'])
            elif key in ['type', 'name', 'content']:
                entity[key] = value
        
        # Update the timestamp
        entity['updated_at'] = datetime.utcnow().isoformat()
        
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE entities
                SET type = :type,
                    name = :name,
                    content = :content,
                    metadata = :metadata,
                    updated_at = :updated_at
                WHERE id = :id
            ''', entity)
            conn.commit()
        
        # Convert metadata back to dict for the response
        if 'metadata' in entity and isinstance(entity['metadata'], str):
            entity['metadata'] = json.loads(entity['metadata'])
            
        return entity
    
    def delete_entity(self, entity_id: str) -> bool:
        """Delete an entity from the memory system.
        
        Args:
            entity_id: ID of the entity to delete
            
        Returns:
            bool: True if the entity was deleted, False if not found
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            
            # First, delete any relations involving this entity
            cursor.execute('DELETE FROM relations WHERE source_id = ? OR target_id = ?', 
                         (entity_id, entity_id))
            
            # Then delete the entity
            cursor.execute('DELETE FROM entities WHERE id = ?', (entity_id,))
            conn.commit()
            
            return cursor.rowcount > 0
    
    def search_entities(self, query: str, entity_type: str = None, limit: int = 10) -> List[Dict[str, Any]]:
        """Search for entities by name or content.
        
        Args:
            query: Search query string
            entity_type: Optional entity type to filter by
            limit: Maximum number of results to return
            
        Returns:
            List of matching entities
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            
            search_term = f"%{query}%"
            
            if entity_type:
                cursor.execute('''
                    SELECT * FROM entities 
                    WHERE (name LIKE ? OR content LIKE ?) 
                      AND type = ?
                    ORDER BY updated_at DESC
                    LIMIT ?
                ''', (search_term, search_term, entity_type, limit))
            else:
                cursor.execute('''
                    SELECT * FROM entities 
                    WHERE name LIKE ? OR content LIKE ?
                    ORDER BY updated_at DESC
                    LIMIT ?
                ''', (search_term, search_term, limit))
            
            rows = cursor.fetchall()
            
            # Convert rows to dictionaries and parse metadata
            entities = []
            for row in rows:
                entity = dict(row)
                entity['metadata'] = json.loads(entity['metadata']) if entity['metadata'] else {}
                entities.append(entity)
            
            return entities
    
    def create_relation(self, source_id: str, target_id: str, 
                        relation_type: str, properties: Dict[str, Any] = None) -> Dict[str, Any]:
        """Create a relationship between two entities.
        
        Args:
            source_id: ID of the source entity
            target_id: ID of the target entity
            relation_type: Type of the relationship
            properties: Additional properties for the relationship
            
        Returns:
            Dictionary containing the created relation
        """
        if properties is None:
            properties = {}
        
        # Check if entities exist
        if not self.get_entity(source_id):
            raise ValueError(f"Source entity not found: {source_id}")
        if not self.get_entity(target_id):
            raise ValueError(f"Target entity not found: {target_id}")
        
        relation = {
            'source_id': source_id,
            'target_id': target_id,
            'type': relation_type,
            'properties': json.dumps(properties),
            'created_at': datetime.utcnow().isoformat()
        }
        
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO relations (source_id, target_id, type, properties, created_at)
                VALUES (:source_id, :target_id, :type, :properties, :created_at)
            ''', relation)
            relation['id'] = cursor.lastrowid
            conn.commit()
        
        # Convert properties back to dict for the response
        relation['properties'] = json.loads(relation['properties'])
        return relation
    
    def get_relations(self, entity_id: str = None, relation_type: str = None) -> List[Dict[str, Any]]:
        """Get relations from the memory system.
        
        Args:
            entity_id: Optional ID of an entity to get relations for
            relation_type: Optional type of relations to filter by
            
        Returns:
            List of relations
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            
            if entity_id and relation_type:
                cursor.execute('''
                    SELECT * FROM relations 
                    WHERE (source_id = ? OR target_id = ?) AND type = ?
                    ORDER BY created_at DESC
                ''', (entity_id, entity_id, relation_type))
            elif entity_id:
                cursor.execute('''
                    SELECT * FROM relations 
                    WHERE source_id = ? OR target_id = ?
                    ORDER BY created_at DESC
                ''', (entity_id, entity_id))
            elif relation_type:
                cursor.execute('''
                    SELECT * FROM relations 
                    WHERE type = ?
                    ORDER BY created_at DESC
                ''', (relation_type,))
            else:
                cursor.execute('SELECT * FROM relations ORDER BY created_at DESC')
            
            rows = cursor.fetchall()
            
            # Convert rows to dictionaries and parse properties
            relations = []
            for row in rows:
                relation = dict(row)
                relation['properties'] = json.loads(relation['properties']) if relation['properties'] else {}
                relations.append(relation)
            
            return relations
    
    def delete_relation(self, relation_id: int) -> bool:
        """Delete a relation by its ID.
        
        Args:
            relation_id: ID of the relation to delete
            
        Returns:
            bool: True if the relation was deleted, False if not found
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM relations WHERE id = ?', (relation_id,))
            conn.commit()
            return cursor.rowcount > 0

# Singleton instance
memory = SQLiteMemory()

# ---
# TROUBLESHOOTING & ONBOARDING TIPS
# ---
# - If you encounter 'database is locked', ensure no other process is holding a long transaction.
# - To reset the DB, delete 'memory-bank/windsurf_memory.db' (will be recreated on next use).
# - Logs are written to 'logs/sqlite_memory.log' for all operations and errors.
# - For integration with memory sync and protocols, see tools/check_memory_sync.py and session protocol docs.
# - For onboarding, see memory_system_guide.ps1 or contact the Architect agent.

# Example usage
if __name__ == "__main__":
    # Create a test database in memory
    test_db = ":memory:"
    mem = SQLiteMemory(test_db)
    
    # Create some test entities
    doc1 = mem.create_entity({
        'type': 'document',
        'name': 'Project Overview',
        'content': 'This is a test document about the Windsurf Project.',
        'metadata': {
            'author': 'system',
            'tags': ['important', 'overview']
        }
    })
    
    doc2 = mem.create_entity({
        'type': 'document',
        'name': 'Development Guide',
        'content': 'This guide explains how to develop features for the Windsurf Project.',
        'metadata': {
            'author': 'dev-team',
            'tags': ['guide', 'development']
        }
    })
    
    # Create a relation
    relation = mem.create_relation(
        source_id=doc1['id'],
        target_id=doc2['id'],
        relation_type='references',
        properties={'context': 'The overview references the development guide'}
    )
    
    # Search for entities
    results = mem.search_entities('windsurf')
    print(f"Found {len(results)} entities matching 'windsurf':")
    for entity in results:
        print(f"- {entity['name']} ({entity['type']}): {entity['content'][:50]}...")
    
    # Get relations
    relations = mem.get_relations(relation_type='references')
    print(f"\nFound {len(relations)} 'references' relations:")
    for rel in relations:
        print(f"- {rel['source_id']} -> {rel['target_id']}: {rel['properties'].get('context', '')}")
