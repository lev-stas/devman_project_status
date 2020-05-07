import requests
import telegram
from dotenv import load_dotenv
import os
import time

DEVMAN_API_URL = 'https://dvmn.org/api/long_polling/'

def check_project_status(url):
    params = {}
    request_attempt = 0
    while True:
        try:
            response = requests.get(url, headers=devman_api_headers, params = params)
            response.raise_for_status()
            devman_answer = response.json()
            if devman_answer ['status'] == 'timeout':
                params['timestamp'] = devman_answer['timestamp_to_request']
            else:
                params['timestamp'] = devman_answer['last_attempt_timestamp']
                info = devman_answer['new_attempts'][0]
                status = info['is_negative']
                lesson_title = info['lesson_title']
                if status:
                    text = f'Преподаватель проверил проект "{lesson_title}". Есть замечания.'
                else:
                    text = f'Преподаватель проверил проект "{lesson_title}". Проект принят.'
                bot.send_message(chat_id = telegram_chat_id, text = text)
            request_attempt = 0

        except requests.exceptions.ReadTimeout:
            request_attempt += 1
            if request_attempt > 3:
                time.sleep(300)
            continue
        except requests.exceptions.ConnectionError:
            time.sleep(60)
            continue

if __name__ == '__main__':
    load_dotenv()
    devman_token = os.getenv('DEVMAN_TOKEN')
    proxy_login = os.getenv('SOCKS5_LOGIN')
    proxy_password = os.getenv('SOCKS5_PASSWORD')
    proxy_url = os.getenv('SOCKS5_SERVER_URL')
    telegram_token = os.getenv('TELEGRAM_BOT_TOKEN')
    telegram_chat_id = os.getenv('CHAT_ID')

    devman_api_headers = {'Authorization' : f'Token {devman_token}'}
    telegram_proxy = telegram.utils.request.Request(proxy_url=f'socks5h://{proxy_login}:{proxy_password}@{proxy_url}')
    bot = telegram.Bot(token=telegram_token, request = telegram_proxy)

    check_project_status(DEVMAN_API_URL)
 





