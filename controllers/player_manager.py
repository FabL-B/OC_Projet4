import os
import json

from models.player import Player
from views.player_view import PlayerView

class PlayerManager:
    """Player manager."""
    
    def create_new_player(self):
        """Add a new player."""
        name = PlayerView.get_player_name()
        surname = PlayerView.get_player_surname()
        birth_date = PlayerView.get_player_birth_date()
        chess_id = PlayerView.get_player_chess_id()
        score_tournament = 0
        
        new_player = Player(name,
                            surname,
                            birth_date,
                            chess_id,
                            score_tournament)
        
        self.save_player_in_db(new_player)
        
        return new_player

    def save_player_in_db(self, player):
        """Save the player in the database."""
        json_file_path = "players.json"
        if os.path.exists(json_file_path):
            with open(json_file_path, "r") as file:
                players_data = json.load(file)
        else:
            players_data = []

        # Convert the player to a dictionary  
        player = player.to_dict_player()

        # Check if the player already exists
        player_in_db = False
        for index, existing_player in enumerate(players_data):
            # If player exist, update it.
            if existing_player["chess_id"] == player["chess_id"]:
                players_data[index] = player
                player_in_db = True
                break
        
        # If not in data base add it.
        if not player_in_db:
            players_data.append(player)
        
        
        with open(json_file_path, "w") as file:
            json.dump(players_data, file, indent=4)
        print(f"Player {player["name"]} updated in data base.")

    def load_players_from_db(self):
        """Load players from the database."""
        json_file_path = "players.json"
        players_list = []

        if os.path.exists(json_file_path):
            with open(json_file_path, "r") as file:
                players_data = json.load(file)
                for player_data in players_data:
                    player = Player.from_dict_player(player_data)
                    players_list.append(player)
        
        return players_list

    def create_players_list(self):
        """Create a list of players for tournament."""
        players_list = []

        while True:
            # Add a player
            new_player = self.create_new_player()
            players_list.append(new_player)
            # Ask if more player to add
            user_request = PlayerView.add_player_request()
            if user_request == "N":
                # Player lists needs to be paire
                if len(players_list) % 2 != 0:
                    print("The number of players is odd you need one more.")
                else:
                    break

        return players_list
