import os
import json

from controllers.player_manager import PlayerManager
from models.tournament import Tournament
from views.tournament_view import TournamentView

class TournamentManager:
    """Tournament manager."""
    
    def __init__(self):
        pass
    
    def create_new_tournament(self):
        """Add a new tournament in data base."""
        # Create the tournaments general infos.
        name = TournamentView.get_tournament_name()
        location = TournamentView.get_tournament_location()
        start_date = TournamentView.get_tournament_start_date()
        end_date = TournamentView.get_tournament_end_date()
        numbers_of_rounds = TournamentView.get_number_of_rounds()
        actual_round = 0
        rounds_list = []
        players_list = PlayerManager().create_players_list()
        general_remarks = TournamentView.get_general_remarks()
        
        new_tournament = Tournament(name,
                                    location,
                                    start_date,
                                    end_date,
                                    numbers_of_rounds,
                                    actual_round,
                                    rounds_list,
                                    players_list,
                                    general_remarks
                                    )
        self.save_tournament(new_tournament)
        return new_tournament
        
    
    def save_tournament(self, tournament):
        """Save the current state of the tournament to the database."""
        json_file_path = "tournaments.json"
        
        # Convert each player in the players_list to a dictionary
        for index, player in enumerate(tournament.players_list):
            tournament.players_list[index] = player.to_dict_player()
        
        # Convert the tournament to a dictionary    
        tournament = tournament.to_dict_tournament()
        
        # Check if the file exists and is not empty
        if os.path.exists(json_file_path) and os.path.getsize(json_file_path) > 0:
            try:
                with open(json_file_path, "r") as file:
                    tournaments = json.load(file)
            except json.JSONDecodeError:
                tournaments = []
        else:
            tournaments = []

        # Check if the tournament already exists
        tournament_exists = False
        for index, existing_tournament in enumerate(tournaments):
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