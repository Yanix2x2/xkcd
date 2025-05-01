import os
import random
import time
import argparse
from dotenv import load_dotenv

import telegram

from xkcd import get_comic_data


def send_message(bot, tg_chat_id):
    num_comic = random.randint(1, 3083)

    comment, title, photo = get_comic_data(num_comic)

    bot.send_photo(
        chat_id=tg_chat_id,
        photo=photo,
        caption=f'<b>{title}</b>\n\n{comment}',
        parse_mode='HTML'
    )


def main():
    load_dotenv()
    tg_token = os.environ['TELEGRAM_BOT_TOKEN']
    tg_chat_id = os.environ['TELEGRAM_CHAT_ID']
    bot = telegram.Bot(token=tg_token)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--time', '-t', type=int, help='Время в секундах', default='86400'
    )

    args = parser.parse_args()

    while True:
        try:
            send_message(bot, tg_chat_id)
            time.sleep(args.time)
        except telegram.error.NetworkError as err:
            print(f"Ошибка подключения: {err}, повтор через 5 секунд")
            time.sleep(5)


if __name__ == '__main__':
    main()
