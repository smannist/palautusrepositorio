
class PlayerStats:
    def __init__(self, player_reader):
        self.players = player_reader.get_players()
    
    def top_scorers_by_nationality(self, nationality):
        players_by_nationality = list(filter(lambda player: player.nationality == nationality, self.players))
        top_scorers_by_nationality = sorted(players_by_nationality, key=lambda player: player.points, reverse=True)
        return top_scorers_by_nationality