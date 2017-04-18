## How to run

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

## How to test the app

Follow this guide to create a FB Page & a messenger bot:
https://blog.hartleybrody.com/fb-messenger-bot/

Get the ACCESS TOKEN of the app & the VERIFY_TOKEN of the bot to config

Try to add the user to the list of test / developer so that the bot can send message to