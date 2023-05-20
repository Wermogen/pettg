from db import users_db
from bot import bot


def send_message_to_all_users(message: str):
    if message != '':
        for user in users_db.find():
            try:
                bot.send_message(user['chat_id'], message)
            except Exception as e:
                print('Что-то не так')


if __name__ == '__main__':
    input_message = input('Сообщение  для рассылки: ')
    send_message_to_all_users(input_message)