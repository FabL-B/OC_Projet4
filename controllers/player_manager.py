from models.player import Player
from views.player_view import PlayerView

class PlayerManager:
    """Player manager."""
    
    def __init__(self):
        self.players = Player.load_players_from_db() #liste de joueurs

    def create_new_player(self):
        """Add a new player."""
        name = PlayerView.get_player_name()
        surname = PlayerView.get_player_surname()
        birth_date = PlayerView.get_player_birth_date()
        chess_id = PlayerView.get_player_chess_id()
        score_tournament = 0
        
        new_player = Player(name, surname, chess_id, birth_date, score_tournament)
        Player.save_player_in_db(new_player)
        return new_player

    def create_players_list(self):
        """Create a list of players for tournament."""
        players_list = []
        
         # A voir pour les selectionner depuis la base de données
        
        while True:
            # Add a player
            new_player = self.create_new_player()
            players_list.append(new_player)
            
            # Ask if more players to add
            user_request = PlayerView.add_player_request()
            if user_request == "N":
                # Player list needs to be even
                if len(players_list) % 2 != 0:
                    print("The number of players is odd; you need one more.")
                else:
                    break

        return players_list
