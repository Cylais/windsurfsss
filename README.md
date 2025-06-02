# Windsurf Project - Multi-Agent Collaboration Platform

This project enables efficient, autonomous, and accurate collaboration between multiple AI agents and human team members through a unified memory system and structured workflows.

## Core Components

### Unified Memory System

The Unified Memory System enables seamless collaboration between agents through a dual-layer architecture:

- **File-based Layer**: Human-editable markdown files in `memory-bank/`
- **Database Layer**: High-performance SQLite database for programmatic access
- **Automatic Sync**: Changes in one layer are automatically reflected in the other
- **Consistent API**: Single interface for all memory operations

### Documentation

- `docs/AGENT_GUIDE.md`: Comprehensive guide for agent developers
- `docs/MEMORY_CHEATSHEET.md`: Quick reference for common operations
- `memory-bank/MEMORY_SYSTEM.md`: Technical architecture and administration
- `examples/agent_example.py`: Practical usage examples

### Key Files

- `memory-bank/`: Central storage for all project knowledge
- `tools/unified_memory.py`: Core memory interface
- `tools/agent_interface.py`: High-level API for agents
- `config/cascades.yaml`: Defines agent roles and responsibilities
- `workflow.yaml`: Describes the step-by-step collaboration workflow
- `context.schema.json`: Specifies the shared context structure and validation
- `config/notifications.yaml`: Outlines notification rules and templates
- `collaboration_log.md`: Living documentation for traceability

## Getting Started

### Multi-Agent Collaboration Examples

- Out of the box, you can run 1-agent, 2-agent, or full 6-agent workflows using:
  - `examples/agent_example.py`
  - `scripts/crewai_test.py`
- See the examples directory for plug-and-play templates for any team size.

**Session Start:**

- Before beginning work, follow the Session Start Protocol in [`rules/session_management.rules.md`](rules/session_management.rules.md) and reference the pseudocode in [`tools/session_start_protocol.md`](tools/session_start_protocol.md).

### For New Agents

1. Read `docs/AGENT_GUIDE.md` for an overview of the memory system
2. Use the `docs/MEMORY_CHEATSHEET.md` as a quick reference
3. Review `examples/agent_example.py` for implementation patterns

### For Project Setup

1. Assign each agent a role from `config/cascades.yaml`
2. Follow the process in `workflow.yaml`
3. Update shared context according to `context.schema.json`
4. Use `config/notifications.yaml` to automate communication
5. Log major changes in `collaboration_log.md`

### For Developers

1. The `tools/` directory contains all memory system components
2. The `memory-bank/` directory stores all shared knowledge
3. See `memory-bank/MEMORY_SYSTEM.md` for architecture details

## Improvements

- Auditability: Context schema includes `lastUpdatedBy` and `timestamp`.
- Notification templates support dynamic variables.
- Modular: Add new agents/steps by editing YAML/JSON files.

---

For questions or onboarding, see `collaboration_log.md` for project history and guidelines.
