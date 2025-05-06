#!/usr/bin/env python3
import sys
from fasta_to_dict import read_fasta_to_dict
from dict_to_header import create_nexus_header
from dict_to_matrix import create_nexus_matrix

def main():
    if len(sys.argv) != 2:
        print("Usage: python fasta2nexus.py input.fasta", file=sys.stderr)
        sys.exit(1)
    
    sequences = read_fasta_to_dict(sys.argv[1])
    print(create_nexus_header(sequences) + create_nexus_matrix(sequences))

if __name__ == "__main__":
    main()