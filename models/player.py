import os
import json


class Player:
    """A class that defines player."""

    def __init__(self, name, surname, chess_id, birth_date, score_tournament):
        """Initialize a player."""
        self.name = name
        self.surname = surname
        self.chess_id = chess_id
        self.birth_date = birth_date
        self.score_tournament = score_tournament

    @staticmethod
    def save_player_in_db(player):
        """Save the player in the database."""
        json_file_path = "players.json"
        if os.path.exists(json_file_path):
            with open(json_file_path, "r") as file:
                players_data = json.load(file)
        else:
            players_data = []

        # Convert the player to a dictionary
        player_dict = player.to_dict_player()

        # Check if the player already exists
        player_in_db = False
        for index, existing_player in enumerate(players_data):
            # If player exists, update it.
            if existing_player["chess_id"] == player_dict["chess_id"]:
                players_data[index] = player_dict
                player_in_db = True
                break

        # If not in database, add it.
        if not player_in_db:
            players_data.append(player_dict)

        with open(json_file_path, "w") as file:
            json.dump(players_data, file, indent=4)

        print(f"Player {player.name} updated in database.")

    @staticmethod
    def load_players_from_db():
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

    def to_dict_player(self):
        """Set player data in dictionary."""
        return {
            "name": self.name,
            "surname": self.surname,
            "birth_date": self.birth_date,
            "chess_id": self.chess_id,
            "score_tournament": self.score_tournament
        }

    @staticmethod
    def from_dict_player(player_data):
        """Create a Player instance from a dictionary."""
        return Player(
            name=player_data["name"],
            surname=player_data["surname"],
            chess_id=player_data["chess_id"],
            birth_date=player_data["birth_date"],
            score_tournament=player_data["score_tournament"]
        )
