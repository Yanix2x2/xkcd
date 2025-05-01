import requests


def get_comic(num_comic):
    url = f"https://xkcd.com/{num_comic}/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    comic = response.json()
    comment = comic.get("alt")
    comic_name = comic.get("title")
    link = comic.get("img")
    return comment, comic_name, link
