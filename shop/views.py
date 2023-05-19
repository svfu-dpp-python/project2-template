from flask import render_template, request
from . import models


def index_page():
    query = models.db.select(models.Brand)
    brands = models.db.session.execute(query).scalars()

    query = models.db.select(models.Phone)
    brand_pk = request.args.get("brand")
    if brand_pk:
        query = query.filter_by(brand_pk=int(brand_pk))
    phones = models.db.session.execute(query).scalars()

    return render_template(
        "index.html",
        brands=brands,
        phones=phones
    )
