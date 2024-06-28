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
        round_number = tournament.actual_round
        new_round = Round(round_number)
        # For first round, shuffle players list
        if round_number == 1:
            random.shuffle(tournament.players_list)
        # For next rounds, sort players by their tournament score
        else:
            random.shuffle(tournament.players_list)
            self.sort_players_by_score(tournament.players_list)
            self.avoid_previous_matchups(tournament.players_list,
                                         tournament.rounds_list)
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
        RoundView.display_match_view(match)
        player1, player2 = match.player_scores[0][0], match.player_scores[1][0]
        score1 = RoundView.set_scores_view(player1)
        score2 = RoundView.set_scores_view(player2)
        match.set_scores(score1, score2)
        player1.score_tournament += score1
        player2.score_tournament += score2

    def sort_players_by_score(self, players_list):
        """Sort players by their tournament score."""
        players_list.sort(key=lambda player: player.score_tournament, reverse=True)

    def avoid_previous_matchups(self, players_list, rounds_list):
        """Reorder the players list to avoid previous matchups."""
        previous_matches = Round.get_previous_matches(rounds_list)

        i = 0
        while i < len(players_list) - 1:
            player1 = players_list[i]
            player2 = players_list[i + 1]
            if ((player1, player2) in previous_matches or 
                (player2, player1) in previous_matches):
                # Try to find a new matchup for player1
                for j in range(i + 2, len(players_list)):
                    if ((player1, players_list[j]) not in previous_matches and
                        (players_list[j], player1) not in previous_matches):
                        players_list[i + 1], players_list[j] = players_list[j], players_list[i + 1]
                        break
                else:
                    i += 1
            i += 2
