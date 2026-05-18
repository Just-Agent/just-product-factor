# Skill Catalog Exporter

`scripts/export_skill_catalog.py` generates a catalog from every `skills/*/skill.json` manifest.

Use it when you want a single human-readable index for maintainers and a machine-readable catalog for Agents.

## Command

```bash
python scripts/export_skill_catalog.py . --markdown docs/generated-skill-catalog.md --json docs/generated-skill-catalog.json
```

## Outputs

- `docs/generated-skill-catalog.md`: table of Skill names, categories, summaries, and trigger phrases.
- `docs/generated-skill-catalog.json`: machine-readable catalog with all manifest fields.

## Recommended release use

Run the exporter before release when you add, rename, or significantly change a Skill. The exported files can be committed when you want a static catalog, or generated in CI as a validation artifact.
