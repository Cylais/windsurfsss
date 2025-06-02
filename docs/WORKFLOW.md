# Collaborative Workflow Guide for Windsurf Project Startup Pack

**Version:** 2.0.0  
**Last Updated:** 2025-05-25

---

## Purpose

This guide provides a comprehensive overview of the collaborative, multi-agent, and automation-driven workflow for Windsurf projects. It references all major configuration files and protocols, ensuring seamless onboarding and plug-and-play extensibility.

---

## Workflow Overview

Windsurf projects use a milestone-driven, automated workflow that supports both human and AI agents. The workflow is defined in `workflow.yaml` and integrates with:

- **cascades.yaml**: Role definitions, notification routing, and workflow automation
- **notifications.yaml**: Notification rules, escalation paths, and CI triggers
- **agents_config.yaml**: Agent orchestration, memory protocols, and collaboration rules
- **context.schema.json**: Context/config schema for automation and extensibility

### Key Workflow Phases (Dream Team Roles)

The workflow is designed around the "Dream Team" structure defined in `agents_config.yaml`:

- **Product Manager**
- **Solution Architect**
- **Frontend Engineer**
- **Backend Engineer**
- **DevOps/QA**
- **Full-Stack Integrator**

| Phase            | Primary Roles Involved                                           |
|------------------|-----------------------------------------------------------------|
| Ideation         | Product Manager, Solution Architect, Full-Stack Integrator       |
| Design           | Solution Architect, Product Manager, Frontend Engineer, Backend Engineer, Full-Stack Integrator |
| Research         | Solution Architect, Backend Engineer, Frontend Engineer, Full-Stack Integrator |
| Code             | Frontend Engineer, Backend Engineer, Full-Stack Integrator       |
| Test             | DevOps/QA, Frontend Engineer, Backend Engineer, Full-Stack Integrator |
| Deploy/Release   | DevOps/QA, Product Manager, Solution Architect                   |

**Phase Details:**

1. **Ideation**: Product Manager leads brainstorming of goals, requirements, and vision. Solution Architect and Full-Stack Integrator contribute technical feasibility and integration ideas.
2. **Design**: Solution Architect leads system architecture and planning, collaborating with Product Manager and both engineering roles. Full-Stack Integrator ensures cohesion.
3. **Research**: Solution Architect, Backend Engineer, Frontend Engineer, and Full-Stack Integrator conduct technical research, evaluate risks, and explore alternatives.
4. **Code**: Frontend Engineer, Backend Engineer, and Full-Stack Integrator implement features, referencing design decisions and memory logs.
5. **Test**: DevOps/QA leads automated/manual testing, with engineers and Full-Stack Integrator supporting Playwright and integration tests.
6. **Deploy/Release**: DevOps/QA, Product Manager, and Solution Architect coordinate deployment, reporting, and milestone summaries.

Each phase is automated via triggers and integrations (see `workflow.yaml` for details). Collaboration and escalation paths follow the structure in `agents_config.yaml`.

---

## Automation & Integrations

- **Unified Memory System**: All agents log decisions, activities, and votes using the memory interface.
- **Playwright**: Automated browser testing (see `playwright.config.js`).
- **Notifications**: Automated alerts and escalations (see `notifications.yaml`).
- **Voting & Logging**: Structured voting and milestone summaries required at each step.
- **Extensibility**: Add new workflow steps or integrations by editing `workflow.yaml` and referencing new agents or roles in `agents_config.yaml`.

---

## Onboarding & Usage

- **Start Here**: Read `README.md`, `CONTRIBUTING.md`, and this guide.
- **Setup**: Run `scripts/setup.sh` or `scripts/setup.py` for automated onboarding.
- **Agent Collaboration**: Reference `agents_config.yaml` for roles, memory, and protocols.
- **Workflow Customization**: Edit `workflow.yaml` to adapt the workflow for your project.

---

## Troubleshooting & CI

- **CI Integration**: All workflow steps are CI-ready. Reference `notifications.yaml` for CI triggers.
- **Troubleshooting**: See `ONBOARDING.md` and `CONTRIBUTING.md` for escalation and support paths.

---

## References

- `workflow.yaml`: Main workflow definition
- `cascades.yaml`: Agent roles and notifications
- `notifications.yaml`: Notification rules and CI triggers
- `agents_config.yaml`: Agent orchestration and protocols
- `context.schema.json`: Automation schema
- `README.md`, `CONTRIBUTING.md`, `ONBOARDING.md`: Onboarding and collaboration
