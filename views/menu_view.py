class MenuView:

    def display_main_menu():
        """Display main menu."""
        print("Main Menu:")
        print("1. Tournament Menu")
        print("2. Player Menu")
        print("3. Reports Menu")
        print("4. Quit")

    def display_tournament_menu():
        """Display tournament menu."""
        print("\nTournament Menu:")
        print("1. Create a tournament")
        print("2. Play a chosen tournament")
        print("3. Return to main menu")

    def display_player_menu():
        """Display player menu."""
        print("\nPlayer Menu:")
        print("1. Display player list")
        print("2. Create a player")
        print("3. Return to main menu")

    def display_reports_menu():
        """Display reports menu."""
        print("\nReports Menu:")
        print("1. Players reports")
        print("2. Tournaments reports")
        print("3. Return to main menu")

    def user_choice():
        """Ask user to chose."""
        choice = input("\nEnter your choice: ")
        return choice

    def invalid_choice():
        """Display invalid choice error."""
        print("Invalid choice, please try again.")
