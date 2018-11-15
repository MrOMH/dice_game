import unittest
import sys
from playdice import *
class PutDiceToTest(unittest.TestCase):
    def test_dice_roll(self):
        '''Check that the output in valid'''
        self.assertTrue(roll_dice() <= 10,msg = 'OOPs!,10 faces is the max value')
            
    def test_prompt(self):
        '''Scan the prompt to see the actual behavious'''
        self.assertTrue(prompt('play ?(Yes == Pass): '))
        
    def test_throws_to_ordinal_zero(self):
        self.assertEqual( throws_to_ordinal(0) ,'Zero','0 should remain zero in ordinal')
        
    def test_throws_to_ordinal_one(self):
        self.assertEqual( throws_to_ordinal(1) ,'1st','1 should be 1st in ordinal')
        
    def test_throws_to_ordinal_two(self):
        self.assertEqual( throws_to_ordinal(2) ,'2nd','2 should be 2nd in ordinal')
    
    def test_throws_to_ordinal_three(self):
        self.assertEqual( throws_to_ordinal(3) ,'3rd','3 should be 3rd in ordinal')
        
            
if __name__ == '__main__':
    unittest.main()