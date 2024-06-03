import os
import json

from controllers.player_manager import PlayerManager
from models.tournament import Tournament
from views.tournament_view import TournamentView

class TournamentManager:
    """Tournament manager."""
    
    def create_new_tournament():
        """Add a new tournament in data base."""
        name = TournamentView.get_tournament_name()
        location = TournamentView.get_tournament_location()
        start_date = TournamentView.get_tournament_start_date()
        end_date = TournamentView.get_tournament_end_date()
        numbers_of_rounds = TournamentView.get_number_of_rounds()
        actual_round = 0
        rounds_list = []
        players_list = []
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
        
        #Add the new tournament to the data base
        tournament_dict = new_tournament.to_dict_tournament()

        json_file_path = "tournaments.json"
        if os.path.exists(json_file_path):
            with open(json_file_path, 'r') as file:
                tournaments = json.load(file)
        else:
            tournaments = []
        tournaments.append(tournament_dict)

        with open(json_file_path, 'w') as file:
            json.dump(tournaments, file, indent=4)

        return new_tournament

    def checkin_players(self):
        """Add new player in tournament players list"""
        new_player = PlayerManager.create_new_player()
        Tournament.add_player(new_player)
    
    def save_tournament():
        """Save the current state of the tournament to the database."""
        tournament_dict = Tournament.to_dict_tournament()
        
        json_file_path = "tournaments.json"
        if os.path.exists(json_file_path):
            with open(json_file_path, 'r') as file:
                tournaments = json.load(file)
        else:
            tournaments = []

        # Check if the tournament already exists
        for index, existing_tournament in enumerate(tournaments):
            if existing_tournament['name'] == Tournament.name :
                tournaments[index] = tournament_dict
                break
        
        # Add or update the tournament
        tournaments.append(tournament_dict)

        with open(json_file_path, 'w') as file:
            json.dump(tournaments, file, indent=4)
        
        print(f"Tournament {Tournament.name} successfully saved.")
