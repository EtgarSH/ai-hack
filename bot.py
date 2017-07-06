from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from flask import Flask, request, Response


bot_configuration = BotConfiguration(
	name='InvestBot',
	avatar='http://viber.com/avatar.jpg',
	auth_token='4643793ea227d275-7a894dbfc47308e7-8ba014f6e7d19fa8'
)


def main():
    viber = Api(bot_configuration)

if __name__ == "__main__":
    main()
