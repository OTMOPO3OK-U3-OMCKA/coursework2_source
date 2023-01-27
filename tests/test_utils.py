
from utils import get_post_by_pk, get_posts_all, get_comments_by_post_id,\
    get_comments, get_posts_by_user, search_for_posts, www


def test_get_posts_all():
    assert type(get_posts_all()) == list
    assert len(get_posts_all()) > 0


def test_get_comments():
    assert type(get_comments()) == list
    assert len(get_comments()) > 0


def test_get_posts_by_user():
    assert len(get_posts_by_user("leo")) == 2
    assert len(get_posts_by_user("------")) == 0


def test_get_comments_by_post_id():
    id = get_comments_by_post_id(2)
    id_2 = get_comments_by_post_id(-1)
    assert len(id_2) == 0
    assert type(id_2) == list
    assert type(id) == list
    assert len(id) == 4


def test_search_for_posts():
    query = search_for_posts("-----")
    query_2 = search_for_posts("ост")
    assert len(query) == 0
    assert type(query) == list
    assert len(query_2) == 3


def test_get_post_by_pk():
    assert type(get_post_by_pk(1)) == dict
    assert type(get_post_by_pk("33")) == dict
    assert bool(get_post_by_pk(1)) == 1
    assert bool(get_post_by_pk(-1)) == 0
    assert len(get_post_by_pk(-1)) == 0
