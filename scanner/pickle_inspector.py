import os

def inspect_pickle(file_path):
    findings = []
    ext = os.path.splitext(file_path)[1]

    if ext == ".pkl":
        findings.append(
            "Pickle files can execute arbitrary code and are unsafe in BYOM environments"
        )

    return findings
