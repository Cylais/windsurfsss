# Collaboration Rules

> **Literal Execution Rule [MANDATORY]:**
> All team members and agents must follow instructions, rules, and memories exactly as written, without summarizing, interpreting, or making assumptions. Explanations or summaries are only allowed when explicitly requested.
> **Memory Protocol Rule:**
> All project knowledge and collaboration must adhere to the Unified Memory System protocols as defined in `docs/memory-protocols.md`.
> **Exhaustive File Analysis Rule [MANDATORY]:**
> Whenever the user explicitly requests a file to be analyzed, checked, or reviewed, the agent must perform a deep dive and exhaustive review of every single line of the file. This includes checking for legacy references, deprecated instructions, hidden inconsistencies, and any content that may be out of alignment with current protocols or project structure. Partial or summary reviews are not permitted unless the user specifically requests a summary or limited-scope check.

```yaml
---
tags: [collaboration, teamwork, communication, stakeholders]
version: 2.0.0
last_updated: 2025-05-25
depends_on: documentation.rules.md, workflow.rules.md
---
```

## Stakeholder Management

### Communication Protocol

- **Frequency**: Bi-weekly updates at minimum
- **Channels**: Prefer asynchronous updates via documentation updates with scheduled syncs
- **Escalation Path**: Document and communicate clear escalation paths for critical issues

### Feedback Loops

- **Stakeholder Reviews**: Schedule at the end of each phase
- **Feedback Collection**: Use structured forms for consistent input
- **Actionable Insights**: Convert feedback into specific, prioritized tasks

### Decision Making

- **RACI Matrix**: Define who is Responsible, Accountable, Consulted, and Informed
- **Documentation**: Record all major decisions with rationale
- **Alignment**: Ensure decisions align with project goals and stakeholder needs

## Context Management

### Explicit Context Anchors

- At the start of each session, restate the current project goal and the next immediate task
- Maintain context continuity by referencing previous decisions and their rationales
- Document any context shifts or new information that affects project direction
- When files or folders are moved or renamed (e.g., in `docs/`, `config/`, `scripts/`), update all cross-references and documentation links accordingly

## Autonomy & Customization

### Customization Guidelines

- Users may modify, extend, or override operational protocols as needed
- All customizations should be documented in the relevant rule file with rationale
- Custom memory configurations should be stored in the project's memory-bank

## Autonomy Guidelines

### Decision Making Authority

- Team members are authorized to make decisions aligned with the roadmap and sprint goals without constant approval
- For ambiguous requirements, proceed with the most roadmap-aligned interpretation and document your rationale
- Execute safe terminal commands (builds, tests, linting) without approval when needed
- Suggest and implement refactoring if it advances roadmap progress, but always prioritize forward momentum

### Code Improvement Protocol

- All code improvements and documentation updates must comply with the literal execution and memory protocol rules.
- Automation workflows and dual-layer memory system protocols must be followed as described in `docs/memory-protocols.md`.

- Before starting work on a new task, review and update the codebase to ensure alignment with the project's architecture
- When working with code, always aim to improve:
  - Efficiency and performance
  - Readability and maintainability
  - Security and error handling
  - Documentation and comments
  - Test coverage

- Unless specified otherwise, always provide improved versions of code with explanations of changes

## Team Collaboration

### Working Agreements

- **Core Hours**: Define team availability windows
- **Response Times**: Set expectations for different communication channels
- **Meeting Etiquette**: Camera on/off preferences, preparation requirements

### Conflict Resolution

1. **Direct Discussion**: Encourage open dialogue between parties
2. **Mediation**: Involve a neutral third party if needed
3. **Documentation**: Record resolutions and learnings

### Knowledge Sharing

- **Pair Programming**: Encourage regular pairing sessions
- **Tech Talks**: Schedule regular knowledge sharing sessions
- **Documentation**: Maintain a living knowledge base

## Team Autonomy

### Decision Authority

- **Autonomous Decisions**: List of decisions team members can make independently
- **Consult Required**: Items requiring team discussion
- **Approval Needed**: Items requiring formal sign-off

### Execution Boundaries

- **Safe to Try**: Changes that can be made without approval
- **Review Required**: Changes needing peer review
- **Approval Needed**: Changes requiring stakeholder sign-off

## Continuous Improvement

### Retrospectives

- **Frequency**: End of each sprint
- **Format**: What went well, what to improve, action items
- **Follow-up**: Track action items to completion

### Process Optimization

- **Metrics**: Track team velocity, cycle time, and satisfaction
- **Experimentation**: Pilot new tools/processes with clear success criteria
- **Documentation**: Update collaboration rules based on learnings

## Version History

- **1.1.0 (2025-05-25)**: Initial version
  - Established stakeholder management protocols
  - Defined team collaboration standards
  - Outlined autonomy guidelines
