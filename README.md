# raspi_bot
Simple raspberry bot for learning use

## Installation

```
git clone https://github.com/rafen/raspi_bot.git
```

```
cd raspi_bot
```

```
pip install -r requirements.txt
```

Create a setting.py file with the bot `TOKEN` and `ALLOWED_USERS_IDS`.
Example:

```
TOKEN = 'XXXXXX'

ALLOWED_USERS_IDS = [
    658117611,
]
```

## Install supervisor

```
sudo apt-get install supervisor
```

create the following file with sudo:

`/etc/supervisor/conf.d/raspi_bot.conf`

with content:

```
[program:raspi_bot]
command=/usr/bin/python /home/pi/raspi_bot/raspi_bot.py
user=pi
group=pi
autostart=true
autorestart=true
redirect_stderr=true
stopsignal=QUIT
stdout_logfile=/home/pi/raspi_bot/raspi_bot.log
```

Reload supervisor

```
supervisorctl reread
supervisorctl update
```
