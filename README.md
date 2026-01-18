# ML Model Security Scanner (BYOM)

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Security](https://img.shields.io/badge/MLSecOps-BYOM-green)

## 📌 Overview
This project implements a **Python-based security scanning tool** designed for Machine Learning models in **Bring Your Own Model (BYOM)** workflows. 

The primary goal is to proactively identify security risks in untrusted ML artifacts before deployment, particularly in embedded and resource-constrained environments where traditional security layers might be absent.



---

## 🎯 Problem Statement
In BYOM scenarios, users can upload arbitrary ML models for inference. Without proper validation, malicious or malformed models may:

* **Execute arbitrary code** via unsafe serialization (e.g., Python Pickle).
* **Exhaust device resources** through "zip bombs" or massive model architectures.
* **Contain backdoors** or hidden malicious behaviors.
* **Violate deployment constraints** of the target hardware.

This tool provides a **first-line security gate** to mitigate these risks before the model is ever loaded into memory.

---

## 🧠 Threat Model

### Assets
* **Inference Runtime:** The engine executing the model logic.
* **Embedded Devices:** Hardware targets with limited CPU/RAM.
* **Deployment Pipeline:** The CI/CD infrastructure handling model artifacts.

### Threats & Risks
* **Model Tampering:** Unauthorized modification of model weights or architecture.
* **Malicious Serialization:** RCE (Remote Code Execution) via `pickle` or `joblib`.
* **Resource Exhaustion:** Oversized models causing DoS (Denial of Service).
* **Hidden Complexity:** "Layer-bombing" or hidden graphs in ONNX.

**Security Objective:** Prevent unsafe or untrusted models from entering the production deployment pipeline.

---

## 🔍 Security Checks Implemented

| Check | Description |
| :--- | :--- |
| **Model Integrity** | SHA-256 hashing to detect tampering and ensure provenance. |
| **Format Validation** | Strict allowlist of supported formats (e.g., `.onnx`, `.safetensors`). |
| **Size Constraints** | Enforcement of file size limits to prevent resource exhaustion. |
| **Pickle Detection** | Heuristic scanning to flag unsafe serialization in legacy formats. |
| **ONNX Inspection** | Basic structural sanity checks of the model graph. |
| **Risk Scoring** | Automated rule-based classification (Low, Medium, High). |

---

## ⚙️ How It Works
The scanner operates as a standalone utility or can be integrated into a CI/CD pipeline:

1.  **Ingestion:** User uploads a model file.
2.  **Static Analysis:** Scanner performs automated checks without executing the model logic.
3.  **Aggregation:** Findings are scored based on severity.
4.  **Reporting:** A structured JSON security report is generated.
5.  **Enforcement:** Deployment is blocked or allowed based on the defined risk threshold.

---

## 📄 Sample Output
The scanner generates an auditable JSON report for easy integration:

```json
{
  "model": "example.onnx",
  "hash": "b3f9c738e6...",
  "status": "FLAGGED",
  "risk_level": "MEDIUM",
  "findings": [
    "ONNX graph unusually large (depth > 500)",
    "Non-standard ONNX operators detected: ['CustomOp_X']",
    "ONNX operators used: ['Conv', 'Relu', 'Add']"
  ]
}