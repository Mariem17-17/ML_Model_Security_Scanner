import os

ALLOWED_EXTENSIONS = [".onnx", ".pt", ".tflite"]
MAX_SIZE_MB = 50

def validate_format(file_path):
    ext = os.path.splitext(file_path)[1]
    size_mb = os.path.getsize(file_path) / (1024 * 1024)

    findings = []

    if ext not in ALLOWED_EXTENSIONS:
        findings.append("Unsupported model format")

    if size_mb > MAX_SIZE_MB:
        findings.append("Model size exceeds embedded constraints")

    return findings
