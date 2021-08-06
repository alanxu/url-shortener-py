import shortener


def test_get_id():
    _id = shortener.get_id("www.google.com")
    assert _id > 0


