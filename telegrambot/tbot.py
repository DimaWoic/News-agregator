import requests
from news.models import News, TUsers


def get_updates():
    url = 'https://api.telegram.org/bot1263816311:AAHtoS8SYIDL6i1LBPH8Csmf7k985MbpcgA/'
    output = []
    r = requests.get(url + 'getUpdates').json()
    if r['ok'] == True:
        result = r['result']
        end_index = len(output) - 1
        for i in range(end_index, 0):
            output.append(result[i])
    else:
        print('Bad request')
    return output


def send_message(chat_id, text):
    url = 'https://api.telegram.org/bot1263816311:AAHtoS8SYIDL6i1LBPH8Csmf7k985MbpcgA/'
    r = requests.get(url + 'sendMessage?chat_id=' + str(chat_id) + '&text=' + text)


def greetings():
    url = 'https://api.telegram.org/bot1263816311:AAHtoS8SYIDL6i1LBPH8Csmf7k985MbpcgA/'
    chat_id_list = []
    user_list = []
    user_dict = {}

    for chat_id in TUsers.objects.all():
        chat_id_list.append(chat_id.user_id)

    updates = get_updates(url)

    for u in updates:
        chat_id = u['message']['chat']['id']
        if chat_id not in user_list:
            user_list.append(chat_id)
            user_dict[chat_id] = [u['message']['chat']['first_name'], u['message']['text']]
            print(u['message']['text'])

    for chat in user_list:
        if chat not in chat_id_list:
            new_tuser = TUsers()
            new_tuser.user_id = chat
            new_tuser.user = user_dict[chat][0]
            new_tuser.save()
            message = 'Привет, Вас приветствует телеграмм бот автоматической рассылки новостей сайта https://rumagpie.ru/, ' \
                      'для начала работы введите старт /start. ВНИМАНИЕ БОТ РАБОТАЕТ В ТЕСТОВОМ РЕЖИМЕ НЕКОТОРЫЕ ФУНКЦИИ МОГУТ НЕРАБОТАТЬ!'
            send_message(chat, message)
            print(message)
        elif chat in chat_id_list:
            if user_dict[chat][1] == '/start':
                new_tuser = TUsers.objects.get(user_id=chat)
                new_tuser.subscription = True
                new_tuser.save()
            elif user_dict[chat][1] == '/stop':
                new_tuser = TUsers.objects.get(user_id=chat)
                new_tuser.subscription = False
                new_tuser.save()
            else:
                message = 'Я незнаю такой команды, повторите ввод. /start - для запуска рассылки, /stop - для остановки'
                send_message(url, chat, message)


def news_sender():
    url = 'https://api.telegram.org/bot1263816311:AAHtoS8SYIDL6i1LBPH8Csmf7k985MbpcgA/'
    for tuser in TUsers.objects.all():
        if tuser.subscription == True:
            news = News.objects.first()
            message = news.url_source
            send_message(tuser.user_id, message)

