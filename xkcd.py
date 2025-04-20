import os
import argparse
from urllib.parse import urlparse

import requests


def get_image_link():
    url = "https://xkcd.com/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    link = response.json().get("img")
    return link


def get_comment():
    url = "https://xkcd.com/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    comment = response.json().get("alt")
    return comment


def get_name(link):
    parsed = urlparse(link)
    path = parsed.path
    image_name = os.path.basename(path)
    return image_name


def save_comic(link, directory, image_name):
    response = requests.get(link)
    response.raise_for_status()
    path = os.path.join(directory, image_name)
    with open(path, "wb") as image:
        image.write(response.content)


def main():
    parser = argparse.ArgumentParser(description="Загрузка комиксов")
    parser.add_argument(
        "--directory", "-d", help="Директория для комиксов", default="files"
    )
    args = parser.parse_args()

    os.makedirs(args.directory, exist_ok=True)
    link = get_image_link()
    image_name = get_name(link)
    save_comic(link, args.directory, image_name)
    print(get_comment())


if __name__ == "__main__":
    main()
