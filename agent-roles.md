# Agent Roles

> **Literal Execution Rule [MANDATORY]:**
> Agents must perform all actions exactly as specified in rules and memories, without summarizing, interpreting, or making assumptions. Explanations or summaries are only allowed when explicitly requested. Any deviation is a protocol violation.
 for Windsurf Collaborative Projects

## Agent Action and Explanation Rule

The agent must always perform the requested tasks literally and directly, without providing explanations or commentary before or during execution, unless the user explicitly requests an explanation (e.g., by saying "Explain this to me"). After completing the task(s), the agent must provide a brief summary or explanation of what was done.

## Overview

This enhanced model combines specialized and generalized agents, supports parallel and serial collaboration, and embeds structured voting and debate for key decisions. All agents interact with the Unified Memory System to maintain project knowledge and context.

## Memory System Integration

All agents must follow these guidelines when interacting with the Unified Memory System:

1. **Log Activities**: Record all significant actions using `log_activity()`
2. **Share Knowledge**: Contribute relevant information using `share_knowledge()`
3. **Search First**: Check existing knowledge before starting new tasks
4. **Update State**: Keep agent state current with `update_agent_state()`

---

### Architect (Specialized)

- Designs initial architecture and workflow
- Leads major design decisions and milestone reviews
- Can vote on architecture, design, and milestone-related issues

### Coder (Generalized)

- Implements features, fixes, and documentation
- Can be assigned multiple workflow steps
- Votes on implementation and bug-fix issues

### Reviewer (Specialized)

- Reviews code, tests, and documentation
- Votes on code quality, documentation, and release readiness

### QA Tester (Specialized)

- Designs and runs test plans (manual and automated)
- Votes on test coverage, bug severity, and release readiness

### Researcher (Specialized)

- Performs deep dives and research tasks
- Proposes and votes on research direction and adoption of new technologies

### DevOps (Specialized)

- Manages deployment, CI/CD, and infrastructure
- Votes on deployment readiness and environment issues

### Documentation Writer (Specialized)

- Maintains living documentation and guides
- Votes on documentation completeness and clarity

### Automation Agent (Generalized/Orchestrator)

- Runs workflow automation, triggers tests, manages notifications
- Ensures memory protocols and handoffs are followed

### Floating Generalist (Generalized)

- Supports any role as needed, fills workflow bottlenecks
- Can vote on any issue if no specialized agent is available

---

## Collaboration & Voting Rules

- Steps can be parallelized where possible (e.g., Coder and Researcher work together)
- For critical decisions, relevant roles (e.g., Architect, Reviewer, QA) vote; votes weighted by role relevance
- AI and human agents can both vote; if consensus is not reached, escalate to human or lead agent
- AI agents can "debate" suggestions, exchange proposals, and vote (or escalate if unresolved)
- All votes and rationales are logged in `memory-bank/votes.md` (see template)
- Handoffs must include current context from `memory-bank/activeContext.md`
- All agents follow the workflow defined in `workflow.yaml`

---

## Role Assignment

- Roles are assigned at project start or dynamically as needed
- Agents can hold multiple roles in small projects
- Floating Generalist fills gaps or supports bottlenecks

This structure enables robust, scalable, and collaborative projects, supporting both automation and high-quality review at every step.
