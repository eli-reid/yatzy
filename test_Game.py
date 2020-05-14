import unittest
import Game
from Hand import Test_Hand

class Test_Game(unittest.TestCase):

    def setUp(self):
        self.game = Game.Game(["player1", "player2"])

    def test_next_player(self):
        self.assertEqual(self.game.current_player.name, "player1")
        self.game.get_next_player()
        self.assertEqual(self.game.current_player.name, "player2")
        
    def test_is_yatzy_bonus(self):
        self.game.current_player.hand = Test_Hand([1,1,1,1,1])
        self.game.current_player.scorecard.yatzy = self.game.yatzy_value
        self.assertTrue(self.game.is_yatzy_bonus)
    
    def test_not_is_yatzy_bonus(self):
        self.game.current_player.scorecard.yatzy = 0
        self.assertFalse(self.game.is_yatzy_bonus)

    def test_not_game_over(self):
        self.assertFalse(self.game.game_over)
    
    def test_ones(self):
        self.game.current_player.hand = Test_Hand([1,1,2,1,1])
        self.game.score_hand('1')
        self.assertEqual(self.game.current_player.scorecard.ones, 4)

    def test_score_twos(self):
        self.game.current_player.hand = Test_Hand([2,2,2,2,2])
        self.game.score_hand('2')
        self.assertEqual(self.game.current_player.scorecard.twos, 10)

    def test_score_threes(self):
        self.game.current_player.hand = Test_Hand([3,3,3,1,2])
        self.game.score_hand('3')
        self.assertEqual(self.game.current_player.scorecard.threes, 9)

    def test_score_fours(self):
        self.game.current_player.hand = Test_Hand([4,4,4,4,5])
        self.game.score_hand('4')
        self.assertEqual(self.game.current_player.scorecard.fours, 16)

    
    def test_score_fives(self):
        self.game.current_player.hand = Test_Hand([5,5,5,5,2])
        self.game.score_hand('5')
        self.assertEqual(self.game.current_player.scorecard.fives, 20)

    def test_score_sixes(self):
        self.game.current_player.hand = Test_Hand([6,6,6,3,5])
        self.game.score_hand('6')
        self.assertEqual(self.game.current_player.scorecard.sixes, 18)

    def test_score_three_of_kind(self):
        self.game.current_player.hand = Test_Hand([4,4,4,2,5])
        self.game.score_hand('7')
        self.assertEqual(self.game.current_player.scorecard.three_of_kind, 19 )

    def test_score_four_of_kind(self):
        self.game.current_player.hand = Test_Hand([4,4,4,4,5])
        self.game.score_hand('8')
        self.assertEqual(self.game.current_player.scorecard.four_of_kind, 21 )

    def test_score_fullhouse(self):
        self.game.current_player.hand = Test_Hand([4,4,4,5,5])
        self.game.score_hand('9')
        self.assertEqual(self.game.current_player.scorecard.fullhouse, self.game.fullhouse_value )

    def test_score_sm_straight(self):
        self.game.current_player.hand = Test_Hand([4,3,4,2,5])
        self.game.score_hand('10')
        self.assertEqual(self.game.current_player.scorecard.sm_straight, self.game.sm_straight_value ) 

    def test_score_lg_straight(self):
        self.game.current_player.hand = Test_Hand([1,4,3,2,5])
        self.game.score_hand('11')
        self.assertEqual(self.game.current_player.scorecard.lg_straight, self.game.lg_straight_value)

    def test_score_yatzy(self):
        self.game.current_player.hand = Test_Hand([5,5,5,5,5])
        self.game.score_hand('12')
        self.assertEqual(self.game.current_player.scorecard.yatzy, self.game.yatzy_value)
    
    def test_score_chance(self):
        self.game.current_player.hand = Test_Hand([1,4,3,2,5])
        self.game.score_hand('13')
        self.assertEqual(self.game.current_player.scorecard.chance, 15)

    def test_add_yatzy_bonus(self):
        self.game.current_player.hand = Test_Hand([5,5,5,5,5])
        self.game.current_player.scorecard.yatzy = 50
        self.game.score_hand('5')
        self.assertEqual(self.game.current_player.scorecard.yatzy_bonus, self.game.yatzy_bonus_value)
    
    def test_winner(self):
        self.game.current_player.hand = Test_Hand([5,5,5,5,5])
        self.game.score_hand('5')
        self.assertEqual(self.game.get_winner(), self.game.current_player)


if __name__ == '__main__': # pragma: no cover
    unittest.main()