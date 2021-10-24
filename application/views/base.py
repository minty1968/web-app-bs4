"""Routes for base pages."""
from flask.helpers import url_for
from flask_login.utils import login_required
from werkzeug.utils import redirect
from application.views.forms import login
from flask import Blueprint, render_template

# Blueprint Configuration
baseBP = Blueprint('base', __name__,
                      template_folder='application/templates/base/',
                      static_folder='application/static', url_prefix='/')


@baseBP.route('/', methods=['GET', 'POST'])
@baseBP.route('/index', methods=['GET', 'POST'])
@baseBP.route('/home', methods=['GET', 'POST'])
def home():
    """  Main Index or Home page.  """
    

    return render_template('index.html', body="Web App",
                           title='Sharpe Digital Solutions')


@baseBP.route("/dashboard", methods=["GET"])
@login_required
def dashboard():
    """ Success form submission """
 
    return render_template("dashboard.html",  
                           body="Form submitted Successfully", title='Sharpe Digital Solutions')


@baseBP.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('auth_bp.login'))