from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from flask import Flask, request, Response

server_configuration = {
    "host": "http://my_server.com",
    "port": 80,
}

bot_configuration = BotConfiguration(
    name='InvestBot',
    avatar='http://viber.com/avatar.jpg',
    auth_token='4643793ea227d275-7a894dbfc47308e7-8ba014f6e7d19fa8'
)


viber = Api(bot_configuration)
app = Flask(__name__)


@app.route('/incoming', methods=['POST'])
def incoming():
    print('Received request. Post data: {0}'.format(request.get_data()))
    # handle the request here
    return Response(status=200)

app.run(host='0.0.0.0', port=80, debug=True)
viber.set_webhook("{0}:{1}/".format(server_configuration["host"], server_configuration["port"]))
