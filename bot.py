import logging

from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration

from viberbot.api.messages import (
    TextMessage,
    ContactMessage,
    PictureMessage,
    VideoMessage
)
from viberbot.api.messages.data_types.contact import Contact

from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import ViberUnsubscribedRequest

from flask import Flask, request, Response

from actions.echo import echo

server_configuration = {
    "host": "http://my_server.com",
    "port": 25565,
}

bot_configuration = BotConfiguration(
    name='InvestBot',
    avatar='http://viber.com/avatar.jpg',
    auth_token='4643793ea227d275-7a894dbfc47308e7-8ba014f6e7d19fa8'
)

# Logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


# Bot Server
viber = Api(bot_configuration)
app = Flask(__name__)

app.run(host='0.0.0.0', port=server_configuration["port"], debug=True)
viber.set_webhook("{0}:{1}/".format(server_configuration["host"], server_configuration["port"]))


# Simple Echo EVENT
@app.route('/incoming', methods=['POST'])
def incoming():
    return echo(request, viber, logger)

