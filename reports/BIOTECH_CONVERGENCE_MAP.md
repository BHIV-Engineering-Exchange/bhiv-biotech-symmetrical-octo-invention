# BHIV Convergence Map

## Purpose

This map identifies which repository components are converged, where interfaces differ, and what is required for cross-project communication.

## Component Readiness

| Component | Execution | Data Contract | External API | Overall |
|---|---|---|---|---|
| Evidence tracker | Verified | CSV + JSON | None | Operational standalone |
| QC engine | Verified | JSON in + JSON out | None | Operational standalone |
| Evidence framework | Verified | CSV/JSON/JSON Schema | None | Operational dataset and documentation |
| React workflow UI | Verified | Browser state | None | Operational standalone demo |

## Interface Convergence

| Source | Target | Direct Link | Compatibility | Required Work |
|---|---|---|---|---|
| Evidence CSVs | Evidence tracker | Yes | Native | None |
| Evidence tracker | Evidence JSON output | Yes | Native JSON | None |
| Synthetic JSON | QC engine | Yes | Native JSON array | None |
| QC engine | QC JSON output | Yes | Native JSON object | None |
| Evidence tracker | QC engine | No | Not compatible directly | Record adapter |
| QC engine | Evidence tracker | No | Not compatible directly | Result adapter |
| React UI | QC engine | No | No network contract | HTTP API or IPC bridge |
| React UI | Evidence tracker | No | No network contract | HTTP API or shared service |

## Schema Convergence

### Evidence Framework

The evidence framework uses evidence-oriented fields:

- `evidence_id`
- `source_id`
- `concept`
- `evidence_category`
- `evidence_strength`
- `limitations`
- `contradiction_status`
- `provenance`
- `version`

The CSV evidence map uses a flatter representation and does not exactly match the full reusable JSON Schema.

### QC Engine

The QC engine uses processing-oriented fields:

- `schema_version`
- `study_id`
- `source`
- `protocol_reference`
- `measurement_method`
- `method_validation_status`
- `raw_data_availability`
- `missing_data`
- `deviations`
- `reviewer_status`
- `evidence_quality`
- `final_review_status`

These fields are not equivalent to the evidence-framework fields and require transformation when exchanging records.

## Convergence Levels

| Level | Components | Result |
|---|---|---|
| Local execution | Evidence tracker | Converged |
| Local execution | QC engine | Converged |
| Frontend build/runtime | React UI | Converged |
| In-process Python integration | Tracker and QC engine | Not converged |
| File integration | CSV evidence data and QC JSON | Not converged |
| Network integration | React UI and Python projects | Not converged |

## Recommended Convergence Sequence

1. Define a versioned shared envelope for evidence identifiers and source lineage.
2. Add a documented adapter that translates evidence records into QC input records.
3. Add a mapping that preserves evidence tracker identifiers in QC output.
4. Expose a small synchronous HTTP API only if external communication is a requirement.
5. Add React API calls and loading/error states only after the HTTP contract is verified.
6. Add end-to-end tests for each adapter and network boundary.

## Conclusion

The repository contains multiple independently usable components, but it is not an integrated application. Communication exists only at local Python and file boundaries; no verified cross-project communication contract currently exists.
