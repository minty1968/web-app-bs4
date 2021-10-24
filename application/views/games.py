"""Routes for Games pages."""
from flask import Blueprint, render_template, request, flash, url_for
from application.models.games import Game

# Blueprint Configuration
gameBP = Blueprint('games', __name__,
template_folder='application/templates/games/',
static_folder='application/static', url_prefix='/games')


@gameBP.route('/', methods=['GET', 'POST'])
def gamesIndex():
    """ Python Designed Games route. """

    return render_template('games/gamesIndex.html')


@gameBP.route('/rps', methods=['GET', 'POST'])
def rps():
    """ Python Designed Rock Paper Scissors route. """

    if request.method == 'POST':
        player1 = ""
        players_choice = 1

        print('player choice = {}'.format(players_choice))
        if players_choice == 1:
            player1 = "url_for('static', filename='images/games/rock.jpg')"
        elif players_choice == 2:
            player1 = "url_for('static', filename='images/games/paper.jpg')"
        elif players_choice == 3:
            player1 = "url_for('static', filename='images/games/scissors.jpg')"

        computers_choice = Game.rps_comp()
        if computers_choice == 1:
            computer1 = "/static/images/games/rock.jpg"
        elif computers_choice == 2:
            computer1 = "/static/images/games/paper.jpg"
        elif computers_choice == 3:
            computer1 = "/static/images/games/scissors.jpg"

        winner = Game.rps_win(players_choice, computers_choice)

        print('player = {}'.format(players_choice))
        print('computer = {}'.format(computers_choice))
        print('player1 = {}'.format(player1))
        print('computer1 = {}'.format(computer1))
        print('winner = {}'.format(winner))
        return render_template('games/rps.html', player1=player1, computer1=computer1, winner=winner)
    else:
        player = 0
        tie = 0
        computer = 0
        player1 = ""
        players_choice = 0
        computer1 = "/static/images/games/rock_paper_scissors.png"
        winner = ""

        play_total = 0
        comp_total = 0

        print('player = {}'.format(player))
        print('computer = {}'.format(computer))
        print('player1 = {}'.format(player1))
        print('computer1 = {}'.format(computer1))
        print('winner = {}'.format(winner))
        return render_template('games/rps.html', player1=player1, play_total=play_total,
        tie=tie, computer1=computer1, comp_total=comp_total, winner=winner)
