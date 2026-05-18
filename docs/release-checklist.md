# Release Checklist

Use this before publishing a new zip or GitHub release.

## Version

- [ ] `VERSION` is updated.
- [ ] `CHANGELOG.md` has the new version entry.
- [ ] `RELEASE_NOTES.md` has the new release notes.
- [ ] `logs/version-history.md` records the new version.

## Structure

- [ ] Every Skill has all required files.
- [ ] Every Skill has `skill.json`.
- [ ] `product-factor-skills.json` and `skills.json` are updated.
- [ ] `.github/workflows/validate.yml` exists.

## Validation

- [ ] `python scripts/scan_factor_project.py .` passes.
- [ ] README keywords are present.
- [ ] Hidden directories such as `.github` are included in the zip.

## Packaging

- [ ] Zip name follows `product-factor-skills-vX.Y.Z.zip`.
- [ ] Zip contains the full repository, not only changed files.


## Release zip build

```bash
python scripts/build_release_zip.py . --out ../product-factor-skills-$(cat VERSION).zip
```

Then verify:

```bash
unzip -t ../product-factor-skills-$(cat VERSION).zip
```
