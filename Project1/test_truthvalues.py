import unittest
import truthvalues

class TestTruthValues(unittest.TestCase):
    def test_and(self):
        self.assertEqual(truthvalues.getAnd("T", "F"), False)
    
    def test_or(self):
        self.assertEqual(truthvalues.getOr("T", "F"), True)
    
    def test_xor(self):
        self.assertEqual(truthvalues.getXor("T", "F"), True)
    
    def test_implies(self):
        self.assertEqual(truthvalues.getImplies("T", "F"), False)
    
    def test_iff(self):
        self.assertEqual(truthvalues.getIff("T", "F"), False)

if __name__ == '__main__':
    unittest.main()