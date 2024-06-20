from models.player import Player
from views.player_view import PlayerView


class PlayerManager:
    """Player manager."""

    def __init__(self):
        self.players = Player.load_players_from_db()

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
        players_list_for_tournament = []
        players_list_from_db = Player.load_players_from_db()
        players_list_from_db = self.sort_players_list_by_name(players_list_from_db)

        while True:
            PlayerView.display_players(players_list_from_db)
            selected_player = self.select_player_from_db(players_list_from_db)
            if selected_player is None:
                new_player = self.create_new_player()
                if new_player:
                    players_list_for_tournament.append(new_player)
            else:
                players_list_for_tournament.append(selected_player)
                players_list_from_db.remove(selected_player)

            # Ask if more players to add
            user_request = PlayerView.add_player_request()
            if user_request == "N":
                # Player list needs to be even
                if len(players_list_for_tournament) % 2 != 0:
                    print("The number of players is odd; you need one more.")
                else:
                    break
        return players_list_for_tournament

    def sort_players_list_by_name(self, players_list):
        return sorted(players_list, key=lambda player: (player.surname, player.name))

    def select_player_from_db(self, players_list):
        """Ask user to select a tournaments from a list"""
        while True:
            try:
                print("if the player is not in database enter '0': ")
                choice = int(input(
                    "Enter the number of the player to add: ")) - 1
                if 0 <= choice < len(players_list):
                    break
                elif choice == -1:
                    return None
                else:
                    print(
                        "Invalid choice. Please choose a number within the range.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        print()
        print(f"You selected {players_list[choice].name}")
        return players_list[choice]
