from flask import (
    Blueprint, render_template, redirect, url_for, jsonify,
    request, flash, session
)
from ..models import db, maths, science

home_bp = Blueprint(
    'home_bp',
    __name__
)

@home_bp.route('/')
def index():
    session['result']=""
    subList_science=science.query.with_entities(science.subject).distinct()
    subList_maths = maths.query.with_entities(maths.subject).distinct()

    return render_template("home/index.html",subList_science=subList_science, subList_maths=subList_maths)  