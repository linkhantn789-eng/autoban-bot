from telegram.ext import Updater, MessageHandler, Filters

import os
TOKEN = os.getenv("TOKEN")   # Railway မှာ ထည့်မယ့် Token

def member_left(update, context):
    user = update.message.left_chat_member
    if user:
        try:
            context.bot.ban_chat_member(update.message.chat_id, user.id)
            print(f"Banned {user.full_name}")
        except Exception as e:
            print(f"Error: {e}")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.status_update.left_chat_member, member_left))

updater.start_polling()
updater.idle()
