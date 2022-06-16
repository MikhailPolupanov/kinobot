from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, ParseMode
from telegram.ext import ConversationHandler
import random

def anketa_random_start(update, context):
    update.message.reply_text(f'Вы выбрали случайный фильм. Нажмите на кнопку "Получить фильм" и подождите немного, пока его подберу', reply_markup=ReplyKeyboardMarkup([["Получить фильм"]], one_time_keyboard=True))
    return 'anketa_random_result'
    
def anketa_random_result(update, context):

    movies_list = ['Красотка','Зеленая миля','Бетмен: начало','Форрест Гамп','Перл Харбор','Храброе сердце','Девчата']
    
    update.message.reply_text(f'Ваш случайный фильм: {movies_list[random.randint(0,len(movies_list))]}. \nМожете попросить меня подобрать другой случайный фильм', reply_markup=ReplyKeyboardMarkup([['Подобрать другой случайный фильм', 'Я нашел нужный фильм']], one_time_keyboard=True))
    return 'final_random'

def final_random(update, context):
    if str(update.message.text) == 'Подобрать другой случайный фильм':
        return 'anketa_random_result'
    else:
        update.message.reply_text(f'Рад был помочь!', reply_markup=ReplyKeyboardMarkup([['Вернуться в начало']], one_time_keyboard=True))
        return ConversationHandler.END

def anketa_dontknow_random(update, context):
    update.message.reply_text('Я вас не понимаю')
