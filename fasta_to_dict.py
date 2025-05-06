def read_fasta_to_dict(fasta_file):
    """
    Reads a FASTA file and returns a dictionary of {name: sequence}
    Args:
        fasta_file (str): Path to the FASTA file
    Returns:
        dict: Dictionary with sequence names as keys and sequences as values
    """
    sequences = {}
    current_name = None
    current_seq = []
    
    with open(fasta_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if current_name is not None:
                    sequences[current_name] = ''.join(current_seq)
                current_name = line[1:].split()[0]
                current_seq = []
            else:
                current_seq.append(line.upper())
    
    if current_name is not None:
        sequences[current_name] = ''.join(current_seq)
    
    return sequences

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python fasta_to_dict.py input.fasta", file=sys.stderr)
        sys.exit(1)
    print(read_fasta_to_dict(sys.argv[1]))