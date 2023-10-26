import json
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes, InlineQueryHandler




file_path = 'chat_ids.json'
idDictionary = {}

try:
    with open(file_path, 'r') as file:
        idDictionary = json.load(file)
except FileNotFoundError:
    pass

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    if update.effective_chat.id not in idDictionary:
        idDictionary[update.effective_chat.id] = True
        with open(file_path, 'w') as file:
            json.dump(idDictionary, file)


    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="This is the GDSC Networking Bot, you can start chatting with random peers"
    )



if __name__ == '__main__':

    application = ApplicationBuilder().token('6945415262:AAFMVFub4GePSOAjzHjRc3wlNnSMnefJInU').build()

    start_handler = CommandHandler('start', start)
    #process_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), process_message)

    application.add_handler(start_handler)
    #application.add_handler(process_handler)
    
    application.run_polling()