import os
import json

from controllers.player_manager import PlayerManager
from models.tournament import Tournament
from views.tournament_view import TournamentView
from controllers.round_manager import RoundManager

class TournamentManager:
    """Tournament manager."""
    
    def __init__(self):
        self.round_manager = RoundManager()

    def play_tournament(self, tournament):
        for i in range(1, tournament.numbers_of_rounds + 1):
            tournament.actual_round = i
            print(f"Starting Round {i}")
            new_round = self.round_manager.create_new_round(tournament)
            print(f"Round {i} matches:")
            for match in new_round.matchs_list:
                player1, player2 = match.players[0][0], match.players[1][0]
                print(f"{player1.name} {player1.surname} vs {player2.name} {player2.surname}")
                
                self.round_manager.enter_matchs_results(new_round.matchs_list)
                new_round.end_round()
                self.save_tournament(tournament)
                print(f"Round {i} completed.")
                # créer une liste de paires de joueurs (matchs)
                # rentrer résultats des matchs
                # mettre à jour score des joueurs
                # save player data
                # ajouter round à la liste de round du tournoi
                # save tournament data
            # instancier 2ème round actual round = 2
                # créer une liste de paires de joueurs (matchs) en fonction des scores
                # rentrer résultats des matchs
                # mettre à jour score des joueurs
                # save player data
                # ajouter round à la liste de round du tournoi
                # save tournament data    
        print("Tournament completed.")
   
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
        # Convert each player in the players_list to a dictionary
        for index, round in enumerate(tournament.rounds_list):
            tournament.rounds_list[index] = round.to_dict_player()
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

    def load_tournament():
        json_file_path = "tournaments.json"
        
        with open(json_file_path, "r") as file:
            tournaments = json.load(file)
            user_entry = TournamentView.load_tournament_view(tournaments)
            for tournament in tournaments:
                if user_entry == tournament["name"]:
                    loaded_tournament = tournament
        return loaded_tournament
        
