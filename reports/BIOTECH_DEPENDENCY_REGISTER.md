# BHIV Dependency Register

## Purpose

This register identifies runtime, library, data, interface, and informational dependencies observed in the repository. It distinguishes verified dependencies from external assumptions.

## Repository Components

| Component | Type | Verified Dependencies | Interface |
|---|---|---|---|
| Scientific evidence tracker | Python CLI/library | Python standard library; local evidence CSV files | CSV input and JSON output |
| Evidence QC engine | Python CLI/library | Python standard library; JSON input file | JSON input and JSON output |
| React workflow workspace | Frontend UI | React, Vite, TypeScript, Zustand package availability | Browser state only |
| Evidence framework | Data/schema package | CSV and JSON files; JSON Schema documentation | File-based |

## Evidence Tracker Dependencies

| Dependency | Location | Required | Status |
|---|---|---|---|
| Evidence map | `evidence_framework/evidence_map.csv` | Yes | Verified |
| Claim traceability map | `evidence_framework/claim_traceability.csv` | Yes | Verified |
| Contradiction register | `evidence_framework/contradiction_register.csv` | Yes | Verified |
| Python runtime | System | Yes | Verified |
| External package | None observed | No | Not required |
| Network/API service | None observed | No | Not required |

The evidence tracker uses the Python standard library and writes `sample_implementation/sample_output.json`.

## QC Engine Dependencies

| Dependency | Location | Required | Status |
|---|---|---|---|
| Python runtime | System | Yes | Verified |
| Synthetic/structured evidence JSON | `data/synthetic_evidence.json` or caller-provided JSON | Yes | Verified |
| QC JSON Schema | `evidence_packet/code_packet/schema.json` | Recommended | Verified |
| External package | None observed | No | Not required |
| Network/API service | None observed | No | Not required |

CLI:

```powershell
python qc_engine\engine.py data\synthetic_evidence.json -o qc_output.json
```

## Frontend Dependencies

The React project depends on packages declared in `package.json`, including React, Vite, TypeScript, Zustand, and testing tools. The frontend build and Vitest suite are currently verifiable.

The frontend does not import or invoke the Python evidence tracker or QC engine.

## Cross-Component Dependencies

| Relationship | Current State | Dependency Required |
|---|---|---|
| Evidence tracker -> evidence CSVs | Direct file dependency | Local CSV files |
| Evidence tracker -> JSON output | Direct file creation | Local writable output directory |
| QC engine -> evidence JSON | Direct file/library dependency | JSON array matching its record contract |
| QC engine -> evidence tracker | None | Integration adapter would be required |
| React UI -> Python projects | None | HTTP API or separate bridge would be required |
| External API client -> repository | None | HTTP service implementation would be required |

## External and Informational Dependencies

| Item | Status | Treatment |
|---|---|---|
| Final Test Task 1 evaluation | Unavailable locally | Preserve as informational unknown |
| Exact authoritative BHIV source pack | Not confirmed locally | Do not substitute assumptions |
| Final reviewer-specific requirements | Not yet received | Preserve as pending external input |
| Hosted deployment environment | Not present | Deployment proof is not applicable |
| Laboratory or clinical data | Not required for current scope | Outside system boundary |

## Dependency Risks

- Duplicate implementations of the QC engine exist at `qc_engine/engine.py` and `evidence_packet/code_packet/engine.py`; synchronization is required.
- Duplicate evidence-tracker implementations exist at `code_packet/evidence_tracker.py` and `evidence_packet/code_packet/evidence_tracker.py`; synchronization is required.
- The evidence-tracker CSV schema and QC-engine JSON schema are distinct contracts.
- The React UI has no network dependency and no live data dependency.

## Dependency Conclusion

The repository is internally runnable with local files and Python/Node tooling. It has no verified external runtime API dependency and no verified live integration between the React UI and Python components.
