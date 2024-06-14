
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
    
    @staticmethod
    def select_tournament_view(tournaments):
        """Ask user to select a tournaments from a list"""
        for idx, tournament in enumerate(tournaments, 1):
            print(f"{idx}. {tournament['name']}")
        choice = int(input("Choose a tournament to play: ")) - 1
        return tournaments[choice]
