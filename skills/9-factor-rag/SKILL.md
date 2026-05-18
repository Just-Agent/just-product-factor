# 9-factor-rag Skill

## Name

9-factor-rag

## Purpose

Audit and refactor RAG systems for ingestion, chunking, retrieval, reranking, grounding, citations, evaluation, and context control.

## When to use

- RAG apps
- Knowledge bases
- Document QA
- Search-augmented Agents
- Citation-heavy assistants

## When not to use

- Pure chatbots with no retrieval
- Static documents without query flow

## Inputs

Ask for or inspect:

- README and docs
- source files
- examples and recipes
- configuration files
- tests and validation scripts
- CI/CD workflow files
- logs, changelog, release notes, or version history

## Workflow

1. Identify the project goal and user-facing promise.
2. Inspect available files.
3. Apply `checklist.md`.
4. Score with `scoring-rubric.md`.
5. Produce an audit report using `audit-report-template.md`.
6. Produce a refactor plan using `refactor-plan-template.md`.
7. Prioritize changes by product value and release readiness.
8. Validate changes if the environment allows.

## Review dimensions

- Data ingestion
- Chunking
- Indexing
- Retrieval
- Reranking
- Context assembly
- Citations
- Evaluation
- Failure handling

## Refactor priorities

1. Make data pipeline explicit
2. Improve retrieval quality
3. Enforce citations
4. Add evaluation
5. Add monitoring and fallbacks

## Output format

Return:

1. Summary
2. Scorecard
3. Critical findings
4. Recommended changes
5. Refactor plan
6. Validation plan
7. Next iteration suggestions

## Example calls

See `usage-examples.md`.

## Version

v0.5.0

## Agent manifest

This Skill includes a machine-readable `skill.json` manifest so an Agent can quickly identify triggers, expected inputs, expected outputs, required files, and the review protocol before reading the full markdown pack.

