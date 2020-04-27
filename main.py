from db import list_users, query_user_last_seen
import datetime
from check_email import check_mail
import time
import os
registered_users = list_users()


def enter_mail():
    i = 0
    while(True):
        email=input('Введите email:')
        if check_mail(email):
            check_base(email)
            break
        elif i+1==3:
            print('Введен не верный Email, попробуйте позднее.')
            i=0
            sl_time =10
            while(sl_time>0):
                time.sleep(1)
                print('\r', end='')
                print(sl_time,end='')
                sl_time -=1

        else:
            print('Email не верен, попробуйте еще раз')
            i +=1

def check_base(login):
    print(login)
    login = login[:login.find('@')].lower()
    print(login)
    now = datetime.datetime.now()
    last = query_user_last_seen(login)
    delta = datetime.timedelta(days=180)
    if now ==last:
        print('Вы с нами совсем недавно! Добро пожаловать')
    elif now - last < delta:
        print(f'Ваш аккаунт подтвержден до {now+delta}')
    else:
        print('Вам нужно подтвердить логин')

enter_mail()
