from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

from datetime import date

"""
This file defines all backend logic that interacts with database and other services
"""


def get_user(email):
    """
    Get a user by a given email
    :param email: the email of the user
    :return: a user that has the matched email address
    """
    user = User.query.filter_by(email=email).first()
    return user


def login_user(email, password):
    """
    Check user authentication by comparing the password
    :param email: the email of the user
    :param password: the password input
    :return: the user if login succeeds
    """
    # if this returns a user, then the name already exists in database
    user = get_user(email)
    if not user or not check_password_hash(user.password, password):
        return None
    return user


def register_user(email, name, password, password2):
    """
    Register the user to the database
    :param email: the email of the user
    :param name: the name of the user
    :param password: the password of user
    :param password2: another password input to make sure the input is correct
    :return: an error message if there is any, or None if register succeeds
    """
    user = User.query.filter_by(email=email).first()

    if user:
        return "User existed"

    if password != password2:
        return "The passwords do not match"

    if len(email) < 1:
        return "Email format error"

    if len(password) < 1:
        return "Password not strong enough"

    hashed_pw = generate_password_hash(password, method='sha256')
    # store the encrypted password rather than the plain password
    new_user = User(email=email, name=name, password=hashed_pw)

    db.session.add(new_user)
    db.session.commit()
    return None


def create_ticket(name, quantity, price, date):
    ticket = Ticket.query.filter_by(name=name).first()

    if ticket:
        return "Ticket already exists"

    if not name.isalnum():
        return "Ticket name isn't alpha-numeric"

    if not (name[0] == " " or name[-1] == " "):
        return "Ticket starts or ends with a space"

    if len(name) > 60:
        return "Ticket name too long"

    if quantity < 1:
        return "Quantity of ticket must be more than 0"

    if quantity > 100:
        return "Quantity of ticket must be less than equal to 100"

    if price < 10:
        return "Price of ticket must be more than equal to 10"

    if price > 100:
        return "Price of ticket must be less than equal to 100"

    if len(date) != 8 or type(date) != String:
        return "Date must be given in the format YYYYMMDD"
    
    new_ticket = Ticket(name=name, quantity=quantity, price=price, date=date)

    db.session.add(new_ticket)
    db.session.commit()
    return None


def get_available_tickets(user):
    # Placeholder code for later
    return user.tickets


def check_if_expired(ticket):
    currDay = date.today().strftime("%Y%m%d")

    return ticket.date <= currDay