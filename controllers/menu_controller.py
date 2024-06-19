from models.tournament import Tournament
from models.player import Player
from controllers.tournament_manager import TournamentManager
from controllers.player_manager import PlayerManager

from views.menu_view import MenuView
from views.tournament_view import TournamentView
from views.player_view import PlayerView

class MenuController:
    """Controller for handling menu interactions."""
    def __init__(self):
        self.player_manager = PlayerManager()
        self.tournament_manager = TournamentManager()

    def display_main_menu(self):
        """Display the main menu and handle user choices."""
        while True:
            print("Main Menu:")
            print("1. Tournament Menu")  #faire des view
            print("2. Player Menu")
            print("3. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.display_tournament_menu()
            elif choice == "2":
                self.display_player_menu()
            elif choice == "3":
                exit()
            else:
                print("Invalid choice, please try again.")

    def display_tournament_menu(self):
        """Display the tournament menu and handle user choices."""
        while True:
            print("\nTournament Menu:")
            print("1. Display tournament infos")  #faire des view
            print("2. Create a tournament")
            print("3. Play a chosen tournament")
            print("4. Return to main menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                selected_tournament = TournamentManager.select_tournament_from_list()
                #display tournaments infos
                #display rounds and matches
                
            elif choice == "2":
                self.tournament_manager.create_new_tournament()
            elif choice == "3":
                selected_tournament = TournamentManager.select_tournament_from_list()
                TournamentManager.play_tournament(selected_tournament)
            elif choice == "4":
                self.display_main_menu()
            else:
                print("Invalid choice, please try again.")

    def display_player_menu(self):
        """Display the player menu and handle user choices."""
        while True:
            print("\nPlayer Menu:")
            print("1. Display player list")  #faire des view
            print("2. Create a player")
            print("3. Return to main menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                players_list = Player.load_players_from_db()
                PlayerView.display_players(players_list)
            elif choice == "2":
                PlayerManager.create_new_player()
            elif choice == "3":
                self.display_main_menu()
            elif choice == "5":
                test_list = self.player_manager.create_players_list()
                PlayerView.display_players(test_list)
            else:
                print("Invalid choice, please try again.")