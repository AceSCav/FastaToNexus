import unittest
from dict_to_matrix import create_nexus_matrix

class TestDictToMatrix(unittest.TestCase):
    def setUp(self):
        self.test_dict = {'seq1': 'ATCG', 'seq2': 'TGCA'}
        self.expected = """seq1                  ATCG
seq2                  TGCA
;
END;
"""

    def test_create_nexus_matrix(self):
        result = create_nexus_matrix(self.test_dict)
        self.assertEqual(result, self.expected)

if __name__ == "__main__":
    unittest.main()