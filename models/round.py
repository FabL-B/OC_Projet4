import random
import datetime

from models.player import Player

class Round:
    """A class that defines round."""

    def __init__(
            self, round_number, start_date_time, end_date_time, 
            matchs_list, players_list):
        """Initialize a round."""
        self.round_number = round_number
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.matchs_list = matchs_list
        self.players_list = players_list

    def generate_players_pairs(self):
        """Generate random pairs of player at the start of each rounds."""
        # If first round, randomize all players in the list to generate pair

        # After first round
        # Sort players by their total score
            # If players have same score, randomize them
        # Associate player like following : p1 with p2, p3 with p4, ...
            # Try to avoid to create same matches as previously


    def start_round_model(self):
        '''Permet d'ajouter la date de début de round'''
        self.start_date = datetime.datetime.today().strftime("%d/%m/%Y")[0:10]

    def end_round(self):
        '''Permet d'ajouter la date de fin de round'''
        self.end_date = datetime.datetime.today().strftime("%d/%m/%Y")[0:10]
