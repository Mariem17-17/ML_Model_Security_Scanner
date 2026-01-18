def assess_risk(findings):
    risk = "LOW"

    for f in findings:
        if "pickle" in f.lower():
            return "HIGH"
        if "Unsupported" in f or "exceeds" in f:
            risk = "MEDIUM"

    return risk
