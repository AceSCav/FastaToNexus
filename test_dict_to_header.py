import unittest
from dict_to_header import create_nexus_header

class TestDictToHeader(unittest.TestCase):
    def setUp(self):
        self.test_dict = {'seq1': 'ATCG', 'seq2': 'TGCA'}
        self.expected = """#NEXUS

BEGIN DATA;
DIMENSIONS NTAX=2 NCHAR=4;
FORMAT DATATYPE=DNA MISSING=N GAP=-;
MATRIX
"""

    def test_create_nexus_header(self):
        result = create_nexus_header(self.test_dict)
        self.assertEqual(result, self.expected)

if __name__ == "__main__":
    unittest.main()