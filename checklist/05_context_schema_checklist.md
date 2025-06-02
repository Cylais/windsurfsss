# Checklist for context.schema.json

## Current Content Review

- [ ] Are all required context fields present, clearly described, and typed?
- [ ] Are audit fields (lastUpdatedBy, timestamp) included and used?
- [ ] Is the schema modular and easily extensible for new project needs?
- [ ] Are field descriptions and allowed values (enums) included?
- [ ] Does the context schema provide the data and fields needed for all six core roles to collaborate effectively?
  - Product Manager
  - Solution Architect
  - Frontend Engineer
  - Backend Engineer
  - DevOps/QA
  - Full-Stack Integrator

## Improvements

- [ ] Add field usage examples and reference to workflow.yaml steps.
- [ ] Cross-link schema fields with agent roles in cascades.yaml.
- [ ] Document how to extend or override schema for project-specific requirements.

## Further Enhancements

- [ ] Provide a script or markdown guideline for validating context updates against the schema.
- [ ] Add a template for extending the schema and documenting new fields.
- [ ] Suggest automated schema checks as part of onboarding or CI (if possible).
