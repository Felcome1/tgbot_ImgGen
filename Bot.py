import ImgGen
import telebot as tb
from PIL import Image

TOKEN = '6670216674:AAE499rSLCF9QRM_kDrDD_FnWyMh_Zt2pcs'
bot = tb.TeleBot(TOKEN)

bot_answer = ['placeholder' for i in range(7)]

values = {}


@bot.message_handler(content_types=['text'])
def get_txt_msg(msg):
    if msg.text == '/start':
        bot.send_message(msg.from_user.id, 'Привет! \nВведите /new чтобы начать работу с ботом!')

    elif msg.text == '/new':
        values[msg.from_user.id] = []
        bot.send_message(msg.from_user.id, 'Скриншоты для наглядности (элементы редактируются в их порядке')
        comp = Image.open('templates/complete.JPG')
        bot.send_photo(msg.from_user.id, comp)
        order = Image.open('templates/order.JPG')
        bot.send_photo(msg.from_user.id, order)

        bot.send_message(msg.from_user.id, bot_answer[0])
        bot.register_next_step_handler(msg, get_time)


def get_value(msg):
    if msg.text:
        values[msg.from_user.id].append(msg.text)


def send_pics(id):
    print(values)
    img_complete, img_order = ImgGen.generate(*[values[id].pop(0) for i in range(len(values[id]))])
    bot.send_photo(id, img_complete)
    bot.send_photo(id, img_order)


def get_time(msg):
    if msg.text:
        bot.send_message(msg.from_user.id, bot_answer[1])
        values[msg.from_user.id].append(msg.text)
        bot.register_next_step_handler(msg, get_cur)


def get_cur(msg):
    if msg.text:
        bot.send_message(msg.from_user.id, bot_answer[2])
        values[msg.from_user.id].append(msg.text)
        bot.register_next_step_handler(msg, get_sum)


def get_sum(msg):
    if msg.text:
        bot.send_message(msg.from_user.id, bot_answer[3])
        values[msg.from_user.id].append(msg.text)
        bot.register_next_step_handler(msg, get_cost)


def get_cost(msg):
    if msg.text:
        bot.send_message(msg.from_user.id, bot_answer[4])
        values[msg.from_user.id].append(msg.text)
        bot.register_next_step_handler(msg, get_num)


def get_num(msg):
    if msg.text:
        bot.send_message(msg.from_user.id, bot_answer[5])
        values[msg.from_user.id].append(msg.text)
        bot.register_next_step_handler(msg, get_datetime)


def get_datetime(msg):
    if msg.text:
        bot.send_message(msg.from_user.id, bot_answer[6])
        values[msg.from_user.id].append(msg.text)
        bot.register_next_step_handler(msg, get_name)


def get_name(msg):
    if msg.text:
        bot.send_message(msg.from_user.id, bot_answer[7])
        values[msg.from_user.id].append(msg.text)
        bot.register_next_step_handler(msg, get_num2)


def get_num2(msg):
    if msg.text:
        bot.send_message(msg.from_user.id, 'Результат:')
        values[msg.from_user.id].append(msg.text)

        print(values)
        send_pics(msg.from_user.id)
        bot.send_message(msg.from_user.id, 'Чтобы начать снова введите /new.')


bot.polling(none_stop=True, interval=0)