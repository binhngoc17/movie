## How to register FB bot

Follow this guide to create a FB Page & a messenger bot:
https://blog.hartleybrody.com/fb-messenger-bot/

Get the ACCESS TOKEN of the app & the VERIFY_TOKEN of the bot to config

Try to add the user to the list of test / developer so that the bot can send message to

## How to run

The challenge of running a FB bot is we need an HTTPS server. There are 2 options to help us create a HTTPS server as below

### Using Heroku

```
# Install Heroku
brew install heroku

# Set up heroku app
heroku create

# Set application environment
heroku config:set ACCESS_TOKEN=<ACCESS_TOKEN>
heroku config:set VERIFY_TOKEN=<VERIFY_TOKEN>

# Deploy the app
git push heroku master

# Run the app
heroku ps:scale web=1
```

### Using Ngrok

```
# Download Ngrok from this URL
# https://dashboard.ngrok.com/get-started

# Move ngrok to the executable path (e.g. /usr/local/bin)

# Add ngrok token
$ ngrok authtoken <token>

# Run the bot server
$ python bot.py

# pipe ngrok to your localhost
$ ngrok http <port your bot is running on> (Default of Flask is 5000)

# Add the URL of ngrok to FB App Messenger settings
```
