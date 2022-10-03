import telebot
from telebot import types
import time


from datetime import datetime as dt
from time import time


def answer_logger(data):
    file_log_answer = 'answer1.txt'
    time = dt.now().strftime("%d/%m/%Y Time %H:%M")
    with open(file_log_answer, 'a') as file:
        file.write(f'{time} Answer = {data}\n')


def game_tik_logger(data):
    f_game_log = 'game.txt'
    time = dt.now().strftime("%d/%m/%Y Time %H:%M")
    with open(f_game_log, 'a') as f:
        f.write(f'{time} - {data}')

import re


def frm_value(num_str):
    if num_str.find(',') != -1:
        num_str = re.sub(",", ".", num_str)
    return num_str


def check_answer_calc(num):
    if float(num) == int(num):
        return int(num)
    else:
        num = ('{:.3f}'.format(num))
        return float(num)


def calc(num_str, firstname, lastname):
    try:
        num_str = frm_value(num_str)
        if num_str.find('+') != -1:
            a = float(num_str[0:num_str.find('+'):])
            b = float(num_str[num_str.find('+') + 1::])
            num = a + b
            answer = check_answer_calc(num)
            write_loger(answer, num_str, firstname, lastname)
            return answer
        elif num_str.find('-') != -1:
            a = float(num_str[0:num_str.find('-'):])
            b = float(num_str[num_str.find('-') + 1::])
            num = a - b
            answer = check_answer_calc(num)
            write_loger(answer, num_str, firstname, lastname)
            return answer
        elif num_str.find('*') != -1:
            a = float(num_str[0:num_str.find('*'):])
            b = float(num_str[num_str.find('*') + 1::])
            num = a * b
            answer = check_answer_calc(num)
            write_loger(answer, num_str, firstname, lastname)
            return answer
        elif num_str.find('/') != -1:
            a = float(num_str[0:num_str.find('/'):])
            b = float(num_str[num_str.find('/') + 1::])
            if b == 0:
                return 'На 0 делить нельзя'
            num = a / b
            answer = check_answer_calc(num)
            write_loger(answer, num_str, firstname, lastname)
            return answer
    except ValueError:
        return 'Упс, что-то пошло не так. Попробуй еще раз;)'


def write_loger(answer, num_str, firstname, lastname):
    answer_str = f'{firstname} {lastname}: {num_str} = {answer}'
    Logger.answer_logger(answer_str)

from selenium import webdriver
from selenium.webdriver.common.by import By

def get_exchange():
    driver = webdriver.Chrome(r'C:\Users\Lenovo\Documents\chromedriver.exe')
    url = 'https://www.banki.ru/products/currency/cash/sankt-peterburg/'
    driver.maximize_window()
    driver.get(url)
    currency = driver.find_elements(By.XPATH,"//div[@class='table-flex__cell table-flex__cell--without-padding padding-left-default']")
    return currency[1].text, currency[2].text

def game_field():
    mas_game = f'_1_2_3_\n_4_5_6_\n_7_8_9_'
    return mas_game


def process_game(field, num, how_walks):
    mas_game = field
    sign_x = 'X'
    sign_o = 'O'
    if how_walks == 1:
        if mas_game.find(num) != -1:
            mas_game = mas_game.replace(num, sign_x)
            return mas_game
    elif how_walks == 2:
        if mas_game.find(num) != -1:
            mas_game = mas_game.replace(num, sign_o)
            return mas_game


def check_win(field, user_name):
    mas_game = field.split(f'\n')
    sign_x = 'X'
    sign_o = 'O'
    for i in range(len(mas_game)):
        tmp = str(mas_game[i])
        if tmp.count('X') == 3:
            Logger.game_tik_logger(f'Победил {sign_x} он же {user_name}')
            return sign_x
        elif tmp.count('O') == 3:
            Logger.game_tik_logger(f'Победил {sign_o} он же {user_name}')
            return sign_o
    if mas_game[0][1] == mas_game[1][1] == mas_game[2][1]:
        Logger.game_tik_logger(f'Победил {mas_game[0][1]} он же {user_name}')
        return mas_game[0][1]
    if mas_game[0][3] == mas_game[1][3] == mas_game[2][3]:
        Logger.game_tik_logger(f'Победил {mas_game[0][3]} он же {user_name}')
        return mas_game[0][3]
    if mas_game[0][5] == mas_game[1][5] == mas_game[2][5]:
        Logger.game_tik_logger(f'Победил {mas_game[0][5]} он же {user_name}')
        return mas_game[0][5]
    if mas_game[0][1] == mas_game[1][3] == mas_game[2][5]:
        Logger.game_tik_logger(f'Победил {mas_game[0][1]} он же {user_name}')
        return mas_game[0][1]
    if mas_game[0][5] == mas_game[1][3] == mas_game[2][1]:
        Logger.game_tik_logger(f'Победил {mas_game[0][5]} он же {user_name}')
        return mas_game[0][5]



bot = telebot.TeleBot(config.token)
# command /start


num_user_str = ''
paint_field = f'_1_2_3_\n_4_5_6_\n_7_8_9_'
count = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
pos = 9
how_walks = 1


@bot.message_handler(commands=["start"])
def start_command(msg):
    butt = types.ReplyKeyboardRemove(selective=False)
    mess = f'Приветуствую тебя, {msg.from_user.first_name} {msg.from_user.last_name}'
    bot.send_message(msg.chat.id, mess, reply_markup=butt)


@bot.message_handler(commands=["calc"])
def calc_command(msg):
    butt = types.ReplyKeyboardRemove(selective=False)
    mess = f'Я простой калькулятор\nВведите выражение - Пример: 10+20, 30/10 и т.д.)'
    msg2 = bot.send_message(msg.chat.id, mess, reply_markup=butt)
    bot.register_next_step_handler(msg2, get_value)


def get_value(msg, result=None):
    try:
        global num_user_str
        if result == None:
            num_user_str = msg.text
        else:
            num_user_str = msg.text
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Результат')
        markup.add(btn1)
        msg2 = bot.send_message(msg.chat.id, 'Сейчас, я покажу ответ)))Жмакай на кнопку', reply_markup=markup)
        bot.register_next_step_handler(msg2, step_for_calc)
    except ValueError:
        bot.reply_to(msg, 'Упс!(Что-то пошло не так(Попродуй еще раз!)')


def step_for_calc(msg):
    try:
        global num_user_str
        answer_user = calc(num_user_str, msg.from_user.first_name, msg.from_user.last_name)
        butt = types.ReplyKeyboardRemove(selective=False)
        if msg.text == 'Результат':
            bot.send_message(msg.chat.id, answer_print(answer_user), reply_markup=butt)
    except ValueError:
        bot.reply_to(msg, 'Упс!(Что-то пошло не так(Попродуй еще раз!)')


def answer_print(answer_user):
    global num_user_str
    return f'Результат: {num_user_str} = {answer_user}'


@bot.message_handler(commands=["exchange"])
def exchange(msg):
    exg = exchange_methods.get_exchange()
    mess = f'Сейчас я открою сайт курса валют и выведу тебе курс евра и доллара:)))\nUSD: {exg[0]}\nEUR: {exg[1]}'
    bot.send_message(msg.chat.id, mess)


@bot.message_handler(commands=["help"])
def exchange(msg):
    mess = f'Я покажу тебе, все, что я могу.А могу, я очень мало:(((\nТы не обижайся, ведь, я только учусь\nЛови команды\n/calc\n/start\n/exchange'
    bot.send_message(msg.chat.id, mess)


@bot.message_handler(commands=["Game"])
def start_game(msg):
    mess = f'Игра крестики нолики\n\n{game_Tic.game_field()}'
    bot.send_message(msg.chat.id, mess)
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('1')
    btn2 = types.KeyboardButton('2')
    btn3 = types.KeyboardButton('3')
    btn4 = types.KeyboardButton('4')
    btn5 = types.KeyboardButton('5')
    btn6 = types.KeyboardButton('6')
    btn7 = types.KeyboardButton('7')
    btn8 = types.KeyboardButton('8')
    btn9 = types.KeyboardButton('9')
    markup1.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
    mess = 'Выбери куда поставишь X или О'
    msg2 = bot.send_message(msg.chat.id, mess, reply_markup=markup1)
    bot.register_next_step_handler(msg2, continuation_game)


def continuation_game(msg):
    global paint_field
    global count
    global pos
    global how_walks
    markup1 = types.ReplyKeyboardRemove(selective=False)
    ans = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    while pos >= 1:
        if how_walks == 1 or how_walks == 2:
            for i in range(len(ans)):
                if msg.text == ans[i] and how_walks == 1:
                    paint_field1 = process_game(paint_field, msg.text, how_walks)
                    paint_field = paint_field1
                    how_walks += 1
                    qqq = game_Tic.check_win(paint_field, msg.from_user.first_name)
                    if qqq == None:
                        count = [x for x in count if x != msg.text]
                        bot.send_message(msg.chat.id, paint_field, reply_markup=markup1)
                        time.sleep(1)
                        pos -= 1
                        break
                    else:
                        count = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                        pos = 9
                        how_walks = 1
                        paint_field = f'_1_2_3_\n_4_5_6_\n_7_8_9_'
                        markup1 = types.ReplyKeyboardRemove(selective=False)
                        bot.send_message(msg.chat.id, f'Ура!! {qqq} Победил', reply_markup=markup1)
                elif msg.text == ans[i] and how_walks == 2:
                    paint_field1 = game_Tic.process_game(paint_field, msg.text, how_walks)
                    paint_field = paint_field1
                    how_walks -= 1
                    qqq = game_Tic.check_win(paint_field, msg.from_user.first_name)
                    if qqq == None:
                        count = [x for x in count if x != msg.text]
                        bot.send_message(msg.chat.id, paint_field, reply_markup=markup1)
                        time.sleep(1)
                        pos -= 1
                        break
                    else:
                        count = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                        pos = 9
                        how_walks = 1
                        paint_field = f'_1_2_3_\n_4_5_6_\n_7_8_9_'
                        markup1 = types.ReplyKeyboardRemove(selective=False)
                        bot.send_message(msg.chat.id, f'Ура!! {qqq} Победил', reply_markup=markup1)
        if len(count) == 0:
            bot.send_message(msg.chat.id, 'Победила дружба)))')
        elif qqq == None:
            markup1 = get_btn()
            mess = 'Выбери куда поставишь X или О'
            msg2 = bot.send_message(msg.chat.id, mess, reply_markup=markup1)
            print(len(count))
        break
    if len(count) != 0 and qqq == None:
        bot.register_next_step_handler(msg2, continuation2_game)


def continuation2_game(msg):
    global paint_field
    global count
    global pos
    global how_walks
    markup1 = types.ReplyKeyboardRemove(selective=False)
    ans = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    while pos >= 1:
        if how_walks == 1 or how_walks == 2:
            for i in range(len(ans)):
                if msg.text == ans[i] and how_walks == 1:
                    paint_field1 = game_Tic.process_game(paint_field, msg.text, how_walks)
                    paint_field = paint_field1
                    how_walks += 1
                    qqq = game_Tic.check_win(paint_field, msg.from_user.first_name)
                    if qqq == None:
                        count = [x for x in count if x != msg.text]
                        bot.send_message(msg.chat.id, paint_field, reply_markup=markup1)
                        time.sleep(1)
                        pos -= 1
                        break
                    else:
                        count = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                        pos = 9
                        how_walks = 1
                        paint_field = f'_1_2_3_\n_4_5_6_\n_7_8_9_'
                        markup1 = types.ReplyKeyboardRemove(selective=False)
                        bot.send_message(msg.chat.id, f'Ура!! {qqq} Победил', reply_markup=markup1)
                elif msg.text == ans[i] and how_walks == 2:
                    paint_field1 = process_game(paint_field, msg.text, how_walks)
                    paint_field = paint_field1
                    how_walks -= 1
                    qqq = game_Tic.check_win(paint_field, msg.from_user.first_name)
                    if qqq == None:
                        count = [x for x in count if x != msg.text]
                        bot.send_message(msg.chat.id, paint_field, reply_markup=markup1)
                        time.sleep(1)
                        pos -= 1
                        break
                    else:
                        count = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                        pos = 9
                        how_walks = 1
                        paint_field = f'_1_2_3_\n_4_5_6_\n_7_8_9_'
                        markup1 = types.ReplyKeyboardRemove(selective=False)
                        bot.send_message(msg.chat.id, f'Ура!! {qqq} Победил', reply_markup=markup1)
        if len(count) == 0:
            bot.send_message(msg.chat.id, 'Победила дружба)))')
        elif qqq == None:
            markup1 = get_btn()
            mess = 'Выбери куда поставишь X или О'
            msg2 = bot.send_message(msg.chat.id, mess, reply_markup=markup1)
            print(len(count))
        break
    if len(count) != 0 and qqq == None:
        bot.register_next_step_handler(msg2, continuation_game)


def get_btn():
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    if len(count) == 8:
        btn1 = types.KeyboardButton(count[0])
        btn2 = types.KeyboardButton(count[1])
        btn3 = types.KeyboardButton(count[2])
        btn4 = types.KeyboardButton(count[3])
        btn5 = types.KeyboardButton(count[4])
        btn6 = types.KeyboardButton(count[5])
        btn7 = types.KeyboardButton(count[6])
        btn8 = types.KeyboardButton(count[7])
        markup1.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        return markup1
    if len(count) == 7:
        btn1 = types.KeyboardButton(count[0])
        btn2 = types.KeyboardButton(count[1])
        btn3 = types.KeyboardButton(count[2])
        btn4 = types.KeyboardButton(count[3])
        btn5 = types.KeyboardButton(count[4])
        btn6 = types.KeyboardButton(count[5])
        btn7 = types.KeyboardButton(count[6])
        markup1.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        return markup1
    if len(count) == 6:
        btn1 = types.KeyboardButton(count[0])
        btn2 = types.KeyboardButton(count[1])
        btn3 = types.KeyboardButton(count[2])
        btn4 = types.KeyboardButton(count[3])
        btn5 = types.KeyboardButton(count[4])
        btn6 = types.KeyboardButton(count[5])
        markup1.add(btn1, btn2, btn3, btn4, btn5, btn6)
        return markup1
    if len(count) == 5:
        btn1 = types.KeyboardButton(count[0])
        btn2 = types.KeyboardButton(count[1])
        btn3 = types.KeyboardButton(count[2])
        btn4 = types.KeyboardButton(count[3])
        btn5 = types.KeyboardButton(count[4])
        markup1.add(btn1, btn2, btn3, btn4, btn5)
        return markup1
    if len(count) == 4:
        btn1 = types.KeyboardButton(count[0])
        btn2 = types.KeyboardButton(count[1])
        btn3 = types.KeyboardButton(count[2])
        btn4 = types.KeyboardButton(count[3])
        markup1.add(btn1, btn2, btn3, btn4)
        return markup1
    if len(count) == 3:
        btn1 = types.KeyboardButton(count[0])
        btn2 = types.KeyboardButton(count[1])
        btn3 = types.KeyboardButton(count[2])
        markup1.add(btn1, btn2, btn3)
        return markup1
    if len(count) == 2:
        btn1 = types.KeyboardButton(count[0])
        btn2 = types.KeyboardButton(count[1])
        markup1.add(btn1, btn2)
        return markup1
    if len(count) == 1:
        btn1 = types.KeyboardButton(count[0])
        markup1.add(btn1)
        return markup1
    if len(count) == 0:
        return 0
    # for i in range(len(count)):
    #         btn = types.KeyboardButton(count[i])
    #         markup1.add(btn)
    # return markup1


bot.polling(none_stop=True)