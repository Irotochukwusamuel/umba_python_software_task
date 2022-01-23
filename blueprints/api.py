import math

from flask import Blueprint, render_template, request

import root
import seed
from modules.validations import Validation

API_bp = Blueprint("API_bp", __name__)
validate = Validation()


@API_bp.route("/")
def index():
    pagination = request.args.get('pagination', default=25, type=int)
    data = validate.filter_API_By_Pagination_And_Page(root.table_name, pagination, int(1))
    total_records = seed.total
    total_pages = int(math.ceil(seed.total / int(pagination)))
    page_link = request.url
    print(page_link)
    return render_template("index.html", data=data, total_pages=total_pages, page_id=int(1),total_records=total_records)


@API_bp.route("/users/<page>")
def users_page(page):
    # getting the page number ( E.g http://localhost:5000/users/1)
    pagination = request.args.get('pagination', default=25, type=int)
    data = validate.filter_API_By_Pagination_And_Page(root.table_name, pagination, int(page))
    total_records = seed.total
    total_pages = int(math.ceil(seed.total / int(pagination)))
    url = request.url.split('/')
    if "users" in url and f"{page}?pagination={pagination}" in url:
        page_link = "yes"
    else:
        page_link = "no"
    return render_template("index.html", data=data, total_pages=total_pages, page_id=int(page), page_link=page_link, pagination=int(pagination),total_records=total_records)


@API_bp.route("/users")
def users():
    # getting the pagination value attached to the url ( E.g http://localhost:5000/users?pagination=1)
    pagination = request.args.get('pagination', default=25, type=int)
    page = int(1)
    data = validate.filter_API_By_Pagination_And_Page(root.table_name, pagination, page)
    total_records = seed.total
    total_pages = int(math.ceil(seed.total / int(pagination)))
    url = request.url.split('/')
    path = request.full_path
    if path.split('/')[0] in url:
        page_link = "yes"
    else:
        page_link = "no"
    return render_template("index.html", data=data, total_pages=total_pages, page_id=int(page), page_link=page_link, pagination=int(pagination), total_records=total_records)


@API_bp.route("/api/users/profiles")
def profiles():
    # getting any values/arguments attached to the url (http://localhost:5000/api/users/profiles) as list

    username = request.args.get("username", default=None, type=str)
    page = request.args.get("page", default=1, type=int)
    pagination = request.args.get("pagination", default=25, type=int)
    order_by = request.args.get("order_by", default="id", type=str)
    user_id = request.args.get("id", default=None, type=int)

    return validate.fetch_API(root.table_name, page=page, pagination=pagination, username=username, user_id=user_id,
                              order_by=order_by)
