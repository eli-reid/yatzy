import unittest
import Scorecard

class Test_Scorecard(unittest.TestCase):

    def setUp(self):
        self.scorecard = Scorecard.Scorecard()

    def test_change_score_ones(self):
        self.scorecard.ones = 4
        with self.assertRaises(ValueError):
            self.scorecard.ones = 4
    
    def test_change_score_twos(self):
        self.scorecard.twos = 4
        with self.assertRaises(ValueError):
            self.scorecard.twos = 4

    def test_change_score_threes(self):
        self.scorecard.threes = 4
        with self.assertRaises(ValueError):
            self.scorecard.threes = 4

    def test_change_score_fours(self):
        self.scorecard.fours = 4
        with self.assertRaises(ValueError):
            self.scorecard.fours= 4
    
    def test_change_score_fives(self):
        self.scorecard.fives = 4
        with self.assertRaises(ValueError):
            self.scorecard.fives = 4

    def test_change_score_sixes(self):
        self.scorecard.sixes = 4
        with self.assertRaises(ValueError):
            self.scorecard.sixes = 4

    def test_change_score_three_of_kind(self):
        self.scorecard.three_of_kind = 4
        with self.assertRaises(ValueError):
            self.scorecard.three_of_kind = 4

    def test_change_score_four_of_kind(self):
        self.scorecard.four_of_kind = 4
        with self.assertRaises(ValueError):
            self.scorecard.four_of_kind = 4
    
    def test_change_score_fullhouse(self):
        self.scorecard.fullhouse = 4
        with self.assertRaises(ValueError):
            self.scorecard.fullhouse = 4

    def test_change_score_sm_straight(self):
        self.scorecard.sm_straight = 4
        with self.assertRaises(ValueError):
            self.scorecard.sm_straight = 4
    
    def test_change_score_lg_straight(self):
        self.scorecard.lg_straight = 4
        with self.assertRaises(ValueError):
            self.scorecard.lg_straight = 4
    
    def test_change_score_yatzy(self):
        self.scorecard.yatzy = 4
        with self.assertRaises(ValueError):
            self.scorecard.yatzy = 4
        
    def test_change_score_chance(self):
        self.scorecard.chance = 4
        with self.assertRaises(ValueError):
            self.scorecard.chance = 4