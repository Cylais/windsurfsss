# Memory System Cheat Sheet

## Version: 1.0.0 (Last updated: 2025-05-25)

## Quick Start

```python
from tools.agent_interface import AgentMemoryInterface

# Initialize agent
agent = AgentMemoryInterface(
    agent_id="your_id",
    agent_type="your_type"  # e.g., 'coder', 'reviewer'
)
```

## Common Operations

### Logging Activities

```python
agent.log_activity(
    activity_type="task_started",
    data={"details": "Task details here"}
)
```

### Sharing Knowledge

```python
knowledge = agent.share_knowledge(
    content="Information to share",
    tags=["tag1", "tag2"],
    related_to=["entity:id"]  # Optional
)
```

### Searching Knowledge

```python
# Basic search
results = agent.search_knowledge("search terms")

# Search with filters
results = agent.search_knowledge(
    "search terms",
    tags=["documentation", "api"],
    limit=5
)
```

### Managing Agent State

```python
# Get current state
state = agent.get_agent_state()

# Update state
agent.update_agent_state({
    "status": "working",
    "current_task": "task_id"
})
```

## Best Practices

1. **Always search before creating**

   ```python
   if not agent.search_knowledge("specific query"):
       # Only create if not found
       agent.share_knowledge(...)
   ```

2. **Use descriptive tags**

   ```python
   # Good
   tags=["authentication", "bug", "high_priority"]
   
   # Avoid
   tags=["a", "b", "c"]
   ```

3. **Log important decisions**

   ```python
   agent.log_activity("decision_made", {
       "decision": "Chose library X over Y",
       "reason": "Better performance in benchmarks",
       "alternatives": ["library_y", "library_z"]
   })
   ```

## Common Patterns

### Documenting Code Changes

```python
def some_function():
    """Function documentation here."""
    agent.log_activity("code_modified", {
        "file": "path/to/file.py",
        "function": "some_function",
        "changes": "Added input validation",
        "related_issue": "issue_123"
    })
    # Function implementation
```

### Collaborative Debugging

```python
try:
    # Potentially problematic code
    pass
except Exception as e:
    # Log the error with context
    agent.log_activity("error_occurred", {
        "error": str(e),
        "context": "During data processing",
        "stack_trace": traceback.format_exc()
    })
    # Check for similar issues
    similar_issues = agent.search_knowledge("similar error message")
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Permission denied | Check file permissions on `memory-bank/` and `windsurf_memory.db` |
| Database locked | Ensure no other process is writing to the database |
| Slow queries | Add specific tags, limit result size, use more specific search terms |
| Missing updates | Run manual sync: `python tools/sync_memory.py` |

## Need More Help?

- See `docs/AGENT_GUIDE.md` for detailed documentation
- Check `examples/agent_example.py` for complete examples
- Review `memory-bank/MEMORY_SYSTEM.md` for system architecture
