from flask import (
    Blueprint,
    abort,
    render_template,
    request
)
from functools import wraps

from models.items import User

main = Blueprint("main", __name__)


@main.route("/")
def item():
    return render_template('index.html')


def login_required(func):

    @wraps(func)
    def wrapper():
        email = request.args.get('email')

        user = User.query.filter(User.email == email).first()
        if not user:
            abort(403)

        return func(user)

    return wrapper


@main.route("/user", methods=['GET'])
@login_required
def function(user):
    _user = User.filter(User.id==1).first()
    if _user == user:
        print "yes"
    return {'sucess': True}
