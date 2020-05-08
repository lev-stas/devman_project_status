## Check DevMan project status
This project creates telegram bot which notifies when your project is checked by DevMav expert.

#### Dependencies
You need Python3 interpreter to use this script. All needed dependencies are included in requirements.txt file. Use 
```
pip install -r requirements.txt
```
to install them (use `pip3` instead `pip`  if you have both python2 and python3 versions).

#### Usage
To run this script, type in console, beeing in the same directory, where project_status.py located:
```
python project_status.py &
```
Use `python3` instead `python` if you have both python2 and python3 versions.
When you run project_status.py, it will work until your server power off or until you`ll kill a process. It will send you messages in telegram every time, your project status changes.

This script allows to use telegram bot even in case telegram is blocked in your country. To make it work you need socks5 server. If telegram is not blocked in your country, you can remove 
``` 
telegram_proxy = telegram.utils.request.Request(proxy_url=f'socks5h://{proxy_login}:{proxy_password}@{proxy_url}') 
```
and replace
``` 
bot = telegram.Bot(token=telegram_token) 
```
instead of 
```
bot = telegram.Bot(token=telegram_token, request = telegram_proxy)
```


#### Environment variables
This script needs some environment variables for correct work. Create file .env in the same directory, where project_status.py located and specify `DEVMAN_TOKEN`, `TELEGRAM_BOT_TOKEN`, `SOCKS5_LOGIN`, `SOCKS5_PASSWORD`, `SOCKS5_SERVER_URL`, `TELEGRAM_CHAT_ID` veriables.


#### Purpose of project
This script was performed as a part of API web-services course by [Devman](https://dvmn.org/modules)
