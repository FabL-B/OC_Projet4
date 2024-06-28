from datetime import datetime

from models.match import Match


class Round:
    """A class that defines round."""

    def __init__(self, round_number):
        """Initialize a round."""
        self.round_number = round_number
        self.start_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.end_date_time = None
        self.matches_list = []

    def end_round(self):
        """End the round by setting the end date and time."""
        self.end_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict_round(self):
        """Convert a round instance to a dictionary."""
        matches_as_tuples = [
            match.to_tuples_match()
            for match in self.matches_list
            ]
        return {
            "round_number": self.round_number,
            "start_date_time": self.start_date_time,
            "end_date_time": self.end_date_time,
            "matches_list": matches_as_tuples
        }

    @staticmethod
    def from_dict_round(round_data):
        """Create a Round instance from a dictionary."""
        matches_list = [Match.from_tuples_match(match_tuple)
                        for match_tuple in round_data["matches_list"]]

        round_instance = Round(round_data["round_number"])
        round_instance.start_date_time = round_data["start_date_time"]
        round_instance.end_date_time = round_data["end_date_time"]
        round_instance.matches_list = matches_list
        return round_instance

    @staticmethod
    def get_previous_matches(rounds_list):
        """Get the previous matches in a list."""
        previous_matches = []
        for round in rounds_list:
            for match in round.matches_list:
                previous_matches.append(
                    match.get_players()
                    )
                previous_matches.append(
                    (match.get_players()[1], match.get_players()[0])
                    )
        return previous_matches
