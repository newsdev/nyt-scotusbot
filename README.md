![](https://cloud.githubusercontent.com/assets/109988/10309923/32507b92-6c0d-11e5-8ae9-5bb0ca46077e.png)

A Python-based SlackBot derived from [SlackHQ's](https://github.com/slackhq/) remarkable [RTMBot](https://github.com/slackhq/python-rtmbot)

## Getting started

* This bot uses MongoDB instead of the filesystem for persistence. You can install MongoDB locally (default) or export `SCOTUSBOT_MONGO_URL` with your custom connection string.
```
brew install mongodb
ln -sfv /usr/local/opt/mongodb/*.plist ~/Library/LaunchAgents
launchctl load ~/Library/LaunchAgents/homebrew.mxcl.mongodb.plist
```

* Create a virtualenv and install the required packages.
```
mkvirtualenv nyt-scotusbot && pip install -r requirements.txt
```

* Create a bot integration for your scotusbot and get the [channel ID](https://api.slack.com/methods/channels.list/test). Then export the channel ID and the token.
```
export CAMPFINBOT_SLACK_CHANNEL=C012345
export CAMPFINBOT_SLACK_TOKEN=ABCEFGHIJKLMNOPQRSTUVWXYZ01234567890
```

* Create the log file if it doesn't exist.
```
touch /tmp/scotusbot.log
```

* Preload data for the bot. It needs to get loaded with old cases (grants and opinions) so it doesn't spam your slack channel with stuff you already know about.
```
python -m scotusbot.preload
```

* Run the bot itself.
```
python -m scotusbot.bot
```

* Tail the log to see what's going on.
```
tail -f /tmp/scotusbot.log
``` 

## Deployment
### Ubuntu Linux
* Make an Upstart script in `/etc/init/scotusbot.conf` and use this template.
```
start on runlevel [2345]
stop on runlevel [!2345]

respawn

script
  export SCOTUSBOT_SLACK_CHANNEL='C012345'
  export SCOTUSBOT_SLACK_TOKEN='xoxb-1234567890-AbcDefGhijkLmNOpQRstUvWXyz'
  export SCOTUSBOT_PRD_HOST='ec2-0-0-0-0.compute-99.amazonaws.com'
  export SCOTUSBOT_MONGO_URL='127.0.0.1:12345'
  cd /home/ubuntu/nyt-scotusbot && /home/ubuntu/.virtualenvs/nyt-scotusbot/bin/python /home/ubuntu/nyt-scotusbot/scotusbot/bot.py
end script
```