def handle_contents(bot_instance, chat_id):
    @bot_instance.message_handler(content_types=["photo"])
    def handle_images(message):
        if message["from_user"]["id"] == chat_id:
            bot_instance.send_message(chat_id, 'The Image will be saved')
        else:
            bot_instance.reply_to("You're not authorized")
