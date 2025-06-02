# Security Rules

> **Literal Execution Rule [MANDATORY]:**
> All security rules and protocols must be followed exactly as written, without summarizing, interpreting, or making assumptions. Explanations or summaries are only allowed when explicitly requested.
> **Memory Protocol Rule:**
> All security operations and documentation must comply with the Unified Memory System protocols in `docs/memory-protocols.md`.
> **Exhaustive File Analysis Rule [MANDATORY]:**
> Whenever the user explicitly requests a file to be analyzed, checked, or reviewed, the agent must perform a deep dive and exhaustive review of every single line of the file. This includes checking for legacy references, deprecated instructions, hidden inconsistencies, and any content that may be out of alignment with current protocols or project structure. Partial or summary reviews are not permitted unless the user specifically requests a summary or limited-scope check.
> **Cross-Reference Protocol:**
> When files or folders are moved or renamed (especially in `docs/`, `config/`, `scripts/`), update all cross-references and documentation links accordingly.

```yaml
---
tags: [security, compliance, access-control, data-protection]
version: 1.2.0
last_updated: 2025-05-25
depends_on: documentation.rules.md, technical.rules.md
---
```

## Access Control

### Authentication

- Use multi-factor authentication (MFA) for all systems
- Implement OAuth 2.0 with PKCE for web applications
- Enforce strong password policies
- Implement account lockout after failed attempts

### Authorization

- Follow principle of least privilege
- Use role-based access control (RBAC)
- Document all permission levels
- Review access rights quarterly

## Data Protection

### Encryption

- Encrypt data in transit (TLS 1.2+)
- Encrypt sensitive data at rest
- Use strong encryption algorithms
- Manage encryption keys securely

### Data Handling

- Classify data by sensitivity
- Log all access to sensitive data
- Implement data retention policies
- Secure data disposal procedures

## Secure Development

### Code Security

- Perform static code analysis
- Conduct regular dependency checks
- Implement secure coding standards
- Review security implications of third-party code

### API Security

- Validate all inputs
- Implement rate limiting
- Use API keys and tokens
- Document security requirements

## Incident Response

### Reporting

- Document all security incidents
- Report incidents within 1 hour of detection
- Follow incident response plan
- Conduct post-incident reviews

### Recovery

- Maintain secure backups
- Test restoration procedures
- Document recovery steps
- Update response plans based on incidents

## Compliance

### Regulations

- Document applicable regulations
- Implement required controls
- Conduct regular compliance audits
- Maintain audit trails

### Vendor Management

- Assess vendor security
- Include security requirements in contracts
- Monitor vendor compliance
- Review vendor access regularly

## Version History

- **1.1.0 (2025-05-25)**: Initial version
  - Established security protocols
  - Defined access control measures
  - Outlined incident response procedures
