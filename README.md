# NYT-SCOTUSBOT

## BOOTSTRAP
To get nyt-scotusbot running on your local machine, follow these steps.

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

* Create a bot integration for your ScotusBot and get the [channel ID](https://api.slack.com/methods/channels.list/test).
```
export SCOTUSBOT_SLACK_CHANNEL=C012345
export SCOTUSBOT_SLACK_TOKEN=ABCEFGHIJKLMNOPQRSTUVWXYZ01234567890
```

* Create the log file if it doesn't exist.
```
touch /tmp/scotusbot.log
```

* Run the bot itself.
```
python -m scotusbot.bot
```

* Tail the log to see what's going on.
```
tail -f /tmp/scotusbot.log
``` 