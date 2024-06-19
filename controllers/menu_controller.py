from models.tournament import Tournament
from models.player import Player
from controllers.tournament_manager import TournamentManager
from controllers.player_manager import PlayerManager

from views.menu_view import MenuView
from views.tournament_view import TournamentView
from views.player_view import PlayerView
from views.round_view import RoundView

class MenuController:
    """Controller for handling menu interactions."""
    def __init__(self):
        self.player_manager = PlayerManager()
        self.tournament_manager = TournamentManager()

    def display_main_menu(self):
        """Display the main menu and handle user choices."""
        while True:
            MenuView.display_main_menu()
            choice = MenuView.user_choice()

            if choice == "1":
                self.display_tournament_menu()
            elif choice == "2":
                self.display_player_menu()
            elif choice == "3":
                self.display_reports_menu()
            elif choice == "4":
                exit()
            else:
                print("Invalid choice, please try again.")

    def display_tournament_menu(self):
        """Display the tournament menu and handle user choices."""
        while True:
            MenuView.display_tournament_menu()
            choice = MenuView.user_choice()

            if choice == "1":
                self.tournament_manager.create_new_tournament()
            elif choice == "2":
                selected_tournament = TournamentManager.select_tournament_from_list()
                TournamentManager.play_tournament(selected_tournament)
            elif choice == "3":
                self.display_main_menu()
            else:
                print("Invalid choice, please try again.")

    def display_player_menu(self):
        """Display the player menu and handle user choices."""
        while True:
            MenuView.display_player_menu
            choice = MenuView.user_choice()

            if choice == "1":
                players_list = Player.load_players_from_db()
                PlayerView.display_players(players_list)
            elif choice == "2":
                PlayerManager.create_new_player()
            elif choice == "3":
                self.display_main_menu()
            elif choice == "5":#a supprimer
                test_list = self.player_manager.create_players_list()
                PlayerView.display_players(test_list)
            else:
                print("Invalid choice, please try again.")

    def display_reports_menu(self):
        """Display the reports menu and handle user choices."""
        while True:
            MenuView.display_reports_menu()
            choice = MenuView.user_choice()
            
            if choice == "1":
                players_list = Player.load_players_from_db()
                PlayerView.display_players(players_list)
            elif choice == "2":
                            #demander de choisir un tournoi
                    #demander d'afficher la liste des joueurs du tournoi
                    #demander d'afficher la liste des rounds et matchs du tournoi
                selected_tournament = TournamentManager.select_tournament_from_list()
                TournamentView.display_selected_tournament(selected_tournament)
                PlayerView.display_players(selected_tournament.players_list)
                RoundView.display_rounds(selected_tournament.rounds_list)
            elif choice == "3":
                self.display_main_menu()
            else:
                print("Invalid choice, please try again.")        
