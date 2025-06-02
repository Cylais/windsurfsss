# Checklist for .windsurfrules

## Modularization & Structure

- [ ] Audit existing .windsurfrules for natural split points (topics, roles, workflows, volatility)
- [ ] Create a master index file (rules_index.md) summarizing and linking all rule modules
- [ ] Split rules into separate, clearly-named files (e.g., memory.rules.md, workflow.rules.md, security.rules.md, docs.rules.md)
- [ ] Add YAML front-matter or inline tags to each rule/section for topic, role, and workflow step
- [ ] At the top of each module, add a summary and explicit context anchor (when/where the rules apply)
- [ ] For rules to be enforced automatically, create a parallel YAML/JSON file (enforceable.rules.yaml)
- [ ] Add versioning and change logs to each rule module

## Current Content Review

- [ ] Are all rules modular, clearly sectioned, and easy to update?
- [ ] Do rules reference other Starter Pack files (workflow, context, roles, notifications)?
- [ ] Are project-specific overrides and inheritance supported?
- [ ] Are rules versioned or dated for traceability?
- [ ] Do rules have clear context about when and where they apply?
- [ ] Are there any redundant or conflicting rules?

## Implementation & Integration

- [ ] Update onboarding docs and agent logic to reference the new modular rule structure
- [ ] Develop scripts or endpoints for agents to fetch rules by tag, topic, or scenario
- [ ] Implement CI checks to validate the existence, structure, and up-to-dateness of all rule modules
- [ ] Integrate notification hooks (e.g., Slack/Discord) for rule violations or updates
- [ ] Protect sensitive rule modules (e.g., security/auth) with correct file permissions

## Documentation & Usability

- [ ] Add detailed comments/headers for quick navigation and onboarding
- [ ] Provide a "Quick Reference" or "Agent Cheat Sheet" at the top of each module
- [ ] Document safe customization boundaries for each module
- [ ] Add a "How to use these rules" section to the master index
- [ ] Provide diagrams or workflow charts for visual navigation of rule relationships

## Review & Maintenance

- [ ] Schedule periodic reviews to optimize structure and tagging based on usage patterns
- [ ] Benchmark agent rule retrieval and context-switching performance before and after modularization
- [ ] Test the modular rules system with a new project to ensure true plug-and-play usability
- [ ] Collect feedback from both AI/agents and human users after rollout and iterate
- [ ] Cross-reference rules with collaboration_log.md for major updates

## Further Enhancements

- [ ] Add a section/template for custom project overrides and exceptions
- [ ] Provide real-world usage examples for advanced rules
- [ ] Suggest a periodic review cadence (e.g., quarterly) for rules relevance
