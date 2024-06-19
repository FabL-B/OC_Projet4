from rich.console import Console
from rich.table import Table
from rich.box import HEAVY_HEAD

class TournamentView:

    @staticmethod
    def get_tournament_name():
        """Ask user to enter the player name"""
        return input("Enter the tournament name: ")

    @staticmethod
    def get_tournament_location():
        """Ask user to enter the player name"""
        return input("Enter the tournament location: ")

    @staticmethod
    def get_tournament_start_date():
        """Ask user to enter the player name"""
        return input("Enter the tournament start date (YYYY-MM-DD): ")

    @staticmethod
    def get_tournament_end_date():
        """Ask user to enter the player name"""
        return input("Enter the tournament end date (YYYY-MM-DD): ")

    @staticmethod
    def get_number_of_rounds():
        """Ask user to enter the player name"""
        while True:
            rounds = input("Enter the number of rounds: ")
            if rounds.isdigit():
                return int(rounds)
            else:
                print("Invalid input. Please enter a valid number.")

    @staticmethod
    def get_general_remarks():
        """Ask user to enter the player name"""
        return input("Enter any general remarks for the tournament: ")
    
    @staticmethod
    def ask_add_players_list(): # ??? A VERIFIER
        return input("To add a new player press enter, else press 'q'")
    
    
    def select_tournament_view(tournaments_list):
        """Ask user to select a tournaments from a list"""
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
        print(f"You selected {tournaments_list[choice]["name"]}")
        return tournaments_list[choice]

    def display_tournaments_list(tournaments_list):
        console = Console()
        table = Table(
            title="Tournaments list from database",
            style='green',
            box=HEAVY_HEAD
        )
        table.add_column("N°", style="cyan", justify="left")
        table.add_column("Name", style="cyan", justify="left")
        table.add_column("Location", style="cyan", justify="left")
        table.add_column("Start date", style="cyan", justify="left")
        table.add_column("End date", style="cyan", justify="left")
        table.add_column("Numbers of rounds", style="cyan", justify="left")
        table.add_column("Actual round", style="cyan", justify="left")
        table.add_column("General remarks", style="cyan", justify="left")
        
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
        console = Console()
        table = Table(
            title="Tournaments list from database",
            style='green',
            box=HEAVY_HEAD
        )
        table.add_column("Name", style="cyan", justify="left")
        table.add_column("Location", style="cyan", justify="left")
        table.add_column("Start date", style="cyan", justify="left")
        table.add_column("End date", style="cyan", justify="left")
        table.add_column("Numbers of rounds", style="cyan", justify="left")
        table.add_column("Actual round", style="cyan", justify="left")
        table.add_column("General remarks", style="cyan", justify="left")
        

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
