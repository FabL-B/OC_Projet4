from rich.console import Console
from rich.table import Table
from rich.box import HEAVY_HEAD


class RoundView:
    """A class to represent the view for rounds in a tournament."""
    
    def set_scores_view(player):
        """Ask user to enter a valid score for the given player."""
        valid_scores = [0, 0.5, 1]
        print(f"Enter score for {player.name} {player.surname} (0, 0.5, 1): ")
        while True:
            try:
                score = float(input())
                if score in valid_scores:
                    return score
                else:
                    print("Invalid score. Please enter 0, 0.5, or 1.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def display_match_view(match):
        """Display names of the players opposing each other in the match."""
        player1 = match.player_scores[0][0]
        player2 = match.player_scores[1][0]
        print(f"Macth opposing {player1.name} VS {player2.name}")

    def display_rounds(round_list):
        """Display rounds list and each matches for the round."""
        console = Console()
        table = Table(
            title="Rounds list",
            style="green",
            box=HEAVY_HEAD
        )
        table.add_column("Round number", style="magenta", justify="center")
        table.add_column("Round start time", style="cyan2", justify="left")
        table.add_column("Round end time", style="cyan2", justify="left")
        table.add_column("Matches", style="cyan3", justify="center")

        for round in round_list:
            matches = round.matches_list
            for match in matches:
                match_info = f"{match.player_scores[0][0].name} {match.player_scores[0][1]} VS {match.player_scores[1][1]} {match.player_scores[1][0].name}"
                table.add_row(
                    str(round.round_number),
                    str(round.start_date_time),
                    str(round.end_date_time),
                    str(match_info)
                )
            table.add_section()
        console.print(table)
        print()
