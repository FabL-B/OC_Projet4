#import

class Player:
    """A class that defines player."""

    def __init__(self, name, surname, chess_id, birth_date, score_tournament):
        """Initialize a player."""
        self.name = name
        self.surname = surname
        self.chess_id = chess_id
        self.birth_date = birth_date
        self.score_tournament = 0

    def to_dict_player(self):
        """Set player data in dictionnary."""
        return {
            "name": self.name,
            "surname": self.surname,
            "date_of_birth": self.birth_date,
            "chess_id": self.chess_id,
            "score tournament": self.score_tournament
        }
