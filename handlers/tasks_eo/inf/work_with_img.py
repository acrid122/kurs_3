from bs4 import BeautifulSoup
from html2image import Html2Image
from aiohttp_req import get_body
from PIL import Image
from cairosvg import svg2png
import os.path


hti = Html2Image()



async def get_image(subject, theme_number, id):
     doujin_page = await get_body(
                    f'https://{subject}-ege.sdamgia.ru/problem?id={id}')
     soup = BeautifulSoup(doujin_page, 'html.parser')

     k = soup.find('div', {'class': 'prob_maindiv'})
     if k is None:
          return None

     d = ['https://inf-ege.sdamgia.ru' + i['src'] if not 'sdamgia.ru' in i['src'] else i['src'] for i in k.find_all('div', {'class': 'pbody'})[0].find_all('img')]
     return d


#Функция сложения картинок
async def join_pics(k, text, subject, theme_number, id):
     image = Image.open(text)
     width, height = image.size
     k = [Image.open(images) for images in k]
     back_im = image.copy()
     for c in k:
          width_c, height_c = c.size
          back_im.paste(c, (width//2 - width_c//2, height - height//2))
          back_im.save(f'{subject}_{theme_number}_{id}_zad.png', quality=95)
          back_im = back_im.copy()

     # grid_image.show()


#Функция проверки скачанной картинки или svg
async def check_pic(f, subject, theme_number, id):
     df = await get_image(subject, theme_number, id)
     r = await download_pic(df, subject, theme_number, id)
     if r != ():
          await join_pics(r, f, subject, theme_number, id)


          


#Функция обработки текста заданий (html кода)
async def hanldle_text(subject, theme_number, id, width, height):
    doujin_page = await get_body(
                    f'https://{subject}-ege.sdamgia.ru/problem?id={id}')
    soup = BeautifulSoup(doujin_page, 'html.parser')
    div = soup.select('.pbody')[0]
    try:
         div.select_one('img').decompose()
    except AttributeError:
         pass
    hti.size = (width, height)
    hti.screenshot(html_str=str(soup.select('.pbody')[0]), save_as=f'{subject}_{theme_number}_{id}_zad.png')
    await check_pic(f'{subject}_{theme_number}_{id}_zad.png', subject, theme_number, id)
    return f'{subject}_{theme_number}_{id}_zad.png'


#Функция скачивания картинки
async def download_pic(pics, subject, theme_number, id):
     f, r = [], []
     if len(pics) > 0:
          for k in pics:
               p = await get_body(k)
               d = f'{subject}_{theme_number}_{id}_download_zad.png'
               if not os.path.exists(d):
                    if 'PNG' in p.decode('cp437'):
                         out = open(d, 'wb+')
                         out.write(p)
                         out.close()
                         f.append(d)
                    else:
                         r.append(await hanlde_svg(p.decode('cp437'), subject, theme_number, id))
               else:
                     f.append(d)
          if len(r) > 0:
               return r
          else:
               return f
     else:
          return ()


#Функция обработки svg 
async def hanlde_svg(k, subject,theme_number,id):
     d = f"{subject}_{theme_number}_{id}_svg.png"
     svg2png(bytestring=k, write_to = d)
                    
     return d
