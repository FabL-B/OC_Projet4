from rich.console import Console
from rich.table import Table
from rich.box import HEAVY_HEAD


class RoundView:

    def match_view(match):
        player1 = match.player_scores[0][0]
        player2 = match.player_scores[1][0]
        print(f"Macth opposing {player1.name} VS {player2.name}")

    def set_scores_view(player1, player2):
        print(f"Enter score for {player1.name} {player1.surname} (0, 0.5, 1): ")
        score1 = float(input())
        print(f"Enter score for {player2.name} {player2.surname} (0, 0.5, 1): ")
        score2 = float(input())
        return score1, score2

    def display_rounds(round_list):
        console = Console()
        table = Table(
            title="rounds list from database",
            style='green',
            box=HEAVY_HEAD
        )
        table.add_column("Round number", style="cyan", justify="left")
        table.add_column("Round start time", style="cyan", justify="left")
        table.add_column("Round end time", style="cyan", justify="left")
        table.add_column("Matches", style="cyan", justify="left")

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
        console.print(table)
        print()
