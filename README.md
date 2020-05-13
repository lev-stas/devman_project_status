## Check DevMan project status
This project creates telegram bot which notifies when your project is checked by DevMav expert.

#### Prepare your work environment
You need Python3 interpreter to use this script. You can check what version or python interpreter typing in your terminal
```
python --version
```
If you see `python2.X` version, check if you have python3 version, typing in your terminal
```
python3 --version
```
If you don't have python3 install it. All necessary information about how to install it on your operating system you can find on [python official page](https://www.python.org)
Also, you need pip packet manager to install python libraries. You can find information about pip and how to install it on [pip documntation](https://pip.pypa.io/en/stable/installing/). 

To prepare work environment open terminal, clone `devman_project_status` repository and go to the repository directory typing:
```
git clone https://github.com/lev-stas/devman_project_status.git
cd devman_project_status
```
It is good practice to use virtual environment for your project. It will save you from libraries versions conflicts. To make virtual environment you should install `virtualenv` library, if you don't have it:
```
pip3 install virtualenv
```
Then create and activate virtual environment typing in your terminal
```
python3 -m virtualenv .venv
source .venv/bin/activate
```
All needed dependencies are included in requirements.txt file. To install them, type in your terminal 
```
pip install -r requirements.txt
```
This script needs some environment variables for correct work. Create file `.env` in the same directory, where `project_status.py` is located and specify `DEVMAN_TOKEN`, `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID` variables.

#### Usage
To run this script, type in console:
```
python project_status.py &
```
When you run project_status.py, it will work until your server power off or until you`ll kill a process. It will send you messages in telegram every time, your project status changes.

This script allows to use telegram bot even in case telegram is blocked in your country. If you have credentials from socks5 server, run `project_statys.py` and give to it socks5 server url with port number, your login and password on this socks5 server as arguments:
```
python project_statys.py XXX.XXX.XXX.XXX:1080 login password &
```

#### Purpose of project
This script was performed as a part of API web-services course by [Devman](https://dvmn.org/modules)
