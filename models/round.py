from datetime import datetime
from models.player import Player

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
        return {
            "round_number": self.round_number,
            "start_date_time": self.start_date_time,
            "end_date_time": self.end_date_time,
            "matches_list": self.matches_list
        }

    @staticmethod
    def from_dict_round(round_data):
        """Create a Round instance from a dictionary."""
        round_instance = Round(round_data["round_number"])
        round_instance.start_date_time = round_data["start_date_time"]
        round_instance.end_date_time = round_data["end_date_time"]
        round_instance.matches_list = round_data["matches_list"]
        return round_instance