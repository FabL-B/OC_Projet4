class PlayerView:  

    def get_player_name():
        """Ask user to enter the player name"""
        name = input("Enter the name of the player: ")
        return name
    
    def get_player_surname():
        """Ask user to enter the player surname"""
        surname = input("Enter the surname of the player: ")
        return surname
        
    def get_player_birth_date():
        """Ask user to enter the player birth date"""
        birth_date = input("Enter the birth date of the player: ")
        return birth_date
    
    def get_player_chess_id():
        """Ask user to enter the player chess ID"""
        chess_id = input("Enter the Chess ID of the player: ")
        return chess_id
    
    def add_player_request():
        while True:
            user_request = input(
                "Do you want to add another player (Y/N)?").strip().upper()
            if user_request != "N" and user_request != "Y":
                print("You need to type 'Y' or 'N'")
            else:
                break
        
        return user_request