from rich.console import Console
from rich.table import Table
from rich.box import HEAVY_HEAD

class PlayerView:  

    @staticmethod
    def get_player_name():
        """Ask user to enter the player name"""
        name = input("Enter the name of the player: ")
        return name
    
    @staticmethod
    def get_player_surname():
        """Ask user to enter the player surname"""
        surname = input("Enter the surname of the player: ")
        return surname
        
    @staticmethod
    def get_player_birth_date():
        """Ask user to enter the player birth date"""
        birth_date = input("Enter the birth date of the player: ")
        return birth_date
    
    @staticmethod
    def get_player_chess_id():
        """Ask user to enter the player chess ID"""
        chess_id = input("Enter the Chess ID of the player: ")
        return chess_id
    
    @staticmethod
    def add_player_request():
        while True:
            user_request = input(
                "Do you want to add another player (Y/N)?").strip().upper()
            if user_request != "N" and user_request != "Y":
                print("You need to type 'Y' or 'N'")
            else:
                break
        
        return user_request

    def display_players(players_list):
        console = Console()
        table = Table(
            title="Players list from database",
            style="green",
            box=HEAVY_HEAD
        )
        table.add_column("N°", style="blue", justify="left")
        table.add_column("Name", style="blue", justify="left")
        table.add_column("Surname", style="blue", justify="left")
        table.add_column("Chess ID", style="blue", justify="left")
        table.add_column("Birth date", style="blue", justify="left")
        
        for idx, player in enumerate(players_list, start=1):
            table.add_row(
                str(idx),
                player.name,
                player.surname,
                player.chess_id,
                player.birth_date
            )
        console.print(table)
        
