#!/usr/bin/env python
import sys
import json
from scanner.hash_checker import compute_sha256
from scanner.format_validator import validate_format
from scanner.pickle_inspector import inspect_pickle
from scanner.onnx_inspector import inspect_onnx
from scanner.risk_engine import assess_risk

def main(model_path):
    findings = []

    file_hash = compute_sha256(model_path)
    findings += validate_format(model_path)
    findings += inspect_pickle(model_path)

    if model_path.endswith(".onnx"):
        findings += inspect_onnx(model_path)

    risk = assess_risk(findings)

    report = {
        "model": model_path,
        "hash": file_hash,
        "risk_level": risk,
        "findings": findings
    }

    with open("reports/report.json", "w") as f:
        json.dump(report, f, indent=4)

    print("Security scan completed.")
    print(json.dumps(report, indent=4))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <model_file>")
    else:
        main(sys.argv[1])
