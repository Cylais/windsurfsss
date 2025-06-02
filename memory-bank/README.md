# Memory Bank System

## Version: 1.0.0 (Last updated: 2025-05-25)

This directory contains the file-based memory system for the project, designed to work in harmony with the MCP memory server.

## Overview

**Session Start:**

- All contributors and agents must follow the Session Start Protocol as defined in [`rules/session_management.rules.md`](../rules/session_management.rules.md) and reference [`tools/session_start_protocol.md`](../tools/session_start_protocol.md) before beginning work.

The memory system uses a dual-layer architecture:

1. **File-Based Memory** (this directory)
   - Human-readable markdown files
   - Version-controlled history
   - Primary source of truth

2. **MCP Memory Server**
   - Graph-based knowledge representation
   - Semantic search capabilities
   - Relationship mapping between concepts

## Directory Structure

```-
memory-bank/
├── _conflicts/         # Automatically created for merge conflicts
├── projectbrief.md      # Project vision, objectives, and stakeholders
├── productContext.md    # Problem space and user needs
├── activeContext.md     # Current focus and recent changes
├── systemPatterns.md    # Architecture and technical decisions
├── techContext.md       # Technologies and constraints
├── progress.md          # What works and remaining work
├── decisionLog.md       # Important decisions and rationale
└── lessonsLearned.md    # Patterns and best practices
```

## File Descriptions

### 1. Project Brief (`projectbrief.md`)

- **Purpose**: Define the project's vision, objectives, and success metrics.
- **When to Update**: When project goals or stakeholders change.
- **Key Sections**:
  - Project Vision
  - Business Objectives
  - Success Metrics
  - Key Stakeholders

### 2. Product Context (`productContext.md`)

- **Purpose**: Document the problem space and user needs.
- **When to Update**: When understanding of the problem or users evolves.
- **Key Sections**:
  - Problem Statement
  - Target Users
  - User Pain Points
  - Market Context

### 3. Active Context (`activeContext.md`)

- **Purpose**: Track current focus and recent changes.
- **When to Update**: Daily or as work progresses.
- **Key Sections**:
  - Current Focus
  - Recent Changes
  - Current Blockers

### 4. System Patterns (`systemPatterns.md`)

- **Purpose**: Document architecture and technical decisions.
- **When to Update**: When making architectural changes.
- **Key Sections**:
  - Architecture Overview
  - Design Patterns
  - Technical Constraints
  - Integration Points

### 5. Technical Context (`techContext.md`)

- **Purpose**: Document the technology stack and dependencies.
- **When to Update**: When adding/removing technologies.
- **Key Sections**:
  - Technology Stack
  - Dependencies
  - Infrastructure

### 6. Progress Tracking (`progress.md`)

- **Purpose**: Track project progress and known issues.
- **When to Update**: Regularly (e.g., daily or per sprint).
- **Key Sections**:
  - What Works
  - Remaining Work
  - Known Issues

### 7. Decision Log (`decisionLog.md`)

- **Purpose**: Record important project decisions.
- **When to Update**: When making significant decisions.
- **Format**:

  ```markdown
  ## [YYYY-MM-DD] Short Decision Title
  
  **Status**: Proposed | Accepted | Superseded
  
  **Context**: Brief context for the decision.
  
  **Decision**: The change that was decided upon.
  
  **Consequences**:
  - Impact 1
  - Impact 2
  ```

### 8. Lessons Learned (`lessonsLearned.md`)

- **Purpose**: Document patterns, mistakes, and successes.
- **When to Update**: After completing major features or sprints.
- **Key Sections**:
  - Effective Patterns
  - Mistakes to Avoid
  - Success Stories

## Synchronization with MCP

The memory bank synchronizes with the MCP memory server to provide:

- **Semantic Search**: Find related information across all memories.
- **Relationship Mapping**: Visualize connections between concepts.
- **Context Awareness**: Maintain context across sessions.

### Sync Process

1. **Automatic Sync**:
   - On session start/end
   - When files are modified

2. **Manual Sync**:

   ```bash
   python tools/run_memory_sync.py sync
   ```

3. **Check Status**:

   ```bash
   python tools/run_memory_sync.py check --detailed
   ```

## Best Practices

1. **File Organization**
   - Keep files focused and single-purpose
   - Use clear, descriptive names
   - Group related content together

2. **Content Guidelines**
   - Be concise but complete
   - Use markdown formatting consistently
   - Include examples where helpful

3. **Synchronization**
   - Run sync after significant changes
   - Resolve conflicts promptly
   - Review sync logs regularly

4. **Version Control**
   - Commit related changes together
   - Write clear commit messages
   - Reference issues/PRs when applicable

## Troubleshooting

### Common Issues

1. **Sync Failures**
   - Check `logs/memory_sync.log` for errors
   - Verify MCP server is running
   - Ensure files have valid markdown syntax

2. **Merge Conflicts**
   - Resolve conflicts in `_conflicts/` directory
   - Update references as needed
   - Test after resolution

3. **Performance Issues**
   - Keep individual files under 1MB
   - Split large files when possible
   - Use links to reference other files

## Related Documentation

- [Memory System Rules](../rules/memory.rules.md)
- [Session Management](../rules/session_management.rules.md)
- [MCP Memory Server Documentation](https://mcp.example.com/docs/memory)

## License

[Your License Here]
