import discord
from discord.ext import commands
import logging
import datetime as dt
import time
from random import randint
import pymorphy2
import math

logger = logging.getLogger('discord')  # Подключаем дискорд бота, производим необходимую настройку
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!',
                   intents=intents)  # Ставим префикс боту - символ, на который будут вызываться его команды


@bot.command(
    name='time')  # 1 функция - таймер. Можем поставить таймер на определённое количество минут и секунд,
# когда время закончится бот выведет фразу 'Time X is Over' и закончит работу.
async def time(s, minutes, seconds):
    delta_time = dt.timedelta(minutes=float(minutes), seconds=float(seconds))
    t = delta_time.seconds
    time.sleep(t)
    await s.send(f'Time X is Over')


@bot.command(name='random')  # 2 функция - рандом. Выводит рандомное число из интервала
async def random(s, ch_min, ch_max):
    if int(ch_min) < int(ch_max):
        k = randint(int(ch_min), int(ch_max))
    else:
        k = randint(int(ch_max), int(ch_min))
    await s.send(k)


@bot.command(name='massive')  # 3 функция - массив рандомных чисел.
async def massive(s, st, ch_min, ch_max):
    list_k = []
    if ch_min < ch_max:
        for i in range(int(st)):
            list_k.append(randint(int(ch_min), int(ch_max)))
    else:
        for i in range(int(st)):
            list_k.append(randint(int(ch_max), int(ch_min)))
    await s.send(list_k)


@bot.command(name='eval')  # 4 функция - позволяет посчитать введённое пользователем выражение
async def ev_al(s, *args):
    list_k = []
    for i in args:
        list_k.append(i)
    k = ' '.join(list_k)
    await s.send(eval(k))


@bot.command(name='char')  # 5 функция - позволяет вывести любой элемент из chr по номеру
async def char(s, ch):
    k = chr(int(ch))
    await s.send(k)


@bot.command(name='cat')  # 6 функция - выводит кота
async def cat(s):
    k1 = chr(ord('フ'))
    k2 = chr(ord('＞'))
    k3 = chr(ord('◕'))
    k4 = chr(ord('`'))
    k5 = chr(ord('ミ'))
    k6 = chr(ord('x'))
    k7 = chr(ord('彡'))
    k8 = chr(ord('ヽ'))
    k9 = chr(ord('ﾉ'))
    k10 = chr(ord('￣'))
    k11 = chr(ord('ヽ'))
    k12 = chr(ord('二'))
    k13 = chr(ord('つ'))
    t1 = f'.                    ／{k2}　／{k1}'
    t2 = f'.　　　　| 　{k3} {k3} |'
    t3 = f'.　 　　／{k4}{k5}  {k6} {k7}'
    t4 = f'.　　  /　　　 　 |'
    t5 = f'.　　 /　 {k8}　　 {k9}'
    t6 = f'.／{k10}|　　 |　|　 |'
    t7 = f'.| ({k10}{k11}＿{k11})  {k11}＿{k11})'
    t8 = f'.＼＼{k12}{k13}'
    await s.send(t1)
    await s.send(t2)
    await s.send(t3)
    await s.send(t4)
    await s.send(t5)
    await s.send(t6)
    await s.send(t7)
    await s.send(t8)


@bot.command(name='amogus')  # 7 функция - выводит амогуса
async def amo_gus(s):
    k1 = chr(ord('⬛'))
    k2 = chr(ord('🟥'))
    k3 = chr(ord('🟦'))
    k4 = chr(ord('⬜'))
    k5 = chr(ord('🟪'))
    t1 = f'.                            {k1}{k2}{k2}{k2}{k2}{k2}{k2}{k1}'
    t2 = f'.                      {k1}{k2}{k2}{k2}{k2}{k2}{k2}{k2}{k2}{k1}'
    t3 = f'.                 {k1}{k2}{k2}{k2}{k2}{k1}{k1}{k1}{k1}{k1}{k1}'
    t4 = f'.                    {k1}{k2}{k2}{k2}{k1}{k3}{k3}{k4}{k4}{k4}{k1}'
    t5 = f'.                 {k1}{k2}{k2}{k1}{k5}{k3}{k3}{k3}{k4}{k4}{k4}{k3}{k1}'
    t6 = f'.      {k1}{k1}{k1}{k2}{k2}{k1}{k5}{k3}{k3}{k3}{k3}{k3}{k3}{k3}{k1}'
    t7 = f'.{k1}{k2}{k2}{k1}{k2}{k2}{k1}{k5}{k5}{k5}{k3}{k3}{k3}{k3}{k5}{k1}'
    t8 = f'.{k1}{k2}{k2}{k1}{k2}{k2}{k2}{k1}{k5}{k5}{k5}{k5}{k5}{k1}'
    t9 = f'.{k1}{k2}{k2}{k1}{k2}{k2}{k2}{k2}{k1}{k1}{k1}{k1}{k1}{k1}{k1}'
    t10 = f'.{k1}{k2}{k2}{k1}{k2}{k2}{k2}{k2}{k2}{k2}{k2}{k2}{k2}{k2}{k1}'
    t11 = f'.{k1}{k2}{k2}'
    await s.send(t1)
    await s.send(t2)
    await s.send(t3)
    await s.send(t4)
    await s.send(t5)
    await s.send(t6)
    await s.send(t7)
    await s.send(t8)
    await s.send(t9)
    await s.send(t10)
    await s.send(t10)
    await s.send(t10)
    await s.send(t10)
    await s.send(t10)
    await s.send(t11)


@bot.command(
    name='maths')  # 8 функция - математика, позволяет считать синус, косинус, тангенс, котангенс, арксинус,
# арккосинус, арктангенс или арккотангенс введённого числа
async def maths(s, arg):
    list_k = []
    j = arg.find('(')
    m = float(arg[j + 1: -1])
    for i in arg:
        if i == '(':
            break
        list_k.append(i)
    k = ''.join(list_k)
    if k == 'sin':  # Тригонометрия
        await s.send(round(math.sin(m * math.pi / 180), 3))
    if k == 'cos':
        await s.send(round(math.cos(m * math.pi / 180), 3))
    if k == 'tan':
        await s.send(round(math.tan(m * math.pi / 180), 3))
    if k == 'cot':
        await s.send(1 / round(math.tan(m * math.pi / 180), 3))

    if k == 'asin':
        await s.send(round(math.asin(m) / math.pi * 180, 3))
    if k == 'acos':
        await s.send(round(math.acos(m) / math.pi * 180, 3))
    if k == 'atan':
        await s.send(round(math.atan(m) / math.pi * 180, 3))
    if k == 'acot':
        await s.send(1 / (round(math.atan(m) / math.pi * 180, 3)))


@bot.command(name='nouns')  # 9 функция - выводит из предоставленного текста "правильные" существительные
async def nouns(s, *args):
    list_p = []
    for i in args:  # оставляем только неповторяющиеся существительные из предоставленного текста
        if i != '--' and i != '—' and i != '-':
            if i[-1] == ',' or i[-1] == '.' or i[-1] == ':' or i[-1] == '!' or i[-1] == '?' or i[-1] == ';':
                sa = i[:-1]
                if sa.lower() not in list_p:
                    list_p.append(sa.lower())
            else:
                if i.lower() not in list_p:
                    list_p.append(i.lower())
    morph = pymorphy2.MorphAnalyzer()
    noun = {}
    for j in list_p:  # проверяем являются ли выбранные существительные "правильными" и выводим их
        p = morph.parse(j)[0]
        if 'NOUN' in p.tag and p.score > 0.5:
            noun[p.normal_form] = noun.get(p.normal_form, 0) + 1
    noun = [x[0] for x in sorted(noun.items(), key=lambda x: (x[1], x[0]), reverse=True)]
    await s.send(noun[:10])


@bot.command(name='skl')  # 10 функция - склоняет существительное по числам и подежам
async def skl(s, skl_noun):
    morph = pymorphy2.MorphAnalyzer()
    res = morph.parse(skl_noun)[0]  # считываем слово, ниже склоняем
    if 'NOUN' not in res.tag:
        await s.send(f'Не существительное')
    else:
        await s.send('Единственное число:')
        await s.send(f'Именительный падеж: {res.inflect({"nomn"}).word}')
        await s.send(f'Родительный падеж: {res.inflect({"gent"}).word}')
        await s.send(f'Дательный падеж: {res.inflect({"datv"}).word}')
        await s.send(f'Винительный падеж: {res.inflect({"accs"}).word}')
        await s.send(f'Творительный падеж: {res.inflect({"ablt"}).word}')
        await s.send(f'Предложный падеж: {res.inflect({"loct"}).word}')
        await s.send(f'Множественное число:')
        await s.send(f'Именительный падеж: {res.inflect({"nomn", "plur"}).word}')
        await s.send(f'Родительный падеж: {res.inflect({"gent", "plur"}).word}')
        await s.send(f'Дательный падеж: {res.inflect({"datv", "plur"}).word}')
        await s.send(f'Винительный падеж: {res.inflect({"accs", "plur"}).word}')
        await s.send(f'Творительный падеж: {res.inflect({"ablt", "plur"}).word}')
        await s.send(f'Предложный падеж: {res.inflect({"loct", "plur"}).word}')


TOKEN = "MTA4NzY2OTk5NTIwMDMxNTQ1NA.GeCAJf.fH9stF5P3y-JhaMj9y26z_EW1kuNpGqnDxwWfY"
bot.run(TOKEN)
