"""
Memory System CLI
=================

Command-line interface for interacting with the Windsurf unified memory system.

References:
- Onboarding: README.md, docs/AGENT_GUIDE.md
- Memory Protocols: docs/memory-protocols.md, tools/unified_memory.py
- Workflow: See project.yaml and docs/WORKFLOWS.md

Prerequisite: The memory system must be initialized before using this CLI.

Example usage:
  python tools/memory_cli.py create agent --data '{"name": "Agent Smith"}'
  python tools/memory_cli.py get <entity_id>
  python tools/memory_cli.py update <entity_id> --data '{"role": "Reviewer"}'
  python tools/memory_cli.py list agent
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, Any, Optional, List

# Add parent directory to path to allow imports
sys.path.append(str(Path(__file__).parent.parent))

from tools.unified_memory import UnifiedMemory

def print_entity(entity: Dict[str, Any], indent: int = 0) -> None:
    """
    Print entity data in a readable format.
    Args:
        entity (dict): The entity to print.
        indent (int): Number of spaces to indent.
    """
    indent_str = ' ' * indent
    if not entity:
        print(f"{indent_str}No entity found")
        return
    print(f"{indent_str}ID: {entity.get('id', '<unknown>')}")
    print(f"{indent_str}Type: {entity.get('type', 'unknown')}")
    # Print metadata
    if 'metadata' in entity:
        print(f"{indent_str}Metadata:")
        for k, v in entity['metadata'].items():
            print(f"{indent_str}  {k}: {v}")
    # Print other fields
    for k, v in entity.items():
        if k not in ('id', 'type', 'metadata'):
            if isinstance(v, (dict, list)):
                print(f"{indent_str}{k}:")
                print(json.dumps(v, indent=2))
            else:
                print(f"{indent_str}{k}: {v}")

def parse_args():
    """
    Parse command line arguments for the memory CLI.
    Returns:
        argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description='Windsurf Memory System CLI')
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # Create entity
    create_parser = subparsers.add_parser('create', help='Create a new entity')
    create_parser.add_argument('type', help='Entity type')
    create_parser.add_argument('--data', help='JSON string with entity data')
    
    # Get entity
    get_parser = subparsers.add_parser('get', help='Get an entity by ID')
    get_parser.add_argument('entity_id', help='Entity ID')
    
    # Update entity
    update_parser = subparsers.add_parser('update', help='Update an entity')
    update_parser.add_argument('entity_id', help='Entity ID')
    update_parser.add_argument('--data', required=True, help='JSON string with updates')

    # List entities
    list_parser = subparsers.add_parser('list', help='List entities of a given type')
    list_parser.add_argument('type', help='Entity type to list')
    list_parser.add_argument('--limit', type=int, default=20, help='Max number of entities to list')

    return parser.parse_args()
    
    # Delete entity
    delete_parser = subparsers.add_parser('delete', help='Delete an entity')
    delete_parser.add_argument('entity_id', help='Entity ID')
    
    # Search entities
    search_parser = subparsers.add_parser('search', help='Search for entities')
    search_parser.add_argument('query', help='Search query')
    search_parser.add_argument('--type', help='Filter by entity type')
    search_parser.add_argument('--limit', type=int, default=10, help='Maximum number of results')
    
    # Create relationship
    rel_parser = subparsers.add_parser('relate', help='Create a relationship between entities')
    rel_parser.add_argument('from_id', help='Source entity ID')
    rel_parser.add_argument('to_id', help='Target entity ID')
    rel_parser.add_argument('rel_type', help='Relationship type')
    rel_parser.add_argument('--data', help='JSON string with relationship data')
    
    # Get relationships
    get_rel_parser = subparsers.add_parser('get-rels', help='Get relationships for an entity')
    get_rel_parser.add_argument('entity_id', help='Entity ID')
    get_rel_parser.add_argument('--type', help='Filter by relationship type')
    
    
    return parser.parse_args()

def main():
    """
    Main entry point for the CLI.
    Handles subcommands: create, get, update, list.
    Provides error handling and usage examples.
    """
    args = parse_args()
    memory = UnifiedMemory()

    if args.command is None:
        print("""
Windsurf Memory System CLI
-------------------------
Example usage:
  python tools/memory_cli.py create agent --data '{"name": "Agent Smith"}'
  python tools/memory_cli.py get <entity_id>
  python tools/memory_cli.py update <entity_id> --data '{"role": "Reviewer"}'
  python tools/memory_cli.py list agent
        """)
        return

    try:
        if args.command == 'create':
            data = {}
            if args.data:
                try:
                    data = json.loads(args.data)
                except json.JSONDecodeError:
                    print("Error: Invalid JSON for --data")
                    return
            entity = memory.create_entity(args.type, data)
            print("Entity created:")
            print("Created entity:")
            print_entity(entity)
            
        elif args.command == 'get':
            entity = memory.get_entity(args.entity_id)
            print_entity(entity)
            
        elif args.command == 'update':
            updates = json.loads(args.data)
            entity = memory.update_entity(args.entity_id, updates)
            if entity:
                print("Updated entity:")
                print_entity(entity)
            else:
                print(f"Entity {args.entity_id} not found")
                sys.exit(1)
                
        elif args.command == 'delete':
            success = memory.delete_entity(args.entity_id)
            if success:
                print(f"Deleted entity {args.entity_id}")
            else:
                print(f"Entity {args.entity_id} not found")
                sys.exit(1)
                
        elif args.command == 'search':
            results = memory.search_entities(
                query=args.query,
                entity_type=args.type,
                limit=args.limit
            )
            print(f"Found {len(results)} results:")
            for i, entity in enumerate(results, 1):
                print(f"\n--- Result {i} ---")
                print_entity(entity, indent=2)
                
        elif args.command == 'relate':
            data = json.loads(args.data) if args.data else {}
            success = memory.create_relationship(
                from_id=args.from_id,
                to_id=args.to_id,
                rel_type=args.rel_type,
                data=data
            )
            if success:
                print(f"Created relationship: {args.from_id} --[{args.rel_type}]--> {args.to_id}")
            else:
                print("Failed to create relationship")
                sys.exit(1)
                
        elif args.command == 'get-rels':
            rels = memory.get_relationships(
                entity_id=args.entity_id,
                rel_type=args.type
            )
            print(f"Found {len(rels)} relationships:")
            for rel in rels:
                print(f"\n{rel['from_id']} --[{rel['type']}]--> {rel['to_id']}")
                if rel.get('data'):
                    print("  Data:", json.dumps(rel['data'], indent=2))
                    
        elif args.command == 'sync':
            print("Starting synchronization from files...")
            result = memory.sync_from_files()
            if result['success']:
                print(f"Synchronization complete. Processed {result['processed']} files.")
                if result['errors']:
                    print(f"  - {result['errors']} errors occurred")
            else:
                print("Synchronization failed")
                sys.exit(1)
                
        else:
            print("No command specified. Use --help for usage.")
            sys.exit(1)
            
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
