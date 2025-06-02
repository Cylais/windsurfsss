# Technical Rules

> **Literal Execution Rule [MANDATORY]:**
> All technical rules and protocols must be followed exactly as written, without summarizing, interpreting, or making assumptions. Explanations or summaries are only allowed when explicitly requested.
> **Memory Protocol Rule:**
> All technical operations and documentation must comply with the Unified Memory System protocols in `docs/memory-protocols.md`.
> **Exhaustive File Analysis Rule [MANDATORY]:**
> Whenever the user explicitly requests a file to be analyzed, checked, or reviewed, the agent must perform a deep dive and exhaustive review of every single line of the file. This includes checking for legacy references, deprecated instructions, hidden inconsistencies, and any content that may be out of alignment with current protocols or project structure. Partial or summary reviews are not permitted unless the user specifically requests a summary or limited-scope check.
> **Cross-Reference Protocol:**
> When files or folders are moved or renamed (especially in `docs/`, `config/`, `scripts/`), update all cross-references and documentation links accordingly.

```yaml
---
tags: [technical, code-quality, architecture, testing]
version: 1.2.0
last_updated: 2025-05-25
depends_on: documentation.rules.md, workflow.rules.md
---
```

## Code Quality Standards

### General Principles

- Write clean, self-documenting code with meaningful names
- Follow the Single Responsibility Principle
- Keep functions/methods small and focused
- Prefer immutability where possible
- Handle all errors explicitly

### Code Style

- Use consistent indentation (spaces, not tabs)
- Follow language-specific style guides (PEP 8 for Python, Airbnb for JavaScript, etc.)
- Maximum line length: 100 characters
- Use descriptive variable and function names

### Documentation

- Document public APIs and complex logic

## Version Control

### Git Workflow

- Use feature branches for new development
- Follow semantic versioning for releases
- Write clear, descriptive commit messages
- Rebase feature branches before merging
- Use pull requests for code review

### Backup Procedures

- Push all changes to the remote repository at the end of each session
- Run automated backup scripts:
  - `Backup-Project-7zip-DROPBOX.ps1` for cloud backup
  - `Backup-Project-7zip.ps1` for local backup
- Verify backup completion and integrity
- Document any backup failures and resolution steps
- Keep comments up-to-date
- Use JSDoc/TypeDoc for JavaScript/TypeScript
- Use docstrings for Python
- Include examples in documentation

## Architecture & Design

### Architecture Decision Records (ADRs)

For all significant technical decisions:

1. Create an ADR in `docs/architecture/decisions`
2. Follow the template:

   ```markdown
   # [Short title of decision]
   
   ## Status
   [Proposed | Accepted | Deprecated | Superseded]
   
   ## Context
   [What is the issue we're addressing?]
   
   ## Decision
   [What is the change we're proposing?]
   
   ## Consequences
   [What becomes easier/harder to do?]
   ```

### Design Patterns

- Use established patterns where appropriate
- Document pattern usage in code and architecture docs
- Prefer composition over inheritance

## Testing

### Test Coverage

- Aim for 80%+ test coverage
- Cover edge cases and error conditions
- Test both success and failure paths

### Test Types

- **Unit Tests**: Test individual components in isolation
- **Integration Tests**: Test component interactions
- **E2E Tests**: Test complete user flows
- **Performance Tests**: For performance-critical paths

### Test Structure

- Follow the Arrange-Act-Assert pattern
- One assertion per test case
- Use descriptive test names
- Keep tests independent and idempotent

## Code Review Process

### Before Submitting

- Self-review your changes
- Run all tests locally
- Ensure code meets style guidelines
- Update documentation as needed

### Review Checklist

- [ ] Code is clean and follows standards
- [ ] Tests are present and passing
- [ ] Documentation is updated
- [ ] Performance impact considered
- [ ] Security implications considered

## Security

### Secure Coding

- Validate all inputs
- Use parameterized queries
- Implement proper authentication/authorization
- Follow principle of least privilege
- Keep dependencies updated

### Security Reviews

- Conduct security reviews for sensitive features
- Use automated security scanning tools
- Document security decisions and trade-offs

## Performance

### Optimization Guidelines

- Measure before optimizing
- Focus on bottlenecks
- Consider algorithmic complexity
- Cache appropriately
- Lazy load when possible

### Monitoring & Logging

- Implement logging for critical paths
- Set up performance monitoring
- Create dashboards for key metrics
- Set up alerts for anomalies

### Version Control Guidelines

#### Branching Strategy

- Use feature branches for new work
- Keep branches short-lived
- Rebase before merging
- Delete merged branches

### Commit Messages

Follow the Conventional Commits specification:

```-
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

Types:

- feat: New feature
- fix: Bug fix
- docs: Documentation changes
- style: Code style changes
- refactor: Code changes that don't fix bugs or add features
- perf: Performance improvements
- test: Adding or fixing tests
- chore: Maintenance tasks

## Dependencies

### Management

- Use a package manager
- Pin exact versions in production
- Regularly audit for vulnerabilities
- Document why each dependency is needed

### Updates

- Schedule regular dependency updates
- Test updates in development first
- Have a rollback plan
- Document breaking changes

## Version History

- **1.1.0 (2025-05-25)**: Initial version
  - Established code quality standards
  - Defined architecture guidelines
  - Outlined testing requirements
