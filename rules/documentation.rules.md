# Documentation Rules

```yaml
---
tags: [documentation, standards, markdown]
version: 2.0.0
last_updated: 2025-05-25
---
```

## Core Documentation Files

### Required Files

- **`docs/AGENT_GUIDE.md`**
  - Purpose: Comprehensive agent developer guide.
  - Owner: Team Lead
- **`docs/MEMORY_CHEATSHEET.md`**
  - Purpose: Quick reference for memory system operations.
  - Owner: Knowledge Manager
- **`docs/memory-protocols.md`**
  - Purpose: Unified memory system protocols.
  - Owner: Technical Lead
- **`docs/Initiate_Startup_Flow.md`**
  - Purpose: Step-by-step project onboarding.
  - Owner: Project Manager
- **`config/cascades.yaml`**
  - Purpose: Agent roles and responsibilities.
  - Owner: Team Lead
- **`config/notifications.yaml`**
  - Purpose: Notification rules and templates.
  - Owner: Project Manager
- **`config/playwright.config.js`**
  - Purpose: Playwright automation configuration.
  - Owner: Automation Lead
- **`scripts/crewai_test.py`**
  - Purpose: Utility script for CrewAI integration.
  - Owner: Automation Lead
- **`session_log.md`**
  - Purpose: Summarizes session outcomes, lessons learned, and process improvements.
  - Owner: Team Lead
- **`project_architecture.md`**
  - Purpose: Contains current system design and major architectural decisions.
  - Owner: Technical Lead
- **`knowledge_base.md`**
  - Purpose: Living documentation for domains, SDKs, integration patterns, and best practices.
  - Owner: Knowledge Manager
- **`vendor_checklist.md`**
  - Purpose: Tracks third-party integrations, security audits, and vendor protocols.
  - Owner: Security Lead

> **Literal Execution Rule [MANDATORY]:**
> All documentation must be followed and updated exactly as specified, with no interpretation or summarization unless explicitly requested.
> **Memory Protocol Rule:**
> All documentation and knowledge management must comply with the Unified Memory System protocols in `docs/memory-protocols.md`.
> **Exhaustive File Analysis Rule [MANDATORY]:**
> Whenever the user explicitly requests a file to be analyzed, checked, or reviewed, the agent must perform a deep dive and exhaustive review of every single line of the file. This includes checking for legacy references, deprecated instructions, hidden inconsistencies, and any content that may be out of alignment with current protocols or project structure. Partial or summary reviews are not permitted unless the user specifically requests a summary or limited-scope check.

## Documentation Standards

### Formatting

- All documentation must follow [Markdown](https://www.markdownguide.org/) syntax.
- Use ATX-style headers (e.g., `## Section`).
- Use fenced code blocks with language specifiers.
- Include tables of contents for documents longer than one screen.

### Linting

All documentation must pass the following checks:

1. No trailing whitespace
2. Consistent heading levels
3. Proper list formatting
4. No bare URLs (use `[text](url)` format)
5. Line length limit of 100 characters (except for URLs and code blocks)

### File Naming Conventions

- Use lowercase with hyphens for file names (e.g., `code-style-guide.md`).
- Prefix with date for time-sensitive documents (e.g., `2025-05-meeting-notes.md`).
- Use `.md` extension for all Markdown files.

## Update Protocol

1. **Review** existing documentation for accuracy and relevance.
2. **Update** the document with new information.
3. **Version** the change in the document header.
4. **Link** to related documents using relative paths.
5. **Update all cross-references and links if files/folders are moved or renamed (especially in `docs/`, `config/`, `scripts/`).
6. **Commit** with a descriptive message following the format: `docs: [brief description]`

## Templates

### Meeting Notes

```markdown
# Meeting Title

**Date:** YYYY-MM-DD  
**Time:** HH:MM - HH:MM (Time Zone)  
**Location:** [Physical/Virtual]  

## Attendees
- [ ] Name 1
- [ ] Name 2

## Agenda
1. [ ] Topic 1
2. [ ] Topic 2

## Decisions
- [ ] Decision 1
- [ ] Decision 2

## Action Items
- [ ] Task 1 (@assignee, due: YYYY-MM-DD)
- [ ] Task 2 (@assignee, due: YYYY-MM-DD)

## Notes
[Detailed notes go here]
```

### Technical Documentation

```markdown
# [Component Name]

## Overview
[Brief description of the component]

## Architecture
[Architecture diagram or description]

## Dependencies
- Dependency 1
- Dependency 2

## Configuration

```yaml
# Example configuration
setting1: value1
setting2: value2
```

## API Reference

[API documentation]

## Troubleshooting

| Issue          | Solution         |
|----------------|------------------|
| Error message | Resolution steps |

```markdown

## Review Process

1. **Self-Review**
   - Check for typos and formatting issues
   - Ensure all links work
   - Verify code examples are accurate

2. **Peer Review**
   - Request review from at least one team member
   - Address all feedback
   - Update documentation as needed

3. **Approval**
   - Get final approval from documentation owner
   - Merge changes to main branch

## Version History

- **1.1.0 (2025-05-25)**: Initial version
  - Added documentation standards
  - Included templates for common documents
  - Defined review process
