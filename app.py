from flask import Flask, request, render_template, send_from_directory, Blueprint, jsonify
from utils import get_post_by_pk, get_posts_all, get_comments_by_post_id, \
    get_comments, get_posts_by_user, search_for_posts, www


from logger import my_logg

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


@app.route("/")
def posts_all():
    try:
        posts_all = get_posts_all()
        if len(posts_all) == 0:
            return "", 404
        return render_template("index.html", posts_all=posts_all, len=len(posts_all))
    except FileNotFoundError:
        return "серверы недоступны", 500
    except:
        return "возможна ошибка шаблона", 500


@app.route("/search/")
def search():
    try:
        g = request.args.get("s")
        posts = search_for_posts(g)
        if len(posts) == 0:
            return "", 404
        return render_template("search.html", posts=posts, lener=len(posts))
    except FileNotFoundError:
        return "серверы не доступны", 500
    except:
        return "возможна ошибка шаблона", 500


@app.route("/posts/<int:post_id>")
def posts(post_id):
    try:
        post_id = int(post_id)
        post = get_post_by_pk(post_id)
        if len(post) == 0:
            return "", 404
        comments = get_comments_by_post_id(post_id)
        return render_template("post.html", post=post, comments=comments, lener=www(len(comments)))
    except FileNotFoundError:
        return "серверы не доступны", 500
    except:
        return "возможна ошибка шаблона", 500


@app.route("/users/<username>")
def user_feed(username):
    try:
        posts = get_posts_by_user(username)
        if len(posts) == 0:
            return "", 404
        return render_template("user-feed.html", posts=posts)
    except FileNotFoundError:
        return "серверы не доступны", 500
    except:
        return "возможна ошибка шаблона", 500


@app.route("/api/posts/")
def api_posts():
    my_logg.info("Запрос /api/posts/")
    return jsonify(get_posts_all())


@app.route("/api/posts/<post_id>")
def api_post(post_id):
    my_logg.info(f"Запрос /api/posts/{post_id}")
    return jsonify(get_post_by_pk(int(post_id)))


@app.route("/tag/")
def get_tag():
    return render_template("tag.html")

@app.route("/bookmarks/")
def bookmarks():
    return render_template("bookmarks.html")

app.run()