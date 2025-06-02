# Windsurf Project Rules

> **Literal Execution Rule [MANDATORY]:**
> All rules must be followed exactly as written, without summarizing, interpreting, or making assumptions. Explanations or summaries are only allowed when explicitly requested.
> **Memory Protocol Rule:**
> All project knowledge and automation must comply with the Unified Memory System protocols in `docs/memory-protocols.md`.
> **Exhaustive File Analysis Rule [MANDATORY]:**
> Whenever the user explicitly requests a file to be analyzed, checked, or reviewed, the agent must perform a deep dive and exhaustive review of every single line of the file. This includes checking for legacy references, deprecated instructions, hidden inconsistencies, and any content that may be out of alignment with current protocols or project structure. Partial or summary reviews are not permitted unless the user specifically requests a summary or limited-scope check.

**Version:** 1.2.0  
**Last Updated:** 2025-05-25  

## Table of Contents

- [Documentation Rules](documentation.rules.md)
- [Workflow Rules](workflow.rules.md)
- [Technical Rules](technical.rules.md)
- [Collaboration Rules](collaboration.rules.md)
- [Memory Rules](memory.rules.md)
- [Security Rules](security.rules.md)
- [Session Management](session_management.rules.md)

## How to Use These Rules

- When files or folders are moved or renamed (especially in `docs/`, `config/`, `scripts/`), update all cross-references and documentation links accordingly.

1. **For New Team Members**: Start with the [Documentation Rules](documentation.rules.md) to understand our standards.
2. **For Developers**: Focus on [Technical Rules](technical.rules.md) and [Workflow Rules](workflow.rules.md).
3. **For Project Managers**: Review [Collaboration Rules](collaboration.rules.md) and [Workflow Rules](workflow.rules.md).
4. **For All**: Be familiar with [Security Rules](security.rules.md) and [Memory Rules](memory.rules.md).

## Version History

- **1.2.0 (2025-05-25)**: Added session management rules and deprecated .windsurfrules
- **1.1.0 (2025-05-25)**: Initial modularization of rules
- **1.0.0 (2025-04-29)**: Initial version

## Contributing

To propose changes to these rules:

1. Create a new branch
2. Update the relevant rule files
3. Update the version number and change log
4. Submit a pull request for review
