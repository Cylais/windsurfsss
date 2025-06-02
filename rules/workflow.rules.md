# Workflow Rules

> **Literal Execution Rule [MANDATORY]:**
> All workflow rules and protocols must be followed exactly as written, without summarizing, interpreting, or making assumptions. Explanations or summaries are only allowed when explicitly requested.
> **Memory Protocol Rule:**
> All workflow operations and documentation must comply with the Unified Memory System protocols in `docs/memory-protocols.md`.
> **Exhaustive File Analysis Rule [MANDATORY]:**
> Whenever the user explicitly requests a file to be analyzed, checked, or reviewed, the agent must perform a deep dive and exhaustive review of every single line of the file. This includes checking for legacy references, deprecated instructions, hidden inconsistencies, and any content that may be out of alignment with current protocols or project structure. Partial or summary reviews are not permitted unless the user specifically requests a summary or limited-scope check.
> **Cross-Reference Protocol:**
> When files or folders are moved or renamed (especially in `docs/`, `config/`, `scripts/`), update all cross-references and documentation links accordingly.

```yaml
---
tags: [workflow, agile, collaboration, process]
version: 1.2.0
last_updated: 2025-05-25
depends_on: documentation.rules.md
---
```

## Communication Protocol

### General Guidelines

- All communication must be actionable, concise, and include clear next steps.
- Default to asynchronous communication (e.g., comments, documentation) unless real-time discussion is necessary.
- When in doubt, ask for clarification rather than make assumptions.

### Meeting Standards

- **Stand-ups**: 15 minutes max, focus on blockers and progress.
- **Planning**: 1 hour per week of sprint work.
- **Retrospectives**: 30-60 minutes at the end of each sprint.
- **Documentation**: All meetings must have:
  - Clear agenda (distributed in advance)
  - Designated note-taker
  - Action items with owners and due dates
  - Summary distributed within 1 business day

## Project Roadmap & Agile Rules

### Sprint Planning

- Break down roadmap milestones into 2-4 week sprints.
- Define clear sprint goals and success criteria.
- Ensure all tasks are properly estimated and assigned.
- Review and reprioritize at each sprint boundary.

### Task Management

- Use the following priority levels:
  - P0: Critical (blocking)
  - P1: High (must have)
  - P2: Medium (should have)
  - P3: Low (nice to have)
- Tasks should be small enough to complete in one work session (1-4 hours).
- Always prioritize tasks from the main project roadmap above all other work.

### Workflow

1. At the start of each session, restate the current project goal and next immediate task.
2. Work on the highest priority task that you're capable of completing.
3. If blocked for more than 30 minutes, ask for help.
4. At the end of each work session, document progress and next steps.

## Progress Tracking & Reporting

### Daily Check-ins

- Update task status at the beginning and end of each work session.
- Log time spent on each task.
- Note any blockers or dependencies.

### Sprint Reviews

- Demo completed work to stakeholders.
- Gather feedback and incorporate into the next sprint.
- Update documentation to reflect current state.

### Reporting

- Generate weekly progress reports including:
  - Completed tasks
  - In-progress items
  - Blockers and risks
  - Upcoming priorities

Use the following KPI framework:

```yaml
key_performance_indicators:
  - name: Velocity
    description: Story points completed per sprint
  - name: Cycle Time
    description: Average time to complete tasks
  - name: Blocked Time
    description: Time spent waiting on dependencies
  - name: Quality
    description: Number of bugs/issues found in production
```

## Risk Management

### Risk Register

Maintain a `risk_register.md` with the following for each risk:

- Description
- Probability (High/Medium/Low)
- Impact (High/Medium/Low)
- Mitigation Strategy
- Owner
- Status (Open/Mitigated/Closed)

### Pre-Mortems

Before major phases or releases:

1. Identify potential failure points
2. Rate likelihood and impact
3. Develop prevention strategies
4. Assign owners for each risk

## Checklist & Cross-Referencing Protocol

### For Every Task

1. Search all checklist files for related tasks
2. If a related task exists and is complete (`[x]`), review artifacts
3. Reference and update related checklists
4. Use the format: `Referenced by: [filename.md], Task: [task_name]`

### Example

```markdown
## Feature Implementation
- [ ] Write implementation plan
  - Referenced by: roadmap/phase1/features.md, Task: "Design API endpoints"
  - Referenced by: docs/architecture.md, Task: "Update system diagram"
```

## Continuous Improvement

### Retrospectives

After each sprint or major milestone:

1. What went well?
2. What could be improved?
3. Action items for next sprint

### Process Improvement

- Document all process changes in `session_log.md`
- Track impact of changes on team velocity and quality
- Regularly review and update workflow rules

## Version History

- **1.1.0 (2025-05-25)**: Initial version
  - Defined workflow standards
  - Added risk management process
  - Included progress tracking guidelines
