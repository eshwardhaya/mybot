import telebot
import logging
from decouple import config
from src import helpers, jenkins, handle_contents


def init_bot():
    # Initialisation
    logger = telebot.logger
    telebot.logger.setLevel(logging.DEBUG)
    bot_instance = telebot.TeleBot(config("BOT_TOKEN"), parse_mode=None)
    helpers.bot_helpers(bot_instance)
    # Handle Various FileTypes
    handle_contents.handle_contents(bot_instance, 1002045138)
    # Jenkins Props
    jenkins_instance = jenkins.Jenkins(bot_instance)
    jenkins_instance.is_job_running()
    bot_instance.polling()
    logger.debug("Bot Initiated")


init_bot()
