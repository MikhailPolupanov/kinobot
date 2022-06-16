from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, ParseMode
from telegram.ext import ConversationHandler

def anketa_reco_start(update, context):
    update.message.reply_text('Напишите названия фильмов или сериалов через запятую (можно указать и одно название). \nЯ их проанализирую и подберу для вас похожие')
    return 'user_movies'

def users_movies(update, context):
    context.user_data['user_movies'] = str(update.message.text).lower()
    update.message.reply_text(f'Вы ввели следующие названия: {context.user_data["user_movies"]}')
    update.message.reply_text('Дайте мне немного времени')
    update.message.reply_text(
        f'Вот ваша подборка: \nфильм1 \nфильм2 \nфильм3 \nфильм4 \nфильм5',
        reply_markup=ReplyKeyboardMarkup([['Следующие 5 фильмов', 'Я нашел нужный фильм']], one_time_keyboard=True)
    )
    return 'final_reco'

def final_reco(update, context):
    update.message.reply_text(f'Рад был помочь!', reply_markup=ReplyKeyboardMarkup([['Вернуться в начало']], one_time_keyboard=True))
    return ConversationHandler.END

def anketa_dontknow_reco(update, context):
    update.message.reply_text('Я вас не понимаю')