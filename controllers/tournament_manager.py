from models.tournament import Tournament
from models.player import Player
from models.round import Round
from controllers.round_manager import RoundManager
from controllers.player_manager import PlayerManager
from views.tournament_view import TournamentView

class TournamentManager:
    """Tournament manager."""
    
    def __init__(self):
        self.player_manager = PlayerManager()
        self.round_manager = RoundManager()
        self.tournament_view = TournamentView()

    def select_tournament_from_list():
        tournaments = Tournament.load_tournaments_from_db()
        if not tournaments:
            print("No tournaments available.")
            return
        selected_tournament = TournamentView.select_tournament_view(tournaments)

        # Instantiate player list and round list from dictionnary
        players_list = []
        for player_dict in selected_tournament["players_list"]:
            player = Player.from_dict_player(player_dict)
            players_list.append(player)
        rounds_list = []
        for round_dict in selected_tournament["rounds list"]:
            round_instance = Round.from_dict_round(round_dict)
            rounds_list.append(round_instance)
        
        # Instantiate the selected tournament    
        selected_tournament = Tournament.from_dict_tournament({
                **selected_tournament,
                "players_list": players_list,
                "rounds_list": rounds_list
            })
        return selected_tournament
    
    def play_tournament(selected_tournament):
        actual_round = selected_tournament.actual_round
        print("round : ", actual_round)
        for i in range(actual_round, selected_tournament.numbers_of_rounds + 1):
            print(f"Starting Round {i}")
            new_round = RoundManager.create_new_round(selected_tournament)
            print(f"Round {i} matches:")
            for match in new_round.matchs_list:
                player1, player2 = match.players[0][0], match.players[1][0]
                print(f"{player1.name} {player1.surname} vs {player2.name} {player2.surname}")
                
                RoundManager.enter_matchs_results(new_round.matchs_list)
                new_round.end_round()
                print(f"Round {i} completed.")
                Tournament.save_tournament(selected_tournament)
                
            print(f"Round {i} completed.")
            actual_round += 1
            selected_tournament.actual_round = actual_round

        print("Tournament completed.")

    
    def create_new_tournament(self):
        """Add a new tournament in data base."""
        name = TournamentView.get_tournament_name()
        location = TournamentView.get_tournament_location()
        start_date = TournamentView.get_tournament_start_date()
        end_date = TournamentView.get_tournament_end_date()
        numbers_of_rounds = TournamentView.get_number_of_rounds()
        actual_round = 0
        rounds_list = []
        players_list = self.player_manager.create_players_list()
        general_remarks = TournamentView.get_general_remarks()
        
        new_tournament = Tournament(
            name,
            location,
            start_date,
            end_date,
            numbers_of_rounds,
            actual_round,
            rounds_list,
            players_list,
            general_remarks
        )
        Tournament.save_tournament(new_tournament)