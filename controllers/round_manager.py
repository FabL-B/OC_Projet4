import random

from models.round import Round
from models.match import Match

class RoundManager:
    """Round manager."""
    
    def __init__(self):
        pass
    
    def create_new_round(self, tournament):
        """Create a new round."""
        round_number = tournament.actual_round + 1
        new_round = Round(round_number)

        # For first round, shuffle players list
        if round_number == 1:
            random.shuffle(tournament.players_list)
        # For next rounds, sort players by their tournament score
        else:
            tournament.players_list.sort(key=lambda player: player.score_tournament, reverse=True)
        new_round.matchs_list = self.create_match_list(tournament.players_list)
        return new_round
    
    def create_match_list(self, players_list):
        """Create matches list."""
        matchs_list = []
        for i in range(0, len(players_list), 2):
            match = Match(players_list[i], players_list[i+1])
            matchs_list.append(match)
        return matchs_list

    def enter_match_result(self, match):
        """Enter scores for each match manually."""
        player1, player2 = match.players[0][0], match.players[1][0]
        print(f"Enter score for {player1.name} {player1.surname} (0, 0.5, 1): ")
        score1 = float(input())
        print(f"Enter score for {player2.name} {player2.surname} (0, 0.5, 1): ")
        score2 = float(input())
        match.set_scores(score1, score2)
        player1.score_tournament += score1
        player2.score_tournament += score2