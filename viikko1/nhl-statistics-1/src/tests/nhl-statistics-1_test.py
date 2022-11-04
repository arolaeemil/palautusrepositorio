import unittest
from player_reader import PlayerReader
from statistics import Statistics, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(PlayerReaderStub())

    def test_searchworks(self):
        player1 = self.statistics.search("Semenko")

        self.assertEqual(player1.name, "Semenko")
    
    def test_searchreturnsnoneifnamenotexist(self):
        player1 = self.statistics.search("Testinimieiloydyvarmasti")

        self.assertEqual(player1, None)

    def test_teamworks(self):
        team1 = self.statistics.team("PIT")
        team2 = self.statistics.team("EDM")
        for player in team1:
            teamname = player.team
        self.assertEqual(teamname, "PIT")
        self.assertEqual(len(team2),3)

    def test_top_works(self):
        top2 = self.statistics.top(2)
        player1 = top2[0]
        player2 = top2[1]
        self.assertEqual(player1.name, "Gretzky")
        self.assertAlmostEqual(int(player1.points), int(35+89))
        self.assertEqual(player2.name, "Lemieux")
        self.assertAlmostEqual(int(player2.points), int(45+54))
    
    def test_top_goals(self):
        top1 = self.statistics.top(1, SortBy.GOALS)
        player1 = top1[0]
        self.assertEqual(player1.name, "Lemieux")
        self.assertAlmostEqual(int(player1.goals), int(45))
    
    def test_top_assists(self):
        top1 = self.statistics.top(1, SortBy.ASSISTS)
        player1 = top1[0]
        self.assertEqual(player1.name, "Gretzky")
        self.assertAlmostEqual(int(player1.assists), int(89))