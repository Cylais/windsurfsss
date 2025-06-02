# Unified Memory System Protocols

## Version: 1.0.0 (Last updated: 2025-05-25)

> **Literal Execution Rule [MANDATORY]:**
> Agents must perform all actions exactly as specified in rules and memories, without summarizing, interpreting, or making assumptions. Explanations or summaries are only allowed when explicitly requested. Any deviation is a protocol violation.

## Purpose

The Unified Memory System provides a structured, searchable, and persistent way to store all project knowledge, decisions, and activities. It ensures full transparency, traceability, and serves as living documentation for the project.

## Key Principles

1. **Single Source of Truth**: All project knowledge is stored in the unified memory system
2. **Automatic Attribution**: All entries are automatically attributed and timestamped
3. **Dual-Layer Storage**: Data is stored in both human-readable and database formats
4. **Searchable**: All content is indexed for fast retrieval
5. **Versioned**: Full history of all changes is maintained

## What to Log

- **Actions**: All significant activities and operations
- **Decisions**: Design choices, architecture decisions, and their rationales
- **Knowledge**: Important information, research findings, and documentation
- **State Changes**: Updates to project or agent state
- **Votes & Debates**: All proposals, discussions, and their outcomes

## How to Log

### Using the Agent Interface

```python
# Log an activity
agent.log_activity(
    activity_type="task_completed",
    data={
        "task": "Implement login feature",
        "status": "completed",
        "details": "Added JWT authentication"
    }
)

# Share knowledge
agent.share_knowledge(
    content="Research on authentication methods",
    tags=["authentication", "security", "research"],
    related_to=["task:login_implementation"]
)

# Update agent state
agent.update_agent_state({
    "current_task": "Implement user profile",
    "status": "in_progress"
})
```

## When to Update

- **Automatically**:
  - At the start/end of major operations
  - After completing significant tasks
  - When encountering errors or issues

- **Manually**:
  - After important decisions or discussions
  - When sharing knowledge with the team
  - During handoffs between agents or team members

## Best Practices

1. **Be Descriptive**: Use clear, specific language in all entries
2. **Use Tags**: Add relevant tags for better searchability
3. **Link Related Items**: Connect related entries using `related_to`
4. **Keep State Updated**: Regularly update your agent's state
5. **Search First**: Always search before creating new content
6. **Handle Errors**: Include error details and context when logging issues

## Accessing Stored Information

```python
# Search for knowledge
results = agent.search_knowledge("authentication implementation")

# Get agent state
state = agent.get_agent_state()

# Get activity history
history = agent.get_activity_history(limit=10)
```

## Templates

### Activity Log Entry

```python
agent.log_activity(
    activity_type="task_completed",
    data={
        "task": "Task description",
        "status": "completed",
        "details": "Detailed description of what was done",
        "related_pr": "#PR_NUMBER",
        "time_spent": "2h 30m"
    }
)
```

### Knowledge Entry

```python
agent.share_knowledge(
    content="Detailed information or documentation",
    tags=["category1", "category2"],
    related_to=["task:task_id", "doc:document_id"],
    title="Descriptive Title"
)
```

### Voting/Decision

```python
agent.log_activity(
    activity_type="vote_recorded",
    data={
        "issue": "Issue description",
        "options": ["Option 1", "Option 2"],
        "vote": "Selected option",
        "rationale": "Reason for the vote"
    }
)
```

## Maintenance

- The system automatically handles synchronization between layers
- Regular backups are recommended
- Monitor logs in `logs/` for any issues
- Run consistency checks with `python tools/sync_memory.py --check`

## Implementation Guidelines

- Keep logs concise, structured, and linked
- Use markdown tables and links for clarity
- Attribute all actions/votes to agent/role and timestamp

---
This protocol ensures your Windsurf projects always retain critical context, enable robust collaboration, and support onboarding and audits at any scale.
