import os
import json

from models.player import Player
from models.round import Round

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
        
        rounds_as_dicts = [round.to_dict_round() 
            for round in self.rounds_list
            ]
        players_as_dicts = [player.to_dict_player() 
            for player in self.players_list
            ]
        
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "numbers of rounds": self.numbers_of_rounds,
            "actual_round": self.actual_round,
            "rounds_list": rounds_as_dicts,
            "players_list": players_as_dicts,
            "general remarks": self.general_remarks
        }

    @staticmethod
    def from_dict_tournament(tournament_dict):
        """Instantiate a tournament from a dictionnary."""
        # Instantiate player list from dictionary
        players_list = [
            Player.from_dict_player(player_dict) 
            for player_dict in tournament_dict["players_list"]
        ]

        # Instantiate round list from dictionary
        rounds_list = [
            Round.from_dict_round(round_dict)
            for round_dict in tournament_dict["rounds_list"]
        ]

        return Tournament(
            name=tournament_dict["name"],
            location=tournament_dict["location"],
            start_date=tournament_dict["start_date"],
            end_date=tournament_dict["end_date"],
            numbers_of_rounds=tournament_dict["numbers of rounds"],
            actual_round=tournament_dict["actual_round"],
            rounds_list=rounds_list,
            players_list=players_list,
            general_remarks=tournament_dict["general remarks"]
        )
    @staticmethod
    def save_tournament(tournament):
        """Save the current state of the tournament to the database."""
        json_file_path = "tournaments.json"

        # Convert the tournament to a dictionary    
        tournament = tournament.to_dict_tournament()
        
        # Check if the file exists
        if os.path.exists(json_file_path):
                with open(json_file_path, "r") as file:
                    tournaments = json.load(file)
        else:
            tournaments = []

        # Check if the tournament already exists
        tournament_exists = False
        for index, existing_tournament in enumerate(tournaments):
            # If exist, update it
            if existing_tournament["name"] == tournament["name"]:
                tournaments[index] = tournament
                tournament_exists = True
                break
        # Add the tournament if it doesn't already exist
        if not tournament_exists:
            tournaments.append(tournament)
        temp_file_path = f"{json_file_path}.tmp"
        with open(temp_file_path, "w") as file:
            json.dump(tournaments, file, indent=4)
        
        os.replace(temp_file_path, json_file_path)
        
        print(f"Tournament '{tournament['name']}' successfully saved.")

    @staticmethod
    def load_tournaments_from_db():
        json_file_path = "tournaments.json"
        
        with open(json_file_path, "r") as file:
            tournaments = json.load(file)
        return tournaments