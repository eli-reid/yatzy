import unittest
import Hand

class Test_Hand(unittest.TestCase):

    def setUp(self):
        self.hand = Hand.yatzy_hand()

    def test_Dice_list_of_type_die(self):
        self.assertIsInstance(self.hand._dice, list)
        for die in self.hand._dice:
            self.assertIsInstance(die, Hand.Die)
    
    def test_total_by_value(self):
        self.assertEqual(self.hand.total_by_value(1),5)   

    def test_type(self):
        self.assertIsInstance(self.hand, Hand.Hand_of_dice)

    def test_hand_has_dice(self):
        self.assertEqual(len(self.hand),5)
        return

    def test_count(self):
        self.assertEqual(self.hand.count(1),5)
    
    def test_roll(self):
        temp = self.hand.total
        self.hand.roll()
        self.assertNotEqual(temp, self.hand.total)
    
    def test_roll_die1(self):
        temp = int(self.hand[0])
        self.hand.roll('1')
        self.assertNotEqual(temp,int(self.hand[0]))

    def test_roll_4_die(self):
        temp = [self.hand[0].value, self.hand[1].value, self.hand[2].value, self.hand[3].value]
        self.hand.roll('1234')
        self.assertNotEqual(temp, [self.hand[0].value, self.hand[1].value, self.hand[2].value, self.hand[3].value])
    
    def test_test_invalid_roll(self):
        with self.assertRaises(ValueError):
            self.hand.roll('wer')
    
    def test_sort(self):
        self.hand.roll()
        temp = sorted(self.hand)
        self.hand.sort()
        self.assertEqual(sorted(self.hand), self.hand)

    def test_is_three_kind(self):
        self.hand._dice=[2,1,1,2,2]
        self.assertTrue(self.hand.is_three_kind)
    
    def test_not_is_three_kind(self):
        self.hand._dice=[1,1,3,2,2]
        self.assertFalse(self.hand.is_three_kind)

    def test_is_four_kind(self):
        self.hand._dice=[2,2,1,2,2]
        self.assertTrue(self.hand.is_four_kind)

    def test_not_is_four_kind(self):
        self.hand._dice=[1,2,3,2,2]
        self.assertFalse(self.hand.is_four_kind)
    
    def test_is_fullhouse(self):
        self.hand._dice = [1,1,3,3,3]
        self.assertTrue(self.hand.is_fullhouse)
    
    def test_not_is_fullhouse(self):
        self.hand._dice = [1,1,4,3,3]
        self.assertFalse(self.hand.is_fullhouse)
    
    def test_is_sm_straight(self):
        self.hand._dice = [1,4,5,3,6]
        self.assertTrue(self.hand.is_sm_straight)
        self.hand._dice = [2,4,5,3,2]
        self.assertTrue(self.hand.is_sm_straight)
        self.hand._dice = [1,4,2,3,2]
        self.assertTrue(self.hand.is_sm_straight)
    
    def test_not_is_sm_straight(self):
        self.hand._dice = [2,4,5,3,6]
        self.assertTrue(self.hand.is_sm_straight)

    def test_is_lg_straight(self):
        self.hand._dice = [2,4,5,3,6]
        self.assertTrue(self.hand.is_lg_straight)
        self.hand._dice = [1,4,5,3,2]
        self.assertTrue(self.hand.is_lg_straight)

    def test_not_is_lg_straight(self):
        self.hand._dice = [2,4,5,3,6]
        self.assertTrue(self.hand.is_lg_straight)

    def test_is_yatzy(self):
        self.hand._dice = [2,2,2,2,2]
        self.assertTrue(self.hand.is_yatzy)
            
    def test_not_is_yatzy(self):
        self.hand._dice = [2,2,3,2,2]
        self.assertFalse(self.hand.is_yatzy)

if __name__ == '__main__':
    unittest.main() # pragma: no cover