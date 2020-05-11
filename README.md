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

This script allows to use telegram bot even in case telegram is blocked in your country. If you have credentials from socks5 server, run `project_statys.py` and give to it socks5 server url with port number, your login and password on this socks5 server as arguments
```
python project_statys.py XXX.XXX.XXX.XXX:1080 login password &
```
Use `python3` instead `python` if you have both python2 and python3 versions.

#### Environment variables
This script needs some environment variables for correct work. Create file .env in the same directory, where project_status.py located and specify `DEVMAN_TOKEN`, `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID` variables.


#### Purpose of project
This script was performed as a part of API web-services course by [Devman](https://dvmn.org/modules)
