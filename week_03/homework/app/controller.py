from flask import render_template, request, redirect, url_for
from app import app
from app.models.game_moves import *
from app.models.game_class import *
from app.models.player_class import *
import random


@app.route('/')
def welcome():
    return render_template('welcome.html', title='Welcome')

@app.route('/play')
def index():
    return render_template('index.html', title='Home')

@app.route('/add-move', methods=['POST'])
def play():
    name1 = request.form["name1"]
    move1 = request.form["moves1"]

    name2 = request.form["name2"]
    move2 = request.form["moves2"]
    player1 = Player(name1, move1)
    player2 = Player(name2, move2)
    computerOptions = ['Rock', 'Paper', 'Scissors']
    computerMove = random.choice(computerOptions)
    computerPlayer = Player('Computer', computerMove)
    computerChecked = True if 'computer' in request.form else False
    if computerChecked:
        game_result = play_game(player1, computerPlayer)      
        if game_result == 'Draw':
            return render_template('result.html', title='result', game_result='Nobody is the Winner', move1=move1, move2=computerPlayer.move)
        else:
            return redirect(f'/{move1}/{computerMove}', code=307)
    else:
        game_result = play_game(player1, player2)
        if game_result == 'Draw':
            return render_template('result.html', title='result', game_result='Nobody is the Winner', move1=move1, move2=move2)
    return redirect(f'/{move1}/{move2}', code=307)

@app.route('/Rock/Scissors', methods=['POST'])
def resultrs():
    name1 = request.form['name1']
    return render_template('result.html', title='result',winner=name1, game_result=' Wins, Rock beats Scissors', move1='Rock', move2='Scissors')

@app.route('/Paper/Rock', methods=['POST'])
def resultpr():
    name1 = request.form['name1']
    return render_template('result.html', title='result', winner=name1, game_result=' Wins, Paper beats Rock', move1='Paper', move2='Rock')

@app.route('/Scissors/Paper', methods=['POST'])
def resultsp():
    name1 = request.form['name1']
    return render_template('result.html', title='result', winner=name1, game_result=' Wins, Scissors beats Paper', move1='Scissors', move2='Paper')

@app.route('/Rock/Paper', methods=['POST'])
def resultrp():
    if 'computer' in request.form:
        name2 = 'Computer'
        return render_template('result.html', title='result',winner=name2, game_result=' Wins, Scissors beats Paper', move1='Paper', move2='Scissors')
    else: name2 = request.form['name2']
    return render_template('result.html', title='result',winner=name2, game_result=' Wins, Paper beats Rock', move1='Rock', move2='Paper')

@app.route('/Paper/Scissors', methods=['POST'])
def resultps():
    if 'computer' in request.form:
        name2 = 'Computer'
        return render_template('result.html', title='result',winner=name2, game_result=' Wins, Scissors beats Paper', move1='Paper', move2='Scissors')
    else: name2 = request.form['name2']
    return render_template('result.html', title='result',winner=name2, game_result=' Wins, Scissors beats Paper', move1='Paper', move2='Scissors')

@app.route('/Scissors/Rock', methods=['POST'])
def resultsr():
    if 'computer' in request.form:
        name2 = 'Computer'
        return render_template('result.html', title='result',winner=name2, game_result=' Wins, Scissors beats Paper', move1='Paper', move2='Scissors')
    else: name2 = request.form['name2']
    return render_template('result.html', title='result',winner=name2, game_result=' Wins, Rock beats Scissors', move1='Scissors', move2='Rock')

