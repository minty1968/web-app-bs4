"""Routes for password generator pages."""
from flask import Blueprint, render_template, request

# Blueprint Configuration
passwdBP = Blueprint('password', __name__,
                        template_folder='application/templates/password/',
                        static_folder='static')


@passwdBP.route('/password', methods=['GET', 'POST'])
def passwd():
    """Password route."""

    return render_template('passwd.html', body="Password Generator",
                           title='Sharpe Digital Solutions | Password Generator')
 