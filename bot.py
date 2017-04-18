"""
This bot listens to port 5002 for incoming connections from Facebook. It takes
in any messages that the bot receives and echos it back.
"""
from flask import Flask, request
from command_handlers.movies import Movies
from util import bot
app = Flask(__name__)

command_prefix = {
    'movies': Movies
}

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        else:
            return 'Invalid verification token'

    if request.method == 'POST':
        output = request.get_json()
        print output
        for event in output['entry']:
            messaging = event['messaging']
            for x in messaging:
                if x.get('message'):
                    recipient_id = x['sender']['id']
                    if x['message'].get('text'):
                        message = x['message']['text']
                        prefix, command = message.split('.')
                        if not command_prefix.get(prefix):
                            bot.send_text_message(recipient_id, message)
                            break
                        command_prefix[prefix](recipient_id).execute(command)
                    # if x['message'].get('attachments'):
                    #     for att in x['message'].get('attachments'):
                    #         bot.send_attachment_url(recipient_id, att['type'], att['payload']['url'])
                else:
                    pass
        return "Success"


@app.route("/health")
def health():
    return 'ok'

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0', debug=True)
