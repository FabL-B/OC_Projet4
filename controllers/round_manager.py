from models.round import Round

class RoundManager:
    """round manager."""
    
    def __init__(self):
        pass
    
    def create_new_round(self, tournament):
        """Create a new round."""
        round_number = tournament.actual_round
        start_date_time = Round.start_round_modelstart_round
        end_date_time = ""
        matchs_list = []
        players_list = tournament.players_list
        round = Round(round_number,
                      start_date_time,
                      end_date_time,
                      matchs_list,
                      players_list,
                          )
        # créer une liste de paires de joueurs (matchs)
        for player in players_list:
            pass
        # rentrer résultats des matchs
        # mettre à jour score des joueurs
        # save player data
        # ajouter round à la liste de round du tournoi
        # save tournament data
        
    