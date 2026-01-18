import onnx

def inspect_onnx(file_path):
    findings = []

    try:
        model = onnx.load(file_path)
        num_nodes = len(model.graph.node)

        if num_nodes > 1000:
            findings.append("ONNX graph unusually large")

        op_types = set(node.op_type for node in model.graph.node)
        findings.append(f"ONNX operators used: {list(op_types)}")

    except Exception as e:
        findings.append(f"ONNX parsing failed: {str(e)}")

    return findings
