# Governance — mirrornode-index

## Decision Authority
Index entries must reflect actual repo state. Changes that add, remove, or reclassify repos require review.

## Branch Model
- main — canonical index state.
- Structural updates should use pull requests.
- Minor reference updates may be direct only when authorized.

## Prohibited Actions
- Do not list repos that do not exist or cannot be verified.
- Do not mark a repo production without deployment evidence.
- Do not mark a repo deprecated without a corresponding note or governance record.
- Do not commit secrets.

## Documentation Priority
If repository structure, runtime behavior, deployment configuration, or system contracts differ from documentation, the discrepancy must be corrected.

Documentation describes reality; reality does not change to satisfy documentation.
