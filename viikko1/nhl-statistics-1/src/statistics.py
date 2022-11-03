from enum import Enum

def sort_by_points(player):
    return player.points

def sort_by_goals(player):
    return player.goals

def sort_by_assists(player):
    return player.assists

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class Statistics:
    def __init__(self, player_reader):
        self._player_reader = player_reader
        self._players = self._player_reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)
        
    #sorting defaults to points
    def top(self, how_many, sort_by: SortBy = sort_by_points):

        if sort_by == SortBy.POINTS:
            sort_by = sort_by_points
        if sort_by == SortBy.GOALS:
            sort_by = sort_by_goals
        if sort_by == SortBy.ASSISTS:
            sort_by = sort_by_assists

        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_by
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
