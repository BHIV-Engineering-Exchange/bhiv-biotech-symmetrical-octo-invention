# BHIV Biosimilarity & Preclinical Evidence QC Engine
# Technical Gap Register

## 1. Document Overview

| Attribute | Details |
|---|---|
| Project | BHIV Biosimilarity & Preclinical Evidence QC Engine |
| Engine Version | 1.0.0 |
| Schema Version | 1.0.0 |
| Dataset | Synthetic |
| Processing Model | One-time command-line execution |
| Records Processed | 11 |
| Output Generation | Successful |
| Document Type | Technical Gap Register |

## 2. Purpose

This document identifies technical limitations, operational boundaries, and potential improvement areas for the BHIV Biosimilarity & Preclinical Evidence QC Engine.

The project currently provides deterministic QC processing for structured evidence records.

The gap register focuses on:

- Execution architecture.
- API and batch-processing separation.
- Synthetic-data limitations.
- Human-review workflow.
- QC classification interpretation.
- Evidence validation.
- Output management.
- Testing and repeatability.
- Operational traceability.

This document does not assess scientific biosimilarity, safety, efficacy, interchangeability, or regulatory approval.

## 3. Current System Baseline

The following capabilities are documented.

| Component | Current Status |
|---|---|
| Engine version | 1.0.0 |
| Schema version | 1.0.0 |
| CLI execution | Available |
| Input format | JSON |
| Output format | JSON |
| Schema validation | Supported |
| Required-field validation | Supported |
| Evidence completeness checks | Supported |
| Duplicate detection | Supported |
| Conflict detection | Supported |
| Evidence-quality classification | Supported |
| Human-review routing | Supported |
| Candidate/reference comparison | Supported |
| Synthetic-data protection | Supported |
| Deterministic repeatability testing | Supported |
| Reported records processed | 11 |
| Output file writing | Successful |
| Evidence tracker interfaces | Python functions, CSV input, JSON output |
| React/Python integration | Not implemented |
| HTTP API implementation | Not found in source |
| Cross-project adapter | Not implemented |
| Frontend build | Successful |
| Frontend tests | 6 passed |
| Python tests | 24 passed |

## 4. Gap Register

### GAP-01: One-Time Execution Architecture

**Category:** Execution and Operations

**Current State:**

The QC engine operates as a command-line script.

It is started using:

```powershell
python qc_engine\engine.py data\synthetic_evidence.json -o evidence_packet\api_samples\qc_output.json
```

The engine processes the supplied dataset, writes the output file, and terminates normally.

**Identified Limitation:**

The engine does not continuously run as a background process.

Each new dataset requires another command execution.

**Impact:**

- Processing is dependent on manual command execution or an external orchestration mechanism.
- There is no established continuous processing lifecycle.
- Repeated processing requires separate executions.

**Recommended Improvement:**

Document the batch execution model clearly and introduce scheduling or orchestration only if recurring automated processing becomes a requirement.

**Priority:** P2

**Status:** Documented architectural boundary.

---

### GAP-02: API and Engine Execution Separation

**Category:** Application Architecture

**Current State:**

A web API endpoint may be included in the project, while the QC engine itself is executed through a Python command.

**Identified Limitation:**

The API endpoint and the command-line processing engine must not be assumed to have the same execution lifecycle.

The supplied information does not establish that the API automatically invokes the engine or provides continuous processing.

**Impact:**

- API availability may be misunderstood as evidence of engine availability.
- Users may assume the engine continuously processes incoming requests.
- The API-to-engine integration boundary requires explicit documentation.

**Recommended Improvement:**

Document separately:

1. Web API responsibilities.
2. Command-line engine responsibilities.
3. Input and output interfaces.
4. Whether an API request invokes a separate engine process.
5. Whether processing is synchronous or asynchronous.

Do not claim API-driven execution until verified in the source code.

**Priority:** P1

**Status:** Verified boundary: no HTTP API or React/Python integration is present.

---

### GAP-03: Synthetic Dataset Limitation

**Category:** Data Quality and Evidence

**Current State:**

The project uses a synthetic dataset labelled:

`SAMPLE / SYNTHETIC / FOR SOFTWARE TESTING`

The engine successfully processed 11 records.

**Identified Limitation:**

Synthetic records cannot demonstrate the validity of real experimental or preclinical evidence.

**Impact:**

- The output demonstrates software processing behavior only.
- Results cannot establish scientific validity.
- Dataset completeness does not establish the reliability of actual scientific observations.

**Recommended Improvement:**

Maintain explicit synthetic-data labelling in:

- Input datasets.
- Generated output files.
- Reports.
- API responses, where applicable.
- Test documentation.

Any future use of real evidence should require a separately defined data-governance and review process.

**Priority:** P1

**Status:** Existing limitation; synthetic-data boundary documented.

---

### GAP-04: VERIFIED Status and Human Review Separation

**Category:** QC Classification and Review Workflow

**Current State:**

The engine supports the `VERIFIED` evidence-quality state.

However, a record may still contain:

```json
{
  "evidence_quality": "VERIFIED",
  "human_review_required": true,
  "reviewer_status": "NOT REVIEWED",
  "final_review_status": "OPEN"
}
```

**Identified Limitation:**

The VERIFIED classification can be misunderstood as final scientific validation.

**Impact:**

- Users may interpret QC completeness as scientific equivalence.
- Users may overlook pending human review.
- The record may be incorrectly treated as final.

**Recommended Improvement:**

Maintain separate QC and human-review indicators.

The system should clearly communicate:

- VERIFIED means QC completeness.
- Human review remains required when specified.
- NOT REVIEWED indicates that a reviewer has not completed the review.
- OPEN indicates that final review is pending.

The user interface and generated reports should display these states independently.

**Priority:** P1

**Status:** Important interpretation boundary documented.

---

### GAP-05: Human Review Completion

**Category:** Review Workflow

**Current State:**

The engine supports the following reviewer statuses:

- NOT REVIEWED
- IN REVIEW
- REVIEWED
- REQUIRES SECOND REVIEW
- CLOSED

It also supports final-review statuses:

- OPEN
- IN REVIEW
- REQUIRES REVISION
- READY FOR HUMAN REVIEW
- REVIEWED
- CLOSED

**Identified Limitation:**

The supplied example remains in the following state:

- `reviewer_status`: NOT REVIEWED
- `final_review_status`: OPEN
- `human_review_required`: true

Therefore, human review has not been completed.

**Impact:**

The record cannot be treated as having completed its review lifecycle.

**Recommended Improvement:**

A human reviewer should assess the record and update the review statuses through the appropriate review process.

Any transition to a final review state should be supported by an actual human review rather than automatic QC classification.

**Priority:** P1

**Status:** Pending human review for the supplied example.

---

### GAP-06: Evidence Completeness Versus Scientific Validation

**Category:** Validation Scope

**Current State:**

The engine performs schema validation, required-field checks, and evidence completeness assessment.

**Identified Limitation:**

Structural completeness does not establish the scientific validity or reliability of evidence.

**Impact:**

A structurally complete record may still require scientific assessment.

**Recommended Improvement:**

Maintain a clear separation between:

1. Software-level structural validation.
2. Evidence completeness assessment.
3. Human review.
4. Scientific interpretation.

The engine should not present QC completeness as a scientific conclusion.

**Priority:** P1

**Status:** Scope limitation documented.

---

### GAP-07: Candidate/Reference Comparison Boundaries

**Category:** Data Processing

**Current State:**

The engine supports candidate/reference field comparison.

**Identified Limitation:**

Structured field comparison does not independently establish biological or clinical equivalence.

**Impact:**

Comparison results may be incorrectly interpreted as proof of biosimilarity.

**Recommended Improvement:**

Clearly label comparison results as structured data-level comparisons.

Do not use them to determine biosimilarity, interchangeability, safety, efficacy, or regulatory approval.

**Priority:** P1

**Status:** Scientific boundary documented.

---

### GAP-08: Batch Execution Traceability

**Category:** Execution Monitoring

**Current State:**

The engine successfully processed 11 records, wrote the output file, and terminated normally.

**Identified Limitation:**

The supplied execution information does not establish the availability of a persistent execution-history or monitoring mechanism.

**Impact:**

It may be difficult to compare separate executions without retaining execution metadata.

**Recommended Improvement:**

Consider recording the following for each execution:

- Execution timestamp.
- Input filename.
- Number of records received.
- Number of records processed.
- Output filename.
- Engine version.
- Schema version.
- Execution completion status.

**Priority:** P2

**Status:** Improvement opportunity; existing logging implementation not verified.

---

### GAP-09: Output Versioning and Traceability

**Category:** Output Management

**Current State:**

The engine writes the generated output to:

`evidence_packet/api_samples/qc_output.json`

**Identified Limitation:**

The supplied information does not establish whether previous outputs are retained or whether output files are versioned.

**Impact:**

Repeated executions may make historical comparison difficult if the same output path is reused.

**Recommended Improvement:**

Consider retaining execution-specific output files or maintaining a separate execution history.

Input and output references should remain traceable to the corresponding engine and schema versions.

**Priority:** P2

**Status:** Retention and versioning behavior not verified.

---

### GAP-10: Deterministic Repeatability Evidence

**Category:** Testing and Reliability

**Current State:**

Deterministic repeatability testing is a documented engine capability.

**Identified Limitation:**

The supplied execution information confirms one successful run but does not provide the results of multiple independent repeatability runs.

**Impact:**

A single successful execution does not independently demonstrate repeatability.

**Recommended Improvement:**

Run the engine multiple times using the same input and configuration.

Compare the resulting QC outputs and document whether they are identical.

**Priority:** P2

**Status:** Capability documented; execution evidence not supplied.

---

### GAP-11: API Operational Behavior

**Category:** API Integration

**Current State:**

A web API endpoint may exist in the project.

The primary QC execution method remains the command-line script.

**Identified Limitation:**

The supplied information does not confirm:

- Whether the endpoint is currently running.
- Whether it invokes the QC engine.
- Whether it accepts evidence records.
- Whether it returns QC output.
- Whether it supports repeated requests.

**Impact:**

The API's operational capabilities cannot be established from the engine execution result alone.

**Recommended Improvement:**

Document and test API behavior independently from command-line execution.

Avoid claiming that the API provides continuous QC processing unless that behavior is verified.

**Priority:** P2

**Status:** API implementation details not verified.

---

## 5. Priority Summary

| Priority | Gap | Area |
|---|---|---|
| P1 | GAP-02 | API and engine separation |
| P1 | GAP-03 | Synthetic dataset limitations |
| P1 | GAP-04 | VERIFIED versus human review |
| P1 | GAP-05 | Human review completion |
| P1 | GAP-06 | Structural versus scientific validation |
| P1 | GAP-07 | Candidate/reference comparison boundaries |
| P2 | GAP-01 | One-time execution architecture |
| P2 | GAP-08 | Batch execution traceability |
| P2 | GAP-09 | Output versioning |
| P2 | GAP-10 | Repeatability evidence |
| P2 | GAP-11 | API operational verification |

## 6. Recommended Action Plan

### Phase 1: Documentation and Interpretation

1. Document the one-time command-line execution model.
2. Clearly separate API responsibilities from engine execution.
3. Preserve synthetic-data labelling.
4. Explain the meaning of VERIFIED.
5. Document the pending human-review requirement.

### Phase 2: Operational Improvements

1. Improve execution traceability.
2. Consider output versioning.
3. Document API behavior separately.
4. Maintain engine and schema version information.

### Phase 3: Testing Improvements

1. Perform repeatability testing.
2. Compare outputs across independent runs.
3. Verify API behavior independently.
4. Maintain execution evidence and test results.

## 7. Important Scientific and Regulatory Boundaries

The QC engine does NOT determine:

- Biosimilarity.
- Clinical equivalence.
- Interchangeability.
- Safety.
- Efficacy.
- Regulatory approval.
- Therapeutic effectiveness.

Its responsibility is limited to software-based quality-control classification, structured record validation, and review routing.

Synthetic data must not be interpreted as actual scientific evidence.

## 8. Overall Gap Assessment

The project has a documented QC processing workflow and a successful reported execution involving 11 synthetic records.

The principal areas requiring attention are the separation of API and command-line execution, clear interpretation of QC classifications, human-review completion, and improved execution traceability.

The most important distinction is that a record marked `VERIFIED` may still require human review.

The example record remains open because:

- `human_review_required` is `true`.
- `reviewer_status` is `NOT REVIEWED`.
- `final_review_status` is `OPEN`.

This is a valid distinction between software QC completeness and completion of the human-review process.

The current implementation should be represented as a deterministic, one-time batch-processing QC script rather than a continuously running scientific