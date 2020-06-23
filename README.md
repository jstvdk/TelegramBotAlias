# Telegram Bot for Alias game.

Python version = 3.8.1

Main logic was written with help of aiogram - https://aiogram.dev/en/home, modern and fully asynchronous framework for TelegramBot API - https://core.telegram.org/bots/api.

Words database made with sqlite3 - https://www.sqlite.org.

Player's statistic database made with Redis https://redis.io.

# For starting bot on your machine, you need to install next Python packages:

1. aiogram
2. redis
3. sqlite3

## For OSX and Linux users:

All next lines, except of customization redis config, must be written into command line of terminal.

### Aiogram:
```
pip install aiogram
```

### Redis:
Downloading Redis source code as tarball

```
 redisurl="http://download.redis.io/redis-stable.tar.gz"
 curl -s -o redis-stable.tar.gz $redisurl

```
then unpacking it into /usr/local/lib:
```
 sudo su root
 mkdir -p /usr/local/lib/
 chmod a+w /usr/local/lib/
 tar -C /usr/local/lib/ -xzf redis-stable.tar.gz
 rm redis-stable.tar.gz
 ```
 and installing it:

 ```
 cd /usr/local/lib/redis-stable/
 make && make install
 sudo su root
```
Lets create config file:

```
 mkdir -p /etc/redis/
 touch /etc/redis/6379.conf

```
and customizing it by writing next lines into config file:

```
# /etc/redis/6379.conf

port              6379
daemonize         yes
save              60 1
bind              127.0.0.1
tcp-keepalive     300
dbfilename        dump.rdb
dir               ./
rdbcompression    yes

```
After all let's install redis-py package:
```
pip install redis

```

### Sqlite3

```
pip install sqlite3

```

## Launching bot

After downloading python code, and installing all neccesary packages, you need to put your bot token into file "config.py", into variable BOT_TOKEN.

Then just run file "app.py"

Words database lies in file Words_Data_Base.db

Player statistic are saving into file dump.rdb

If you want to check words or add new, you can do it through the file game_words.csv

## Link to bot  - https://t.me/alias_v1_bot.
