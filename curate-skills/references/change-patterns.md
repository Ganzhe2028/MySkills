# Change Patterns

Use these playbooks after deciding the action.

## Merge Playbook

1. Pick the survivor with the clearer trigger surface.
2. Copy every unique script, reference, and asset from the retiring skill into the survivor.
3. Rewrite the survivor's description so it names the combined intent directly.
4. Remove duplicated prose and keep only one workflow.
5. Delete the retiring skill after every unique resource is preserved.
6. Update existing docs, cross-links, and metadata that still mention the old name.

## Split Playbook

1. Split only when the child skills can trigger independently.
2. Give each child a different description and default prompt.
3. Move shared policy into the smaller common core only if the overlap remains real.
4. Move variant-specific procedures into each child's `references/` or `scripts/`.
5. Validate both children separately.

## Replace Or Remove Playbook

1. Check whether the base model already covers the skill's behavior with plain prompting.
2. Keep one short wrapper only if it still provides non-obvious workflow, tooling, or artifacts.
3. Delete decorative guidance that does not change behavior.
4. Remove the entire skill if nothing unique survives.

## Tighten Playbook

1. Rewrite the frontmatter description before expanding the body.
2. Rename the folder only when the current name harms triggering.
3. Cut sections that explain obvious model behavior.
4. Move detail-heavy material into `references/`.
5. Make `agents/openai.yaml` match the rewritten skill.

## Final Sweep

1. Re-run the inventory script on the whole skills directory.
2. Validate every changed skill.
3. Search for stale references to renamed or removed skills.
4. Report every keep, merge, split, replace, and remove decision with a concrete reason.
