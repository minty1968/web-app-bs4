"""Routes for lottery pages."""
from flask import Blueprint, render_template, request, flash, url_for
from application.models.lottery import Lottery

# Blueprint Configuration
lotteryBP = Blueprint('lottery', __name__,
                      template_folder='application/templates/lottery/',
                      static_folder='application/static', url_prefix='/lottery')


@lotteryBP.route('/lottery', methods=['GET'])
def lotteryDraws():
    """Lottery route.  First we generate numbers, then sort them. """
    lotto_nums = Lottery.get_sorted_main_numbers(59, 6)
    euro_nums = Lottery.get_sorted_main_numbers(50, 5)
    euro_bonus = Lottery.get_sorted_bonus_numbers(12, 2)
    s4l_nums = Lottery.get_sorted_main_numbers(47, 5)
    s4l_bonus = Lottery.get_sorted_bonus_numbers(10, 1)
    thunderball_nums = Lottery.get_sorted_main_numbers(39, 5)
    thunderball_bonus = Lottery.get_sorted_bonus_numbers(14, 1)
    
    return render_template('lotteryDraws.html', title='Sharpe Digital Solutions | Lottery Draws',
                           lotto_nums=lotto_nums, euro_nums=euro_nums, s4l_nums=s4l_nums, euro_bonus=euro_bonus, 
                           s4l_bonus=s4l_bonus, thunderball_nums=thunderball_nums, thunderball_bonus=thunderball_bonus)
