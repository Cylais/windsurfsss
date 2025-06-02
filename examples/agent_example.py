"""
Agent Example for Windsurf Unified Memory System
=================================================

---
ONBOARDING & USAGE
---
- Purpose: Demonstrates plug-and-play agent usage of the unified memory system for Windsurf projects.
- Quickstart (Manual):
    python examples/agent_example.py
- CI Integration:
    - Add to your CI pipeline to validate agent memory workflows.
    - Example:
        - name: Run Agent Example
          run: python examples/agent_example.py
- Multi-Agent Example:
    - Includes both a single-agent and a multi-agent (Reviewer/Architect) collaboration workflow.
- Troubleshooting:
    - See troubleshooting tips at the end of this file.
    - Ensure dependencies are installed and onboarding scripts are referenced.
- References:
    - See session_start_protocol.md, session_end_protocol.md, memory_system_guide.ps1 for onboarding and protocol integration.
"""

import os
import sys
import time
import uuid
from datetime import datetime
from typing import Dict, Any, List, Optional

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.agent_interface import AgentMemoryInterface

class ExampleAgent:
    """Example agent demonstrating the unified memory system."""
    
    def __init__(self, agent_id: str, agent_type: str):
        """Initialize the agent with a unique ID and type."""
        self.agent_id = agent_id or f"agent_{str(uuid.uuid4())[:8]}"
        self.agent_type = agent_type
        self.memory = AgentMemoryInterface(
            agent_id=self.agent_id,
            agent_type=self.agent_type
        )
        self.current_task: Optional[Dict[str, Any]] = None
    
    def start_task(self, task_name: str, description: str, **kwargs) -> Dict[str, Any]:
        """Start a new task and log it."""
        task_id = f"task_{str(uuid.uuid4())[:8]}"
        self.current_task = {
            "task_id": task_id,
            "name": task_name,
            "description": description,
            "status": "in_progress",
            "start_time": datetime.utcnow().isoformat(),
            **kwargs
        }
        
        # Log the task start
        self.memory.log_activity(
            activity_type="task_started",
            data={
                "task": self.current_task,
                "message": f"Starting task: {task_name}"
            }
        )
        
        print(f"✅ Started task: {task_name}")
        return self.current_task
    
    def complete_task(self, result: Dict[str, Any] = None) -> Dict[str, Any]:
        """Mark the current task as complete."""
        if not self.current_task:
            raise ValueError("No active task to complete")
        
        self.current_task.update({
            "status": "completed",
            "end_time": datetime.utcnow().isoformat(),
            "result": result or {}
        })
        
        # Log the task completion
        self.memory.log_activity(
            activity_type="task_completed",
            data={
                "task": self.current_task,
                "message": f"Completed task: {self.current_task['name']}"
            }
        )
        
        print(f"✅ Completed task: {self.current_task['name']}")
        completed_task = self.current_task
        self.current_task = None
        return completed_task
    
    def log_decision(self, decision: str, rationale: str, **kwargs) -> Dict[str, Any]:
        """Log an important decision."""
        decision_id = f"decision_{str(uuid.uuid4())[:8]}"
        decision_data = {
            "decision_id": decision_id,
            "decision": decision,
            "rationale": rationale,
            "timestamp": datetime.utcnow().isoformat(),
            "agent_id": self.agent_id,
            "task_id": self.current_task["task_id"] if self.current_task else None,
            **kwargs
        }
        
        # Store the decision
        self.memory.share_knowledge(
            content=decision,
            title=f"Decision: {decision[:50]}...",
            data=decision_data,
            tags=["decision"] + kwargs.get("tags", []),
            related_to=kwargs.get("related_to", [])
        )
        
        # Also log as an activity
        self.memory.log_activity(
            activity_type="decision_made",
            data=decision_data
        )
        
        print(f"📝 Decision logged: {decision[:60]}...")
        return decision_data
    
    def search_knowledge(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """Search for knowledge in the memory system."""
        print(f"🔍 Searching for: {query}")
        results = self.memory.search_knowledge(query, limit=limit)
        print(f"   Found {len(results)} results")
        return results
    
    def update_agent_state(self, state_updates: Dict[str, Any]) -> Dict[str, Any]:
        """Update the agent's state in the memory system."""
        current_state = self.memory.get_agent_state() or {}
        new_state = {**current_state, **state_updates, "last_updated": datetime.utcnow().isoformat()}
        
        self.memory.update_agent_state(new_state)
        print(f"🔄 Updated agent state: {', '.join(state_updates.keys())}")
        return new_state

def example_workflow():
    """Run an example workflow demonstrating the agent's capabilities."""
    print("\n=== Starting Agent Example ===\n")
    
    # Initialize the agent
    print("Initializing example agent...")
    agent = ExampleAgent(
        agent_id="example_agent_1",
        agent_type="demo"
    )
    
    # Update agent state
    agent.update_agent_state({
        "status": "active",
        "location": "example_workflow"
    })
    
    # Start a task
    task = agent.start_task(
        task_name="Documentation Update",
        description="Update project documentation with new memory system features",
        priority="high"
    )
    
    # Log some decisions
    agent.log_decision(
        decision="Adopt Markdown for all documentation",
        rationale="Markdown is widely supported and easily readable in both raw and rendered forms.",
        impact="high",
        tags=["documentation", "format"]
    )
    
    # Share some knowledge
    print("\nSharing knowledge about the memory system...")
    knowledge = agent.memory.share_knowledge(
        content="The unified memory system provides a dual-layer storage solution with automatic synchronization.",
        title="Unified Memory System Overview",
        tags=["memory", "architecture", "documentation"],
        related_to=[f"agent:{agent.agent_id}"]
    )
    print(f"  - Shared knowledge with ID: {knowledge['id']}")
    
    # Search for knowledge
    print("\nSearching for documentation-related knowledge...")
    results = agent.search_knowledge("documentation format", limit=3)
    print("Search results:")
    for i, result in enumerate(results, 1):
        print(f"  {i}. {result.get('title', 'Untitled')}")
        print(f"     {result.get('content', 'No content')[:80]}...")
    
    # Complete the task
    agent.complete_task({
        "files_updated": ["README.md", "docs/AGENT_GUIDE.md", "docs/MEMORY_CHEATSHEET.md"],
        "changes_made": "Updated documentation to reflect unified memory system"
    })
    
    # Final state update
    agent.update_agent_state({
        "status": "idle",
        "last_activity": "completed_documentation_update"
    })
    
    print("\n=== Example Workflow Completed ===\n")
    
    # Get agent state
    print("\n4. Getting agent state...")
    state = agent.get_agent_state()
    print(f"  - Agent ID: {state['id']}")
    print(f"  - Type: {state.get('type', 'unknown')}")
    print(f"  - First seen: {state.get('first_seen')}")
    print(f"  - Recent activities: {', '.join(state.get('recent_activities', []))}")
    
    # Log completion
    agent.log_activity(
        activity_type="example_workflow_completed",
        data={"status": "success", "message": "Completed example workflow"}
    )
    
    print("\n=== Example Completed Successfully ===")

if __name__ == "__main__":
    example_agent_workflow()

    # ---
    # Single-agent example: Product Manager only
    # ---
    print("\n=== Single-Agent Example: Product Manager ===\n")
    pm = ExampleAgent(agent_id="product_manager_1", agent_type="Product Manager")
    pm_task = pm.start_task(
        task_name="Define App Vision",
        description="Outline the vision and requirements for a collaborative note-taking app."
    )
    pm_decision = pm.log_decision(
        decision="Target users are remote teams needing real-time collaboration.",
        rationale="Market research shows demand for this feature set.",
        tags=["requirements", "vision"]
    )
    pm_knowledge = pm.memory.share_knowledge(
        content="Vision: Real-time, multi-user note-taking for remote teams.",
        title="Product Vision",
        tags=["vision", "requirements"],
        related_to=[f"agent:{pm.agent_id}"]
    )
    pm.complete_task({"vision": "defined"})

    # ---
    # Two-agent example: Product Manager and Solution Architect collaborating
    # ---
    print("\n=== Two-Agent Collaboration Example: Product Manager + Solution Architect ===\n")
    pm2 = ExampleAgent(agent_id="product_manager_2", agent_type="Product Manager")
    sa2 = ExampleAgent(agent_id="solution_architect_2", agent_type="Solution Architect")
    # Product Manager defines requirements
    pm2_task = pm2.start_task(
        task_name="Define App Vision (Collab)",
        description="Define requirements for a new app."
    )
    pm2_decision = pm2.log_decision(
        decision="App must support offline editing.",
        rationale="Critical for remote teams.",
        tags=["requirements"]
    )
    pm2_knowledge = pm2.memory.share_knowledge(
        content="Requirement: Offline editing support.",
        title="Offline Requirement",
        tags=["requirements"],
        related_to=[f"agent:{pm2.agent_id}"]
    )
    pm2.complete_task({"vision": "offline editing required"})
    # Solution Architect references Product Manager's shared knowledge
    sa2_task = sa2.start_task(
        task_name="Design System (Collab)",
        description="Design architecture based on PM's requirements."
    )
    sa2_decision = sa2.log_decision(
        decision="Use PouchDB for offline sync.",
        rationale="Best for offline-first architectures.",
        tags=["architecture"],
        related_to=[pm2_knowledge["id"]]
    )
    sa2.memory.share_knowledge(
        content="Architecture: Offline sync with PouchDB.",
        title="Offline Architecture",
        tags=["architecture"],
        related_to=[pm2_knowledge["id"]]
    )
    sa2.complete_task({"architecture": "offline sync"})

    # ---
    # Multi-agent example: Dream Team Collaboration
    # ---
    print("\n=== Multi-Agent Dream Team Collaboration Example ===\n")
    product_manager = ExampleAgent(agent_id="product_manager_1", agent_type="Product Manager")
    solution_architect = ExampleAgent(agent_id="solution_architect_1", agent_type="Solution Architect")
    frontend_engineer = ExampleAgent(agent_id="frontend_engineer_1", agent_type="Frontend Engineer")
    backend_engineer = ExampleAgent(agent_id="backend_engineer_1", agent_type="Backend Engineer")
    devops_qa = ExampleAgent(agent_id="devops_qa_1", agent_type="DevOps/QA")
    fullstack_integrator = ExampleAgent(agent_id="fullstack_integrator_1", agent_type="Full-Stack Integrator")

    # Product Manager defines the vision
    pm_task = product_manager.start_task(
        task_name="Define App Vision",
        description="Outline the vision and requirements for a collaborative note-taking app."
    )
    pm_decision = product_manager.log_decision(
        decision="Target users are remote teams needing real-time collaboration.",
        rationale="Market research shows demand for this feature set.",
        tags=["requirements", "vision"]
    )
    pm_knowledge = product_manager.memory.share_knowledge(
        content="Vision: Real-time, multi-user note-taking for remote teams.",
        title="Product Vision",
        tags=["vision", "requirements"],
        related_to=[f"agent:{product_manager.agent_id}"]
    )
    product_manager.complete_task({"vision": "defined"})

    # Solution Architect designs architecture
    sa_task = solution_architect.start_task(
        task_name="Design System Architecture",
        description="Design system based on PM's requirements."
    )
    sa_decision = solution_architect.log_decision(
        decision="Adopt microservices for scalability and modularity.",
        rationale="Meets real-time and scaling needs.",
        tags=["architecture", "microservices"],
        related_to=[pm_knowledge["id"]]
    )
    sa_knowledge = solution_architect.memory.share_knowledge(
        content="Architecture: Microservices with real-time sync.",
        title="System Architecture",
        tags=["architecture"],
        related_to=[f"agent:{solution_architect.agent_id}"]
    )
    solution_architect.complete_task({"architecture": "microservices"})

    # Frontend Engineer implements UI
    fe_task = frontend_engineer.start_task(
        task_name="Build UI",
        description="Implement collaborative note-taking UI."
    )
    fe_decision = frontend_engineer.log_decision(
        decision="Use React for responsive, real-time UI.",
        rationale="Best fit for real-time updates and component reuse.",
        tags=["frontend", "UI"],
        related_to=[sa_knowledge["id"]]
    )
    frontend_engineer.complete_task({"ui": "built"})

    # Backend Engineer implements APIs
    be_task = backend_engineer.start_task(
        task_name="Develop Backend APIs",
        description="Develop APIs for notes, users, and collaboration."
    )
    be_decision = backend_engineer.log_decision(
        decision="Use FastAPI for backend services.",
        rationale="FastAPI is performant and easy to integrate.",
        tags=["backend", "API"],
        related_to=[sa_knowledge["id"]]
    )
    backend_engineer.complete_task({"api": "implemented"})

    # DevOps/QA automates deployment and tests
    devops_task = devops_qa.start_task(
        task_name="Setup CI/CD and QA",
        description="Automate deployment and run QA tests."
    )
    devops_qa.log_decision(
        decision="Deploy with Docker and GitHub Actions.",
        rationale="Enables continuous delivery and repeatable deployments.",
        tags=["devops", "ci/cd"]
    )
    devops_qa.complete_task({"deployment": "automated", "tests": "passed"})

    # Full-Stack Integrator ensures everything works together
    integrator_task = fullstack_integrator.start_task(
        task_name="System Integration",
        description="Integrate frontend, backend, and deployment for end-to-end delivery."
    )
    fullstack_integrator.log_decision(
        decision="Perform end-to-end tests and resolve integration bugs.",
        rationale="Ensure seamless user experience and system reliability.",
        tags=["integration", "testing"]
    )
    fullstack_integrator.complete_task({"integration": "successful"})

    print("\n=== Multi-Agent Dream Team Collaboration Completed ===\n")

# ---
# TROUBLESHOOTING & ONBOARDING TIPS
# ---
# - If you see ImportError, ensure all dependencies are installed (see requirements.txt).
# - For onboarding and advanced usage, see memory_system_guide.ps1 and protocol docs.
# - Use this script to validate agent memory integration in CI and onboarding workflows.
