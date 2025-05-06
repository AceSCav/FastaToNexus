import sys

def FastaToDict(file):
    """
    Converte o ficheiro FASTA em um dicionário com as sequências que este contem.

    Cada linha identificada o incio com '>' que antecede de cada sequencia para o dicionário até existe outro '>'

    Args:
        file (iteravel): ficheiro que contem dados no formato FASTA.

    Returns:
        dict: O dicionário que as chaves são os nomes das sequências e os valores são as sequências.
    """
    seq_dict = {}
    for line in file:
        if line.startswith(">"):
            seq_name = line.strip()
            seq_dict[seq_name] = ""
        else:
            seq_dict[seq_name] += line.strip()
    return seq_dict 

def NexusHeader(seq_dict):
    """
    cria o cabeçalho do ficheiro NEXUS a partir do dicionário de sequências que foi criada na funcao 'FastaToDict'.

    O cabeçalho inclui a estrutura obrigatória do bloco `BEGIN DATA`, com as dimensões sendo estas número de sequências e das mesmas comprimento das sequências,
    o formato de dados de DNA, que utiliza 'N' para os carácter que nao existem e '-' para os gap, e inicia a seção `MATRIX` onde as sequências serão inceridas
    no ficehiro.

    Args:
        seq_dict (dict): O dicionário que as chaves são cabeçalhos de sequência (ex: '>seq1') e os valores são as sequências a que os chaves correspondem 
                         (ex: 'TAAGC...').

    Returns:
        str: String formatada que contem o cabeçalho do ficheiro NEXUS pronto para ser escrito.
    """
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
    """
    Cria a parte MATRIX do ficheiro NEXUS a partir do dicionário das sequências.

    Para cada chave do dicionário, o nome da sequência sem o '>' é alinhado com a sequência correspondente. A estrutura restringe-se ao padrão do bloco MATRIX
    do formato NEXUS.

    Args:
        seq_dict (dict): Dicionário com chaves que sao os nomes das sequências (ex: '>seq1') e os valores que sao as sequências de nucleótidos (ex: 'TAAGC...').

    Returns:
        str: Uma string que contem as sequências no bloco MATRIX, que termina com ';' e 'END;'.
    """
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


