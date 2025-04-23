import sys

def FastaToDict(file):
    seq_dict = {}
    for line in file:
        if line.startswith(">"):
            seq_name = line.strip()
            seq_dict[seq_name] = ""
        else:
            seq_dict[seq_name] += line.strip()
    return seq_dict 

def NexusHeader(seq_dict):
    seq_length = len(list(seq_dict.values())[0])
    num_seqs = len(seq_dict)
    header = "#NEXUS\n"
    header += "\n"
    header += "BEGIN DATA;\n"
    header += f"DIMENSIONS NTAX={num_seqs} NCHAR={seq_length};\n"
    header += "FORMAT DATATYPE=DNA MISSING=N GAP=-;\n"
    header += "MATRIX\n"
    return header

def NexusMatrix(seq_dict):
    matrix = ""
    for seq_name, seq in seq_dict.items():
        matrix += f"{seq_name[1::]} {seq}\n"
    matrix += ";\nEND;\n"
    return matrix

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        in_file = sys.argv[1]
        with open(in_file, "r") as file:
            seq_dict = FastaToDict(file)
            header = NexusHeader(seq_dict)
            matrix = NexusMatrix(seq_dict)
            print(header + matrix)
    else:
        print("Usage: python FastaToNexus.py file.fasta")
        sys.exit(1)


