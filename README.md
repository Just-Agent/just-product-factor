# just-product-factor

**Reusable Factor Skills for Agent-native product optimization.**

中文定位：**把优秀工程标准，变成 Agent 可以反复调用的产品优化技能。**

Public repository name: `just-product-factor`. Package and catalog name: `product-factor-skills`.

`product-factor-skills` is a multi-skill standard repository. It packages engineering factor standards into reusable Agent Skills for repeatable product audit, project refactor, release readiness, deployability, maintainability, and continuous optimization.

`product-factor-skills` 是一个多 Skill 标准仓库，用于把工程方法论包装成可复用的 Agent Skill，帮助 Agent 在优化 Agent、App、HTML、GitHub Actions、RAG、MCP 等产品工程项目时，执行标准化审查、评分、重构和升级。

> Current version: `v0.9.0`
>
> This repository does **not** require heavy monorepo tooling. It uses a simple multi-skill standard repository structure. If future versions add packages, CLIs, runners, or independent releases, it can evolve into a real monorepo.

---

## Why this exists

很多工程标准本身是文档、方法论或最佳实践，但 Agent 真正需要的是可执行的工作单元：

- 什么时候调用这个标准？
- 输入什么？
- 检查哪些文件？
- 怎么评分？
- 怎么输出审查报告？
- 怎么生成重构计划？
- 怎么持续迭代？

This project turns standards into repeatable skills.

```text
engineering method / factor standard
  -> Agent-callable Skill
  -> checklist
  -> scoring rubric
  -> audit report template
  -> refactor plan template
  -> validation protocol
  -> repeatable optimization loop
```

---

## Included Skills

| Skill | Purpose | Use it when |
|---|---|---|
| `12-factor-agents` | Audit and refactor LLM Agent systems | You are building Agent workflows, tool calls, memory, control flow, or human-in-the-loop systems |
| `12-factor-app` | Audit deployability and product engineering quality | You are building SaaS, APIs, full-stack apps, services, or CLI products |
| `10-factor-html` | Improve HTML pages and web previews | You need semantic HTML, responsive UI, accessibility, SEO, performance, and visual polish |
| `8-factor-github-actions` | Improve CI/CD workflows | You need safe, maintainable, reusable GitHub Actions automation |
| `9-factor-rag` | Improve retrieval-augmented generation systems | You need better chunking, indexing, retrieval, citations, evaluation, and context control |
| `7-factor-mcp` | Improve MCP tools and servers | You need clearer tool boundaries, schema design, permissions, and runtime safety |
| `11-factor-cli` | Improve command-line products | You need installability, command UX, help output, error handling, scriptable output, packaging, and release readiness |
| `13-factor-product-readiness` | Improve launch readiness and product polish | You need stronger positioning, onboarding, examples, release discipline, open-source credibility, and repeat-use value |
| `6-factor-docs` | Improve documentation systems | You need stronger README, quickstart, docs navigation, examples, accuracy, maintenance, and Agent handoff prompts |
| `5-factor-evals` | Improve evaluation and regression confidence | You need golden cases, smoke tests, failure taxonomy, benchmarks, and release gates |
| `14-factor-security-privacy` | Improve security and privacy readiness | You need secrets hygiene, permission boundaries, data handling, dependency hygiene, CI/CD safety, and release blockers |
| `15-factor-observability` | Improve runtime visibility and debugging | You need better logs, metrics, traces, validation artifacts, failure diagnostics, and Agent handoff evidence |

Each Skill includes a machine-readable `skill.json` manifest so an Agent can identify trigger phrases, expected inputs, expected outputs, required files, and the review protocol before reading the full markdown pack.

## Security, privacy, and observability readiness

`14-factor-security-privacy` adds a release-safety pass for projects that touch secrets, credentials, user data, workflows, integrations, Agent tools, MCP servers, RAG sources, or deployment automation. Use it before public release or hosted deployment, and pair it with the domain Skill when mitigation requires technical changes.

`15-factor-observability` adds a runtime visibility pass for projects that need clearer logs, metrics, traces, validation artifacts, failure diagnostics, CI/release summaries, and Agent handoff evidence. Pair it with `14-factor-security-privacy` when debugging data could expose secrets, prompts, tokens, or user data.


---

## Core calls

```text
Use the 12-factor-agents skill to review this agent project.

Use the 12-factor-agents skill to refactor this project into a production-ready agent architecture.

Use the 12-factor-app skill to audit this app for deployability, maintainability, configuration, logging, and release readiness.

Use the 10-factor-html skill to improve this HTML page for semantic structure, responsiveness, accessibility, SEO, performance, and visual polish.

Use the 8-factor-github-actions skill to review this workflow for CI/CD reliability, permissions, caching, release automation, and deployment safety.

Use the 9-factor-rag skill to audit this RAG project for retrieval quality, chunking, indexing, citation, context control, and evaluation.

Use the 7-factor-mcp skill to review this MCP server for tool boundaries, schema clarity, permission design, safety, and integration quality.

Use the 11-factor-cli skill to audit this CLI for installability, command UX, configuration, error handling, logging, testing, packaging, and release readiness.

Use the 13-factor-product-readiness skill to audit this repository for launch readiness, onboarding, product polish, release discipline, and open-source credibility.

Use the 6-factor-docs skill to audit this repository documentation for positioning, onboarding, information architecture, examples, accuracy, maintenance, and Agent handoff readiness.

Use the 5-factor-evals skill to audit this Agent project for golden cases, regression tests, failure taxonomy, and release gates.

Use the 14-factor-security-privacy skill to audit this repository for secrets, permissions, data handling, dependency hygiene, CI/CD safety, and release blockers.

Use the 15-factor-observability skill to audit this Agent project for logs, traces, tool-call evidence, validation artifacts, and debuggability.

Use product-factor-skills to compose a multi-Skill review for this repository.

Use the skill-factory template to create a new xx-factor-* skill.
```

---

## Repository structure

```text
product-factor-skills/
  README.md
  SKILL.md
  VERSION
  CHANGELOG.md
  RELEASE_NOTES.md
  product-factor-skills.json
  skills.json
  schemas/
    skill-manifest.schema.json
  skills/
    12-factor-agents/
      SKILL.md
      skill.json
      checklist.md
      scoring-rubric.md
      audit-report-template.md
      refactor-plan-template.md
      usage-examples.md
    12-factor-app/
    10-factor-html/
    8-factor-github-actions/
    9-factor-rag/
    7-factor-mcp/
    11-factor-cli/
    13-factor-product-readiness/
    6-factor-docs/
    5-factor-evals/
    14-factor-security-privacy/
    15-factor-observability/
  checklists/
  templates/
  examples/
  guides/
  scripts/
  skill-factory/
  docs/
  logs/
  .github/workflows/
```

---

## Agent invocation protocol

1. Select the closest Skill under `skills/`.
2. Read `skills/<skill>/skill.json` first.
3. Read `SKILL.md` for scope and workflow.
4. Apply `checklist.md` and `scoring-rubric.md`.
5. Produce an audit report with `audit-report-template.md`.
6. Produce a refactor plan with `refactor-plan-template.md`.
7. Run validation if possible; otherwise record limits honestly.

See `docs/agent-invocation-protocol.md` for the full protocol. Use `docs/skill-routing-guide.md` to choose the right Skill, `docs/output-contract.md` to keep reports consistent, and `docs/multi-skill-composition-guide.md` when a project needs several Skills in one plan.

---

## Skill Factory

Create a new Skill skeleton:

```bash
python scripts/generate_factor_skill.py xx-factor-cli --title "xx-factor-cli" --category cli
```

Validate the repository:

```bash
python scripts/scan_factor_project.py .
```

Expected result:

```text
PASS: product-factor-skills validation passed
```



## Skill selector

When the request is broad, use the lightweight selector to recommend a primary Skill and useful secondary Skills:

```bash
python scripts/select_factor_skill.py "audit this RAG app for retrieval quality and regression tests" --root . --top 5
```

With a target project path:

```bash
python scripts/select_factor_skill.py "prepare this repo for release" --root . --target ./examples/sample-agent-project --json ./tmp/skill-selection.json --markdown ./tmp/skill-selection.md
```

See `docs/skill-selection-engine.md` and `examples/skill-selection-prompt.md`.

---

## Multi-Skill composer

When one project needs several review lenses, generate a composed review plan:

```bash
python scripts/compose_factor_review.py "prepare this Agent product for public release with security and observability" --root . --target ./examples/sample-agent-project --max-skills 4 --out ./tmp/composed-review
```

This creates `review-plan.md`, `review-plan.json`, and `handoff-prompt.md`. See `docs/multi-skill-composition-guide.md`.

---

## Audit runner

Prepare a repeatable audit package for a target project:

```bash
python scripts/run_skill_audit.py   --repo .   --target ./examples/sample-agent-project   --skill 12-factor-agents   --out ./tmp/agent-audit
```

This generates `audit-brief.md`, `audit-report.md`, `refactor-plan.md`, `validation-summary.md`, `decision-log.md`, and `audit-summary.json`. See `docs/skill-audit-runner.md`.

For projects that span multiple domains, use `docs/multi-skill-routing-matrix.md` to choose one primary Skill and optional secondary Skills.


---

## Prompt renderer

Render a complete one-shot prompt from any Skill folder:

```bash
python scripts/render_skill_prompt.py 13-factor-product-readiness --target ./my-repo --out ./tmp/product-readiness-prompt.md
```

Use this when you want to hand a full Skill pack to another Agent or repeat the same review in a new conversation.

---


## Skill catalog exporter

Generate a manifest-driven catalog for maintainers and Agents:

```bash
python scripts/export_skill_catalog.py . --markdown docs/generated-skill-catalog.md --json docs/generated-skill-catalog.json
```

Use `6-factor-docs` when README, guides, examples, release notes, and Agent handoff prompts need to become clear, accurate, and adoption-ready. Use `15-factor-observability` when logs, traces, validation summaries, release evidence, debugging UX, or Agent handoff artifacts are weak.

## Product readiness pass

When a repository is useful but still feels like a demo, start with:

```text
Use the 13-factor-product-readiness skill to audit this repository for launch readiness, onboarding, product polish, release discipline, Agent-native usage, and open-source credibility.
```

Then pair it with a domain-specific Skill such as `12-factor-agents`, `12-factor-app`, `10-factor-html`, `8-factor-github-actions`, `9-factor-rag`, `7-factor-mcp`, `11-factor-cli`, `6-factor-docs`, `14-factor-security-privacy`, or `15-factor-observability`.

---

## Release and validation

Before publishing a new version:

1. Update `VERSION`.
2. Update `CHANGELOG.md` and `RELEASE_NOTES.md`.
3. Update `logs/iteration-log.md`, `logs/file-manifest.md`, and `logs/version-history.md`.
4. Run `python scripts/scan_factor_project.py .`.
5. Zip the full repository, including `.github`.

See `docs/release-checklist.md`.

---

## Attribution

`12-factor-agents` is inspired by the HumanLayer 12-factor-agents project. This repository does not include upstream images or upstream source code; it packages the general idea into an Agent-callable Skill pack with checklists, scoring rubrics, refactor workflows, templates, and validation conventions. See `ATTRIBUTION.md`.

---

## Keywords

Factor Skill, Agent-native, reusable standards, project audit, project refactor, engineering checklist, release readiness, deployability, maintainability, Skill Factory, repeatable optimization.

标准化审查、可复用 Skill、Agent 原生、项目重构、工程清单、发布就绪、可部署、可维护、可扩展、技能工厂、反复优化。

---

## Status

`v0.9.0` adds `15-factor-observability`, a dependency-free multi-Skill composer, observability playbook, composed review template, and expanded validation for twelve bundled Skills.
