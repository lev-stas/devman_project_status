import requests
import telegram
from dotenv import load_dotenv
import os
import time
import argparse

DEVMAN_API_URL = 'https://dvmn.org/api/long_polling/'


def check_project_status(url, headers, bot, chat_id):
    params = {}
    while True:
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            devman_answer = response.json()
            if devman_answer['status'] == 'timeout':
                params['timestamp'] = devman_answer['timestamp_to_request']
            else:
                params['timestamp'] = devman_answer['last_attempt_timestamp']
                attempt = devman_answer['new_attempts'][0]
                attempt_status = attempt['is_negative']
                lesson_title = attempt['lesson_title']
                if attempt_status:
                    message_text = f'Преподаватель проверил проект "{lesson_title}". Есть замечания.'
                else:
                    message_text = f'Преподаватель проверил проект "{lesson_title}". Проект принят.'
                bot.send_message(chat_id=chat_id, text=message_text)

        except requests.exceptions.ReadTimeout:
            continue

        except requests.exceptions.ConnectionError:
            continue

if __name__ == '__main__':
    load_dotenv()
    devman_token = os.getenv('DEVMAN_TOKEN')
    telegram_token = os.getenv('TELEGRAM_BOT_TOKEN')
    telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')

    parser = argparse.ArgumentParser(description='Check project status on devman resource')
    parser.add_argument('-u', '--socks5_url', help='enter yor proxy server url')
    parser.add_argument('-l', '--socks5_login', help='enter your login on socks5 server')
    parser.add_argument('-p', '--socks5_passwd', help='enter your password on socks5 server')

    script_args = parser.parse_args()

    if script_args.socks5_url and script_args.socks5_login and script_args.socks5_passwd:
        proxy_url = script_args.socks5_url
        proxy_login = script_args.socks5_login
        proxy_password = script_args.socks5_passwd
        telegram_proxy = telegram.utils.request.Request(proxy_url=f'socks5h://{proxy_login}:{proxy_password}@{proxy_url}')
        t_bot = telegram.Bot(token=telegram_token, request=telegram_proxy)

    else:
        t_bot = telegram.Bot(token=telegram_token)

    devman_api_headers = {'Authorization': f'Token {devman_token}'}

    check_project_status(DEVMAN_API_URL, devman_api_headers, t_bot, telegram_chat_id)

