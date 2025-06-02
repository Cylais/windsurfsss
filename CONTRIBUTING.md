# Contributing to Windsurf Project Startup Pack

## Version: 2.0.0 (Last updated: 2025-05-25)

Thank you for your interest in contributing to the Windsurf Project Startup Pack! We value high-quality, collaborative, and protocol-driven contributions.

---

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone <your-repo-url>
   cd Windsurf-Project-Startup-Pack
   ```

2. **Install requirements:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Review onboarding docs:**
   - `README.md`
   - `docs/AGENT_GUIDE.md`
   - `essentials_checklist.md`
   - `checklist/dream_team_setup_checklist.md`
4. **Run tests:**

   ```bash
   pytest
   ```

5. **Set up your agent environment:**
   - Reference `agents_config.yaml` for roles and protocols.
   - Use `project.yaml` for metadata and project context.

---

## How to Contribute

1. **Read the Documentation:**
   - Review all relevant guides and checklists.
2. **Discuss Major Changes:**
   - Open an issue or discussion before large changes.
3. **Follow Coding Standards:**
   - Adhere to the project’s coding structure and memory protocols.
   - Use established agent roles and workflows.
4. **Testing:**
   - Add/maintain tests for any new or changed functionality.
5. **Documentation:**
   - Update documentation as needed.
6. **Pull Requests:**
   - Reference relevant issues and checklist items.
   - Clearly describe your changes and rationale.

---

## Branching & Review Process

- Use feature branches for new work: `feature/<short-description>`
- All PRs require at least one review from a different role (see `agents_config.yaml`).
- Escalation: See escalation paths in `agents_config.yaml`.
- Reference `workflow.yaml` for process automation and review steps.

---

## Roles & Collaboration

- This project supports multi-agent, multi-role collaboration (see `agents_config.yaml` and `project.yaml`).
- Use the session log (`docs/session_log.md`) to document significant agent actions and discussions.
- Reference and update relevant checklists:
  - `essentials_checklist.md`
  - `checklist/dream_team_setup_checklist.md`
  - Role-specific checklists in `checklist/`

---

## Code of Conduct

- Be respectful, constructive, and inclusive.
- Follow the established communication protocols.

---

## Versioning

- This project follows protocol versioning (see `project.yaml`).
- Update the version and last updated date in new major contributions.

---

## FAQ & Troubleshooting

- **Common issues:**
  - Dependency errors? Check your Python version and `requirements.txt`.
  - Workflow confusion? Review `workflow.yaml` and `agents_config.yaml`.
  - Unsure about your role? See `agents_config.yaml` and team checklists.
- For more help, see `docs/FAQ.md` (add if missing).

---

## Badges & CI

- Add status badges here if using CI/CD (e.g., GitHub Actions, Travis).
- Ensure all tests pass before submitting a PR.

---

For questions, contact the maintainers listed in `project.yaml`.
