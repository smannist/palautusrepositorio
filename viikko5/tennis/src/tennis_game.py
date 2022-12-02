class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0
        self.score = ""

    def won_point(self, player_name):
        POINT = 1

        if player_name == "player1":
            self.player1_points += POINT

        if player_name == "player2":
            self.player2_points += POINT

    def game_is_even(self):
        if self.player1_points == 0:
            self.score = "Love-All"
        elif self.player1_points == 1:
            self.score = "Fifteen-All"
        elif self.player1_points == 2:
            self.score = "Thirty-All"
        elif self.player1_points == 3:
            self.score = "Forty-All"
        else:
            self.score = "Deuce"

    def check_point_difference(self):
        PLAYER_TWO_ADV = -1
        PLAYER_ONE_ADV = 1
        DOUBLE_ADV = 2

        point_difference = self.player1_points - self.player2_points
        
        if point_difference == PLAYER_ONE_ADV:
            self.score = "Advantage player1"
        elif point_difference == PLAYER_TWO_ADV:
            self.score = "Advantage player2"
        elif point_difference >= DOUBLE_ADV:
            self.score = "Win for player1"
        else:
            self.score = "Win for player2"

    def check_player_lead(self):
        temp_score = 0
        
        for i in range(1, 3):
            if i == 1:
                temp_score = self.player1_points
                self.score = ""
            else:
                self.score = self.score + "-"
                temp_score = self.player2_points

            if temp_score == 0:
                self.score = self.score + "Love"
            elif temp_score == 1:
                self.score = self.score + "Fifteen"
            elif temp_score == 2:
                self.score = self.score + "Thirty"
            elif temp_score == 3:
                self.score = self.score + "Forty"

    def get_score(self):
        if self.player1_points == self.player2_points:
            self.game_is_even()
            return self.score

        if self.player1_points >= 4 or self.player2_points >= 4:
            self.check_point_difference()
            return self.score

        self.check_player_lead()
        return self.score
