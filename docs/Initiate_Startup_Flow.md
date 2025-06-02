# 🚀 Windsurf Project "Initiate Startup" Flow

## Version: 1.0.0 (Last updated: 2025-05-25)

A step-by-step, AI-powered onboarding and configuration flow for customizing your plug-and-play starter pack. Use this as a checklist, script, or as an interactive session with your AI assistant.

---

## Quick Links

- [1. Welcome & Purpose](#1-welcome--purpose)
- [2. Project Vision & Discovery](#2-project-vision--discovery)
- [3. Tech Stack & Constraints](#3-tech-stack--constraints)
- [4. Team & Roles](#4-team--roles)
- [5. Repo Setup & Naming Conventions](#5-repo-setup--naming-conventions)
- [6. License & Compliance](#6-license--compliance)
- [7. Integration Points](#7-integration-points)
- [8. Workflow Customization](#8-workflow-customization)
- [9. Testing & Quality](#9-testing--quality)
- [10. Deployment/Release](#10-deploymentrelease)
- [11. Notifications & Communication](#11-notifications--communication)
- [12. Context & Memory](#12-context--memory)
- [13. Risks, Dependencies & Logs](#13-risks-dependencies--logs)
- [14. User/Stakeholder Involvement](#14-userstakeholder-involvement)
- [15. Retrospectives & Continuous Improvement](#15-retrospectives--continuous-improvement)
- [16. Accessibility & Internationalization](#16-accessibility--internationalization)
- [17. AI/Automation-Specific Prompts](#17-aiautomation-specific-prompts)

---

> *Tip:* You can skip any section and return later. At any step, ask the AI for help, examples, or clarification.  
> *If you skip a section, add it to the [Skipped Sections Log](#skipped-sections-log) at the end of this file. This ensures you can easily revisit and complete it later.*  
> *Note:* As part of your project setup, be sure to define or review the six core roles for your team:
>
>
> - Product Manager
> - Solution Architect
> - Frontend Engineer
> - Backend Engineer
> - DevOps/QA
> - Full-Stack Integrator
> This ensures your project is ready for high-performance, collaborative development from day one.

---

## 1. Welcome & Purpose

Welcome to the Windsurf Project Startup! This flow will help you:

- Clarify your project vision and goals
- Define your tech stack and team
- Set up workflows, notifications, context, and memory
- Automate updates to all relevant files for immediate productivity
- Ensure nothing is missed, from repo setup to accessibility and continuous improvement

---

## 2. Project Vision & Discovery

### 2.1 Project Vision

- **What is the vision for this project?**
  - What problem will it solve?
  - Who is it for?
  - What impact do you want it to have?
- **If vision is unclear, use these prompts:**
  - What inspired this project?
  - Who are the intended users or customers?
  - What would success look like in 6 months?
  - Any similar products you admire or want to improve on?
  - What are the “must-have” vs “nice-to-have” outcomes?
  - *Example:* "A collaborative platform for remote teams to manage workflows and share knowledge. Success means teams onboard in <1 hour and reduce onboarding time by 50%."
- _If you skip this section, add it to the [Skipped Sections Log](#skipped-sections-log) below.*

### 2.2 Project Goals & Success Criteria

- What are the primary goals?
- How will you measure success?
- Any key deliverables or milestones?
  - *Example:* "Deliver MVP in 6 weeks, onboard 3 pilot teams, achieve >80% positive feedback."
- _If you skip this section, add it to the [Skipped Sections Log](#skipped-sections-log) below.*

---

## 3. Tech Stack & Constraints

- **Which technologies do you plan to use?** (Frontend, Backend, Database, Hosting, etc.)
- **If unsure, AI can suggest based on your vision, team skills, or constraints.**
- Any special requirements or limitations? (e.g., budget, compliance, preferred tools)
  - *Example:* "Frontend: React, Backend: Node.js, DB: PostgreSQL, Hosting: Vercel. Must support SSO."
- _If you skip this section, add it to the [Skipped Sections Log](#skipped-sections-log) below.*

---

## 4. Team & Roles

- Who are the main agents/roles? (Architect, Coder, Reviewer, Product Owner, etc.)
  - For each: Name, Contact, Responsibilities
- Any gaps or roles to fill?
  - *Example:*
    - Architect: Alice (<alice@domain.com>) – system design
    - Coder: Bob (<bob@domain.com>) – implementation
    - Reviewer: Carol (<carol@domain.com>) – code review
- _If you skip this section, add it to the [Skipped Sections Log](#skipped-sections-log) below.*

---

## 5. Repo Setup & Naming Conventions

- What should the repository/project be called?
- Any naming conventions for files, branches, or directories?
- Should a git repository be initialized? (Y/N)
- Preferred branching strategy? (e.g., main/dev/feature)
  - *Example:* `Repo: windsurf-collab, branch: main/develop/feature-*, dirs: src/, docs/, checklist/`
- _If you skip this section, add it to the [Skipped Sections Log](#skipped-sections-log) below.*

---

## 6. License & Compliance

- What license should the project use? (MIT, Apache 2.0, GPL, etc.)
- Any compliance requirements? (e.g., GDPR, security, accessibility)
- Any code of conduct or contributing guidelines?
  - *Example:* "MIT License, GDPR compliance, basic CONTRIBUTING.md."
- _If you skip this section, add it to the [Skipped Sections Log](#skipped-sections-log) below.*

---

## 7. Integration Points

- Will the project connect to external APIs, services, or legacy systems?
- Any integration requirements or constraints?
- Document any authentication, data exchange, or sync needs.
  - *Example:* "Integrate with Slack API for notifications; sync with legacy CRM."
- _If you skip this section, add it to the [Skipped Sections Log](#skipped-sections-log) below.*

---

## 8. Workflow Customization

- What are the main workflow steps? (e.g., Design, Implementation, Review, Deployment)
  - For each step:
    - Responsible agent/role
    - Triggers for next step (e.g., file updated, review approved)
    - Special instructions or requirements
- Any automation or notification triggers needed?
  - *Example:*
    - Step: Design → Agent: Architect → Trigger: designDoc updated
    - Step: Implementation → Agent: Coder → Trigger: review requested
- _If you skip this section, add it to the [Skipped Sections Log](#skipped-sections-log) below.*

---

## 9. Testing & Quality

- What testing frameworks or tools will you use?
- Any code coverage or quality goals?
- Should CI/CD be set up? (e.g., GitHub Actions, Jenkins)
  - *Example:* "Jest for unit tests, 80%+ coverage, GitHub Actions for CI."
- _If you skip this section, add it to the [Skipped Sections Log](#skipped-sections-log) below.*

---

## 10. Deployment/Release

- Where will the project be deployed? (cloud, on-prem, static hosting, etc.)
- What is the release process? (manual, automated, blue/green, etc.)
- Any deployment automation or rollback requirements?
  - *Example:* "Deploy to Netlify on main branch push, auto rollback on failure."
- _If you skip this section, add it to the [Skipped Sections Log](#skipped-sections-log) below.*

---

## 11. Notifications & Communication

- Should notifications be sent on step changes, errors, or other events?
- Who should receive them? (List agents, emails, channels)
- Any custom templates or channels? (Email, Slack, etc.)
  - *Example:* "Send Slack notification to #dev-team on deployment."
- _If you skip this section, add it to the [Skipped Sections Log](#skipped-sections-log) below.*

---

## 12. Context & Memory

- Any custom fields to add to the context schema? (e.g., project goals, key metrics, tags)
- Any initial knowledge, docs, or memory-bank entries to pre-populate?
  - *Example:* "Add context field: 'customerSegment', memory-bank: onboarding tips."
- _If you skip this section, add it to the [Skipped Sections Log](#skipped-sections-log) below.*

---

## 13. Risks, Dependencies & Logs

- Any known risks, dependencies, or mitigation strategies to log at the start?
- Any recurring meetings, session types, or collaboration log templates to predefine?
  - *Example:* "Risk: API rate limits; Mitigation: caching. Weekly sync meeting."
- _If you skip this section, add it to the [Skipped Sections Log](#skipped-sections-log) below.*

---

## 14. User/Stakeholder Involvement

- Who are the key stakeholders or users?
- Should they be involved in reviews, demos, or feedback loops?
- What is the feedback/demo cadence?
  - *Example:* "Product Owner: Dana (<dana@domain.com>), biweekly demo, feedback via Google Form."
- _If you skip this section, add it to the [Skipped Sections Log](#skipped-sections-log) below.*

---

## 15. Retrospectives & Continuous Improvement

- How often will you hold retrospectives or reviews?
- Where will you log lessons learned or improvement ideas?
- Any process for acting on feedback?
  - *Example:* "Monthly retro, lessons in retro_log.md, action items tracked in issues."
- _If you skip this section, add it to the [Skipped Sections Log](#skipped-sections-log) below.*

---

## 16. Accessibility & Internationalization

- Are accessibility (a11y) or internationalization (i18n) required?
- Any standards or guidelines to follow? (WCAG, ARIA, etc.)
- Should templates/checklists be included?
  - *Example:* "WCAG 2.1 AA compliance, i18n for English/Spanish, a11y checklist in docs."
- _If you skip this section, add it to the [Skipped Sections Log](#skipped-sections-log) below.*

---

## 17. AI/Automation-Specific Prompts

- Will you use AI agents? If so, any custom behaviors or escalation rules?
- Any "human-in-the-loop" requirements?
- Should agent actions be logged or require approval?
  - *Example:* `Reviewer agent escalates to human if test coverage <70%. All agent actions logged.`
- _If you skip this section, add it to the [Skipped Sections Log](#skipped-sections-log) below.*

---

## 6. Notifications & Communication

- Should notifications be sent on step changes, errors, or other events?
- Who should receive them? (List agents, emails, channels)
- Any custom templates or channels? (Email, Slack, etc.)

---

## 7. Context & Memory

- Any custom fields to add to the context schema? (e.g., project goals, key metrics, tags)
- Any initial knowledge, docs, or memory-bank entries to pre-populate?

---

## 8. Risks, Dependencies & Logs

- Any known risks, dependencies, or mitigation strategies to log at the start?
- Any recurring meetings, session types, or collaboration log templates to predefine?

---

## 9. Review & Confirm

- Review all entered information (AI can summarize)
- Confirm or edit details before proceeding

---

## 10. Automated Update

- Automatically update all relevant files:
  - README, workflow.yaml, config/cascades.yaml, notifications, context.schema.json, etc.
  - Replace placeholders, add/remove templates as needed

---

## 11. Final Output & Next Steps

- Onboarding checklist generated for your team
- All docs, workflows, and notifications tailored to your project
- Start collaborating and let the agents work!

---

## 12. Advanced/Optional Steps

- Save this flow as a script or CLI tool (e.g., `initiate-startup`)
- Re-run or update the flow as your project evolves
- Integrate with AI assistants for interactive Q&A and automation

---

## Skipped Sections Log

> **Instructions:**
>
> - If you skip any section above, record it here with the section name, date, and any notes or blockers.
> - Review this log regularly and revisit skipped sections when you have the information or bandwidth.
> - The AI (or team lead) can prompt you to complete these later for a fully robust project setup.

**Example Entry:**

- **Section:** 6. License & Compliance
  - **Date Skipped:** 2025-05-11
  - **Notes:** Waiting for legal team to confirm license choice.

- **Section:** 14. User/Stakeholder Involvement
  - **Date Skipped:** 2025-05-11
  - **Notes:** Stakeholders not yet identified, will revisit after team kickoff.

---

**Tip:** You can use this file as a conversational script with Cascade or any LLM assistant—just start at the top and answer each section. The AI can guide you, fill in gaps, and update your project files automatically.

**Improvements included:**

- Vision and tech stack discovery with guided prompts
- Success criteria and deliverables
- Explicit review/confirm step before file updates
- Advanced/optional automation and re-run support
- Designed for both manual and AI-powered onboarding
