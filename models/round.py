import random
from datetime import datetime

from models.player import Player

class Round:
    """A class that defines round."""

    def __init__(
            self, round_number):
        """Initialize a round."""
        self.round_number = round_number
        self.start_date_time = ""
        self.end_date_time = None
        self.matchs_list = []

    def end_round(self):
        """End the round by setting the end date and time."""
        self.end_date_time = ""

    def round_to_dict(self, round_instance):
        """Convert a round instance to a dictionary."""
        return {
            "round_number": round_instance.round_number,
            "start_date_time": round_instance.start_date_time,
            "end_date_time": round_instance.end_date_time,
            "matchs_list": round_instance.matchs_list
        }
