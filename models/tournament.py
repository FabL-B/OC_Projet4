#import

class Tournament:
    """A class that defines tournament."""

    def __init__(
            self, name, location, start_date, end_date, numbers_of_rounds=4, 
            actual_round = 0, rounds_list = None, players_list = None, general_remarks = ""):
        """Initialize a tournament."""
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.numbers_of_rounds = numbers_of_rounds
        self.actual_round = actual_round
        self.rounds_list = rounds_list if rounds_list is not None else []
        self.players_list = players_list if players_list is not None else []
        self.general_remarks = general_remarks

    def set_players_list():
            pass

    def to_dict_tournament(self):
        """Set tournament data in dictionnary."""
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "numbers of rounds": self.numbers_of_rounds,
            "actual round": self.actual_round,
            "rounds list": self.rounds_list,
            "players list": self.players_list,
            "general remarks": self.general_remarks
        }

    def add_player(self, player):
        """Add a player to the tournament."""
        self.players_list.append(player)

    def remove_player(self, player):
        """Remove a player from the tournament."""
        self.players_list.remove(player)

    def get_players(self):
        """Return the list of players."""
        return self.players_list
    