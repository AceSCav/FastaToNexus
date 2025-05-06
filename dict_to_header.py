def create_nexus_header(sequences_dict):
    """
    Creates the NEXUS DATA block header from the sequences dictionary
    Args:
        sequences_dict (dict): Dictionary of {name: sequence}
    Returns:
        str: NEXUS DATA block header
    """
    if not sequences_dict:
        return ""
    
    seq_len = len(next(iter(sequences_dict.values())))
    ntax = len(sequences_dict)
    
    return (
        "#NEXUS\n\n"
        "BEGIN DATA;\n"
        f"DIMENSIONS NTAX={ntax} NCHAR={seq_len};\n"
        "FORMAT DATATYPE=DNA MISSING=N GAP=-;\n"
        "MATRIX\n"
    )

if __name__ == "__main__":
    import ast
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python dict_to_header.py '{sequence_dict}'", file=sys.stderr)
        sys.exit(1)
    
    try:
        seq_dict = ast.literal_eval(sys.argv[1])
        print(create_nexus_header(seq_dict))
    except (ValueError, SyntaxError) as e:
        print(f"Error parsing dictionary: {e}", file=sys.stderr)
        sys.exit(1)