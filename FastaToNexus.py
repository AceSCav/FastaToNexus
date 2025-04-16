import sys

with open("C:/Users/alfca/OneDrive/Desktop/Estudos/Python/small_seq.txt") as file:
    file = file.readlines()
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
    header += "BEGIN DATA;\n"
    header += f"DIMENSIONS NTAX={num_seqs} NCHAR={seq_length};\n"
    header += "FORMAT DATATYPE=DNA MISSING=N GAP=-;\n"
    header += "MATRIX\n"
    return header

def NexusMatrix(seq_dict):
    matrix = ""
    for seq_name, seq in seq_dict.items():
        matrix += f"{seq_name[1::]} {seq}\n"
    matrix += ";\n"
    return matrix

seq_dict = FastaToDict(file)
print(NexusHeader(seq_dict))
print(NexusMatrix(seq_dict))