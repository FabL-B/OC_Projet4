from models.player import Player


class Match:
    """A class to define a match."""

    def __init__(self, player1, player2):
        """Initialize a match with two players."""
        self.player_scores = [[player1, 0], [player2, 0]]

    def set_scores(self, score1, score2):
        """Set the scores for both players."""
        self.player_scores[0][1] = score1
        self.player_scores[1][1] = score2

    def to_tuples_match(self):
        """Convert the match to a tuple of lists."""
        return ([self.player_scores[0][0].to_dict_player(), self.player_scores[0][1]],
                [self.player_scores[1][0].to_dict_player(), self.player_scores[1][1]])

    @staticmethod
    def from_tuples_match(tuples_list):
        """Convert a tuple of lists back into a Match object."""
        player1_dict, score1 = tuples_list[0]
        player2_dict, score2 = tuples_list[1]
        # Convert both players to a Player object.
        player1 = Player.from_dict_player(player1_dict)
        player2 = Player.from_dict_player(player2_dict)

        match = Match(player1, player2)
        match.set_scores(score1, score2)
        return match

    def get_players(self):
        """Return a tuple of the players in the match to check previous matches from db."""
        return (self.player_scores[0][0], self.player_scores[1][0])
