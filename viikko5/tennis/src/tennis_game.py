class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def score_even(self, score_points):
        score_as_string = ""
        if score_points == 0:
            score_as_string = "Love-All"
        elif score_points == 1:
            score_as_string = "Fifteen-All"
        elif score_points == 2:
            score_as_string = "Thirty-All"
        elif score_points == 3:
            score_as_string = "Forty-All"
        else:
            score_as_string = "Deuce"
        return score_as_string


    def advantage_or_win(self, player1_score, player2_score):
        score_as_string = ""
        minus_result = player1_score - player2_score
        if minus_result == 1:
            score_as_string = "Advantage player1"
        elif minus_result == -1:
            score_as_string = "Advantage player2"
        elif minus_result >= 2:
            score_as_string = "Win for player1"
        else:
            score_as_string = "Win for player2"
        return score_as_string

    def uneven_situation(self, player1_score, player2_score):
        score_as_string = ""
        temp_score = 0
        for i in range(1, 3):
            if i == 1:
                temp_score = player1_score
            else:
                score_as_string = score_as_string + "-"
                temp_score = player2_score
            if temp_score == 0:
                score_as_string = score_as_string + "Love"
            elif temp_score == 1:
                score_as_string = score_as_string + "Fifteen"
            elif temp_score == 2:
                score_as_string = score_as_string + "Thirty"
            elif temp_score == 3:
                score_as_string = score_as_string + "Forty"
        return score_as_string

    def get_score(self):
        score_string = ""
        if self.m_score1 == self.m_score2:
            score_string = self.score_even(self.m_score2)

        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            score_string = self.advantage_or_win(self.m_score1, self.m_score2)

        else:
            score_string = self.uneven_situation(self.m_score1, self.m_score2)

        return score_string
