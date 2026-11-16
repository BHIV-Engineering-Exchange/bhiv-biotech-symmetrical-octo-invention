# BHIV Biosimilarity & Preclinical Evidence QC Engine
# Technical Audit Report

## 1. Project Overview

| Attribute | Details |
|---|---|
| Project | BHIV Biosimilarity & Preclinical Evidence QC Engine |
| Engine Version | 1.0.0 |
| Schema Version | 1.0.0 |
| Audit Type | Technical and Structural Audit |
| Execution Type | One-time command-line execution |
| Dataset Type | Synthetic Data |
| Records Processed | 11 |
| Output | JSON QC evidence packet |
| Execution Result | Successfully completed |
| Scientific Validation | Not performed |

## 2. Executive Summary

The BHIV Biosimilarity & Preclinical Evidence QC Engine is a deterministic software-based quality-control system designed to validate structured biosimilarity and preclinical evidence records.

The system focuses on checking the structural completeness, consistency, and quality of submitted evidence records.

The engine provides:

- Record structure, required-field, and status-value checks.
- Required-field validation.
- Evidence completeness checks.
- Duplicate detection.
- Conflict detection.
- Evidence-quality classification.
- Human-review routing.
- Candidate/reference field comparison through a separate helper.
- Synthetic-data declaration validation.
- Deterministic processing, with a repeatability test in the test suite.

The engine successfully processed 11 records, generated the QC output file, and terminated normally.

The application operates as a command-line script. Each execution processes the supplied input dataset once, writes the output, and exits. It is not a continuously running engine.

The reviewed source contains a React workflow demo and a Python command-line engine. No web API endpoint or connection from the React UI to the Python engine was found.

## 3. Audit Scope

This audit covers the following areas:

1. Project purpose and functionality.
2. Execution architecture.
3. Application entry points.
4. Input and output handling.
5. Record validation.
6. Evidence-quality classification.
7. Human-review requirements.
8. Synthetic-data handling.
9. Execution behavior.
10. Technical limitations and improvement areas.

The audit included a review of the relevant source files and one successful command-line run. Scientific and regulatory validity were not assessed.

## 4. System Architecture

### 4.1 Architecture Overview

The system follows a command-driven processing architecture.

The primary workflow is:

Input Dataset → Command-Line Entry Point → QC Processing Engine → Validation and Quality Checks → Classification and Review Routing → JSON Output File → Process Termination

### 4.2 Architecture Components

#### A. Input Dataset Layer

The input layer provides structured evidence records in JSON format.

Input file:

`data/synthetic_evidence.json`

The included dataset is explicitly labelled:

`SAMPLE / SYNTHETIC / FOR SOFTWARE TESTING`

The dataset is intended for software testing and validation.

It must not be interpreted as real experimental, clinical, or preclinical scientific evidence.

#### B. Command-Line Entry Point

The primary execution entry point is:

`qc_engine/engine.py`

The engine is started through a Python command that accepts:

- Input JSON file.
- Output file location through the `-o` argument.

The script is responsible for initiating the QC processing workflow.

#### C. QC Processing Engine

The processing engine performs deterministic quality-control operations on the supplied records.

Its documented responsibilities include:

- Record structure, required-field, and status-value checks.
- Required-field checks.
- Evidence completeness assessment.
- Duplicate detection.
- Conflict detection.
- Evidence-quality classification.
- Human-review routing.

The separate `compare_candidate_reference()` helper compares selected fields, but the batch command does not call that helper.

The engine evaluates whether submitted records satisfy configured software QC checks.

#### D. Classification and Review Layer

The engine assigns one of the following evidence-quality states:

- VERIFIED
- PARTIAL
- NEEDS REVIEW
- CONFLICTING
- INSUFFICIENT

It also maintains reviewer and final-review statuses.

These statuses support quality-control tracking and human-review workflows.

#### E. Output Layer

The engine writes the processed results into a JSON output file.

Configured output path:

`evidence_packet/api_samples/qc_output.json`

The output contains the QC processing results.

The generated output represents a software quality-control assessment and must not be treated as a scientific determination.

#### F. Process Termination

After processing the supplied records and writing the output file, the command-line process terminates normally.

There is no indication from the supplied execution information that the engine remains active in the background.

Each new processing run requires another command execution.

## 5. Application Entry Points

### 5.1 Primary Entry Point

**File:** `qc_engine/engine.py`

This is the documented command-line execution entry point.

It accepts an input dataset and an output destination.

### 5.2 Input Entry Point

**File:** `data/synthetic_evidence.json`

This is the supplied synthetic evidence dataset used for processing.

### 5.3 Output File

**File:** `evidence_packet/api_samples/qc_output.json`

This is the output path used in the example command. It is not an application entry point.

### 5.4 Command-Line Execution

The application can be executed using PowerShell.

```powershell
python qc_engine\engine.py data\synthetic_evidence.json -o evidence_packet\api_samples\qc_output.json
```

The command performs the following operations:

1. Starts the Python QC engine.
2. Loads the synthetic evidence JSON file.
3. Processes the supplied records.
4. Performs the configured QC checks.
5. Generates evidence-quality classifications.
6. Determines human-review routing requirements.
7. Writes the JSON output file.
8. Terminates the process.

### 5.5 Execution Model

The application follows a one-command, one-execution model.

| Execution Property | Observed Behavior |
|---|---|
| Execution method | Python command |
| Execution frequency | Once per command |
| Input | JSON dataset |
| Processing | Batch-based |
| Records processed | 11 |
| Output generation | Successful |
| Process termination | Normal |
| Continuous execution | No |
| Background processing | Not established |
| Scheduled execution | Not established |

The system should therefore be documented as a one-time batch-processing script rather than a continuously running application.

## 6. Core Functional Capabilities

### 6.1 Schema-Aligned Validation

The engine validates evidence records against the configured schema.

Engine Version: `1.0.0`

Schema Version: `1.0.0`

This provides a structured basis for evaluating whether records follow the expected data format.

### 6.2 Required-Field Checks

The engine checks whether required information is present in the submitted records.

Missing required information can affect the QC classification.

### 6.3 Evidence Completeness Checks

The engine evaluates whether the expected evidence fields and supporting information are available.

This is a completeness assessment, not an assessment of scientific validity.

### 6.4 Duplicate Detection

The engine includes duplicate detection to identify repeated evidence records.

This supports dataset quality and prevents repeated records from being treated as independent entries without appropriate review.

### 6.5 Conflict Detection

The engine checks for conflicting information within the submitted evidence records.

Conflicts can affect the assigned evidence-quality state and human-review requirements.

### 6.6 Candidate/Reference Field Comparison

The engine performs structured comparisons between candidate and reference fields.

This is a data-level comparison only.

It does not establish that a candidate product is biologically or clinically equivalent to a reference product.

### 6.7 Deterministic Processing

The engine is designed to produce repeatable QC results when processing the same input under the same configuration.

Deterministic repeatability supports software testing and reproducibility.

## 7. Evidence Quality Classification

The engine supports five evidence-quality states.

| Status | Description |
|---|---|
| VERIFIED | QC requirements for the record have been satisfied according to the configured checks. |
| PARTIAL | The record has incomplete QC information. |
| NEEDS REVIEW | Additional assessment is required. |
| CONFLICTING | Conflicting information has been detected. |
| INSUFFICIENT | Available information is insufficient for the configured QC requirements. |

### Important Interpretation of VERIFIED

A record marked `VERIFIED` must not automatically be considered scientifically validated.

In this system, VERIFIED refers to QC completeness.

It does not indicate:

- Biosimilarity.
- Clinical equivalence.
- Safety.
- Efficacy.
- Interchangeability.
- Regulatory approval.

A record can be structurally complete and still require human review.

## 8. Human Review and Final Review Status

The system maintains separate reviewer and final-review status fields.

### 8.1 Reviewer Status Values

- NOT REVIEWED
- IN REVIEW
- REVIEWED
- REQUIRES SECOND REVIEW
- CLOSED

### 8.2 Final Review Status Values

- OPEN
- IN REVIEW
- REQUIRES REVISION
- READY FOR HUMAN REVIEW
- REVIEWED
- CLOSED

### 8.3 Important QC Observation

The following record state is possible:

```json
{
  "evidence_quality": "VERIFIED",
  "human_review_required": true,
  "reviewer_status": "NOT REVIEWED",
  "final_review_status": "OPEN"
}
```

This is not necessarily an inconsistency.

The record can satisfy the configured software QC completeness requirements while still awaiting human review.

The interpretation is:

- `VERIFIED`: QC completeness requirements have been satisfied.
- `human_review_required: true`: Human review is still required.
- `reviewer_status: NOT REVIEWED`: No reviewer has completed the assessment.
- `final_review_status: OPEN`: The final review process remains open.

Therefore, the evidence record is structurally sound and complete enough for QC, but it still needs a human reviewer before it is considered final.

## 9. Synthetic Data Assessment

The project uses synthetic data.

Dataset classification:

`SAMPLE / SYNTHETIC / FOR SOFTWARE TESTING`

The synthetic dataset is intended to demonstrate and test:

- JSON record handling.
- Schema validation.
- Required-field checks.
- Evidence completeness.
- Duplicate detection.
- Conflict detection.
- Quality classification.
- Human-review routing.
- Repeatability.

### Synthetic Data Restrictions

The dataset must not be represented as:

- Actual clinical evidence.
- Actual preclinical study results.
- Real biosimilarity evidence.
- Verified experimental findings.
- Evidence of therapeutic performance.

The results demonstrate software behavior only.

## 10. API and Execution Architecture Clarification

A web API endpoint may be included in the project.

However, the presence of an API endpoint should not be confused with the actual execution lifecycle of the QC engine.

The documented engine execution is:

- Started through a Python command.
- Processes the supplied records.
- Writes the output file.
- Terminates normally.

The engine is not documented as a persistent API server.

The API endpoint and the one-time execution engine should be treated as separate architectural concerns unless their integration is independently verified from the source code.

No claim is made that the engine continuously accepts requests or processes records in the background.

## 11. Execution Verification Summary

Based on the supplied execution information:

| Verification Item | Result |
|---|---|
| Python engine execution | Successful |
| Input dataset processing | Successful |
| Records processed | 11 |
| QC processing | Completed |
| Output file generation | Successful |
| Output file writing | Successful |
| Process termination | Normal |
| Continuous engine execution | Not applicable |
| Scientific validation | Not performed |

### Execution Conclusion

The engine successfully processed 11 records, generated the expected output file, and terminated normally.

This confirms the reported batch-execution workflow.

It does not independently establish the scientific validity of the synthetic evidence.

## 12. Technical Limitations and Boundaries

The following boundaries are important when interpreting the project.

1. The dataset is synthetic.
2. The engine performs software QC rather than scientific validation.
3. VERIFIED represents QC completeness only.
4. Human review remains a separate requirement.
5. The engine runs once per command.
6. The engine terminates after processing the input.
7. The React demo does not call the Python engine.
8. Candidate/reference comparison is limited to structured field comparison.
9. QC classifications must not be treated as regulatory conclusions.

## 13. Audit Findings

| ID | Finding | Assessment |
|---|---|---|
| AUD-01 | Synthetic dataset is explicitly identified. | Documented |
| AUD-02 | Engine and schema versions are defined. | Documented |
| AUD-03 | Command-line entry point is identified. | Documented |
| AUD-04 | Engine supports structured QC operations. | Documented |
| AUD-05 | Engine processed 11 records successfully. | Reported successful |
| AUD-06 | Output file was generated successfully. | Reported successful |
| AUD-07 | Execution terminates after processing. | Documented behavior |
| AUD-08 | VERIFIED does not represent scientific equivalence. | Important boundary |
| AUD-09 | Human review remains required for the example record. | Confirmed by supplied statuses |
| AUD-10 | React demo and Python CLI are separate in the reviewed source; no API connection was found. | Confirmed by source review |

## 14. Overall Audit Conclusion

The BHIV Biosimilarity & Preclinical Evidence QC Engine provides a structured and deterministic software workflow for validating synthetic biosimilarity and preclinical evidence records.

The documented functionality covers schema validation, required-field checks, evidence completeness, duplicate detection, conflict detection, candidate/reference field comparison, quality classification, and human-review routing.

The reported execution successfully processed 11 records and wrote the output file before terminating normally.

The project should be understood as a command-driven batch QC engine.

The `VERIFIED` classification indicates QC completeness only. It does not represent scientific equivalence, biosimilarity, safety, efficacy, interchangeability, or regulatory approval.

The reviewed example record remains subject to human review because `reviewer_status` is `NOT REVIEWED`, `final_review_status` is `OPEN`, and `human_review_required` remains `true`.

**Final Assessment:** The supplied evidence supports successful execution of the synthetic-data QC workflow. Final scientific interpretation is outside the scope of this software system.

---
