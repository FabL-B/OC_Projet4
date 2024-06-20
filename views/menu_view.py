class MenuView:

    def display_main_menu():
        print("Main Menu:")
        print("1. Tournament Menu")
        print("2. Player Menu")
        print("3. Reports Menu")
        print("4. Quit")

    def display_tournament_menu():
        print("\nTournament Menu:")
        print("1. Create a tournament")
        print("2. Play a chosen tournament")
        print("3. Return to main menu")

    def display_player_menu():
        print("\nPlayer Menu:")
        print("1. Display player list")
        print("2. Create a player")
        print("3. Return to main menu")

    def display_reports_menu():
        print("\nReports Menu:")
        print("1. Players reports")
        print("2. Tournaments reports")
        print("3. Return to main menu")

    def user_choice():
        choice = input("\nEnter your choice: ")
        return choice
