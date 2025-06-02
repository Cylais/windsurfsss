# Session Management

> **Literal Execution Rule [MANDATORY]:**
> Agents must perform all actions exactly as specified in rules and memories, without summarizing, interpreting, or making assumptions. Explanations or summaries are only allowed when explicitly requested. Any deviation is a protocol violation.
> **Exhaustive File Analysis Rule [MANDATORY]:**
> Whenever the user explicitly requests a file to be analyzed, checked, or reviewed, the agent must perform a deep dive and exhaustive review of every single line of the file. This includes checking for legacy references, deprecated instructions, hidden inconsistencies, and any content that may be out of alignment with current protocols or project structure. Partial or summary reviews are not permitted unless the user specifically requests a summary or limited-scope check.
> **Cross-Reference Protocol:**
> When files or folders are moved or renamed (especially in `docs/`, `config/`, `scripts/`), update all cross-references and documentation links accordingly.

## Agent Action and Explanation Rule

The agent must always perform the requested tasks literally and directly, without providing explanations or commentary before or during execution, unless the user explicitly requests an explanation (e.g., by saying "Explain this to me"). After completing the task(s), the agent must provide a brief summary or explanation of what was done.

## Session Start Protocol (Trigger)

- The Session Start Protocol is triggered only if a user, agent, or system message contains the exact phrase "Start Session" (case sensitive).
- If a message contains a similar phrase (e.g., "session start", "begin session", "start the session", etc.), the agent must ask: "Did you mean to start the Start Session Protocol?" before proceeding.

## Session Start Protocol (Actions)

### 1. Discover and Read All Rules, Memory, and Context Files

- **Find and list all relevant files:**
  - All rule files in `rules/` (e.g., `memory.rules.md`, `session_management.rules.md`, etc.)
  - All core memory and context files in `memory-bank/` (e.g., `projectbrief.md`, `productContext.md`, `activeContext.md`, `systemPatterns.md`, `techContext.md`, `progress.md`, `decisionLog.md`, `lessonsLearned.md`, `votes.md`, etc.)
  - System documentation (e.g., `MEMORY_SYSTEM.md`, `README.md` in root and memory-bank)
- **For each file:**
  - Open and read the file contents
  - Summarize key points, requirements, and current project state
  - Document evidence of reading (e.g., file list, checksums, or brief summaries in the session log)
- Internalize naming conventions, retention policies, relationship types, agent protocols, etc.

### 2. Internalize and Commit to All Rules and Protocols

- Explicitly acknowledge understanding and intent to obey all rules and protocols for the session
- Record in session memory/log which rules and protocols are in force
- Example: "I have read and internalized the following rules and protocols for this session: memory system rules, session management, collaboration, workflow, technical, and security protocols. I will obey and reference these in all actions."
- Attach evidence: log entry, file references, or memory snapshot

### 3. Initialize the Dual-Layer Memory System

- **File-Based Layer:**
  - Verify `memory-bank/` is present, readable, and writable
  - Confirm all core markdown files are accessible (list files and check read/write status)
- **SQLite Database Layer:**
  - Ensure `windsurf_memory.db` exists and is accessible
  - Start/connect to the local SQLite server if needed
  - Verify schema and tables are present (output schema/tables or DB status)
- **Unified Memory Interface:**
  - Import and instantiate the unified memory interface (`unified_memory.py`)
  - Confirm the interface can read/write both layers (show test read/write evidence)

### 4. Synchronize and Validate Both Memory Layers

- Run the sync tool (`sync_memory.py --check` or equivalent)
  - Check for:
    - Out-of-sync files/records
    - Unresolved conflicts in `_conflicts/`
    - Errors in `logs/memory_sync.log` and `logs/memory_system.log`
- If issues are found:
  - Resolve per protocol (file layer precedence, log all resolutions)
  - Re-run sync until layers are fully in sync
- Attach evidence: sync log output, conflict resolutions, final sync status

### 5. Load and Refresh Internal Context

- Read all memory and context files into session memory
- Summarize project vision, goals, current blockers, technical context, recent decisions, and lessons learned
- Ensure the latest state is reflected in agent context for this session
- Attach evidence: context snapshot, summaries, or log entries

### 6. Acknowledge Readiness and Commit to Protocols

- State explicitly that the system is initialized, in sync, and all context is loaded
- Confirm that all protocols and rules will be obeyed for the duration of the session
- Attach evidence: session log entry, memory snapshot, or system status report

#### Example Session Start Statement

> **Session Start Protocol Complete:**
>
> - All rule, memory, and context files have been read and internalized (see attached evidence).
> - The dual-layer memory system (file-based and SQLite) is accessible, functional, and fully synchronized (see sync logs/status).
> - No unresolved conflicts or errors found.
> - Project and technical context is loaded and fresh (see context summary).
> - I acknowledge and commit to obeying all protocols and rules for this session.
> - Ready to proceed.

---

## During Session

### For New Information

```python
create_entities([
  {
    "name": "concept_name",
    "entityType": "concept|feature|decision|task",
    "observations": ["Description of the concept"],
    "source": "file_based|mcp",
    "last_updated": "2025-05-25T18:44:17+01:00"
  }
])
```

### For Relationships

```python
create_relations([
  {
    "from": "source_entity",
    "to": "target_entity",
    "relationType": "depends_on|implements|references",
    "source": "file_based|mcp",
    "last_updated": "2025-05-25T18:44:17+01:00"
  }
])
```

### Tagging

- Use `source: file_based` for content from files
- Use `source: unified` for unified memory-originated content
- Add `last_updated` timestamp to all changes

## Session End Protocol (Trigger)

- The Session End Protocol is triggered only if a user, agent, or system message contains the exact phrase "End Session" (case sensitive).
- If a message contains a similar phrase (e.g., "session end", "end the session", "close session", etc.), the agent must ask: "Did you mean to start the End Session Protocol?" before proceeding.

## Session End Protocol (Actions)

### 1. Review and Document Session Progress

- **Review all message exchanges and activities from the session**
  - Attach: summary or export of session chat/logs
- **Identify and summarize key discussion topics, decisions, blockers, and resolutions**
  - Attach: summary list and rationale for each
- **Note all code changes, file modifications, and configuration updates**
  - Attach: git diff, file lists, or change logs
- **List all completed tasks with brief descriptions**
  - Attach: checklist or task log
- **Track all action items, completed tasks, outstanding issues, and blockers**
  - Attach: updated task tracker or issue list
- **Document decisions made and their rationales**
  - Attach: decision log entries
- **Update `session_log.md` with session details**
  - Attach: excerpt or file reference
- **Track session metrics:**
  - Time spent on tasks
  - Number of tasks completed
  - Lines of code changed
  - Files modified
  - Attach: metrics summary
- **Document manual testing performed**
  - Attach: test results or screenshots

### 2. Update Living Documentation and Knowledge Base

- **Verify all `memory-bank/` files are current and accurate**
  - Attach: file list, checksums, or summaries
- **Update any modified documentation with today’s date**
  - Attach: git log or file headers
- **Ensure all cross-references are valid and up-to-date**
  - Attach: link check report
- **Remove deprecated or duplicate content**
  - Attach: before/after diff or removal log
- **Add new learnings and lessons to appropriate knowledge base files**
  - Attach: lessons learned log
- **Update system patterns with any architectural changes**
  - Attach: system patterns diff or summary
- **Document new technical decisions in `decisionLog.md`**
  - Attach: decision log excerpt
- **Record lessons learned in `lessonsLearned.md`**
  - Attach: lessons log excerpt

### 3. Synchronize and Validate Memory Layers

- **Run the memory sync tool (`sync_memory.py --check` or equivalent)**
  - Attach: sync log output
- **Check for unresolved conflicts in `_conflicts/` and errors in logs**
  - Attach: conflict or error log excerpts
- **Resolve any issues per protocol and re-run sync as needed**
  - Attach: resolution log and final sync status
- **Confirm that the dual-layer memory system is fully synchronized and consistent before session close**
  - Attach: status report

### 4. Quality Assurance

- **Run `markdownlint` to check documentation**
  - Attach: lint output
- **Verify all files are properly formatted**
  - Attach: formatting tool output
- **Check for broken links or references**
  - Attach: link check output
- **Ensure all temporary files are cleaned up**
  - Attach: cleanup log or confirmation
- **Document new tests added, test coverage changes, and test failures**
  - Attach: test summary or coverage report

### 5. Prepare for Next Session

- **Update `activeContext.md` with current focus, immediate next steps, and any pending tasks or follow-ups**
  - Attach: file excerpt
- **Update project status in `progress.md`**
  - Attach: file excerpt
- **Ensure all context and session state is preserved for a seamless next session start**
  - Attach: context snapshot or summary

### 6. Version Control & Backup

#### Git Operations

- **Stage all modified files:**

  ```bash
  git add .

  ```

  - Attach: output or file list

- **Commit changes with a descriptive message:**

  ```bash
  git commit -m "Session end: [Brief summary of changes]"

  ```

- Attach: commit hash or message

- **Push to remote repository:**

  ```bash
  git push

  ```

  - Attach: push confirmation

- **Verify successful push on remote repository**

  ```bash
  git status

  ```

  - Attach: remote status check

#### Backup Procedures

- **Run local backup script:**

  ```bash
  ./Backup-Project-7zip.ps1
  ```

  - Attach: backup log

- **Run cloud backup script:**

  ```bash
  ./Backup-Project-7zip-DROPBOX.ps1
  ```

  - Attach: backup log

- **Verify backup completion and integrity**
  - Attach: verification log

- **Document any backup issues in `session_log.md`**
  - Attach: log excerpt

### Example Session End Statement

> **Session End Protocol Complete:**
>
> - All session activities, changes, and decisions have been reviewed and documented (see attached evidence).
> - Living documentation and knowledge base are up to date (see file summaries).
> - The dual-layer memory system is fully synchronized and consistent (see sync logs/status).
> - Quality checks and backups are complete (see reports).
> - Context and next steps are preserved for the next session (see context snapshot).
> - Ready to close this session.
> - The dual-layer memory system is fully synchronized and consistent.
> - Living documentation and knowledge base are up-to-date.
> - All backups and version control operations are complete.
> - Context and next steps are preserved for the next session.
> - Rule/protocol adherence and lessons learned have been recorded.
> - Session is finalized and ready for handoff or continuation.

### 9. Automation Reference

For automation or agent implementation, see [tools/session_end_protocol.md](../tools/session_end_protocol.md) for pseudocode and checklist reference.

## Memory System Management

### Dual-Layer Memory System

1. **File-Based Memory** (`memory-bank/` directory)
   - Human-readable, version-controlled documents
   - Primary source of truth for project knowledge
   - Files include:
     - `projectbrief.md`: Core requirements and goals
     - `productContext.md`: Purpose and problems addressed
     - `activeContext.md`: Current focus and changes
     - `systemPatterns.md`: Architecture and tech decisions
     - `techContext.md`: Technologies and constraints
     - `progress.md`: Status and known issues
     - `decisionLog.md`: Decisions and rationale
     - `lessonsLearned.md`: Patterns and best practices

2. **unified memory Memory Server**
   - Graph-based knowledge representation
   - Enables semantic search and relationship mapping
   - Automatically synchronized with file-based memory
   - Provides context-aware recommendations

### Synchronization Process

1. **On Session Start**
   - Load all memory bank files
   - Create/update unified memory entities
   - Resolve any conflicts

2. **During Session**
   - Track changes to memory bank files
   - Queue updates for unified memory server
   - Batch process updates every 5 minutes

3. **On Session End**
   - Final sync with unified memory server
   - Generate sync report
   - Log any issues

### Conflict Resolution

1. **Detection**
   - Compare timestamps and content hashes
   - Check for conflicting updates

2. **Resolution**
   - File-based changes take precedence
   - Flag conflicts for review
   - Log resolution actions

3. **Recovery**
   - Maintain sync logs
   - Support rollback if needed
   - Generate reconciliation reports

## Cross-Referencing and Relationships

### File-Based Cross-References

- Use markdown links for file references: `[description](path/to/file.md)`
- Maintain a consistent heading structure for reference anchors
- Update cross-references when moving or renaming files

### unified memory Relationships

- Create explicit relationships between related concepts
- Use standard relationship types:

  ```python
  create_relations([{
    "from": "project:requirements:user_auth",
    "to": "project:implementation:auth_service",
    "relationType": "implements"
  }])
  ```

- Document relationship semantics in `systemPatterns.md`

### Bidirectional Linking

- Maintain forward and backward links
- Update related entities when changes occur
- Use unified memory queries to discover implicit relationships

## Version History

- **2.0.0 (2025-05-25)**: unified memory Integration
  - Added unified memory memory server support
  - Implemented dual-layer synchronization
  - Added conflict resolution protocols
  - Enhanced cross-referencing capabilities

- **1.0.0 (2025-05-25)**: Initial version
  - Basic session management protocols
  - File-based memory system
  - Simple cross-referencing
