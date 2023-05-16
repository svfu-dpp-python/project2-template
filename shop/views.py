from flask import render_template
from . import models


def index_page():
    query = models.db.select(models.Phone)
    phones = models.db.session.execute(query).scalars()
    return render_template("index.html", phones=phones)
