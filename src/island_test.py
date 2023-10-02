import unittest

from mycode.island import Field
  
class FieldAdjectantTest(unittest.TestCase):
  
    f1 = Field(0,0, False)    

    def test_adjected_case1(self):           
        f2 = Field(0,1, False)
        self.assertTrue(self.f1.isAdjected(f2)) 

    def test_adjected_case2(self):   
        f2 = Field(0,-1, False)
        self.assertTrue(self.f1.isAdjected(f2)) 

    def test_adjected_case3(self):   
        f2 = Field(-1,0, False)
        self.assertTrue(self.f1.isAdjected(f2)) 

    def test_adjected_case4(self):   
        f2 = Field(1,0, False)
        self.assertTrue(self.f1.isAdjected(f2))   

    def test_adjected_case4(self):   
        f3 = Field(0,3, False)
        self.assertFalse(self.f1.isAdjected(f3))  
  
if __name__ == '__main__':
    unittest.main()