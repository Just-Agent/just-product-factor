# 15-factor-observability Skill

## Skill 名称

15-factor-observability

## 适用场景

Use this Skill when a product, Agent, app, RAG system, MCP server, CLI, workflow, or service needs clearer runtime visibility, logs, metrics, traces, audit artifacts, failure diagnostics, and operator handoff.

适用于这些情况：

- 项目能运行，但失败后不知道发生了什么。
- Agent 有工具调用、长任务、异步任务、RAG 检索、MCP 调用或 CI/CD 工作流，但缺少可追踪证据。
- README 写了功能，但没有说明如何观察运行状态、定位错误、复现问题。
- 开源项目要发布，需要基础日志、调试信息、验证产物和 issue 诊断路径。
- 需要把一次 Agent 优化过程变成可复盘的审查记录。

## 不适用场景

- 只需要概念解释，不需要审查项目。
- 项目仍处于纯草稿阶段，连最小运行路径都不存在。
- 用户只关心视觉样式或文案，此时优先使用 `10-factor-html` 或 `6-factor-docs`。

## 输入要求

优先读取：

- README、quickstart、docs、examples
- 源码中的日志、错误处理、运行入口、配置文件
- CI/CD workflow、测试脚本、release 脚本
- Agent trace、tool call 记录、RAG 检索日志、MCP tool schema
- issue 模板、bug report 模板、validation summary、audit report
- 运行失败日志或用户报告的问题

## 工作流程

1. 明确系统的关键运行路径和用户承诺。
2. 找出失败点：安装、配置、命令、网络、权限、工具调用、数据输入、部署、发布。
3. 检查日志是否结构化、可定位、可脱敏、可复现。
4. 检查 metrics / traces / run artifacts 是否覆盖关键路径。
5. 检查 Agent、RAG、MCP、CI/CD 是否留下足够审计证据。
6. 使用 `checklist.md` 做逐项审查。
7. 使用 `scoring-rubric.md` 评分。
8. 使用 `audit-report-template.md` 输出审查报告。
9. 使用 `refactor-plan-template.md` 输出分阶段改造计划。
10. 如涉及安全、隐私或敏感日志，联动 `14-factor-security-privacy`。

## 审查维度

1. Runtime map：关键运行路径是否清楚。
2. Structured logging：日志是否结构化、分级、可搜索。
3. Error diagnostics：错误是否可行动、可复现。
4. Metrics：是否有基础计数、耗时、失败率和吞吐指标。
5. Tracing：是否能串起请求、Agent step、tool call、workflow job。
6. Artifacts：是否保存审查报告、运行摘要、验证结果、失败样例。
7. Privacy-safe observability：日志是否避免泄露 secrets、PII、tokens、prompt 原文。
8. Debug UX：用户和维护者是否知道如何提交有用 bug report。
9. CI/release visibility：自动化流程是否产出可读验证结果。
10. Agent handoff visibility：Agent 是否能基于日志和产物继续迭代。

## 评分方式

使用 0-5 分：

- 0：完全缺失。
- 1：有零散日志，但不可复现。
- 2：有基本日志和错误信息，但缺少结构和关键路径覆盖。
- 3：覆盖主要路径，有基础验证产物。
- 4：日志、指标、trace、产物、issue 诊断路径基本完整。
- 5：可发布级 observability，支持用户、维护者和 Agent 持续定位问题。

## 重构优先级

优先级顺序：

1. 先让失败可见：安装、运行、测试、构建、核心命令。
2. 再让失败可定位：错误码、上下文、建议修复动作。
3. 再让运行可复盘：audit summary、validation summary、decision log。
4. 再让系统可度量：耗时、次数、失败率、覆盖率。
5. 最后接入更高级 tracing / dashboards / release reporting。

## 输出格式

输出必须包含：

- Observability diagnosis
- 15-factor scorecard
- Critical blind spots
- Recommended logs / metrics / traces / artifacts
- Privacy-safe logging notes
- Refactor plan
- Validation plan
- Paired Skill recommendations

## 示例调用

```text
Use the 15-factor-observability skill to audit this Agent project for logs, traces, tool-call evidence, validation artifacts, and debuggability.
```

```text
Use the 15-factor-observability skill with 14-factor-security-privacy to make this app easier to debug without leaking secrets or user data.
```

## 版本记录

v0.9.0：首次加入 observability 标准，用于补齐运行可见性、失败诊断、审查产物和 Agent handoff 证据。
