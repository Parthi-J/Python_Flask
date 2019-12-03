import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('main', __name__, url_prefix='/main')

@bp.route('/')
def index():
    return 'Index Page'

@bp.route('/hello')
def hello():
    return 'Hello, World!'

@bp.route('/<name>')
def hello_name(name):
	log.debug("HOST:" + os.getenv("HOST"))
	return "Hello {}!".format(name)