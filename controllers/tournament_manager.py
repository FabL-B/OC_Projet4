from models.tournament import Tournament
from controllers.round_manager import RoundManager
from controllers.player_manager import PlayerManager
from views.tournament_view import TournamentView

class TournamentManager:
    """Tournament manager."""

    def __init__(self):
        self.player_manager = PlayerManager()
        self.tournament_view = TournamentView()

    def select_tournament_from_list(self):
        tournaments_list = Tournament.load_tournaments_from_db()
        if not tournaments_list:
            print("No tournaments available.")
            return
        # Display the tournaments list
        TournamentView.display_tournaments_list(tournaments_list)
        # Select the tournament from list with index
        selected_tournament = TournamentView.select_tournament_view(tournaments_list)
        # Instantiate the selected tournament    
        selected_tournament = Tournament.from_dict_tournament(selected_tournament)
        return selected_tournament

    def play_tournament(self, selected_tournament):

        selected_tournament.actual_round += 1
        for i in range(selected_tournament.actual_round, selected_tournament.numbers_of_rounds + 1):
            round_manager = RoundManager()
            new_round = round_manager.create_new_round(selected_tournament)
            print(f"Starting Round {i}")
            for match in new_round.matches_list:
                round_manager.enter_match_result(match)
            new_round.end_round()
            print(f"Round {i} completed.")
            selected_tournament.rounds_list.append(new_round)
            selected_tournament.actual_round += 1
            Tournament.save_tournament(selected_tournament)

            if selected_tournament.actual_round == selected_tournament.numbers_of_rounds + 1:
                print(f"Tournament {selected_tournament.name} is over")
                return

            print("Play new round or exit? (P to play, N to exit)")
            answer = input().capitalize()
            if answer == "N":
                break
        print("Returning to menu.")

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
