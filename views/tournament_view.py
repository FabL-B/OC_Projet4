class TournamentView:

    def get_tournament_name():
        """Ask user to enter the player name"""
        return input("Enter the tournament name: ")

    def get_tournament_location():
        """Ask user to enter the player name"""
        return input("Enter the tournament location: ")

    def get_tournament_start_date():
        """Ask user to enter the player name"""
        return input("Enter the tournament start date (YYYY-MM-DD): ")

    def get_tournament_end_date():
        """Ask user to enter the player name"""
        return input("Enter the tournament end date (YYYY-MM-DD): ")

    def get_number_of_rounds():
        """Ask user to enter the player name"""
        rounds = input("Enter the number of rounds: ")
        return int(rounds)

    def get_general_remarks():
        """Ask user to enter the player name"""
        return input("Enter any general remarks for the tournament: ")
    
    def ask_add_players_list():
        return input("To add a new player press enter, else press 'q'")