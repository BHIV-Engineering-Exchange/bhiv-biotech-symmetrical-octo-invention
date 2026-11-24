
import json
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def test_cli_processes_synthetic_dataset(tmp_path):
    input_file = PROJECT_ROOT / "data" / "synthetic_evidence.json"
    output_file = tmp_path / "qc_output.json"

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "qc_engine",
            str(input_file),
            "-o",
            str(output_file),
        ],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert "QC processing complete: 11 record(s)" in result.stdout
    assert output_file.exists()

    with open(output_file, encoding="utf-8") as file:
        output = json.load(file)

    assert output["record_count"] == 11
    assert len(output["results"]) == 11
    assert output["scientific_conclusion"] is None
