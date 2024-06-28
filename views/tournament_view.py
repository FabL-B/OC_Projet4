from rich.console import Console
from rich.table import Table
from rich.box import HEAVY_HEAD
from datetime import datetime


class TournamentView:
    """A class to represent the view for tournaments."""

    @staticmethod
    def get_tournament_name():
        """Ask user to enter the tournament name"""
        return input("\nEnter the tournament name: ")

    @staticmethod
    def get_tournament_location():
        """Ask user to enter the tournament location"""
        return input("\nEnter the tournament location: ")

    @staticmethod
    def get_tournament_start_date():
        """Ask user to enter the tournament start date."""
        while True:
            user_input = input("\nEnter the tournament start date (YYYY-MM-DD): ")
            try:
                tournament_date = datetime.strptime(user_input, '%Y-%m-%d')
                return tournament_date.strftime('%Y-%m-%d')
            except ValueError:
                print("The date format is incorrect. Please enter the date in the format YYYY-MM-DD.")

    @staticmethod
    def get_tournament_end_date():
        """Ask user to enter the tournament end date."""
        while True:
            user_input = input("\nEnter the tournament end date (YYYY-MM-DD): ")
            try:
                tournament_date = datetime.strptime(user_input, '%Y-%m-%d')
                return tournament_date.strftime('%Y-%m-%d')
            except ValueError:
                print("The date format is incorrect. Please enter the date in the format YYYY-MM-DD.")

    @staticmethod
    def get_number_of_rounds():
        """Ask user to enter the numbers of rounds."""
        while True:
            rounds = input("\nEnter the number of rounds: ")
            if rounds.isdigit():
                return int(rounds)
            else:
                print("Invalid input. Please enter a valid number.")

    @staticmethod
    def get_general_remarks():
        """Ask user to enter general remarks."""
        return input("\nEnter any general remarks for the tournament: ")

    @staticmethod
    def selected_tournament_is_over():
        """Display error message when trying to play a completed tournament."""
        print("This tournament is over and cannot be played anymore.")

    def get_play_new_round_or_exit(self):
        """Ask user to play a new round or exit."""
        while True:
            choice = input("\nDo you want to play new round? (Y/N): ").strip().upper()
            if choice in ["Y", "N"]:
                return choice
            else:
                print("Invalid input. Please enter 'P' to play or 'N' to exit.")

    def select_tournament_view(tournaments_list):
        """Ask user to select a tournaments from a list."""
        while True:
            try:
                choice = int(input(
                    "Enter the number of the tournament to play: ")) - 1
                if 0 <= choice < len(tournaments_list):
                    break
                else:
                    print(
                        "Invalid choice. Please choose a number within the range.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        print()
        print(f"\nYou selected {tournaments_list[choice]["name"]}")
        return tournaments_list[choice]

    def display_starting_round(self, round_number):
        """Display indication of the starting of a round in tournament."""
        print(f"\nStarting Round {round_number}")

    def display_round_completed(self, round_number):
        """Display indication of the ending of a round in tournament."""
        print(f"\nRound {round_number} completed.")

    def display_tournament_over(self, tournament_name):
        """Display indication of the ending of a tournament."""
        print(f"\nTournament {tournament_name} is over")

    def display_tournaments_list(tournaments_list):
        """Display a list of tournaments in a table."""
        console = Console()
        table = Table(
            title="Tournaments list",
            style="green",
            box=HEAVY_HEAD
        )
        table.add_column("N°", style="magenta", justify="left")
        table.add_column("Name", style="cyan3", justify="left")
        table.add_column("Location", style="cyan3", justify="left")
        table.add_column("Start date", style="cyan2", justify="left")
        table.add_column("End date", style="cyan2", justify="left")
        table.add_column("Numbers of rounds", style="magenta", justify="left")
        table.add_column("Actual round", style="magenta", justify="left")
        table.add_column("General remarks", style="cyan3", justify="left")

        for idx, tournament in enumerate(tournaments_list, start=1):
            table.add_row(
                str(idx),
                tournament["name"],
                tournament["location"],
                tournament["start_date"],
                tournament["end_date"],
                str(tournament["numbers of rounds"]),
                str(tournament["actual_round"]),
                tournament["general remarks"]
            )
        console.print(table)
        print()

    def display_selected_tournament(selected_tournament):
        """Display informations about a selected tournament in a table."""
        console = Console()
        table = Table(
            title=f"Tournament {selected_tournament.name} infos",
            style="green",
            box=HEAVY_HEAD
        )
        table.add_column("Name", style="cyan3", justify="left")
        table.add_column("Location", style="cyan", justify="left")
        table.add_column("Start date", style="cyan2", justify="left")
        table.add_column("End date", style="cyan2", justify="left")
        table.add_column("Numbers of rounds", style="magenta", justify="left")
        table.add_column("Actual round", style="magenta", justify="left")
        table.add_column("General remarks", style="cyan3", justify="left")

        table.add_row(
            selected_tournament.name,
            selected_tournament.location,
            selected_tournament.start_date,
            selected_tournament.end_date,
            str(selected_tournament.numbers_of_rounds),
            str(selected_tournament.actual_round),
            selected_tournament.general_remarks
            )
        console.print(table)
        print()
