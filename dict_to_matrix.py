def create_nexus_matrix(sequences_dict):
    """
    Creates the NEXUS MATRIX block from the sequences dictionary
    Args:
        sequences_dict (dict): Dictionary of {name: sequence}
    Returns:
        str: NEXUS MATRIX block
    """
    matrix_lines = []
    for name, seq in sequences_dict.items():
        matrix_lines.append(f"{name.ljust(20)} {seq}")
    return "\n".join(matrix_lines) + "\n;\nEND;\n"

if __name__ == "__main__":
    import ast
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python dict_to_matrix.py '{sequence_dict}'", file=sys.stderr)
        sys.exit(1)
    
    try:
        seq_dict = ast.literal_eval(sys.argv[1])
        print(create_nexus_matrix(seq_dict))
    except (ValueError, SyntaxError) as e:
        print(f"Error parsing dictionary: {e}", file=sys.stderr)
        sys.exit(1)