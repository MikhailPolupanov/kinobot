import logging
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

from anketa_parametres import (anketa_start, movie_type, anketa_oskar, anketa_dontknow, genre, 
                                director, actor, years, country, not_want, final_task)
from handlers import greet_user


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher

    anketa = ConversationHandler(
    entry_points=[MessageHandler(Filters.regex('^(Подобрать по параметрам)$'), anketa_start)],
    states={
        'type': [MessageHandler(Filters.regex('^(Подобрать фильм|Подобрать сериал)$'), movie_type)],
        'oskar': [MessageHandler(Filters.regex('^(Да, хочу чтобы была премия|Наличие премии не важно|да|Да|нет|Нет)$'), anketa_oskar)],
        'genre': [MessageHandler(Filters.text, genre)],
        'director': [MessageHandler(Filters.text, director)],
        'actor': [MessageHandler(Filters.text, actor)],
        'years': [MessageHandler(Filters.text, years)],
        'country': [MessageHandler(Filters.text, country)],
        'not_want': [MessageHandler(Filters.text, not_want)],
        'final_task': [MessageHandler(Filters.regex('^(Я нашел нужный фильм)$'), final_task)]
    },
    fallbacks=[
        MessageHandler(Filters.text | Filters.photo | Filters.video | Filters.document | Filters.location, anketa_dontknow)
    ]
    )
    
    dp.add_handler(anketa)
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.regex('^(Вернуться в начало)$'), greet_user))



    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()