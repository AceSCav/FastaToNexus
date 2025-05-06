import unittest
import tempfile
import os
from fasta_to_dict import read_fasta_to_dict

class TestFastaToDict(unittest.TestCase):
    def setUp(self):
        self.test_fasta = """>seq1
ATCG
>seq2
TGCA
"""
        self.expected = {'seq1': 'ATCG', 'seq2': 'TGCA'}

    def test_read_fasta_to_dict(self):
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_f:
            temp_f.write(self.test_fasta)
            temp_f_path = temp_f.name
            temp_f.close()
            
            result = read_fasta_to_dict(temp_f_path)
            os.unlink(temp_f_path)
        
        self.assertEqual(result, self.expected)

if __name__ == "__main__":
    unittest.main()