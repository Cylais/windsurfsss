# Agent Guide: Using the Unified Memory System

## Version: 2.0.0 (Last updated: 2025-05-25)

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Core Concepts](#core-concepts)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)
- [Examples](#examples)

## Introduction

The Unified Memory System is the central knowledge repository for all agents in the Windsurf Project. It provides a consistent way to store, retrieve, and share information across all agents and sessions.

## Getting Started

### Initialization

```python
from tools.agent_interface import AgentMemoryInterface

# Initialize with your agent's unique ID and type
agent = AgentMemoryInterface(
    agent_id="your_agent_id",
    agent_type="your_agent_type"  # e.g., 'coder', 'reviewer', 'tester'
)
```

### Basic Operations

```python
# Log an activity
agent.log_activity(
    activity_type="task_started",
    data={"task": "Implement feature X"}
)

# Share knowledge
knowledge = agent.share_knowledge(
    content="Important information about the project",
    tags=["documentation", "api"],
    related_to=["entity:123"]  # Optional: related entities
)

# Search for information
results = agent.search_knowledge("search query")

# Get your agent's state
state = agent.get_agent_state()
```

## Examples

### Example 1: Simple Activity Log

```python
agent.log_activity(
    activity_type="task_started",
    data={"task": "Implement login endpoint"}
)
```

### Example 2: Detailed Knowledge Sharing

```python
knowledge = agent.share_knowledge(
    content="OAuth2 implementation details for login flow",
    tags=["auth", "backend", "security"],
    related_to=["entity:login-module", "task:auth-refactor"]
)
```

---

## Core Concepts

### Dual-Layer Architecture

1. **File-based Layer** (`memory-bank/`)
   - Human-readable markdown files
   - Version controlled
   - Direct editing support

2. **SQLite Database** (`windsurf_memory.db`)
   - High-performance queries
   - Structured data storage
   - Automatic indexing

### Entity Types

- `agent`: Represents an agent in the system
- `knowledge`: Information shared by agents
- `activity`: Logged actions and events
- `project`: Project-related information
- `document`: Documentation and files

## Best Practices

### For All Agents

1. **Always Search First**

```python
results = agent.search_knowledge("your query")
if results:
    # Use existing knowledge
    pass
```

2.**Be Descriptive**

- Use clear, specific activity types
- Add relevant tags to knowledge entries
- Include context in the data field

3.**Maintain State**

```python
# Update your state when tasks change
agent.update_agent_state({
    "current_task": "Implementing feature X",
    "status": "in_progress"
})
```

### For Agent Developers

1. **Handle Errors Gracefully**

```python
try:
    # Memory operation
except Exception as e:
    agent.log_activity("error", {"error": str(e), "context": "operation_name"})
    # Handle or re-raise
```

2.**Respect Concurrency**

- The system handles concurrent access
- Use transactions for multiple related operations

## Troubleshooting

### Common Issues

1. **Permission Errors**
   - Ensure the agent has write access to `memory-bank/`
   - Check file permissions on `windsurf_memory.db`

2. **Sync Issues**
   - Run manual sync: `python tools/sync_memory.py`
   - Check logs in `logs/memory_sync.log`

3. **Performance Problems**
   - Break large operations into smaller chunks
   - Use specific queries rather than broad searches

## Workflow Examples

### Complete Workflow

```python
# 1. Initialize
from tools.agent_interface import AgentMemoryInterface
agent = AgentMemoryInterface("agent123", "tester")

# 2. Log start of task
agent.log_activity("test_started", {
    "test_suite": "authentication",
    "environment": "staging"
})

# 3. Check for known issues
known_issues = agent.search_knowledge("authentication test failures")
if known_issues:
    print(f"Found {len(known_issues)} related issues")

# 4. Document findings
agent.share_knowledge(
    content="Discovered race condition in auth token refresh",
    tags=["bug", "authentication", "race_condition"],
    related_to=["test:auth_flow"]
)

# 5. Update state
agent.update_agent_state({
    "status": "idle",
    "last_activity": "completed_test_suite"
})
```

## Need Help?

1. Check `memory-bank/MEMORY_SYSTEM.md` for detailed documentation
2. Review examples in `examples/agent_example.py`
3. Contact the project maintainers for support
