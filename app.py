from flask import Flask
from flask import request
from secrets import FB_VERIFY_TOKEN
from secrets import FB_ACCESS_TOKEN
from pymessenger.bot import Bot

app = Flask(__name__)
bot = Bot(FB_ACCESS_TOKEN)


def verify_fb_token(token_sent):
    print('Checking verification token')
    if token_sent == FB_VERIFY_TOKEN:
        return request.args.get('hub.challenge')
    return 'Invalid verification token'

def send_message(recipient_id, response):
    print('Sending message to {}')
    bot.send_text_message(recipient_id, response)
    return "success"

def get_message():
    return "Hi there!"

@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        token_sent = request.args.get('hub.verify_token')
        return verify_fb_token(token_sent)
    else:
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    recipient_id = message['sender']['id']
                    if message['message'].get('text'):
                        response_sent_text = get_message()
                        send_message(recipient_id, response_sent_text)
        return "Message processed"


if __name__ == '__main__':
    app.run(debug=True)
