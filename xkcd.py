import requests


def get_response(num_comic):
    url = f"https://xkcd.com/{num_comic}/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def get_comment(num_comic):
    comic_data = get_response(num_comic)
    comment = comic_data.get("alt")
    return comment


def get_picture_link(num_comic):
    comic_data = get_response(num_comic)
    link = comic_data.get("img")
    return link


def get_comic_name(num_comic):
    comic_data = get_response(num_comic)
    comic_name = comic_data.get("title")
    return comic_name
