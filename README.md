# FASTA to NEXUS Converter

## Overview
A modular Python toolkit for converting biological sequence data from FASTA format to NEXUS format, with complete unit test coverage.

# Components

## 1. `fasta_to_dict.py`

### Function
Converts FASTA files to Python dictionaries

### Docstring
```py
def read_fasta_to_dict(fasta_file):
    """
    Reads a FASTA file and returns a dictionary of {name: sequence}
    
    Args:
        fasta_file (str): Path to the FASTA file
        
    Returns:
        dict: Dictionary with sequence names as keys and sequences as values
        (e.g., {'seq1': 'ATCG', 'seq2': 'TGCA'})
    """
```

### Usage
```py
python fasta_to_dict.py input.fasta
```

## 2. `dict_to_header.py`

### Function
Generates NEXUS header block

### Docstring
```py
def create_nexus_header(sequences_dict):
    """
    Creates the NEXUS DATA block header from the sequences dictionary
    
    Args:
        sequences_dict (dict): Dictionary of {name: sequence}
        
    Returns:
        str: NEXUS DATA block header with dimensions and format info
    """
```

### Usage
```py
python dict_to_header.py "{'seq1':'ATCG','seq2':'TGCA'}"
```

## 3. `dict_to_matrix.py`

### Function
Generates NEXUS matrix block

### Docstring
```py
def create_nexus_matrix(sequences_dict):
    """
    Creates the NEXUS MATRIX block from the sequences dictionary
    
    Args:
        sequences_dict (dict): Dictionary of {name: sequence}
        
    Returns:
        str: NEXUS MATRIX block with aligned sequences
    """
```

### Usage
```py
python dict_to_matrix.py "{'seq1':'ATCG','seq2':'TGCA'}"
```


## 4. `fasta2nexus.py` (Main Script)

### Function
Complete FASTA→NEXUS conversion pipeline

### Usage
```py
python fasta2nexus.py input.fasta > output.nex
```

# Testing
Individual component tests:
```py
python -m unittest test_fasta_to_dict.py
python -m unittest test_dict_to_header.py
python -m unittest test_dict_to_matrix.py
```

# Output format
Standard NEXUS format with:

- DNA datatype

- N for missing data

- for gaps

20-character sequence name padding

Example output:
```
#NEXUS

BEGIN DATA;
DIMENSIONS NTAX=2 NCHAR=4;
FORMAT DATATYPE=DNA MISSING=N GAP=-;
MATRIX
seq1                  ATCG
seq2                  TGCA
;
END;
```
