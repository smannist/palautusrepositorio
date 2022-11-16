
class Player:
    def __init__(self, name, nationality, team, goals, assists):
        self.name = name
        self.team = team
        self.nationality = nationality
        self.goals = goals
        self.assists = assists
    
    @property
    def points(self):
        return self.goals + self.assists
    
    def __str__(self):
        return f"{self.name} {self.nationality} {self.team} {self.goals} + {self.assists} = {self.points}"
