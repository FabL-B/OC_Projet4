from controllers.match_controller import Match, MatchController


players = [
    {
        "name": "Magnus",
        "surname": "Carlsen",
        "chess_id": "1503014",
        "birth_date": "1990-11-30",
        "score_tournament": 0
    },
    {
        "name": "Fabiano",
        "surname": "Caruana",
        "chess_id": "2020009",
        "birth_date": "1992-07-30",
        "score_tournament": 0
    },
    {
        "name": "Ding",
        "surname": "Liren",
        "chess_id": "8603677",
        "birth_date": "1992-10-24",
        "score_tournament": 0
    },
    {
        "name": "Ian",
        "surname": "Nepomniachtchi",
        "chess_id": "4168119",
        "birth_date": "1990-07-14",
        "score_tournament": 0
    }
]

players_pair = [
    {
        "name": "Magnus",
        "surname": "Carlsen",
        "chess_id": "1503014",
        "birth_date": "1990-11-30",
        "score_tournament": 0
    },
    {
        "name": "Fabiano",
        "surname": "Caruana",
        "chess_id": "2020009",
        "birth_date": "1992-07-30",
        "score_tournament": 0
    }]



MatchController.play_match(players_pair)