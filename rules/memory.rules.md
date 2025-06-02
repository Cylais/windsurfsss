# Unified Memory System Rules

> **Literal Execution Rule [MANDATORY]:**
> All agents and team members must follow memory rules and protocols exactly as written, without summarizing, interpreting, or making assumptions. Explanations or summaries are only allowed when explicitly requested.
> **Memory Protocol Rule:**
> All memory operations must comply with the Unified Memory System protocols defined in `docs/memory-protocols.md`.
> **Exhaustive File Analysis Rule [MANDATORY]:**
> Whenever the user explicitly requests a file to be analyzed, checked, or reviewed, the agent must perform a deep dive and exhaustive review of every single line of the file. This includes checking for legacy references, deprecated instructions, hidden inconsistencies, and any content that may be out of alignment with current protocols or project structure. Partial or summary reviews are not permitted unless the user specifically requests a summary or limited-scope check.

```yaml
---
tags: [memory, context, knowledge, persistence, unified]
version: 3.1.0
last_updated: 2025-05-25
depends_on: [documentation.rules.md, session_management.rules.md]
---
```

## Memory System Architecture

### Dual-Layer Memory System

1. **File-Based Memory Layer** (`memory-bank/`)
   - Human-readable documentation (in `memory-bank/` and `docs/` as appropriate)

- When files or folders are moved or renamed (especially in `docs/`, `config/`, `scripts/`), update all memory cross-references and documentation links accordingly
  - Version-controlled history
  - Structured markdown format
  - Direct editing support

2.**SQLite Database Layer** (`windsurf_memory.db`)

- High-performance structured storage
- Advanced querying capabilities
- Automatic indexing
- Concurrent access support

### Unified Memory Interface

> **Session initialization and memory system startup must follow the Session Start Protocol in [`rules/session_management.rules.md`](../rules/session_management.rules.md). For automation and agent reference, see [`tools/session_start_protocol.md`](../tools/session_start_protocol.md).**

- **Single API** for all memory operations
- Automatic synchronization between layers
- Consistent access patterns for all agents
- Built-in conflict resolution

---

## Agent Integration

All agents must follow these guidelines when using the unified memory system:

1. **Initialization**

   ```python
   from tools.agent_interface import AgentMemoryInterface
   agent = AgentMemoryInterface(agent_id="unique_id", agent_type="agent_type")
   ```

2. **Required Operations**
   - Log all significant activities with `log_activity()`
   - Share knowledge using `share_knowledge()`
   - Search before creating new content
   - Keep agent state updated

3. **Best Practices**
   - Use descriptive tags and metadata
   - Follow the project's naming conventions
   - Handle errors gracefully
   - Respect concurrency

---

### Synchronization Protocol

1. **Automatic Sync**
   - Changes are automatically synchronized between layers
   - No manual sync required in normal operation

2. **Conflict Resolution**
   - File-based memory takes precedence by default
   - All operations are logged to `logs/memory_system.log`
   - Conflicts are automatically resolved with timestamps

3. **Maintenance**
   - Run `python tools/sync_memory.py --check` to verify consistency
   - Review logs in `logs/` for any issues
   - Regular backups are recommended

### Entity Naming

- Use reverse-DNS notation: `domain:type:name`
- Example: `com.example.project:feature:user_auth`
- Always include `source` and `last_updated` metadata

### Relationship Types

- `depends_on`: Component dependencies
- `implements`: Feature implementation
- `references`: Cross-document links
- `evolves_from`: Version relationships
- `related_to`: General association

### Memory Retention

- Keep all historical versions in unified memory
- Set TTL for temporary context (default: 30 days)
- Tag memories with expiration when relevant
- Use `status: deprecated` instead of deletion

## Core Memory Files

Maintain these files in the `memory-bank/` directory:

### 1. `projectbrief.md`

- **Purpose**: Core requirements and project goals
- **Update When**: Project scope changes
- **Sections**:
  - Project Vision
  - Business Objectives
  - Success Metrics
  - Key Stakeholders

### 2. `productContext.md`

- **Purpose**: Project purpose and problems addressed
- **Update When**: Problem space evolves
- **Sections**:
  - Problem Statement
  - Target Users
  - User Pain Points
  - Market Context

### 3. `activeContext.md`

- **Purpose**: Current focus and recent changes
- **Update When**: Context changes
- **Sections**:
  - Current Sprint Focus
  - Recent Decisions
  - Pending Actions
  - Current Blockers

### 4. `systemPatterns.md`

- **Purpose**: System architecture and technical decisions
- **Update When**: Architecture changes
- **Sections**:
  - System Architecture
  - Design Patterns
  - Technical Constraints
  - Integration Points

## Memory Management

### Update Protocol

1. **Review** existing context before making changes
2. **Update** relevant memory files
3. **Version** changes with timestamps
4. **Link** to related decisions or documentation

### Context Anchors

- Use explicit anchors to maintain context:

  ```markdown
  <!-- context:project-goal -->
  Increase user engagement by 20% in Q3 2025
  <!-- /context:project-goal -->
  ```

- Reference anchors in discussions: `{{context:project-goal}}`

## Knowledge Graph

### Structure

- **Nodes**: Concepts, features, components
- **Edges**: Relationships between nodes
- **Properties**: Attributes and metadata

### Maintenance

- Add new concepts as they emerge
- Update relationships when architecture changes
- Prune outdated information

## Version History

- **2.0.0 (2025-05-25)**: unified memory Integration
  - Added unified memory memory server support
  - Implemented dual-layer memory architecture
  - Added sync protocols and conflict resolution
  - Updated documentation and guidelines

- **1.1.0 (2025-05-25)**: Initial version
  - Defined core memory files
  - Established update protocol
  - Added context anchoring system
