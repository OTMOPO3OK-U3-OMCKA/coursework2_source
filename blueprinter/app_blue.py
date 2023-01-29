from flask import Blueprint, jsonify
from logger import my_logg
from utils import get_post_by_pk, get_posts_all


api_blu = Blueprint("api_blu", __name__)

@api_blu.route("/")
def api_posts():
    my_logg.info("Запрос /api/posts/")
    return jsonify(get_posts_all())


@api_blu.route("/<post_id>")
def api_post(post_id):
    my_logg.info(f"Запрос /api/posts/{post_id}")
    return jsonify(get_post_by_pk(int(post_id)))
