import json


def get_json(file):
    try:
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)

    except ValueError:
        return None


def get_posts_all():
    return get_json("data/posts.json")


def get_comments():
    return get_json("data/comments.json")


def get_posts_by_user(user_name):
    list_posts = []
    for i in get_posts_all():
        if i.get("poster_name") == user_name:
            list_posts.append(i)
    return list_posts


def get_comments_by_post_id(post_id):
    list_comments = []
    for i in get_comments():
        if i.get("post_id") == post_id:
            if i.get("comment") is not None:
                list_comments.append(i)
    return list_comments


def search_for_posts(query):
    list_post = []
    for i in get_posts_all():
        if query in i.get("content"):
            list_post.append(i)
    return list_post


def get_post_by_pk(pk):
    for i in get_posts_all():
        if i.get("pk") == pk:
            return i
    return {}

def www(w):
    ww = f'{w} комментари'
    if 5 <= w % 100 <= 20:
        return ww + "ев"
    elif w % 10 == 1:
        return ww + "й"
    elif 2 <= w % 10 <= 4:
        return ww + "я"
    else:
        return ww + "ев"
