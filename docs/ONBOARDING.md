# Windsurf Project Startup Pack: Onboarding Guide

Welcome to the Windsurf Project Startup Pack! This guide will help you get started with plug-and-play multi-agent workflows using your dream team roles.

## Quick Start

1. **Install dependencies** (if not already done):
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the example scripts:**
   ```bash
   python examples/agent_example.py
   python scripts/crewai_test.py
   ```
   These scripts demonstrate:
   - Single-agent workflow (1 agent)
   - Two-agent collaboration (2 agents)
   - Full dream team orchestration (6 agents)

## Example Scenarios

### 1-Agent Example
- The Product Manager defines requirements and shares knowledge.

### 2-Agent Example
- Product Manager and Solution Architect collaborate: PM shares requirements, Architect references them to design a solution.

### 6-Agent Example
- All dream team roles work together from product vision to deployment and integration.

See `examples/README.md` for sample output and detailed explanations.

## Configuring Your Team

Edit `agents_config.yaml` to set up your agents. See the commented templates for 1, 2, and 6-agent teams.

## How Agents Collaborate
- Agents share knowledge using the unified memory system.
- Other agents can search for and reference this knowledge in their own decisions and tasks.

## Additional Resources
- [examples/README.md](../examples/README.md): Detailed examples and outputs
- [README.md](../README.md): Project overview and protocols

## Troubleshooting
- If you see ImportError, ensure dependencies are installed.
- For onboarding and advanced usage, see protocol and memory system guides in the `rules/` and `tools/` directories.
