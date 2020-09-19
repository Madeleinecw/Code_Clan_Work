from app.models.game_class import Game

def play_game(player1, player2):
        if player1.move == player2.move:
            return 'Draw'
        elif player1.move == 'Rock' and player2.move == 'Scissors':
            return 'Player 1 Wins, Rock beats Scissors'
        elif player1.move == 'Scissors' and player2.move == 'Paper':
            return 'Player 1 Wins, Scissots beats Paper'
        elif player1.move == 'Paper' and player2.move == 'Rock':
            return 'Player 1 Wins, Paper beats Rock'
        elif player1.move == 'Rock' and player2.move == 'Paper':
            return 'Player 2 Wins, Paper beats Rock'
        elif player1.move == 'Scissors' and player2.move == 'Rock':
            return 'Player 2 Wins, Rock beats Paper'
        elif player1.move == 'Paper' and player2.move == 'Scissors':
            return 'Player 2 Wins, Scissors beats Paper'