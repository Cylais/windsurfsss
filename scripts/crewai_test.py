"""
CrewAI Integration Test Script

---
ONBOARDING & USAGE
---
- Purpose: Demonstrates plug-and-play CrewAI agent integration for Windsurf projects.
- Quickstart (Manual):
    python scripts/crewai_test.py
- CI Integration:
    - Add to your CI pipeline to ensure CrewAI agent workflows are functional.
    - Example:
        - name: Run CrewAI Test
          run: python scripts/crewai_test.py
- Multi-Agent Example:
    - Shows both a simple agent and a multi-agent (Architect/Reviewer) workflow.
- Troubleshooting:
    - See troubleshooting tips at the end of this file.
    - Ensure crewai is installed and API keys are set if required.
- References:
    - See session_start_protocol.md and memory_system_guide.ps1 for agent onboarding and workflow integration.
"""

from crewai import Crew, CrewMember

# ---
# Single-agent example: Product Manager only
# ---
single_agent_crew = Crew(
    members=[
        CrewMember(
            name="Product Manager",
            role="You are the Product Manager. Define the vision and requirements for the new collaborative note-taking app."
        )
    ]
)
single_result = single_agent_crew.run("Define the vision for a collaborative note-taking app.")
print("Single-agent result:", single_result)

# ---
# Two-agent example: Product Manager and Solution Architect collaborating
# ---
two_agent_crew = Crew(
    members=[
        CrewMember(
            name="Product Manager",
            role="You are the Product Manager. Define the vision and requirements for the new collaborative note-taking app."
        ),
        CrewMember(
            name="Solution Architect",
            role="You are the Solution Architect. Design the overall system architecture based on requirements from the Product Manager. Communicate with the Product Manager to clarify requirements."
        )
    ]
)
two_result = two_agent_crew.run("Product Manager: define requirements. Solution Architect: design a system based on those requirements and confirm with Product Manager.")
print("Two-agent collaboration result:", two_result)

# ---
# Six-agent example: Full Dream Team Collaboration
# ---
# ---
# Multi-agent example: Full Dream Team Collaboration
# ---
product_manager = CrewMember(
    name="Product Manager",
    role="You are the Product Manager. Define the vision and requirements for the new collaborative note-taking app."
)
solution_architect = CrewMember(
    name="Solution Architect",
    role="You are the Solution Architect. Design the overall system architecture based on requirements."
)
frontend_engineer = CrewMember(
    name="Frontend Engineer",
    role="You are the Frontend Engineer. Implement the user interface and ensure a seamless user experience."
)
backend_engineer = CrewMember(
    name="Backend Engineer",
    role="You are the Backend Engineer. Develop the backend logic, APIs, and data storage."
)
devops_qa = CrewMember(
    name="DevOps/QA",
    role="You are responsible for deployment, automation, and quality assurance."
)
fullstack_integrator = CrewMember(
    name="Full-Stack Integrator",
    role="You are the Full-Stack Integrator. Ensure all components work together and handle integration issues."
)

multi_crew = Crew(members=[
    product_manager,
    solution_architect,
    frontend_engineer,
    backend_engineer,
    devops_qa,
    fullstack_integrator
])

multi_result = multi_crew.run("Work together to deliver a collaborative note-taking app from idea to deployment, ensuring all requirements are met and the system is fully integrated.")
print("Multi-agent result:", multi_result)

# ---
# TROUBLESHOOTING & ONBOARDING TIPS
# ---
# - If you see ImportError, ensure crewai is installed: pip install crewai
# - For API/auth errors, check CrewAI docs for setup instructions and API keys.
# - For onboarding and advanced usage, see memory_system_guide.ps1 and protocol docs.
# - Use this script to validate agent integration in CI and onboarding workflows.
