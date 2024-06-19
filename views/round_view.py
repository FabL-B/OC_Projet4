class RoundView:
    
    def match_view(match):
        player1 = match.players[0][0]
        player2 = match.players[1][0]
        print(f"Macth opposing {player1.name} VS {player2.name}")
    
    def set_scores_view(player1, player2):
        print(f"Enter score for {player1.name} {player1.surname} (0, 0.5, 1): ")
        score1 = float(input())
        print(f"Enter score for {player2.name} {player2.surname} (0, 0.5, 1): ")
        score2 = float(input())
        return score1, score2
    
    def display_round(round_list):
        pass