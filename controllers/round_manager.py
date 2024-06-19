import random

from models.round import Round
from models.match import Match
from views.round_view import RoundView

class RoundManager:
    """Round manager."""

    def __init__(self):
        self.round_view = RoundView()

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
        new_round.matches_list = self.create_match_list(tournament.players_list)
        return new_round

    def create_match_list(self, players_list):
        """Create matches list."""
        matches_list = []
        for i in range(0, len(players_list), 2):
            match = Match(players_list[i], players_list[i+1])
            matches_list.append(match)
        return matches_list

    def enter_match_result(self, match):
        """Enter scores for each match manually."""
        RoundView.match_view(match)
        player1, player2 = match.players[0][0], match.players[1][0]
        score1, score2 = RoundView.set_scores_view(player1, player2)
        match.set_scores(score1, score2)
        player1.score_tournament += score1
        player2.score_tournament += score2

    def play_round(self, matches_list):
        pass
