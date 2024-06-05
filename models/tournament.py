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

    def to_dict_tournament(self):
        """Set tournament data in dictionnary."""
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "numbers of rounds": self.numbers_of_rounds,
            "actual round": self.actual_round,
            "rounds list": [self.round_to_dict(round_instance) for round_instance in self.rounds_list],
            "players_list": [player.to_dict_player() for player in self.players_list],
            "general remarks": self.general_remarks
        }

    def round_to_dict(self, round_instance):
        """Convert a round instance to a dictionary."""
        return {
            "round_number": round_instance.round_number,
            "start_date_time": round_instance.start_date_time,
            "end_date_time": round_instance.end_date_time,
            "matchs_list": [self.match_to_dict(match) for match in round_instance.matchs_list]
        }

    def match_to_dict(self, match):
        """Convert a match instance to a dictionary."""
        return {
            "players": [
                {"player": match.players[0][0].to_dict_player(), "score": match.players[0][1]},
                {"player": match.players[1][0].to_dict_player(), "score": match.players[1][1]}
            ]
        }