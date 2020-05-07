## Check DevMan project status
This project creates telegram bot which notifies when your project is checked by DevMav expert.

#### Dependences
You need Python3 interpreter to use this script. All needed dependences are included in requirements.txt file. Use 
```pip install -r requirements.txt```
 to install them (use `pip3` instead `pip`  if you have both python2 and python3 versions).

#### Usage
To run this script, type in console, beeing in the same directory, where project_status.py located:
```python project_status.py &```
Use `python3` instead `python` if you have both python2 and python3 versions.
When you run project_status.py, it will work until your server power off or until you`ll kill a process. It will send you messages in telegram every time, your project status changes.

This script allows to use telegram bot even in case telegram is blocked in your country. To make it work you need socks5 server. If telegram is not blocked in your country, you can remove 
``` telegram_proxy = telegram.utils.request.Request(proxy_url=f'socks5h://{proxy_login}:{proxy_password}@{proxy_url}') ```
and replace
``` bot = telegram.Bot(token=telegram_token) ```
isntead of 
```bot = telegram.Bot(token=telegram_token, request = telegram_proxy)```


#### Environment variables
This script needs some environment variables for correct work. Create file .env in the same directory, where project_status.py located with such content:
``` 
DEVMAN_TOKEN = <your personal token> on [Devman](https://dvmn.org/api/docs/)
TELEGRAM_BOT_TOKEN = <your telegram bot token>
SOCKS5_LOGIN = <login of your socks5 servers> (if exists)
SOCKS5_PASSWORD = <password of your socks5 server> (if exists)
SOCKS5_SERVER_URL = <your socks5 server url:port> (if exists)
CHAT_ID = <yout telegram chat_id> 
```


#### Purpose of project
This script was performed as a part of API web-services cource by [Devman](https://dvmn.org/modules)
