# FastaToNexus

## Structure
- `fasta_to_dict.py` - Converts FASTA to dictionary
- `dict_to_header.py` - Generates NEXUS header
- `dict_to_matrix.py` - Generates NEXUS matrix
- `fasta2nexus.py` - Main conversion script
- Test files for each component

## Usage
```bash
# Run conversion
python fasta2nexus.py input.fasta > output.nex

# Run tests example
python -m unittest test_fasta_to_dict.py
```

## Testing
Individual test files for each component:
- `test_fasta_to_dict.py`
- `test_dict_to_header.py`
- `test_dict_to_matrix.py`
