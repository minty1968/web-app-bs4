"""Routes for base pages."""
from flask import Blueprint, redirect, render_template, flash, request, session, url_for
from flask_login import login_required, logout_user, current_user, login_user
from wtforms.validators import email
from application.models.forms import LoginForm, RegistrationForm, ContactForm
from application import lm
from application.common.database import User, db

# Blueprint Configuration
formsBP = Blueprint('forms', __name__,
                      template_folder='application/templates',
                      static_folder='application/static', url_prefix='/forms')


@formsBP.route('/login', methods=['GET', 'POST'])
def login():
    """
    Log-in page for registered users.

    GET requests serve Log-in page.
    POST requests validate and redirect user to dashboard.
    """
    # Bypass if user is logged in
    if current_user.is_authenticated:
        return redirect(url_for('baseBP.dashboard'))

    form = LoginForm()
    # Validate login attempt
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        print(user)
        if user and user.check_password(password=form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('baseBP.dashboard'))
        flash('Invalid username/password combination')
        return redirect(url_for('baseBP.dashboard', email=email))
    return render_template('forms/login_form.html', form=form, template="form-template", 
                           body="Login Form", title='Sharpe Digital Solutions')


@formsBP.route("/register", methods=["GET", "POST"])
def register():
    """
    User Registration page.

    GET requests serve sign-up page.
    POST requests validate form & user creation.
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user is None:
            user = User(
                name=form.name.data,
                email=form.email.data,
            )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()  # Create new user
            login_user(user)  # Log in as newly created user
            return redirect(url_for('BaseBP.dashboard'))
        flash('A user already exists with that email address.')
    return render_template("forms/register_form.html", form=form, template="form-template", 
                           body="Registration Form", title='Sharpe Digital Solutions')


@formsBP.route("/contact", methods=["GET", "POST"])
def contact():
    """Standard `contact` form."""
    form = ContactForm()
    if request.method == "POST":
        if form.validate():

            return redirect(url_for('dashboard'))
    return render_template("forms/contact_form.html", form=form, template="form-template", 
                           body="Contact Form", title='Sharpe Digital Solutions')


@lm.user_loader
def load_user(user_id):
    """Check if user is logged-in upon page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@lm.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page.')
    return redirect(url_for('auth_bp.login'))
