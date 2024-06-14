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
        return self.players