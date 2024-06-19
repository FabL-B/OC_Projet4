from models.player import Player

class Match:
    """A class to define a match."""

    def __init__(self, player1, player2):
        """Initialize a match with two players."""
        self.players = [(player1, 0), (player2, 0)]
    
    def set_scores(self, score1, score2):
        """Set the scores for both players."""
        self.players[0] = (self.players[0][0], score1)
        self.players[1] = (self.players[1][0], score2)
        
    def to_tuples_match(self):
        """Convert the match to a list of tuples."""
        match = []
        for player, score in self.players:
            player_dict = player.to_dict_player()
            match.append((player_dict, score))
        return match

    @staticmethod
    def from_tuples_match(tuples_list):
        """Convert a list of tuples back into a Match object."""
        player1_dict, score1 = tuples_list[0]
        player2_dict, score2 = tuples_list[1]
        player1 = Player.from_dict_player(player1_dict)
        player2 = Player.from_dict_player(player2_dict)
        
        match = Match(player1, player2)
        match.set_scores(score1, score2)
        return match