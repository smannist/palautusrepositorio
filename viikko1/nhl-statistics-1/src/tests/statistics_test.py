import unittest
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
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_player_search_existing_player(self):
        player_to_search = self.statistics.search("Lemieux")
        player_to_match = "Lemieux PIT 45 + 54 = 99"
        self.assertEqual(str(player_to_search), player_to_match)

    def test_player_search_nonexistent_player(self):
        player_to_search = self.statistics.search("Laine")
        self.assertIsNone(player_to_search)

    def test_search_by_team(self):
        search_team_players = self.statistics.team("EDM")
        search_tl = list(map(lambda player: str(player), search_team_players))
        match_tl = ["Semenko EDM 4 + 12 = 16", "Kurri EDM 37 + 53 = 90", "Gretzky EDM 35 + 89 = 124"]
        self.assertEqual(search_tl, match_tl)

    def test_search_top_points(self):
        search_top = self.statistics.top(1, SortBy.POINTS)
        search_top_tl = list(map(lambda player: str(player), search_top))
        match_top_tl = ["Gretzky EDM 35 + 89 = 124", "Lemieux PIT 45 + 54 = 99"]
        self.assertEqual(search_top_tl, match_top_tl)

    def test_search_top_goals(self):
        search_top_goals = self.statistics.top(1, SortBy.GOALS)
        search_top_goals_tl = list(map(lambda player: str(player), search_top_goals))
        match_top_goals = ["Lemieux PIT 45 + 54 = 99", "Yzerman DET 42 + 56 = 98"]
        self.assertEqual(search_top_goals_tl, match_top_goals)
    
    def test_search_top_assists(self):
        search_top_assists = self.statistics.top(1, SortBy.ASSISTS)
        search_top_assists_tl = list(map(lambda player: str(player), search_top_assists))
        match_top_assists = ["Gretzky EDM 35 + 89 = 124", "Yzerman DET 42 + 56 = 98"]
        self.assertEqual(search_top_assists_tl,match_top_assists)