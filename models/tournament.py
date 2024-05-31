#import

class Tournament:
    """A class that defines tournament."""

    def __init__(
            self, name, location, start_date, end_date, numbers_of_rounds, 
            actual_round, rounds_list, players_list, general_remarks):
        """Initialize a tournament."""
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.numbers_of_rounds = numbers_of_rounds
        self.actual_round = actual_round
        self.rounds_list = rounds_list
        self.players_list = players_list
        self.general_remarks = general_remarks

    def tournament_add_player():
        