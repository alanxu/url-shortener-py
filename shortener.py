import time
import base62

index = round(time.time() * 1000)


def get_id(url: str):
    global index
    index += 1
    return index


def get_url_token(_id: int, url: str) -> str:
    return base62.encode(_id)
