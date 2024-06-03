import os
import json

from models.player import Player
from views.player_view import PlayerView

class PlayerManager:
    """Player manager."""
    
    def create_new_player():
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
        
        
        player_dict = new_player.to_dict_player()
        
        json_file_path = "players.json"
        if os.path.exists(json_file_path):
            with open(json_file_path, 'r') as file:
                players = json.load(file)
        else:
            players = []
        players.append(player_dict)

        with open(json_file_path, 'w') as file:
            json.dump(players, file, indent=4)
            
        return new_player


    def save_player_in_db():
        """Save the player object to the database (JSON file)."""
        player_dict = Player.to_dict_player()
        
        json_file_path = "players.json"
        if os.path.exists(json_file_path):
            with open(json_file_path, 'r') as file:
                players = json.load(file)
        else:
            players = []
        
        # Check if the player already exists
        for existing_player in players:
            if existing_player['chess_id'] == Player.chess_id:
                print(f"Player with chess_id {Player.chess_id} already exists.")
                return None
            else:
                # Add new player
                players.append(player_dict)
                with open(json_file_path, 'w') as file:
                    json.dump(players, file, indent=4)
                print(f"Player {Player.chess_id} added in data base.")

    def modify_player():
        pass
