def bot_helpers(bot_instance):
    @bot_instance.message_handler(commands=["info"])
    def bot_info(message):
        info = '''
            I'm a bot to monitor system activites.I'm being developed by Dhaya
        '''
        bot_instance.reply_to(message, info)
