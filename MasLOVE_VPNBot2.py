import telebot

bot = telebot.TeleBot('')
joinedFile = open("joined.txt", "r")
joinedUsers = set()
for line in joinedFile:
    joinedUsers.add(line.strip())
joinedFile.close()


@bot.message_handler(commands=['start'])
def startjoin(message):
    bot.send_message(message.chat.id,
                     'Привет! Я буду напоминать тебе об оплате ВПН! Маслов понял, что вручную всем писать долго и впадлу, поэтому создал меня)')
    if not str(message.chat.id) in joinedUsers:
        joinedFile = open("joined.txt", "a")
        joinedFile.write(str(message.chat.id) + "\n")
        joinedUsers.add(message.chat.id)


@bot.message_handler(commands=['special'])
def mess(message):
    for user in joinedUsers:
        bot.send_message(user, message.text[message.text.find(' '):])

bot.polling(none_stop=True, interval=0)
