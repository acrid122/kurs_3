# -*- coding: utf-8 -*-
from sdamgia import SdamGIA
import json, asyncio
from random import randint
from bs4 import BeautifulSoup
from cairosvg import svg2png
from handlers.tasks_eo.inf.work_with_img import hanldle_text
import os.path
from aiohttp_req import get_body


sdamgia = SdamGIA()


#Распарсить текст
async def get_text(text):
        json_format = json.dumps(text, ensure_ascii=False).encode('utf-8')
        json_format = json.loads(json_format.decode('utf-8'))
        data = json_format['condition']['text']
        return data



#Распарсить картинку
async def get_image(image):
        json_format = json.dumps(image)
        json_format = json.loads(json_format)
        data = json_format['condition']['images']
        return data


#Получить категории по названию задания
async def get_category_id_from_s(subject, theme_number):
    categories = []
    if subject == 'inf' and theme_number == '18':
        categories.append('412')
        return categories
    for i in sdamgia.get_catalog(subject):
        if theme_number == i['topic_id']:
            for x in i['categories']:
                print(x['category_id'])
                categories.append(x['category_id'])
    return categories



#Получение задач по категории
async def get_list_of_tasks_by_c(subject, categoryid, theme_number):
        k = []
        #Поправить для всех уроков
        for i in range(1, 25):
            doujin_page = await get_body(
                f'https://{subject}-ege.sdamgia.ru/test?&filter=all&theme={categoryid}&page={i}')
            soup = BeautifulSoup(doujin_page, 'html.parser')
            k += [i.text.split()[-1] for i in soup.find_all('span', {'class': 'prob_nums'})]
        return k


async def check_answer(s):
     doujin_page = await get_body(s)
     soup = BeautifulSoup(doujin_page, 'html.parser')
     div = soup.find('div',{'class': 'answer'})
     k = div.select('span')
     print(k)
     t = k[0].text
     return t[t.find(' ') + 1:]


#Генерация теста
async def generate_test(client_actions):
    #Получение урока, его номера и количества заданий
    subject = client_actions[1]['subject'].lower()
    theme_number = client_actions[3]['theme'][client_actions[3]['theme'].rfind('_') + 1:]
    amount = int(client_actions[4]['amount'])
    #Сделать amount, если введено свое количество
    

    categories = await get_category_id_from_s(subject, theme_number)
    full_tasks, tasks, pr_ids = [], [], [] #tasks = {}
    for i in categories:
        for x in await get_list_of_tasks_by_c(subject, i, theme_number):
            full_tasks.append(x)
    while len(pr_ids) != amount:
        random_index = randint(0, len(full_tasks) - 1)
        pr_ids.append(random_index)
        if len(set(pr_ids)) != len(pr_ids):
            pr_ids.pop(-1)
            continue
        pr_id = full_tasks[random_index]
        photo_zad = ()


        # if len(''.join(await get_image(sdamgia.get_problem_by_id(subject, pr_id)))) > 0 and theme_number not in ('6'):
        #     p = await get_body(''.join(await get_image(sdamgia.get_problem_by_id(subject, pr_id))), theme_number, 'pic')
        #     print(p)
        #     d = f".\{subject}_photo\{theme_number}\{pr_id}_ris.png"
        #     if not os.path.exists(d):
        #         if theme_number not in('1', '14'):
        #             out = open(d, 'wb+')
        #             out.write(p)
        #             out.close()
        #         else:
        #         #Конвертирование svg в png. Задекодить строчку, так в методе применяется бинарная строка
        #             p = p.encode()
        #             svg2png(bytestring=p.decode('cp437'), write_to = d)
        # else:
        #      d = []
        # photo_zad = ()
        match theme_number:
            case '1' | '4' | '5' | '7' | '8' | '9' | '10' | '11' | '13' | '14' | '15' | '16' | '17' | '23' | '24' | '25':
                photo_zad = await hanldle_text(subject, theme_number, pr_id, 800, 800)
            case '2' | '6' | '12' | '18' | '19' | '20' | '21' | '22' | '26' | '27':
                photo_zad = await hanldle_text(subject, theme_number, pr_id, 900, 900) 
            case '3':
                photo_zad = await hanldle_text(subject, theme_number, pr_id, 1400, 1400)      
        tasks.append(['Задание: ' + str(len(pr_ids)) + '\n' + f'''Источник: <a href=\"https://{subject}-ege.sdamgia.ru/problem?id={pr_id}\">https://{subject}-ege.sdamgia.ru/problem?id={pr_id}</a>''', photo_zad])
    return tasks

#Обработка задания теста. Вывод условия и картинки
# async def call_tasks(client_actions, test):
#     subject = client_actions[1]['subject'].lower()
#     theme_number = client_actions[3]['theme'][client_actions[3]['theme'].rfind('_') + 1:]
#     print(theme_number)
#     tasks = {}
#     for i in test:
#         if len(''.join(await get_image(sdamgia.get_problem_by_id(subject, i)))) > 0:
#             p = requests.get(''.join(await get_image(sdamgia.get_problem_by_id(subject, i))))
#             d = f".\{subject}_photo\{theme_number}\{i}.png"
#             if not os.path.exists(d):
#                 if ('.png'.encode('utf-8') in p.content or '.jpg'.encode('utf-8') in p.content) and theme_number not in('1'):
#                     out = open(d, 'wb+')
#                     out.write(p.content)
#                     out.close()
#                 else:
#                 #Конвертирование svg в png. Задекодить строчку, так в методе применяется бинарная строка
#                     svg2png(bytestring=p.content.decode('cp437'), write_to = d)
#         else:
#              d = []
#         text = await get_text(sdamgia.get_problem_by_id(subject, i))
#         match theme_number:
#              case '1':
#                 text = await hanlde_inf_1(subject,i,text)         
#         tasks.update({text: d})
        
#     return tasks


    


# def get_text(text):
#     json_format = json.dumps(text)
#     json_format = json.loads(json_format)
#     data = json_format['condition']['text'].replace('\xad', '')
#     return data

# 
# subject = 'inf'
# id = '15619'
# html_string = sdamgia.get_problem_by_id(subject, id)
# print(sdamgia.get_category_by_id(subject, '1'))

# print(get_text(html_string))


