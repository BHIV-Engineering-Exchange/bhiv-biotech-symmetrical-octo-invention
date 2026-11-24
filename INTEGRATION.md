# QC Engine Integration Guide

## 1. Project Overview

The BHIV Biotech Evidence Quality Control (QC) Engine is a standalone Python package designed to validate and assess the structural and reporting quality of biosimilarity and preclinical evidence records.

The engine performs:

- JSON Schema validation
- Evidence completeness assessment
- Duplicate evidence and study ID detection
- Conflicting information detection
- Evidence quality classification
- Human review requirement identification
- Structured JSON output generation

**Important:** The engine does not establish biosimilarity, clinical equivalence, interchangeability, safety, efficacy, or regulatory validity.

## 2. Environment Requirements

- Python 3.10 or later
- pip package manager
- Virtual environment
- Required Python dependencies listed in `requirements.txt`

## 3. Environment Setup

Create and activate the virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the required dependencies:

```powershell
python -m pip install -r requirements.txt
```

## 4. Run the QC Engine

The QC Engine accepts a JSON dataset containing evidence records.

Execute the following command from the project root:

```powershell
python -m qc_engine .\data\synthetic_evidence.json -o .\qc_output.json
```

Expected terminal message:

```text
QC processing complete: 11 record(s)
Output written to: .\qc_output.json
```

## 5. Command-Line Interface

Display the available CLI options:

```powershell
python -m qc_engine --help
```

The CLI accepts:

- Input: Path to the evidence JSON dataset.
- Output: Destination path for the generated QC JSON report.
- Default output filename: `qc_output.json`.

## 6. Generated QC Output

The engine generates a structured JSON report containing:

- Engine and schema versions
- Total evidence record count
- Duplicate records
- Conflicting fields
- Individual evidence quality classifications
- Validation and completeness results
- Human review requirements

The verified synthetic dataset produced:

| QC Parameter | Result |
|---|---:|
| Total records | 11 |
| Duplicate findings | 3 |
| Conflict findings | 2 |
| Human review required | 11 |
| Scientific conclusion | None |

All records remain subject to human review.

## 7. Run Automated Tests

Execute the complete automated test suite:

```powershell
python -m pytest -q
```

Latest verified test result:

```text
32 passed
```

The test suite covers record validation, JSON Schema validation, duplicate detection, conflict detection, classification, malformed input handling, and CLI integration.

## 8. Project Integration Status

The QC Engine is implemented as a standalone Python package.

The command-line interface supports execution through:

```powershell
python -m qc_engine
```

The integration test verifies successful processing of the synthetic evidence dataset and generation of the output JSON report.

**Verification boundary:** Passing automated tests demonstrates software functionality. It does not constitute scientific, clinical, or regulatory validation.