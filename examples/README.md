# Example Agents for Windsurf Unified Memory System

---
ONBOARDING & USAGE

---

- **Purpose:** Demonstrates plug-and-play agent and multi-agent workflows using the Windsurf Unified Memory System.

- **Quickstart:**
  - Run a basic example:

    ```bash
    python examples/agent_example.py
    ```

- **CI Integration:**
  - Add to your CI pipeline to validate agent memory workflows.
  - Example:

    ```yaml
    - name: Run Agent Example
      run: python examples/agent_example.py
    ```

- **References:**
  - See `session_start_protocol.md`, `session_end_protocol.md`, and `memory_system_guide.ps1` for onboarding and protocol integration.

## Prerequisites

- Python 3.8+
- Dependencies installed from `../requirements.txt`

## Running the Examples

### Basic Agent Workflow

```bash
python examples/agent_example.py
```

This example demonstrates:

1. Initializing an agent
2. Logging activities
3. Sharing knowledge
4. Searching for information
5. Retrieving agent state

### Single-Agent Example

A single agent (e.g., Product Manager) can define requirements and share knowledge:

```bash
python examples/agent_example.py
```

Sample output:

```text
=== Single-Agent Example: Product Manager ===
✅ Started task: Define App Vision
📝 Decision logged: Target users are remote teams needing real-time collaboration....
  - Shared knowledge with ID: ...
✅ Completed task: Define App Vision
```

### Two-Agent Collaboration Example

Two agents (e.g., Product Manager and Solution Architect) can collaborate by sharing and referencing knowledge:

```bash
python examples/agent_example.py
```

Sample output:

```text
=== Two-Agent Collaboration Example: Product Manager + Solution Architect ===
✅ Started task: Define App Vision (Collab)
📝 Decision logged: App must support offline editing....
  - Shared knowledge with ID: ...
✅ Completed task: Define App Vision (Collab)
✅ Started task: Design System (Collab)
📝 Decision logged: Use PouchDB for offline sync....
  - Shared knowledge with ID: ...
✅ Completed task: Design System (Collab)
```

**How agents collaborate:**

- Agents share knowledge using the unified memory system.
- Other agents can search for and reference this knowledge in their own decisions and tasks.

### Multi-Agent Dream Team Collaboration Example

The script also demonstrates a multi-agent workflow with the full Windsurf Dream Team (Product Manager, Solution Architect, Frontend Engineer, Backend Engineer, DevOps/QA, and Full-Stack Integrator) collaborating:

```bash
python examples/agent_example.py
```

Sample output:

```text
=== Multi-Agent Dream Team Collaboration Example ===

✅ Started task: Define App Vision
📝 Decision logged: Target users are remote teams needing real-time collaboration....
  - Shared knowledge with ID: ...
✅ Completed task: Define App Vision
✅ Started task: Design System Architecture
📝 Decision logged: Adopt microservices for scalability and modularity....
  - Shared knowledge with ID: ...
✅ Completed task: Design System Architecture
✅ Started task: Build UI
📝 Decision logged: Use React for responsive, real-time UI....
✅ Completed task: Build UI
✅ Started task: Develop Backend APIs
📝 Decision logged: Use FastAPI for backend services....
✅ Completed task: Develop Backend APIs
✅ Started task: Setup CI/CD and QA
📝 Decision logged: Deploy with Docker and GitHub Actions....
✅ Completed task: Setup CI/CD and QA
✅ Started task: System Integration
📝 Decision logged: Perform end-to-end tests and resolve integration bugs....
✅ Completed task: System Integration

=== Multi-Agent Dream Team Collaboration Completed ===
```

```text
=== Starting Agent Example ===

Initializing agent interface...

1. Logging an activity...

2. Sharing knowledge...
  - Shared knowledge with ID: knowledge:example_1

3. Searching for knowledge...
  - Found 1 results:
    1. This is an example of sharing knowledge between agen...

4. Getting agent state...
  - Agent ID: example_agent_1
  - Type: example
  - First seen: 2025-05-25T04:52:00.123456
  - Recent activities: example_workflow_started, example_workflow_completed

=== Example Completed Successfully ===
```

## Creating Your Own Agent

To create your own agent, follow this basic template:

```python
from tools.agent_interface import AgentMemoryInterface

# Initialize the agent
agent = AgentMemoryInterface(
    agent_id="your_agent_id",
    agent_type="your_agent_type"  # e.g., 'coder', 'reviewer', 'tester'
)

# Log activities
agent.log_activity(
    activity_type="task_started",
    data={"task": "Implement feature X"}
)

# Share knowledge
knowledge = agent.share_knowledge(
    content="Important information about the project",
    tags=["documentation", "api"],
    related_to=[]
)

# Search for information
results = agent.search_knowledge("search query")
```

## Best Practices

1. **Agent IDs**: Use a consistent naming convention for agent IDs (e.g., `team1_coder`, `team2_reviewer`)
2. **Activity Logging**: Log important actions to maintain an audit trail
3. **Knowledge Sharing**: Use descriptive tags and relate knowledge to relevant entities
4. **Error Handling**: Always include error handling in production code

## Next Steps

- Explore the `agent_interface.py` module for all available methods
- Check the main documentation for advanced usage patterns
- Review the test suite for additional examples
