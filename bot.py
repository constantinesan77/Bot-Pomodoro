import telebot
import time
import config


global start_time
global stop_time
global current

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Thank for using my bot ^^.\n' +
                     'If u have a questions for bot, send message to me @constantineopole, \n' +
                     'also u can use /help , this command help you :)')


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'You can use this commands : \n' +
                     '/start \n' +
                     '/help \n' +
                     '/concentrate \n' +
                     '/result \n' +
                     '/stop \n' +
                     '/exit')


@bot.message_handler(commands=['concentrate'])
def concentrate_func(message):
    global start_time
    start_time = message.date
    global current
    current = True
    while current:
        for x in range(4):
            if current:
                bot.send_message(message.chat.id, 'You start work')
                time.sleep(1500)

            if current:
                bot.send_message(message.chat.id, 'Please relax 5 minutes')
                time.sleep(300)

            if current:
                bot.send_message(message.chat.id, 'Start work again')

        if current:
            bot.send_message(message.chat.id, 'U need to relax 30 min')
            time.sleep(1800)


@bot.message_handler(commands=['stop'])
def stop_func(message):
    bot.send_message(message.chat.id, 'U stop working')
    global stop_time
    stop_time = message.date
    global current
    current = False


@bot.message_handler(commands=['result'])
def result_func(message):
    bot.send_message(message.chat.id, 'In this time u start working: ' + time.ctime(start_time))
    bot.send_message(message.chat.id, 'In this time u stop working: ' + time.ctime(stop_time))


@bot.message_handler(commands=['exit'])
def exit_func(message):
    bot.send_message(message.chat.id, 'U stop working')


bot.polling(none_stop=True)
