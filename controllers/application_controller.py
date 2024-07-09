from models.player import Player
from controllers.tournament_manager import TournamentManager
from controllers.player_manager import PlayerManager

from views.menu_view import MenuView
from views.tournament_view import TournamentView
from views.player_view import PlayerView
from views.round_view import RoundView


class ApplicationController:
    """Controller for handling application."""

    def __init__(self):
        self.player_manager = PlayerManager()
        self.tournament_manager = TournamentManager()
        self.tournament_view = TournamentView()

    def display_main_menu(self):
        """Display the main menu and handle user choices."""
        while True:
            MenuView.display_main_menu()
            choice = MenuView.user_choice()

            # 1 Tournament menu.
            if choice == "1":
                self.display_tournament_menu()
            # 2 Player menu.
            elif choice == "2":
                self.display_player_menu()
            # 3 reports menu.
            elif choice == "3":
                self.display_reports_menu()
            # 4 Exit.
            elif choice == "4":
                exit()
            else:
                MenuView.invalid_choice()

    def display_tournament_menu(self):
        """Display the tournament menu and handle user choices."""
        while True:
            MenuView.display_tournament_menu()
            choice = MenuView.user_choice()

            # 1 Create a new tournament.
            if choice == "1":
                self.tournament_manager.create_new_tournament()
            # 2 Play a chosen tournament.
            elif choice == "2":
                selected_tournament = self.tournament_manager.select_tournament_from_list()
                if selected_tournament.actual_round == selected_tournament.numbers_of_rounds:
                    self.tournament_view.selected_tournament_is_over()
                else:
                    self.tournament_manager.play_tournament(selected_tournament)
            # 3 Return to main menu.
            elif choice == "3":
                self.display_main_menu()
            else:
                MenuView.invalid_choice()

    def display_player_menu(self):
        """Display the player menu and handle user choices."""
        while True:
            MenuView.display_player_menu()
            choice = MenuView.user_choice()

            # 1 Display players from database.
            if choice == "1":
                players_list = Player.load_players_from_db()
                players_list = self.player_manager.sort_players_list_by_name(players_list)
                PlayerView.display_players(players_list)
            # 2 Create a new player in database.
            elif choice == "2":
                self.player_manager.create_new_player()
            # 3 Return to main menu.
            elif choice == "3":
                self.display_main_menu()
            else:
                MenuView.invalid_choice()

    def display_reports_menu(self):
        """Display the reports menu and handle user choices."""
        while True:
            MenuView.display_reports_menu()
            choice = MenuView.user_choice()

            # 1 Players report.
            if choice == "1":
                players_list = Player.load_players_from_db()
                PlayerView.display_players(players_list)
            # 2 Tournament reports.
            elif choice == "2":
                selected_tournament = self.tournament_manager.select_tournament_from_list()
                if selected_tournament:
                    # Display selected tournament infos.
                    TournamentView.display_selected_tournament(selected_tournament)
                    # Display players info in this tournament.
                    PlayerView.display_players(selected_tournament.players_list)
                    # Display rounds and their matches.
                    RoundView.display_rounds(selected_tournament.rounds_list)
            # 3 Return to main menu.
            elif choice == "3":
                return
            else:
                MenuView.invalid_choice()
