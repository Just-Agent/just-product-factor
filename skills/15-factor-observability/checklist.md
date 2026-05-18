# 15-factor-observability Checklist

## 1. Runtime map

- [ ] README 或 docs 说明关键运行路径。
- [ ] CLI、服务、Agent workflow、RAG pipeline、MCP server 或 CI/CD 的入口清楚。
- [ ] 关键依赖、外部服务、环境变量和数据输入清楚。

## 2. Structured logging

- [ ] 日志有级别：debug / info / warn / error。
- [ ] 日志包含 operation、step、duration、status、error 等字段。
- [ ] 长任务有 start / progress / completed / failed 信息。
- [ ] Agent tool call、RAG retrieval、MCP tool invocation 有可追踪记录。

## 3. Actionable errors

- [ ] 常见失败有明确错误信息。
- [ ] 错误信息包含下一步动作。
- [ ] 配置缺失、权限不足、网络失败、输入无效有专门提示。
- [ ] 错误不会只输出 stack trace。

## 4. Metrics

- [ ] 有基础计数：runs、successes、failures。
- [ ] 有耗时信息：build time、request latency、tool call duration、retrieval latency。
- [ ] 有质量信号：test pass rate、evaluation score、retrieval hit rate、coverage。
- [ ] 指标口径在 docs 中说明。

## 5. Tracing and correlation

- [ ] 单次运行有 run id / request id / trace id。
- [ ] Agent step、tool call、workflow job 可以关联到同一次运行。
- [ ] CI/CD artifact 可以关联 commit、version、workflow run。
- [ ] 审查报告可以关联输入版本和验证命令。

## 6. Artifacts

- [ ] 有 validation summary。
- [ ] 有 audit report。
- [ ] 有 refactor plan。
- [ ] 有 decision log。
- [ ] 失败样例、截图、日志片段或测试输出能保存到 artifacts 或 logs。

## 7. Privacy-safe observability

- [ ] 日志不泄露 tokens、API keys、cookies、passwords。
- [ ] 日志不默认保存用户敏感数据或完整 prompt。
- [ ] sample data 已脱敏。
- [ ] debug 模式和默认模式边界清楚。

## 8. User and maintainer debugging UX

- [ ] issue 模板要求提供版本、环境、命令、输入摘要、错误输出。
- [ ] docs 有 troubleshooting 章节。
- [ ] README 有验证命令。
- [ ] CI 失败信息可读。

## 9. Release visibility

- [ ] Release notes 记录验证结果。
- [ ] CHANGELOG 记录影响运行和诊断体验的变化。
- [ ] CI workflow 产出可下载或可读的验证摘要。

## 10. Agent handoff readiness

- [ ] Agent 可以根据日志继续定位问题。
- [ ] Agent 可以读取 audit summary / validation summary 继续迭代。
- [ ] 产物路径稳定，便于下一轮复用。
