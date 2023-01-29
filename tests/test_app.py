from app import app
def test_app():
    r = app.test_client().get("/api/posts/")
    assert r.status_code == 200
    assert type(r.json) == list


def test_app_id():
    r = app.test_client().get("/api/posts/3")
    assert r.status_code == 200
    assert type(r.json) == dict
    assert r.json.get("pk") == 3
    assert r.json.get("poster_name") is not None
    assert r.json.get("poster_avatar") is not None
    assert r.json.get("pic") is not None
    assert r.json.get("content") is not None
    assert r.json.get("views_count") is not None
    assert r.json.get("likes_count") is not None