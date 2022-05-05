from aiogram import types, executor, Dispatcher, Bot
from aiogram.types.reply_keyboard import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import requests
import random

#-------------------------------
#Russia
#-------------------------------
btnMain = KeyboardButton('◀Главное меню')
###----Links----####
TOKEN = '2136113393:AAEhIWfdRQKcI9IlSAf_cVFm8iOb8U87GFE'
API_LINK = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5' 
response = requests.get(API_LINK).json()
#Chose language menu
btnRussia = KeyboardButton('Русский🐷')
btnEnglish = KeyboardButton('English')
choselanguage = ReplyKeyboardMarkup(resize_keyboard = True).add(btnRussia,btnEnglish)
###----Markups'Main menu'----###
btnRandom = KeyboardButton('🎲Рандомное число')
btnCourse = KeyboardButton('💱Курс валют')
btnInfo = KeyboardButton('📜Информация')
mainmenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnCourse, btnRandom, btnInfo)
###----Markups'Course'----###
btnRub = InlineKeyboardButton('RUB💴', callback_data='RUR')
btnEur = InlineKeyboardButton('EUR💶', callback_data='EUR')
btnUsd = InlineKeyboardButton('USD💵', callback_data='USD')
btnBtc = InlineKeyboardButton('BTC💎', callback_data='BTC')
course = InlineKeyboardMarkup(resize_keyboard = True).add(btnUsd, btnEur, btnRub, btnBtc)
###----Markups'Info'----###
btnAboutBot = KeyboardButton('👾О боте')
btnAboutMe = KeyboardButton('🤓О создатиле')
info = ReplyKeyboardMarkup(resize_keyboard = True).add(btnAboutBot,btnAboutMe,btnMain)
#-------------------------------
#English
#-------------------------------
ebtnMain = KeyboardButton('◀Main menu')
###----Markups'Main menu'----###
ebtnRandom = KeyboardButton('🎲Random number')
ebtnCourse = KeyboardButton('💱Exchange rates')
ebtnInfo = KeyboardButton('📜Info')
emainmenu = ReplyKeyboardMarkup(resize_keyboard = True).add(ebtnCourse, ebtnRandom, ebtnInfo)
###----Markups'Info'----###
ebtnAboutBot = KeyboardButton('👾About bot')
ebtnAboutMe = KeyboardButton('🤓About owner')
einfo = ReplyKeyboardMarkup(resize_keyboard = True).add(ebtnAboutBot,ebtnAboutMe,ebtnMain)
#-------------------------------
def printCoin(buy):
    return "Курс покупки:" + str(buy)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def begin(message :types.Message):
    await bot.send_message(message.chat.id, 'Привет {0.first_name}'.format(message.from_user), reply_markup = choselanguage)

@dp.message_handler()
async def navigationru(message: types.Message):
    if message.text == 'Русский🐷':
        await bot.send_message(message.chat.id, 'Русский🐷', reply_markup=mainmenu)
    elif message.text == '🎲Рандомное число':
        await bot.send_message(message.chat.id, random.randint(0,100))
    elif message.text == '💱Курс валют':
        await bot.send_message(message.chat.id, 'Курс которой валюты, вы хотите узнать?📈', reply_markup = course)
    elif message.text == '📜Информация':
        await bot.send_message(message.chat.id, '📜Информация', reply_markup=info)
    if message.text == '👾О боте':
        await bot.send_message(message.chat.id, 'Данный бот👾 создан в целях изучения языка програмирования Python🐍,\nи не несёт никакой комерчиской цели🌍.Приятного пользования🍀')
    elif message.text == '🤓О создатиле':
        await bot.send_message(message.chat.id, 'Привет меня зовут Олежан🧑, я разроботчик данного бота📦.\nМой дискорд бот: https://bit.ly/3pKOzzd')
    elif message.text == '◀Главное меню':
        await bot.send_message(message.chat.id, '◀Главное меню', reply_markup = mainmenu)
    elif message.text == 'English':
        await bot.send_message(message.chat.id, 'English', reply_markup=emainmenu)
    elif message.text == '🎲Random number':
        await bot.send_message(message.chat.id, random.randint(0,100))
    elif message.text == '💱Exchange rates':
        await bot.send_message(message.chat.id, 'Which currency rate do you want to know?(to UAN)📈', reply_markup = course)
    elif message.text == '📜Info':
        await bot.send_message(message.chat.id, '📜Info', reply_markup=einfo)
    if message.text == '👾About bot':
        await bot.send_message(message.chat.id, 'This bot👾 created to learn Python🐍,\nand does not serve any commercial purpose🌍.Good luck🍀')
    elif message.text == '🤓About owner':
        await bot.send_message(message.chat.id, 'Hi my name is Oleh🧑, i am cretror of this bot📦.\nMy discord bot: https://bit.ly/3pKOzzd')
    elif message.text == '◀Main menu':
        await bot.send_message(message.chat.id, '◀Main menu', reply_markup = emainmenu)


@dp.callback_query_handler(lambda c: c.data == "RUR")
async def RUB_button(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    for coin in response:
        if 'RUR' == coin['ccy']:
            await bot.send_message(call.message.chat.id,"RUB💴\n" + printCoin(coin['buy']))

@dp.callback_query_handler(lambda c: c.data == "USD")
async def USD_button(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    for coin in response:
        if 'USD' == coin['ccy']:
            await bot.send_message(call.message.chat.id,"USD💵\n" + printCoin(coin['buy']))

@dp.callback_query_handler(lambda c: c.data == "EUR")
async def EUR_button(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    for coin in response:
        if 'EUR' == coin['ccy']:
            await bot.send_message(call.message.chat.id,"EUR💶\n" + printCoin(coin['buy']))

@dp.callback_query_handler(lambda c: c.data == "BTC")
async def BTC_button(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    for coin in response:
        if 'BTC' == coin['ccy']:
            await bot.send_message(call.message.chat.id,"BTC💎\n" + printCoin(coin['buy']) + '$')


executor.start_polling(dp)
