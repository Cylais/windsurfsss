"""
Agent Interface for Windsurf Memory System
=========================================

Provides a high-level interface for agents to interact with the unified memory system.
Handles common patterns and provides utility functions for agent operations.

References:
- Onboarding: README.md, docs/AGENT_GUIDE.md
- Protocols: tools/session_start_protocol.md, tools/session_end_protocol.md, rules/session_management.rules.md, docs/memory-protocols.md
- Escalation & conflict: rules/workflow.rules.md, rules/technical.rules.md
"""

import json
from typing import Dict, Any, List, Optional, Union
from pathlib import Path
from datetime import datetime

from unified_memory import UnifiedMemory

class AgentMemoryInterface:
    """
    High-level interface for agents to interact with the Windsurf memory system.
    Provides convenience methods for common agent operations.
    """
    
    def __init__(self, agent_id: str, agent_type: Optional[str] = None) -> None:
        """Initialize the agent interface.
        
        Args:
            agent_id (str): Unique identifier for the agent
            agent_type (Optional[str]): Type/category of the agent (e.g., 'Product Manager', 'Solution Architect')
        """
        self.agent_id = agent_id
        self.agent_type = agent_type
        self.memory = UnifiedMemory()
        
        # Register this agent if not already registered
        self._register_agent()
    
    def _register_agent(self) -> None:
        """Register this agent in the memory system if not already registered."""
        agent_data = {
            'id': f'agent:{self.agent_id}',
            'type': 'agent',
            'agent_type': self.agent_type,
            'first_seen': datetime.utcnow().isoformat(),
            'last_seen': datetime.utcnow().isoformat()
        }
        
        # Check if agent exists
        existing = self.memory.get_entity(agent_data['id'])
        if existing:
            # Update last seen
            self.memory.update_entity(agent_data['id'], {
                'last_seen': datetime.utcnow().isoformat()
            })
        else:
            # Create new agent
            self.memory.create_entity(agent_data)
    
    def log_activity(self, activity_type: str, data: Optional[Dict] = None) -> Dict[str, Any]:
        """Log an activity to the memory system.
        
        Args:
            activity_type (str): Type of activity (e.g., 'task_started', 'code_edited')
            data (Optional[Dict]): Additional activity data
        
        Returns:
            Dict[str, Any]: The created activity record
        """
        activity = {
            'type': 'activity',
            'activity_type': activity_type,
            'agent_id': self.agent_id,
            'timestamp': datetime.utcnow().isoformat(),
            'data': data or {}
        }
        
        # Link to agent
        self.memory.create_relationship(
            from_id=f'agent:{self.agent_id}',
            to_id=f'activity:{activity["timestamp"]}:{activity_type}',
            rel_type='performed_activity',
            data=activity['data']
        )
        
        return self.memory.create_entity(activity)
    
    def get_context(self, entity_id: str, depth: int = 1) -> Dict[str, Any]:
        """Get context (related entities/knowledge) around a given entity.
        
        Args:
            entity_id (str): ID of the entity to get context for
            depth (int): How many levels of relationships to include
        
        Returns:
            Dict[str, Any]: Dictionary with entity and related entities
        """
        def get_related_entities(entity_id: str, current_depth: int, max_depth: int, visited: set) -> Dict:
            if current_depth > max_depth or entity_id in visited:
                return {}
                
            entity = self.memory.get_entity(entity_id)
            if not entity:
                return {}
                
            visited.add(entity_id)
            result = {entity_id: entity}
            
            # Get relationships
            rels = self.memory.get_relationships(entity_id)
            for rel in rels:
                other_id = rel['to_id'] if rel['from_id'] == entity_id else rel['from_id']
                result.update(get_related_entities(other_id, current_depth + 1, max_depth, visited))
                
            return result
        
        return get_related_entities(entity_id, 0, depth, set())
    
    def search_knowledge(self, query: str, context: Optional[Dict] = None, limit: int = 5) -> List[Dict[str, Any]]:
        """Search for knowledge relevant to the query and context.
        
        Args:
            query (str): Search query
            context (Optional[Dict]): Optional context to refine search
            limit (int): Maximum number of results
        
        Returns:
            List[Dict[str, Any]]: List of relevant knowledge items
        """
        # Simple implementation - can be enhanced with semantic search
        return self.memory.search_entities(query=query, limit=limit)
    
    def share_knowledge(self, content: str, tags: Optional[List[str]] = None, 
                       related_to: Optional[List[str]] = None) -> Dict[str, Any]:
        """Share knowledge with other agents.
        
        Args:
            content (str): The knowledge content
            tags (Optional[List[str]]): Optional tags for categorization
            related_to (Optional[List[str]]): Optional list of entity IDs this knowledge relates to
        
        Returns:
            Dict[str, Any]: The created knowledge entity
        """
        knowledge = {
            'type': 'knowledge',
            'content': content,
            'tags': tags or [],
            'created_by': self.agent_id,
            'created_at': datetime.utcnow().isoformat()
        }
        
        entity = self.memory.create_entity(knowledge)
        
        # Create relationships to related entities
        if related_to:
            for related_id in related_to:
                self.memory.create_relationship(
                    from_id=entity['id'],
                    to_id=related_id,
                    rel_type='related_to'
                )
        
        return entity
    
    def get_agent_state(self) -> Dict[str, Any]:
        """Get the current state of this agent, including recent activities.
        
        Returns:
            Dict[str, Any]: Agent state information
        """
        agent = self.memory.get_entity(f'agent:{self.agent_id}')
        if not agent:
            # Shouldn't happen as we register on init
            return {'id': self.agent_id, 'status': 'unknown'}
            
        # Get recent activities
        activities = self.memory.get_relationships(
            from_id=f'agent:{self.agent_id}',
            rel_type='performed_activity'
        )
        
        return {
            'id': self.agent_id,
            'type': agent.get('agent_type'),
            'first_seen': agent.get('first_seen'),
            'last_seen': agent.get('last_seen'),
            'recent_activities': [a.get('type') for a in activities[:5]]
        }

# Example usage:
if __name__ == '__main__':
    # Initialize the agent interface (see onboarding docs for best practices)
    agent = AgentMemoryInterface(
        agent_id="example_agent_1",
        agent_type="Product Manager"
    )
    
    # Log an activity (e.g., starting a session)
    agent.log_activity(
        activity_type="session_started",
        data={"message": "Session started for onboarding demo."}
    )
    
    # Share some knowledge (e.g., workflow protocol reference)
    knowledge = agent.share_knowledge(
        content="Unified Memory System and Session Start Protocol are now active.",
        tags=["protocol", "session"],
        related_to=[]
    )
    print(f"Shared knowledge with ID: {knowledge['id']}")
    
    # Get agent state
    state = agent.get_agent_state()
    print(f"Agent state: {json.dumps(state, indent=2)}")
    
    # --- Protocol Acknowledgement Example ---
    # agent.acknowledge_protocols(["memory", "session_management", "workflow"])
    # --- Session Start/End Example ---
    # agent.session_start_protocol()
    # agent.session_end_protocol()
    # --- Escalation/Conflict Resolution Example ---
    # agent.escalate_issue("Unable to sync memory across agents.")
