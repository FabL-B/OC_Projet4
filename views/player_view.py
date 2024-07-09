from rich.console import Console
from rich.table import Table
from rich.box import HEAVY_HEAD
from datetime import datetime


class PlayerView:

    @staticmethod
    def get_player_name():
        """Ask user to enter the player name."""
        name = input("Enter the name of the player: ")
        return name

    @staticmethod
    def get_player_surname():
        """Ask user to enter the player surname."""
        surname = input("Enter the surname of the player: ")
        return surname

    @staticmethod
    def get_player_birth_date():
        """Ask user to enter the player birth date."""
        while True:
            user_input = input("Enter the birth date of the player(YYYY-MM-DD): ")
            try:
                birth_date = datetime.strptime(user_input, '%Y-%m-%d')
                return birth_date.strftime('%Y-%m-%d')
            except ValueError:
                print("The date format is incorrect. Please enter the date in the format YYYY-MM-DD.")

    @staticmethod
    def get_player_chess_id():
        """Ask user to enter the player chess ID."""
        chess_id = input("Enter the Chess ID of the player: ")
        return chess_id

    @staticmethod
    def add_player_request():
        """Ask user if more players needs to be add in a list."""
        while True:
            user_request = input(
                "Do you want to add another player (Y/N)?").strip().upper()
            if user_request in ["Y", "N"]:
                return user_request
            else:
                print("You need to type 'Y' or 'N'")

    @staticmethod
    def invalid_player_list():
        """Inform user that the players list cannot be odd number."""
        print("The number of players is odd; you need one more.")

    @staticmethod
    def invalid_choice():
        """Display invalid choice error."""
        print("Invalid choice. Please choose a number within the range.")

    @staticmethod
    def invalid_input():
        """Display invalid input error."""
        print("Invalid input. Please enter a number.")

    @staticmethod
    def select_player_from_db():
        """Ask user to chose a player from a list."""
        print("if the player is not in database enter '0': ")
        choice = int(input("Enter the number of the player to add: ")) - 1
        return choice

    def display_players(players_list):
        """Display a list of players."""
        console = Console()
        table = Table(
            title="Players list",
            style="green",
            box=HEAVY_HEAD
        )
        table.add_column("N°", style="magenta", justify="left")
        table.add_column("Surname", style="cyan3", justify="left")
        table.add_column("Name", style="cyan3", justify="left")
        table.add_column("Chess ID", style="cyan", justify="left")
        table.add_column("Birth date", style="cyan2", justify="left")
        table.add_column("Score tournament", style="cyan2", justify="center")

        for idx, player in enumerate(players_list, start=1):
            table.add_row(
                str(idx),
                player.surname,
                player.name,
                player.chess_id,
                player.birth_date,
                str(player.score_tournament)
            )
        console.print(table)
        print()
