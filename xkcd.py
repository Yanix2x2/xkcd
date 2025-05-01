import requests


def get_comic_data(num_comic):
    url = f"https://xkcd.com/{num_comic}/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    comic_data = response.json()
    comment = comic_data.get("alt")
    comic_name = comic_data.get("title")
    link = comic_data.get("img")
    return comment, comic_name, link
