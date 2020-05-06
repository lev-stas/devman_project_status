import requests
import telegram
from dotenv import load_dotenv
import os

DEVMAN_API_URL = 'https://dvmn.org/api/long_polling/'

def check_project_status():
    params = {}
    while True:
        try:
            response = requests.get(DEVMAN_API_URL, headers=devman_api_headers, params = params)
            response.raise_for_status()
            devman_answer = response.json()
            if devman_answer ['status'] == 'timeout':
                params['timestamp'] = devman_answer['timestamp_to_request']
            else:
                params['timestamp'] = devman_answer['last_attempt_timestamp']
                attempt_info = devman_answer['new_attempts'][0]
                negative_status = attempt_info['is_negative']
                lesson_title = attempt_info['lesson_title']
                if negative_status:
                    text = f'Преподаватель проверил проект "{lesson_title}". Есть замечания.'
                else:
                    text = f'Преподаватель проверил проект "{lesson_title}". Проект принят.'
                bot.send_message(chat_id = chat_id, text = text)

        except requests.exceptions.ReadTimeout:
            bot.send_message(chat_id = chat_id, text = 'Сервер devman не отвечает более 90 секунд')
            continue
        except requests.exceptions.ConnectionError:
            continue

if __name__ == '__main__':
    load_dotenv()
    devman_token = os.getenv('DEVMAN_TOKEN')
    proxy_login = os.getenv('SOCKS5_LOGIN')
    proxy_password = os.getenv('SOCKS5_PASSWORD')
    proxy_url = os.getenv('SOCKS5_SERVER_URL')
    telegram_token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('CHAT_ID')

    devman_api_headers = {'Authorization' : devman_token}
    telegram_proxy = telegram.utils.request.Request(proxy_url=f'socks5h://{proxy_login}:{proxy_password}@{proxy_url}')
    bot = telegram.Bot(token=telegram_token, request = telegram_proxy)

    check_project_status()






