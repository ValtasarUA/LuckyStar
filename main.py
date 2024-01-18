from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, LabeledPrice
from sqlite import *
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from random import choice
from buttons import *
from config import *
from adminka_sql import *
import pyttsx3
from asyncio import sleep
from get_dice_result import get_result_text
from get_dice_basket import get_result_text_basket
from get_dice_darts import get_result_text_darts
from get_dice_bouling import get_result_text_bouling
import emoji
from background import keep_alive
from aiogram.utils.exceptions import Throttled
from datetime import datetime
from decimal import Decimal
import os.path
import os
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import re
# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
blocki = [6124970105]
async def delete_message_by_id(message_id: int, chat_id: int):
  try:
    await bot.delete_message(chat_id=chat_id, message_id=message_id)
  except:
    pass





async def checking():
  hour_to = datetime.now().hour
  minute_to = datetime.now().minute
  if str(hour_to) in ['0', '00']:
    if str(minute_to) in ['0', '1', '2']:
      await edit_towidhart('0.0')
      await edit_todeposit('0.0')
      await edit_reftod_all()

class Rosa(StatesGroup):
  text_rosa = State()

class AddPromo1(StatesGroup):
  promo1 = State()
  suma1 = State()
class AddChannel(StatesGroup):
  channel = State()
  lim = State()
class AddPromo2(StatesGroup):
  promo2 = State()
  suma2 = State()

list_baza = []

bot = Bot(TOKEN_API)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


async def anti_flood(*args, **kwargs):
  message = args[0]
  #await bot.send_message(message.from_user.id, 'Не флудити! 😡')

class DuelGra(StatesGroup):
  suma_stavok = State()
  id_1 = State()

class ZminBal(StatesGroup):
  id_z = State()
  suma_z = State()

class Promo(StatesGroup):
  promocode = State()

class perekaz(StatesGroup):
  id_o = State()
  suma_p = State()

mats2 = ["🧸"]

class InfoUser(StatesGroup):
  id_user = State()


class OrelStorage(StatesGroup):
  suma_stavka = State()
  orel_or = State()


class Odno(StatesGroup):
  stavka_odno = State()


class Widwart(StatesGroup):
  suma_w = State()
  karta_w = State()

async def check_verif(user):
  ver = await get_veref(user)

  if ver[2] != 'False':
    return True
  else:
    return False


ikb52563 = InlineKeyboardMarkup(row_width=1)
ik152563 = InlineKeyboardButton(text="Lucky Star - Казино", url=f"https://t.me/Lucky_Star2_bot")
ikb52563.insert(ik152563)

async def on_startup(_):
  await db_start()
  await db_start2()
  await db_start3()
  await create_tran()
  await db_start5()
  await db_start6()
  await db_start7()
  await db_start8()
  await db_start9()
  #await speak("Бот успешно запущен!")
  print("On")
@dp.message_handler(commands=['test'], state=None)
@dp.throttled(anti_flood, rate=1)
async def test(message: types.Message):
  await message.delete()
  print(message.chat.id)

@dp.message_handler(commands=['start'], state=None)
@dp.throttled(anti_flood, rate=1)
async def start(message: types.Message):
  user = message.from_user.id
  await create_veref(message.from_user.id)
  await create_reftod(message.from_user.id)
  await checking()
  await create_balances(message.from_user.id)
  await create_profile(message.from_user.id, message.from_user.username)
  await create_bonus(message.from_user.id, 0)
  await message.delete()
  referrer_id = str(message.text[7:])
  if referrer_id != "":
    if str(referrer_id) != str(message.from_user.id):
      ref = await add_refer(referrer_id, message.from_user.id)

  verres = await check_verif(user)

  if verres == True:

    if 1==1:


        result = await bot.get_chat_member('@lucky_star_chat',
                                           int(message.from_user.id))
        #print(result.status)
        if result.status in ['member', 'administrator', 'creator', 'restricted']:

          if message.from_user.id in admins:
            keyb = menu_admins
          else:
            keyb = menu_kb

          #print("Klick start")
          #await speak("присоединился новый пользователь!")         

          await bot.send_message(message.from_user.id,
                                 "Вітаємо в Lucky Star!",
                                 reply_markup=keyb)
          await bot.send_message(
              message.from_user.id,
              "Перед грою ознайомтесь з правилами та політикою конфідеційності!",
              reply_markup=ikb)
          await create_profile(message.from_user.id, message.from_user.username)
          await create_balances(message.from_user.id)
          await create_bonus(message.from_user.id, 0)
        if result.status not in ['member', 'administrator', 'creator', 'restricted']:
          await bot.send_message(message.from_user.id, "Вітаємо в Lucky Star", reply_markup=menu_kb)
          await bot.send_message(message.from_user.id,
                                 "Виконайте одну обов'язкову дію!",
                                 reply_markup=ikb48)

    else:
        await bot.send_message(message.from_user.id, "Вітаємо в Lucky Star", reply_markup=menu_kb)
        await bot.send_message(message.from_user.id,
                               "Виконайте одну обов'язкову дію!",
                               reply_markup=ikb48)
    if 1==1:
      referrer_id = str(message.text[7:])
      if referrer_id != "":
        if str(referrer_id) != str(message.from_user.id):
          ref = await add_refer(referrer_id, message.from_user.id)

          if ref != False:
            await create_reftod(referrer_id)
            get_ref = await get_user_ref(int(referrer_id))

            get_ref_to = await get_reftod(referrer_id)
            r2 = get_ref_to[0] + 1

            r = int(get_ref[0]) + 1
            await edit_reftod(referrer_id, r2)
            await edit_refp(referrer_id, r)
            username_ref = await get_username(message.from_user.id)
            try:
              if int(referrer_id) not in blocki:
                balansb = await get_bonus(referrer_id)
                resb = float(balansb[0]) + 3
                await edit_bonus(referrer_id, resb)
              await bot.send_message(referrer_id,f"💌 У вас новий реферал!\nВам нараховано 2 UAH бонусу.\nТакож ви будете отримувати 5 UAH з кожного його поповнення.")

            except:
              pass
  else:
    await bot.send_message(message.from_user.id, "Для користування ботом пройдіть верифікацію!", reply_markup=veref_kb)

@dp.message_handler(content_types=['contact'])
async def veref_phone(message: types.Message):
  phone = message.contact.phone_number
  user = message.contact.user_id
  name = message.contact.first_name
  block_num = ['37', '79', '7 ', '+7', '89', '21', '22']
  user = message.from_user.id
  await create_veref(message.from_user.id)
  await create_reftod(message.from_user.id)
  await checking()
  await create_balances(message.from_user.id)
  await create_profile(message.from_user.id, message.from_user.username)
  await create_bonus(message.from_user.id, 0)
  try:
    await message.delete()
  except:
    pass
  verres = await check_verif(user)
  if str(phone[:2]) not in block_num:
    await edit_veref_name(int(user), name)
    await edit_veref_phone(int(user), str(phone))
    await bot.send_message(message.from_user.id, "✅ Ви успішно пройшли верифікацію!", reply_markup=menu_kb)
    referrer_id = await get_reffer_id(message.from_user.id)
    #print(referrer_id)
    if referrer_id:
      if str(referrer_id[0]) != str(message.from_user.id):
        referrer_id1 = int(str(referrer_id[0]))
        ref = await add_refer(referrer_id1, message.from_user.id)
        #print(ref)
        if ref == False:
          await create_reftod(referrer_id1)
          get_ref = await get_user_ref(int(referrer_id1))

          get_ref_to = await get_reftod(referrer_id1)
          r2 = get_ref_to[0] + 1

          r = int(get_ref[0]) + 1
          await edit_reftod(referrer_id1, r2)
          await edit_refp(referrer_id1, r)
          username_ref = await get_username(message.from_user.id)
          try:
            if int(referrer_id1) not in blocki:
              balansb = await get_bonus(referrer_id1)
              resb = float(balansb[0]) + 2
              await edit_bonus(referrer_id1, resb)
            await bot.send_message(referrer_id1,f"💌 У вас новий реферал!\nВам нараховано 2 UAH бонусу.\nТакож ви будете отримувати 5 UAH з кожного його поповнення.")

          except:
            pass

  else:
    await bot.send_message(message.from_user.id, "❌ верифікація не пройдена!")

@dp.message_handler(state=None)
@dp.throttled(anti_flood, rate=1)
async def menu(message: types.Message):
  #await popov_beta()
  await checking()
  await create_reftod(message.from_user.id)
  await create_jetres()
  await create_veref(message.from_user.id)
  checking1 = await check_verif(message.from_user.id)
  if checking1 == True:

    result = await bot.get_chat_member('@lucky_star_chat',
                                       int(message.from_user.id))
    #print(result.status)
    if result.status in ['member', 'creator', 'administrator', 'restricted']:
      #result = await bot.get_chat_member('@lucky_star_chat',
       #                                  int(message.from_user.id))
      if message.text == "🎮 Ігри":
        await create_jet(message.from_user.id)
        await bot.send_message(message.from_user.id,
                               "Виберіть гру",
                               reply_markup=games_kb)
      elif message.text == "➕ Зарахування":
        try:
          subject = 'Виконано платіж' 
          creds = None
          # The file token.json stores the user's access and refresh tokens, and is
          # created automatically when the authorization flow completes for the first
          # time.
          if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
            # If there are no (valid) credentials available, let the user log in.
          if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
              creds.refresh(Request())
            else:
              flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
              creds = flow.run_local_server(port=0)
              # Save the credentials for the next run
              with open("token.json", "w") as token:
                token.write(creds.to_json())
          service = build("gmail", "v1", credentials=creds)
            # Отримання списку останніх листів
          results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
          messages = results.get('messages', [])

            # Перевірка кожного листа зі списку на відповідну тему
          for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            if subject in [header['value'] for header in msg['payload']['headers'] if header['name'] == 'Subject']:
              payload = msg['payload']
              headers = payload['headers']
              for header in headers:
                if header['name'] == 'Subject':
                  subject = header['value']
                  parts = payload['parts']
                  for part in parts:
                    #if part['mimeType'] == 'text/plain':
                    data = part['body']
                    text = base64.urlsafe_b64decode(data['data']).decode('utf-8')
                    #print(f"Текст повідомлення: {text}")
                    words = text.split()
                    text2 = ' '.join(words[words.index('відправника:')+1:])
                    # Задаємо шаблон для пошуку
                    pattern = r"""<font face="Tahoma,Arial,Helvetica,sans-serif" color="#575757" size="2" style="font-size: 13px; color: #575757;">&nbsp;&nbsp;(.*?)</font>"""

                    # Знаходимо співпадіння за допомогою регулярного виразу
                    matches = re.search(pattern, text2)

        # Отримуємо текст між 'перший текст' і 'другий текст'
        #USER_ID
                    if matches:
                      extracted_text1 = matches.group(1)

                      user_id = int(extracted_text1)





                    text = base64.urlsafe_b64decode(data['data']).decode('utf-8')
                    #print(f"Текст повідомлення: {text}")
                    words = text.split()
                    text2 = ' '.join(words[words.index('зарахування:')+1:])
                    pattern = r"""<font face="Tahoma,Arial,Helvetica,sans-serif" color="#575757" size="2" style="font-size: 13px; color: #575757;">&nbsp;&nbsp;(.*?)&nbsp;грн</font>"""

                    # Знаходимо співпадіння за допомогою регулярного виразу
        #SUMA
        #L_ID
                    matches = re.search(pattern, text2)
                    if matches:
                      extracted_text2 = matches.group(1)
                      suma = int(extracted_text2)

                    #await bot.send_message(6506444286, f"{user_id}\n{suma}Error type")
                    date = msg['id']
                    l_id = date
                    res = await create_popov(int(user_id), int(suma), l_id)
                    if res == True:
                      try:

                        await create_balances(int(user_id))
                        bal = await get_balance2(int(user_id))

                        res = float(bal[0]) + float(suma)
                        await edit_balance2(int(user_id), str(res))
                        bal2 = await get_balance2(int(user_id))
                        name = await get_username(int(user_id))
                        ref_all = await get_ref_all()
                        for ref_to in ref_all:
                          try:
                            if int(ref_to[0]) not in blocki:
                              if str(ref_to[1]) == str(user_id):
                                await create_bonus(ref_to[0], 0)
                                balans = await get_bonus(user_id=ref_to[0])
                                resb = float(balans[0]) + 5
                                await edit_bonus(ref_to[0], resb)
                                if 1 == 1:
                                  await bot.send_message(
                                      ref_to[0],
                                      f"💌 Ваш реферал поповнив собі рахунок на суму: {float(suma)} UAH!\n🎁 Ви отримали 5 UAH!\n"
                                  )


                          except:
                            pass
                        bal2 = await get_balance2(int(user_id))
                        name = await get_username(int(user_id))
                        try:
                          await bot.send_message(pro_popov,
                                               f"Баланс користувача {name[0]} - {float(bal2[0])} UAH.",
                                               reply_markup=menu_admins)
                        except:
                          await bot.send_message(pro_popov,
                                               f"Баланс користувача - {float(bal2[0])} UAH.",
                                               reply_markup=menu_admins)
                        statistic = await get_statis()
                        widharts1 = float(statistic[0][0]) + float(suma)
                        widharts2 = float(statistic[0][2]) + float(suma)
                        await edit_deposit(str(widharts1))
                        await edit_todeposit(str(widharts2))
                        await bot.send_message(int(user_id), f"✴Ваш баланс поповнено на суму: {float(suma)} UAH!\nДякуємо що ви знами!")
                      except Exception as e:
                        pass
          await bot.send_message(pro_popov, "Завершено!")
        except Exception as e:
          print(e)
      elif message.text == "👤 Профіль":
        get_ref = await get_refers(message.from_user.id)
        users_all = await get_users_all()
        i = 0
        for user in users_all:
          i += 1
        balance = await get_balance2(message.from_user.id)
        await create_peremog(message.from_user.id)
        await create_bal2(int(message.from_user.id), '0.0')
        bon = await get_bonus(message.from_user.id)
        peremogs = await get_peremog(message.from_user.id)
        await message.answer(f"""
        👤 Профіль

          ♦ Ім'я: {message.from_user.first_name}
          🎇 Username: {message.from_user.username}
          🆔: {int(message.from_user.id)}

          💳 Баланс: {float(balance[0])} UAH
          🎁 Бонус: {float(bon[0])} UAH
          👣 Реферали: {get_ref[0]}

          ⚔ Перемог в дуелі: {peremogs[0]}
          👥 Користувачів: {i}""",
                             reply_markup=profile_kb2)

      elif message.text == "👣 Реферальна система":
        await bot.send_message(
            message.from_user.id,
            f"🗣 Запрошуй друзів та заробляй.\n🎁 Отримайте за приведену людину 2 UAH, також з кoжного поповнення вашого реферала 5 UAH.\n✨ Ваша реферальна силка 👇\n\nhttps://t.me/Lucky_Star2_bot?start={message.from_user.id}",
            disable_web_page_preview=True)

      elif message.text == "LUCKY 🔮":
        await bot.send_message(message.from_user.id,
                               "LUCKY 🔮\n\nНастав час інтуіції!\nОдна з трьох таблеток приховує в собі виграш \nX3 від ставки.\nВаша задача вгадати яка саме.\nВсе залежить тільки від вас.\nСкільки ставимо?",
                               reply_markup=stavka_kb)
        await OrelStorage.suma_stavka.set()

      elif message.text == "⬅ Назад":
        if message.from_user.id in admins:
          keyb = menu_admins
        elif message.from_user.id in admins2:
          keyb = menu_admins2
        else:
          keyb = menu_kb
        await bot.send_message(message.from_user.id,
                               "Головне меню.",
                               reply_markup=keyb)
      elif message.text == "📚 Інформація":
        await bot.send_message(message.from_user.id,
                               "Інформація",
                               reply_markup=info_kb)
        await bot.send_photo(
            message.from_user.id,
            photo="https://telegra.ph/file/37e677ea2d992f4f5926f.png",
            caption=info,
            reply_markup=ikb)
      elif message.text == "💳 Вивести":
        bal = await get_balance2(message.from_user.id)
        if float(bal[0]) >= 100:
          await bot.send_message(message.from_user.id,
                                 "💳 Введіть суму виплати (мінімум 100 UAH)",
                                 reply_markup=c_kb)
          await Widwart.suma_w.set()

        else:
          await bot.send_message(
              message.from_user.id,
              f"❌ Мінімальна сума для виплати: 100 UAH\nУ вас на балансі {float(bal[0])} UAH",
              reply_markup=profile_kb2)
      elif message.text == "💸 Поповнити":
        await bot.send_message(message.from_user.id,
                               "Виберіть тип поповнення.",
                               reply_markup=popov_kb221)
      elif message.text == "💳 UAH":
        await bot.send_message(message.from_user.id,
                               "Виберіть суму поповнення.",
                               reply_markup=popov_kb)
      elif message.text == "💹 USDT":
        await bot.send_message(message.from_user.id, f"""
  При переказі додайте коментар з вашим ігровим ID!

  ID: {message.from_user.id}""", reply_markup=kb_usdt)




      elif message.text == "Адміністрація":
        if message.from_user.id in admins:
          await bot.send_message(message.from_user.id,
                                 "Вітаю вас в панелі адміністрації!",
                                 reply_markup=admin_panel)
      elif message.text == "Адміністрація 2 LEVEL":
        if message.from_user.id in admins2:
          await bot.send_message(message.from_user.id,
                                 "Вітаю вас в панелі адміністрації другого рівня!",
                                 reply_markup=admin_panel2)
      elif message.text == "➕ Баланс":
        if message.from_user.id in admins:
          await bot.send_message(message.from_user.id,
                                 "Введіть ID користувача",
                                 reply_markup=c_kb)
          await ZminBal.id_z.set()
      elif message.text == "📁 База":
        if message.from_user.id in admins:
          res_all = await get_all()
          k = 0
          for us in res_all:
            if float(us[1]) > float(30):
              user = await get_username(us[0])
              bal = await get_balance2(us[0])
              try: 
                list_baza.append(
                    f"ID: {us[0]}\nUsername: {user[0]}\nБаланс: {float(bal[0])}\n\n"
                )
              except:
                list_baza.append(
                    f"ID: {us[0]}\nUsername: {user}\nБаланс: {float(bal[0])}\n\n"
                )

          try:
            await bot.send_message(message.from_user.id, ''.join(list_baza))
            list_baza.clear()
          except:
            pass
        elif message.from_user.id in admins2:
          res_all = await get_all()
          k = 0
          for us in res_all:
            if float(us[1]) > float(30):
              user = await get_username(us[0])
              bal = await get_balance2(us[0])
              try: 
                list_baza.append(
                    f"ID: {us[0]}\nUsername: {user[0]}\nБаланс: {float(bal[0])}\n\n"
                )
              except:
                list_baza.append(
                    f"ID: {us[0]}\nUsername: {user}\nБаланс: {float(bal[0])}\n\n"
                )

          try:
            await bot.send_message(message.from_user.id, ''.join(list_baza))
            list_baza.clear()
          except:
            pass
      elif message.text == "🗯 Розсилка":
        if message.from_user.id in admins:
          await bot.send_message(message.from_user.id,
                                 "🍁 Введіть текст розсилки !",
                                 reply_markup=c_kb)
          await Rosa.text_rosa.set()
      elif message.text == "❔ Реферальна система":
        await bot.send_message(message.from_user.id, info2)
      elif message.text == "❔ Про ігри":
        await bot.send_message(message.from_user.id, info3)
      elif message.text == "❔ Поповнення/Вивід":
        await bot.send_message(message.from_user.id, info4)


      elif message.text in [
          '200 UAH 💸', '25 UAH 💸', '50 UAH 💸', '100 UAH 💸', '10 UAH 💸', '250 UAH 💸', '500 UAH 💸'
      ]:
        res_popov_suma = ''.join(message.text.split(' ')[:-2])
        #ILLIA
        if res_popov_suma == "200":
          url_popov = "https://prt.mn/SsxSQs3Rqy"
        if res_popov_suma == "10":
          url_popov = "https://prt.mn/fvygP2d3H3"
        if res_popov_suma == "25":
          url_popov = "https://prt.mn/3h8f6U8FD_"
        if res_popov_suma == "50":
          url_popov = "https://prt.mn/jWMGc01ztx"
        if res_popov_suma == "100":
          url_popov = "https://prt.mn/Cwe5NyYkVS"
        if res_popov_suma == "250":
          url_popov = "https://prt.mn/-nMDyaopCM"
        if res_popov_suma == "500":
          url_popov = "https://prt.mn/d4E3FaHgTi"
        po5 = InlineKeyboardMarkup(row_width=1)
        pok5 = InlineKeyboardButton(text="Поповнення Luky Star.", url=url_popov)
        po5.insert(pok5)
        await bot.send_message(
            message.from_user.id,
            f"Інструкція поповнення. \n1. Натисніть кнопку 'Поповнення Lucky Star'. \n2. Введіть суму платежу. \n3. Введіть в поле 'коментар' на Portmone ваш ID БЕЗ СИМВОЛІВ ТА ПРОБІЛІВ! \nБаланс оновиться через 1-60 хвилин після поповнення.\n ID: {message.from_user.id}",
            reply_markup=po5)

  # BONUS
      elif message.text == "🎁 Роздати Бонус":
        if message.from_user.id in admins:
          await bot.send_message(message.from_user.id,
                                 "Виберіть суму бонусу.",
                                 reply_markup=bonus_kb)
      elif message.text in ['5 UAH 🎁', '10 UAH 🎁', '25 UAH 🎁', '50 UAH 🎁']:
        if message.from_user.id in admins:
          bonus_suma = ''.join(message.text.split(' ')[:-2])
          users_all = await get_users_all()
          for user in users_all:


            try:
              await create_bonus(user[0], 0)
              res = float(bonus_suma)
              ress = await get_bonus(user[0])
              if float(ress[0]) == 0.0:
                await edit_bonus(user[0], res)
                await bot.send_message(
                  user[0],
                  f"🎁 Вам нараховано бонус!\n  {float(bonus_suma)} - UAH!\nДякуємо що ви знами!"
                )
            except:
              pass
          if message.from_user.id in admins:
            await bot.send_message(message.from_user.id, "Бонус роздано!")



      elif message.text == '💬 Чат':
        await message.delete()
        await bot.send_message(
            message.from_user.id,
            "Приєднуйтесь до нашого чату гравців Lucky Star щоб бути в курсі усіх подій.",
            reply_markup=ichat)

      elif message.text == 'Дартс 🎯':
        await bot.send_message(message.from_user.id,
                               "Гарний вибір!\nСкільки ставимо?",
                               reply_markup=stavka_kb5)
      elif message.text == "Однорукий бандит 🎰":
        await bot.send_message(message.from_user.id,
                               "Гарний вибір!\nСкільки ставимо?",
                               reply_markup=stavka_kb2)
      elif message.text == 'Боулінг 🎳':
        await bot.send_message(message.from_user.id,
                               "Гарний вибір!\nСкільки ставимо?",
                               reply_markup=stavka_kb6)

      elif message.text in [
          '0 UAH 💰', '1 UAH 💰', '5 UAH 💰', '10 UAH 💰', '25 UAH 💰', '50 UAH 💰',
          '100 UAH 💰', '200 UAH 💰'
      ]:

        odno_stavka = ''.join(message.text.split(' ')[:-2])

        bal = await get_balance2(message.from_user.id)
        bon = await get_bonus(message.from_user.id)
        if float(odno_stavka) <= float(bal[0]):

          result_dice = await message.answer_dice(emoji='🎰')
          await sleep(3)
          text = await get_result_text(result_dice=result_dice.dice.value,
                                       bid=float(odno_stavka),
                                       user_id=int(message.from_user.id))
          await bot.send_message(message.from_user.id, text)
        else:
            if float(odno_stavka) <= float(bon[0]):
              result_dice = await message.answer_dice(emoji='🎰')
              await sleep(3)
              text = await get_result_text(result_dice=result_dice.dice.value,
                                           bid=float(odno_stavka),
                                           user_id=int(message.from_user.id))
              await bot.send_message(message.from_user.id, text)
            else:
              bon2 = await get_bonus(message.from_user.id)
              await bot.send_message(
                    message.from_user.id,
                    f"❌ Недостатньо коштів на балансі.\n💳 Баланс: {float(bal[0])} UAH\n🎁 Бонус: {float(bon2[0])} UAH")
      elif message.text == "Баскетбол 🏀":
        await bot.send_message(message.from_user.id,
                               "🏀 Гарний вибір!\nСкільки ставимо?",
                               reply_markup=stavka_kb3)
      #BASKETBOL
      elif message.text in [
          '0 UAH 🏀', '1 UAH 🏀', '5 UAH 🏀', '10 UAH 🏀', '25 UAH 🏀', '50 UAH 🏀'
      ]:

        basket_stavka = ''.join(message.text.split(' ')[:-2])
        #print(f"{message.from_user.id} Баскет - ставка: {basket_stavka} UAH")
        bal = await get_balance2(message.from_user.id)
        bon = await get_bonus(message.from_user.id)
        if float(basket_stavka) <= float(bal[0]):

          result_dice_basket = await message.answer_dice(emoji='🏀')
          #await message.delete()

          await sleep(6)
          text = await get_result_text_basket(
              result_dice_basket=result_dice_basket.dice.value,
              bid=basket_stavka,
              user_id=int(message.from_user.id))
          await bot.send_message(message.from_user.id, text)
        else:
          if float(basket_stavka) <= float(bon[0]):
            result_dice_basket = await message.answer_dice(emoji='🏀')
            #await message.delete()

            await sleep(6)
            text = await get_result_text_basket(
                result_dice_basket=result_dice_basket.dice.value,
                bid=basket_stavka,
                user_id=int(message.from_user.id))
            await bot.send_message(message.from_user.id, text)

          else:
            bon2 = await get_bonus(message.from_user.id)
            await bot.send_message(
              message.from_user.id,
              f"❌ Недостатньо коштів на балансі.\n💳 Баланс: {float(bal[0])} UAH\n🎁 Бонус: {float(bon2[0])} UAH")
      #DARTS 🎯
      elif message.text in [
          '0 UAH 🎯', '1 UAH 🎯', '5 UAH 🎯', '10 UAH 🎯', '25 UAH 🎯', '50 UAH 🎯'
      ]:
        darts_stavka = ''.join(message.text.split(' ')[:-2])
        #print(f"{message.from_user.id} Дартс - ставка: {darts_stavka} UAH")
        bal = await get_balance2(message.from_user.id)
        bon = await get_bonus(message.from_user.id)
        if float(darts_stavka) <= float(bal[0]):

          result_dice_darts = await message.answer_dice(emoji='🎯')
          #await message.delete()

          await sleep(4)
          text = await get_result_text_darts(
              result_dice_darts=result_dice_darts.dice.value,
              bid=darts_stavka,
              user_id=int(message.from_user.id))
          await bot.send_message(message.from_user.id, text)
        else:
          if float(darts_stavka) <= float(bon[0]):
            result_dice_darts = await message.answer_dice(emoji='🎯')
            #await message.delete()

            await sleep(4)
            text = await get_result_text_darts(
                result_dice_darts=result_dice_darts.dice.value,
                bid=darts_stavka,
                user_id=int(message.from_user.id))
            await bot.send_message(message.from_user.id, text)

          else:
            bon2 = await get_bonus(message.from_user.id)
            await bot.send_message(
              message.from_user.id,
              f"❌ Недостатньо коштів на балансі.\n💳 Баланс: {float(bal[0])} UAH\n🎁 Бонус: {float(bon2[0])} UAH")
      #BOULING
      elif message.text in [
          '0 UAH 🎳', '1 UAH 🎳', '5 UAH 🎳', '10 UAH 🎳', '25 UAH 🎳', '50 UAH 🎳'
      ]:
        darts_stavka = ''.join(message.text.split(' ')[:-2])
        #print(f"{message.from_user.id} Боулінг - ставка: {odno_stavka} UAH")
        bal = await get_balance2(message.from_user.id)
        bon = await get_bonus(message.from_user.id)
        if float(darts_stavka) <= float(bal[0]):

          result_dice_bouling = await message.answer_dice(emoji='🎳')
          #await message.delete()

          await sleep(4)
          text = await get_result_text_bouling(
              result_dice_bouling=result_dice_bouling.dice.value,
              bid=darts_stavka,
              user_id=int(message.from_user.id))
          await bot.send_message(message.from_user.id, text)
        else:
          if float(darts_stavka) <= float(bon[0]):
            result_dice_bouling = await message.answer_dice(emoji='🎳')
            #await message.delete()

            await sleep(4)
            text = await get_result_text_bouling(
                result_dice_bouling=result_dice_bouling.dice.value,
                bid=darts_stavka,
                user_id=int(message.from_user.id))
            await bot.send_message(message.from_user.id, text)
          else:
            bon2 = await get_bonus(message.from_user.id)
            await bot.send_message(
              message.from_user.id,
              f"❌ Недостатньо коштів на балансі.\n💳 Баланс: {float(bal[0])} UAH\n🎁 Бонус: {float(bon2[0])} UAH")


      elif message.text == "♦ Інфоюзер":
        if message.from_user.id in admins:
          await bot.send_message(message.from_user.id,
                                 "Введіть ID користувача",
                                 reply_markup=c_kb)
          await InfoUser.id_user.set()
        elif message.from_user.id in admins:
          await bot.send_message(message.from_user.id,
                                 "Введіть ID користувача",
                                 reply_markup=c_kb)
          await InfoUser.id_user.set()
      elif message.text == "📤 Переказ Lucky":
        await bot.send_message(message.from_user.id, '🏦 Переказ між рахунками Lucky Star\nВведіть ID отримувача.', reply_markup=c_kb)
        await perekaz.id_o.set()
      elif message.text == "Дуель 🎲":
        await bot.send_message(message.from_user.id, """
  Дуель 🎲

  Гра 1 VS 1.

  Переможець заберає:
  80% від обох ставок!""", reply_markup=duel1kb)

      elif message.text == '➕ Створити гру':
        await create_mess(message.from_user.id, 0)
        await create_peremog(message.from_user.id)
        await bot.send_message(message.from_user.id, "Оберіть ставку.", reply_markup=stavka_kbduel)
        await DuelGra.suma_stavok.set()
      elif message.text == '⭕ Приєднатися':
        await create_peremog(message.from_user.id)
        await create_gra(0, int(message.from_user.id))
        duels = []

        res1 = await get_all_duel()
        try:
          if res1 != False:
            kd = 0
            for gra in res1:
              if res1[0][3] == 0:
                if int(res1[0][0]) != int(message.from_user.id):
                  kd += 1
                  duels.append(gra)
            res = choice(res1)
            username1 = await get_username(res[0])
            await edit_duel_on(int(res[0]), int(message.from_user.id))
            per = await get_peremog(int(res[0]))
            try:
              await bot.send_message(message.from_user.id ,f"""
    👤 Гравець: {username1[0]}
    ⚔ Перемог: {per[0]}
    💰 Ставка: {float(res[2])} UAH
      """, reply_markup=duel1kb2)
            except:
              await bot.send_message(message.from_user.id ,f"""
              👤 Гравець ID: {res[0]}
              ⚔ Перемог: {per[0]}
              💰 Ставка: {float(res[2])} UAH
                """, reply_markup=duel1kb2)

          else:
            await bot.send_message(message.from_user.id, "🚫 Немає відкритих ігор...")
        except:
          await bot.send_message(message.from_user.id, "🚫 Немає відкритих ігор...")


      elif message.text == '♻ Рулетка':
        await create_peremog(message.from_user.id)
        await create_gra(0, int(message.from_user.id))
        duels = []

        res1 = await get_all_duel()
        kd = 0
        for gra in res1:
          if res1[0][3] == 0:
            kd += 1
            duels.append(gra)
        res = choice(res1)
        username1 = await get_username(res[0])
        await edit_duel_on(int(res[0]), int(message.from_user.id))
        per = await get_peremog(int(res[0]))
        await bot.send_message(message.from_user.id ,f"""
  👤 Гравець: {username1[0]}
  ⚔ Перемог: {per[0]}
  💰 Ставка: {float(res[2])} UAH
  """, reply_markup=duel1kb2)
      elif message.text == '🎲 Грати':
        user1 = await get_duel_on(message.from_user.id)
        res = await get_duel(int(user1[0]))
        bal = await get_balance2(message.from_user.id)
        if float(res[2]) <= float(bal[0]):
          await edit_duel_id2(int(res[0]), int(message.from_user.id))
          await edit_duel_user2(message.from_user.username, int(res[0]))
          res2 = await get_duel(int(user1[0]))
          await bot.send_message(message.from_user.id, "🎈 Ви долучились до гри!", reply_markup=back_kb)
          try:
            re_id = await get_mess(int(user1[0]))
            await delete_message_by_id(int(re_id[0]), -1001973940032)
            await bot.send_message(user1[0], f"🎈 Користувач {res2[4]} долучився!")
            await sleep(1.5)
            result_dice = await bot.send_dice(message.from_user.id, emoji='🎲')
            result_dice2 = await bot.send_dice(user1[0], emoji='🎲')
            await sleep(3)
            r1 = result_dice.dice.value #mess
            r2 = result_dice2.dice.value #too
            if r1 < r2:
              await bot.send_message(res2[0], f"Ваш результат: {result_dice2.dice.value}\nРезультат гравця {message.from_user.username}: {r1}\n🔥 Ви виграли: {float(res[2])-float(res[2])*0.2} UAH", reply_markup=duel1kb)

              resper = await get_peremog(res[0])

              await edit_peremog(res2[0], int(resper[0])+1)
              await bot.send_message(message.from_user.id, f"Ваш результат: {result_dice.dice.value}\nРезультат гравця {res[1]}: {result_dice2.dice.value}\n😞 Ви програли: {res[2]} UAH", reply_markup=duel1kb)
              re_id = await bot.send_message(-1001973940032, f"{message.from_user.username} VS {res[1]}\n🔥 Переможець: {res[1]}")

              bal1 = await get_balance2(res2[0])
              bal2 = await get_balance2(message.from_user.id)
              resbal1 = float(bal1[0]) + float(res[2])-float(res[2])*0.2
              resbal2 = float(bal2[0]) - float(res[2])
              await edit_balance2(res2[0], str(float(resbal1)))
              await edit_balance2(message.from_user.id, str(float(resbal2)))
              try:
                await dell_duel(res2[0])
              except:
                pass
            elif r1 > r2:
              await bot.send_message(res2[0], f"Ваш результат: {result_dice2.dice.value}\nРезультат гравця {message.from_user.username}: {r1}\n😞 Ви програли: {float(res[2])} UAH", reply_markup=duel1kb)
              await bot.send_message(message.from_user.id, f"Ваш результат: {result_dice.dice.value}\nРезультат гравця {res[1]}: {result_dice2.dice.value}\n 🔥 Ви виграли: {float(res[2])-float(res[2])*0.2} UAH", reply_markup=duel1kb)
              re_id = await bot.send_message(-1001973940032, f"{message.from_user.username} VS {res[1]}\n🔥 Переможець: {message.from_user.username}")

              resper = await get_peremog(message.from_user.id)

              await edit_peremog(message.from_user.id, int(resper[0])+1)
              bal1 = await get_balance2(res2[0])
              bal2 = await get_balance2(message.from_user.id)
              resbal1 = float(bal1[0]) - float(res[2])
              resbal2 = float(bal2[0]) + float(res[2])-float(res[2])*0.2
              await edit_balance2(res2[0], str(float(resbal1)))
              await edit_balance2(message.from_user.id, str(float(resbal2)))
              try:
                await dell_duel(res2[0])
              except:
                pass
            else:
              await bot.send_message(res2[0], f"Ваш результат: {result_dice2.dice.value}\nРезультат гравця {message.from_user.username}: {result_dice.dice.value}\n✨ Нічія!\nПеремогла дружба.", reply_markup=duel1kb)
              await bot.send_message(message.from_user.id, f"Ваш результат: {result_dice.dice.value}\nРезультат гравця {res[1]}: {result_dice2.dice.value}\n✨ Нічія!\nПеремогла дружба.", reply_markup=duel1kb)
              re_id = await bot.send_message(-1001973940032, f"{message.from_user.username} VS {res[1]}\n✨ Нічія!\nПеремогла дружба.")

              try:
                await dell_duel(res2[0])
              except:
                pass
          except:
            await dell_duel(res2[0])
            await bot.send_message(message.from_user.id, "Гри не існує!", reply_markup=duel1kb)
        else:
          await bot.send_message(
              message.from_user.id,
              f"❌ Недостатньо коштів на балансі.\n💳 Баланс: {float(bal[0])} UAH", reply_markup=duel1kb)

      elif message.text== '❌ Вийти':
        try:
          await dell_duel(message.from_user.id)
        except:
          pass
        try:
          re_id = await get_mess(message.from_user.id)
          await delete_message_by_id(int(re_id[0]), -1001973940032)
          await bot.send_message(message.from_user.id, '✖ Гру видалено!', reply_markup=duel1kb)
        except:
          pass
      elif message.text== "🎁 Промо":
        await bot.send_message(message.from_user.id, "💢 Введіть промокод!", reply_markup=c_kb)
        await Promo.promocode.set()
      elif message.text== "➕🎁 PROMOCODES":
        if message.from_user.id in admins:
          await bot.send_message(message.from_user.id, "💢 Виберіть тип.", reply_markup=pmtypes_kb)
        elif message.from_user.id in admins2:
          await bot.send_message(message.from_user.id, "💢 Виберіть тип.", reply_markup=pmtypes_kb)

      elif message.text== "Одноразовий":
        if message.from_user.id in admins:
          await bot.send_message(message.from_user.id, "💢 Введіть новий промокод.", reply_markup=c_kb)
          await AddPromo1.promo1.set()
        elif message.from_user.id in admins2:
          await bot.send_message(message.from_user.id, "💢 Введіть новий промокод.", reply_markup=c_kb)
          await AddPromo1.promo1.set()
      elif message.text== "Вічний":
        if message.from_user.id in admins:
          await bot.send_message(message.from_user.id, "💢 Введіть новий промокод.", reply_markup=c_kb)
          await AddPromo2.promo2.set()
        elif message.from_user.id in admins2:
          await bot.send_message(message.from_user.id, "💢 Введіть новий промокод.", reply_markup=c_kb)
          await AddPromo2.promo2.set()
      elif message.text == "📊 Статистика":
        if message.from_user.id in admins:
          user = message.from_user.id
          await create_statis('0.0', '0.0', '0.0', '0.0')
          statistic = await get_statis()
          await bot.send_message(user, f"""
  📊 Статистика

  ВЕСЬ ЧАС
    Виведено: {statistic[0][1]}
    Поповнено: {statistic[0][0]}

  СЬОГОДНІ
    Виведено: {statistic[0][3]}
    Поповнено: {statistic[0][2]}
  """)
        elif message.from_user.id in admins2:
          user = message.from_user.id
          await create_statis('0.0', '0.0', '0.0', '0.0')
          statistic = await get_statis()
          await bot.send_message(user, f"""
  📊 Статистика

  ВЕСЬ ЧАС
    Виведено: {statistic[0][1]}
    Поповнено: {statistic[0][0]}

  СЬОГОДНІ
    Виведено: {statistic[0][3]}
    Поповнено: {statistic[0][2]}
  """)

      elif message.text == '🔥 Топ':
        await bot.send_message(message.from_user.id, '🔥 Топ', reply_markup=top_kb)
      elif message.text == '🔥 Дуель':
        res = await get_top()

        if len(res) ==5 :
          try:
            user1 = await get_username(res[0][0])
            user1 = user1[0]
          except:
            user1 = 'None'
          try:
            user2 = await get_username(res[1][0])
            user2 = user2[0]
          except:
            user2 = "None"
          try:
            user3 = await get_username(res[2][0])
            user3 = user3[0]
          except:
            user3 = 'None'
          try:
            user4 = await get_username(res[3][0])
            user4 = user4[0]
          except:
            user4 = "None"
          try:
            user5 = await get_username(res[4][0])
            user5 = user5[0]
          except:
            user5 = "None"
          await bot.send_message(message.from_user.id, f"""
  🌠 Топ найкращих гравців в Дуель.

  1. {user1} 🥇  ⚔: {res[0][1]}
  2. {user2} 🥈  ⚔: {res[1][1]}
  3. {user3} 🥉  ⚔: {res[2][1]}
  4. {user4}      ⚔: {res[3][1]}
  5. {user5}      ⚔: {res[4][1]}
  """)
        elif len(res) == 4:
          try:
            user1 = await get_username(res[0][0])
            user1 = user1[0]
          except:
            user1 = 'None'
          try:
            user2 = await get_username(res[1][0])
            user2 = user2[0]
          except:
            user2 = "None"
          try:
            user3 = await get_username(res[2][0])
            user3 = user3[0]
          except:
            user3 = 'None'
          try:
            user4 = await get_username(res[3][0])
            user4 = user4[0]
          except:
            user4 = "None"

          await bot.send_message(message.from_user.id, f"""
  🌠 Топ найкращих гравців в Дуель.

  1. {user1} 🥇  ⚔: {res[0][1]}
  2. {user2} 🥈  ⚔: {res[1][1]}
  3. {user3} 🥉  ⚔: {res[2][1]}
  4. {user4}      ⚔: {res[3][1]}

  """)
        elif len(res) == 3:
          try:
            user1 = await get_username(res[0][0])
            user1 = user1[0]
          except:
            user1 = 'None'
          try:
            user2 = await get_username(res[1][0])
            user2 = user2[0]
          except:
            user2 = "None"
          try:
            user3 = await get_username(res[2][0])
            user3 = user3[0]
          except:
            user3 = 'None'

          await bot.send_message(message.from_user.id, f"""
  🌠 Топ найкращих гравців в Дуель.

  1. {user1} 🥇  ⚔: {res[0][1]}
  2. {user2} 🥈  ⚔: {res[1][1]}
  3. {user3} 🥉  ⚔: {res[2][1]}

  """)

        elif len(res) == 2:
          try:
            user1 = await get_username(res[0][0])
            user1 = user1[0]
          except:
            user1 = 'None'
          try:
            user2 = await get_username(res[1][0])
            user2 = user2[0]
          except:
            user2 = "None"

          await bot.send_message(message.from_user.id, f"""
  🌠 Топ найкращих гравців в Дуель.

  1. {user1} 🥇  ⚔: {res[0][1]}
  2. {user2} 🥈  ⚔: {res[1][1]}
  """)
        elif len(res) == 1:
          try:
            user1 = await get_username(res[0][0])
            user1 = user1[0]
          except:
            user1 = 'None'

          await bot.send_message(message.from_user.id, f"""
  🌠 Топ найкращих гравців в Дуель.

  1. {user1} 🥇  ⚔: {res[0][1]}


  """)



      elif message.text == '🔥 Партнер':
        await message.delete()
        await bot.send_message(message.from_user.id, '🔥 Партнер', reply_markup=top_kb2)
      elif message.text == '🌌 Сьогодні':
        res = await get_top_ref()

        if len(res) ==5 :
          try:
            user1 = await get_username(res[0][0])
            user1 = user1[0]
          except:
            user1 = 'None'
          try:
            user2 = await get_username(res[1][0])
            user2 = user2[0]
          except:
            user2 = "None"
          try:
            user3 = await get_username(res[2][0])
            user3 = user3[0]
          except:
            user3 = 'None'
          try:
            user4 = await get_username(res[3][0])
            user4 = user4[0]
          except:
            user4 = "None"
          try:
            user5 = await get_username(res[4][0])
            user5 = user5[0]
          except:
            user5 = "None"
          await bot.send_message(message.from_user.id, f"""
  👤 Топ найкращих партерів.

  1. {user1} 🥇  👥: {res[0][1]}
  2. {user2} 🥈  👥: {res[1][1]}
  3. {user3} 🥉  👥: {res[2][1]}
  4. {user4}      👥: {res[3][1]}
  5. {user5}      👥: {res[4][1]}
  """)
        elif len(res) == 4:
          try:
            user1 = await get_username(res[0][0])
            user1 = user1[0]
          except:
            user1 = 'None'
          try:
            user2 = await get_username(res[1][0])
            user2 = user2[0]
          except:
            user2 = "None"
          try:
            user3 = await get_username(res[2][0])
            user3 = user3[0]
          except:
            user3 = 'None'
          try:
            user4 = await get_username(res[3][0])
            user4 = user4[0]
          except:
            user4 = "None"

          await bot.send_message(message.from_user.id, f"""
  👤 Топ найкращих партерів.

  1. {user1} 🥇  👥: {res[0][1]}
  2. {user2} 🥈  👥: {res[1][1]}
  3. {user3} 🥉  👥: {res[2][1]}
  4. {user4}      👥: {res[3][1]}
  """)
        elif len(res) == 3:
          try:
            user1 = await get_username(res[0][0])
            user1 = user1[0]
          except:
            user1 = 'None'
          try:
            user2 = await get_username(res[1][0])
            user2 = user2[0]
          except:
            user2 = "None"
          try:
            user3 = await get_username(res[2][0])
            user3 = user3[0]
          except:
            user3 = 'None'

          await bot.send_message(message.from_user.id, f"""
  👤 Топ найкращих партерів.

  1. {user1} 🥇  👥: {res[0][1]}
  2. {user2} 🥈  👥: {res[1][1]}
  3. {user3} 🥉  👥: {res[2][1]}

  """)

        elif len(res) == 2:
          try:
            user1 = await get_username(res[0][0])
            user1 = user1[0]
          except:
            user1 = 'None'
          try:
            user2 = await get_username(res[1][0])
            user2 = user2[0]
          except:
            user2 = "None"

          await bot.send_message(message.from_user.id, f"""
  👤 Топ найкращих партерів.

  1. {user1} 🥇  👥: {res[0][1]}
  2. {user2} 🥈  👥: {res[1][1]}
  """)
        elif len(res) == 1:
          try:
            user1 = await get_username(res[0][0])
            user1 = user1[0]
          except:
            user1 = 'None'

          await bot.send_message(message.from_user.id, f"""
  👤 Топ найкращих партерів.

  1. {user1} 🥇  👥: {res[0][1]}


  """)
      elif message.text == '🌠 Весь час':
        res = await get_top_ref2()

        if len(res) ==5 :
          try:
            user1 = await get_username(res[0][0])
            user1 = user1[0]
          except:
            user1 = 'None'
          try:
            user2 = await get_username(res[1][0])
            user2 = user2[0]
          except:
            user2 = "None"
          try:
            user3 = await get_username(res[2][0])
            user3 = user3[0]
          except:
            user3 = 'None'
          try:
            user4 = await get_username(res[3][0])
            user4 = user4[0]
          except:
            user4 = "None"
          try:
            user5 = await get_username(res[4][0])
            user5 = user5[0]
          except:
            user5 = "None"
          await bot.send_message(message.from_user.id, f"""
  👤 Топ найкращих партерів.

  1. {user1} 🥇  👥: {res[0][3]}
  2. {user2} 🥈  👥: {res[1][3]}
  3. {user3} 🥉  👥: {res[2][3]}
  4. {user4}      👥: {res[3][3]}
  5. {user5}      👥: {res[4][3]}
  """)
        elif len(res) == 4:
          try:
            user1 = await get_username(res[0][0])
            user1 = user1[0]
          except:
            user1 = 'None'
          try:
            user2 = await get_username(res[1][0])
            user2 = user2[0]
          except:
            user2 = "None"
          try:
            user3 = await get_username(res[2][0])
            user3 = user3[0]
          except:
            user3 = 'None'
          try:
            user4 = await get_username(res[3][0])
            user4 = user4[0]
          except:
            user4 = "None"

          await bot.send_message(message.from_user.id, f"""
  👤 Топ найкращих партерів.

  1. {user1} 🥇  👥: {res[0][3]}
  2. {user2} 🥈  👥: {res[1][3]}
  3. {user3} 🥉  👥: {res[2][3]}
  4. {user4}      👥: {res[3][3]}
  """)
        elif len(res) == 3:
          try:
            user1 = await get_username(res[0][0])
            user1 = user1[0]
          except:
            user1 = 'None'
          try:
            user2 = await get_username(res[1][0])
            user2 = user2[0]
          except:
            user2 = "None"
          try:
            user3 = await get_username(res[2][0])
            user3 = user3[0]
          except:
            user3 = 'None'

          await bot.send_message(message.from_user.id, f"""
  👤 Топ найкращих партерів.

  1. {user1} 🥇  👥: {res[0][3]}
  2. {user2} 🥈  👥: {res[1][3]}
  3. {user3} 🥉  👥: {res[2][3]}

  """)

        elif len(res) == 2:
          try:
            user1 = await get_username(res[0][0])
            user1 = user1[0]
          except:
            user1 = 'None'
          try:
            user2 = await get_username(res[1][0])
            user2 = user2[0]
          except:
            user2 = "None"

          await bot.send_message(message.from_user.id, f"""
  👤 Топ найкращих партерів.

  1. {user1} 🥇  👥: {res[0][3]}
  2. {user2} 🥈  👥: {res[1][3]}
  """)
        elif len(res) == 1:
          try:
            user1 = await get_username(res[0][0])
            user1 = user1[0]
          except:
            user1 = 'None'

          await bot.send_message(message.from_user.id, f"""
  👤 Топ найкращих партерів.

  1. {user1} 🥇  👥: {res[0][3]}


  """)
      elif message.text == "◀ Назад":
        await message.delete()
        await bot.send_message(message.from_user.id, "🔥 Топ", reply_markup=top_kb)
      elif message.text == "JET X 🚀":
        await bot.send_message(message.from_user.id, "Оберіть ставку", reply_markup=stavkajet_kb2)
      elif message.text in [
          '0 UAH 🚀', '1 UAH 🚀', '5 UAH 🚀', '10 UAH 🚀', '25 UAH 🚀', '50 UAH 🚀'
      ]:
        jet_stavka = ''.join(message.text.split(' ')[:-2])
        bal = await get_balance2(message.from_user.id)
        bon = await get_bonus(message.from_user.id)
        if Decimal(str(jet_stavka)) <= Decimal(str(bal[0])):
          await bot.send_message(message.from_user.id, "Ставка принята!")
          id_jet = await bot.send_message(message.from_user.id, """
  Jet X




    🚀 X 0.0
  __________________""")
          await sleep(0.5)
          await bot.edit_message_text(chat_id = message.chat.id, message_id = id_jet.message_id, text="""
  Jet X



      🚀 X 0.0

  __________________

  """)
          await bot.edit_message_text(chat_id = message.chat.id, message_id = id_jet.message_id, text="""
  Jet X


          🚀 X 0.0


  __________________

  """)
          await bot.edit_message_text(chat_id = message.chat.id, message_id = id_jet.message_id, text="""
  Jet X

            🚀 X 0.0



  __________________

  """)
          await bot.edit_message_text(chat_id = message.chat.id, message_id = id_jet.message_id, text="""
  Jet X
                🚀 X 0.0




  __________________

  """)    
          await edit_jet(message.from_user.id, 'True')
          x_j = 1.0
          jetres = await get_jetres()
          if int(jet_stavka) != 0:
            if Decimal(str(jetres[0])) <= Decimal('1000.0'):
              cc = choice(res_x50)
            else:
              cc = choice(res_x0)
          else:
            cc = choice(res_xin0)

          print(Decimal(str(cc)))
          jet2m = await bot.send_message(message.from_user.id, "🚀 Успішно взлетіли!", reply_markup=back_kb133)
          while True:
            flag_jet = await get_jet(message.from_user.id)
            if flag_jet[0] == 'False':
              res_v = float(jet_stavka) * float(x_j)
              res_v2 = Decimal(str(res_v)) - Decimal(str(jet_stavka))
              await delete_message_by_id(message_id=id_jet.message_id, chat_id=message.chat.id)
              bal1 = await get_balance2(message.from_user.id)

              res_bal228 = Decimal(str(bal1[0])) + Decimal(str(res_v2))
              await edit_balance2(message.from_user.id, str(res_bal228))
              bal002 = await get_balance2(message.from_user.id)
              await delete_message_by_id(message_id=jet2m.message_id, chat_id=message.chat.id)
              print(message.from_user.id, f"""{message.from_user.id}  JET X  +{Decimal(str(res_v2))} UAH  = {str(res_bal228)}""")
              prograno1 = await get_jetres()
              prograno = Decimal(str(prograno1[0])) - Decimal(str(jet_stavka))
              await edit_jetres(str(prograno))
              await bot.send_message(message.from_user.id, f"""
  Jet X 🚀
    Летів до X{Decimal(str(cc))}     
    ✅

  X {x_j}
  + {res_v2} UAH
  💳 Баланс: {float(bal002[0])}
  __________________""", reply_markup=stavkajet_kb2)
              break

            else:
              x_j = Decimal(str(x_j))
              x_j += Decimal("0.1")
              x000 = ''.join(str(x_j).split('.')[:1])
              x001 = ''.join(str(x_j).split('.')[1:])[:1]
              x_j = f"{x000}.{x001}"

              balala = Decimal(str(jet_stavka)) * Decimal(str(x_j))
              balala2 = Decimal(str(balala)) - Decimal(str(jet_stavka))
              await bot.edit_message_text(chat_id = message.chat.id, message_id = id_jet.message_id, text=f"""
  Jet X
                🚀 X {x_j}
              💳 {Decimal(str(balala2))} UAH



  __________________

  """)      

            await sleep(0.4)
            #res_jet = await get_jet(message.from_user.id)

            if Decimal(str(cc)) == Decimal(str(x_j)) or Decimal(str(cc)) == Decimal('1.0'):
              await edit_jet(message.from_user.id, 'False')
              await delete_message_by_id(message_id=id_jet.message_id, chat_id=message.chat.id)
              await delete_message_by_id(message_id=jet2m.message_id, chat_id=message.chat.id)
              bal1 = await get_balance2(message.from_user.id)
              res_bal228 = Decimal(str(bal1[0])) - Decimal(str(jet_stavka))
              await edit_balance2(message.from_user.id, str(res_bal228))
              print(message.from_user.id, f"""{message.from_user.id}  JET X  -{Decimal(str(jet_stavka))} UAH  = {str(res_bal228)}""")
              prograno1 = await get_jetres()
              prograno = Decimal(str(prograno1[0])) + Decimal(str(jet_stavka))
              await edit_jetres(str(prograno))
              bal002 = await get_balance2(message.from_user.id)
              text_jet = f"""
    Jet X 🚀

    💥

    X {x_j}
    - {Decimal(str(jet_stavka))} UAH
    💳 Баланс: {Decimal(str(bal002[0]))}
    __________________"""

              await bot.send_message(chat_id = message.chat.id, text=text_jet, reply_markup=stavkajet_kb2)

              break


        else:
          bon2 = await get_bonus(message.from_user.id)
          await bot.send_message(
                    message.from_user.id,
                    f"❌ Недостатньо коштів на балансі.\n💳 Баланс: {float(bal[0])} UAH")





      elif message.text == '.startrossa':
        user_all = await get_users_all()
        us_all = []
        d_user = 0
        k_user = 0
        for q in user_all:
          try:
            await bot.forward_message(chat_id=q[0], from_chat_id=6506444286, message_id=311751)


            k_user += 1
          except:
            await edit_balance2(q[0], 3)
            d_user += 1

        await bot.send_message(
            message.from_user.id,
            f"{k_user} користувачів отримали ваше повідомлення!\n{d_user} Не отримали.",
            reply_markup=menu_admins)
      elif message.text == "❔ Перевірені":
        await bot.send_message(message.from_user.id, """
  Перевірені - це статус у перевірених власником людей, 
  які дають можливість підзаробити на верифікаціях тощо. 

  Таких людей може бути до 10 в залежності 
  від кількості учасників групи.""", reply_markup=ikbper)

      elif message.text == "💰 Забрати":
        await edit_jet(message.from_user.id, 'False')
      elif message.text == "568568":
        await dell_promocode2()
      elif message.text == "➕ Завдання":
        await bot.send_message(message.from_user.id, """
💎 Тут ви можете додати свій канал/чат на просування
Перед додаванням переконайтесь що бот Lucky Star являється адміністратором вашого каналу/чату.
Ціна за одну підписку складає 1.0 UAH

Відправте ваш канал/чат у такому форматі:
@You_Channel_or_Group""", reply_markup=c_kb)
        await AddChannel.channel.set()
      elif message.text == "💎 Заробити":
        check_ot = await get_jobs_all(message.from_user.id)
        #print(check_ot)
        for q in check_ot:
          result = await bot.get_chat_member(q[1], int(q[0]))
          if result.status not in ['member', 'creator', 'administrator']:
            bal1 = await get_balance2(q[0])
            resbal1 = Decimal(str(bal1[0])) - Decimal('0.50')
            await edit_balance2(q[0], str(resbal1))
            await delete_jobs(q[0], q[1])
            await bot.send_message(q[0], "‼ Вас оштрафовано за відписку.")
            user2 = await get_us_ad(q[1])
            bal2 = await get_balance2(int(user2[0]))
            resbal2 = Decimal(str(bal2[0])) + Decimal('1.0')
            await edit_balance2(user2[0], str(resbal2))
            await bot.send_message(user2[0], '💦 Ви втратили одного підписника.\nВам повернуто 1.0 UAH.')


        res = await get_work_all()
        repp = []
        for ch in res:
          res2 = await get_jobs(message.from_user.id, ch[1])
          if res2 == False:
            repp.append(ch)
            work_kb = InlineKeyboardMarkup(row_width=1)
            workkb = InlineKeyboardButton(text="💎 Заробити 0.50 UAH", url=f"https://t.me/{ch[1][1:]}")
            workkb2 = InlineKeyboardButton("💎 Забрати винагороду", callback_data=f'subdone*{ch[1]}*{message.from_user.id}')
            work_kb.insert(workkb)
            work_kb.insert(workkb2)
            await bot.send_message(message.from_user.id, f"🎃 Підпишіться на канал або групу.\nПролистайте в гору та поставте декілька реакцій.", reply_markup=work_kb)


        if repp == []:
          await bot.send_message(message.from_user.id, '🎃 Завдань покищо немає...')
      elif message.text == "🍓 Лоторея":
        res_users0 = await get_lotorea_all()
        await bot.send_message(message.from_user.id, f'''
🍓 Лоторея - тут ви можете виграти 200-600 UAH.
Для участі купіть лоторейний білет, та очікуйте сповіщення про результат.\nКуплено: {len(res_users0)}/100 ❤️''', reply_markup=kb_graloto)
      elif message.text == "💌 Купити - 10 UAH":
        user_id = message.from_user.id
        bal = await get_balance2(user_id)
        if Decimal(bal[0]) >= Decimal(10.0):
          #resbal = Decimal(bal[0]) - Decimal(10.0)
          #await edit_balance2(user_id, str(resbal))
          res_loto = await create_lotorea(int(user_id))
          #if res_loto == True:
          resbal = Decimal(bal[0]) - Decimal(10.0)
          await edit_balance2(user_id, str(resbal))
          res_users0 = await get_lotorea_all()
          await bot.send_message(user_id, f'🎈 Ви купили квиток!\nКуплено: {len(res_users0)}/100\n❤️ Успіхів!')

          res_users = await get_lotorea_all()


          if len(res_users) >= 100:
            wins_list = []
            for q in range(3):
              win = choice(res_users)
              wins_list.append(win[0])

              resbal002 = await get_balance2(win[0])
              resbal200 = Decimal(resbal002[0]) + Decimal(200)
              await edit_balance2(win[0], str(resbal200))
              await bot.send_message(win[0], """🍓 Вітаємо! Ви виграли в лоторею 200 UAH!""")
            for names in wins_list:
              name = await get_username(names)
              await bot.send_message(-1001973940032, f"""
🍓 BIG WIN 🍓

@{name[0]}

Забирає 200 UAH

ЛОТОРЕЯ 🪄""")
              await dell_lotorea()




        else:
          await bot.send_message(
            message.from_user.id,
            f"❌ Недостатньо коштів на балансі.\n💳 Баланс: {Decimal(bal[0])} UAH")

      else:
        print(message.message_id)
        print(message.from_user.id)

   ####################################################################################################################################   

    else:
      await bot.send_message(message.from_user.id, "Вітаємо в Lucky Star", reply_markup=menu_kb)
      await bot.send_message(message.from_user.id, "Виконайте одну обов'язкову дію!", reply_markup=ikb48)
  else:
    try:
      await bot.send_message(message.from_user.id, "Для користування ботом пройдіть верифікацію!", reply_markup=veref_kb)
    except:
      pass
@dp.callback_query_handler()
async def subdone(callback_query: types.CallbackQuery):

  callback_data_parts = callback_query.data.split('*')
  #print(callback_data_parts)
  channel = callback_data_parts[1]
  user = callback_data_parts[2]
  result = await bot.get_chat_member(channel, int(user))
  if result.status in ['member', 'creator', 'administrator']:
    res1 = await get_jobs(user, channel)
    res2 = await get_jobs_bl(user, channel)
    if res1 == False and res2 == False:
      await create_jobs(user, channel)
      await create_jobs_bl(user, channel)
      bal = await get_balance2(user)
      resbal = Decimal(str(bal[0])) + Decimal('0.50')
      await edit_balance2(user, str(resbal))
      lim = await get_lim(channel)

      reslim = int(lim[0]) - 1
      await edit_work(channel, int(reslim))
      lim2 = await get_lim(channel)
      if int(lim2[0]) <= 0:
        us_ad = await get_us_ad(channel)
        await delete_work(channel)
        await bot.send_message(us_ad[0], "⚡ Ваше замовлення успішно виконано!")
      await callback_query.answer('⚡ Ви отримали 0.50 UAH')
    else:
     await callback_query.answer('❌ Ви вже виконували це завдання.') 
  else:
    await callback_query.answer('❌ Ви не підписались або відписались!')


#CANCEL
@dp.message_handler(Text(equals='❌ Скасувати'), state="*")
@dp.throttled(anti_flood, rate=1)
async def new_cancel(message: types.Message, state: FSMContext):
  current_state = await state.get_state()
  if current_state is None:
    return
  await state.finish()
  await message.delete()
  if message.from_user.id in admins:
    keyb = menu_admins
  elif message.from_user.id in admins2:
    keyb = menu_admins2
  else:
    keyb = menu_kb
  await message.answer("Головне меню", reply_markup=keyb)


@dp.message_handler(state=AddChannel.channel)
@dp.throttled(anti_flood, rate=0.8)
async def new_channel(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['channel'] = message.text
  channel = data['channel'][:1]
  try: 
    result = await bot.get_chat_member(data['channel'], int(message.from_user.id))
    if channel == '@':
      bal002 = await get_balance2(message.from_user.id)
      await bot.send_message(message.from_user.id, f"Введіть кількість підписників.\nОдна підписка 1.0 UAH\n💳 Баланс: {Decimal(str(bal002[0]))}", reply_markup=c_kb)
      await AddChannel.next()
    else:
      await state.finish()
      await bot.send_message(message.from_user.id, "❌ Ви допустили помилку!", reply_markup=menu_kb)
  except:
    await state.finish()
    await bot.send_message(message.from_user.id, "❌ Ви не додали бота в адміністратори!\nАбо ви не знаходитесь в каналі/чаті який намагаєтесь рекламувати!", reply_markup=menu_kb)

@dp.message_handler(state=AddChannel.lim)
@dp.throttled(anti_flood, rate=0.8)
async def new_lim(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['lim'] = message.text
    channel = data['channel']
    lim = data['lim']
  bal = await get_balance2(message.from_user.id)
  if Decimal(str(bal[0])) >= Decimal(str(lim)):
    try:
      cres = await create_work(message.from_user.id, channel, int(lim))
      if cres == True:
        resbal = Decimal(str(bal[0])) - Decimal(str(lim))
        await edit_balance2(message.from_user.id, str(resbal))
        await bot.send_message(message.from_user.id, "✅ Ви успішно створили замовлення!", reply_markup=menu_kb)
      else:
        await bot.send_message(message.from_user.id, "❌ Канал/Чат вже на просувані!")
    except:
      await bot.send_message(message.from_user.id, "Ви допустили помилку.")


  else:
    await state.finish()
    bal = await get_balance2(message.from_user.id)
    await bot.send_message(message.from_user.id, f"❌ Недостатньо коштів на балансі.\n💳 Баланс: {float(bal[0])} UAH\nВведіть кількість підписників.", reply_markup=menu_kb)
  await state.finish()



#EXITE GAMEprint()

#odno promo new
@dp.message_handler(state=AddPromo1.promo1)
@dp.throttled(anti_flood, rate=0.8)
async def new_forever_prom1(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['promo1'] = message.text
  await bot.send_message(message.from_user.id, "Введіть суму бонусу", reply_markup=c_kb)
  await AddPromo1.next()

@dp.message_handler(state=AddPromo1)
@dp.throttled(anti_flood, rate=0.8)
async def new_forever_sum1(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    promo11 = data['promo1']
  async with state.proxy() as data:
    data['suma1'] = message.text
    await create_promocode(promo11, 'N', data['suma1'])
    await bot.send_message(message.from_user.id, "Додано!", reply_markup=menu_admins)
  await state.finish()

#forever promo new
@dp.message_handler(state=AddPromo2.promo2)
@dp.throttled(anti_flood, rate=0.8)
async def new_forever_promo(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['promo2'] = message.text
  await bot.send_message(message.from_user.id, "Введіть суму бонусу", reply_markup=c_kb)
  await AddPromo2.next()

@dp.message_handler(state=AddPromo2)
@dp.throttled(anti_flood, rate=0.8)
async def new_forever_suma(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    promo22 = data['promo2']
  async with state.proxy() as data:
    data['suma2'] = message.text
    await create_promocode(promo22, 'F', data['suma2'])
    await bot.send_message(message.from_user.id, "Додано!", reply_markup=menu_admins2)
  await state.finish()

#DUEL States
@dp.message_handler(state=DuelGra.suma_stavok)
@dp.throttled(anti_flood, rate=0.8)
async def duel_stavka(message: types.Message, state: FSMContext):
  if message.text in ['50 UAH 🎲', '25 UAH 🎲', '10 UAH 🎲', '5 UAH 🎲', '1 UAH 🎲', '0 UAH 🎲', '100 UAH 🎲', '200 UAH 🎲']:

    res_stavka87 = ''.join(message.text.split(' ')[:-2])

    async with state.proxy() as data:
      data['suma_stavok'] = res_stavka87
    bal = await get_balance2(message.from_user.id)
    per = await get_peremog(message.from_user.id)
    username = message.from_user.username
    if float(res_stavka87) <= float(bal[0]):
      res_add_duel = await new_duel(message.from_user.id, username, int(data['suma_stavok']), 0, 'None')
      if res_add_duel == True:
        await state.finish()
        await bot.send_message(message.from_user.id, "✅ Створено!\nОчікуйте соперника.\nГра почнеться автоматично...", reply_markup=back_kb2)
        re_id = await bot.send_message(-1001973940032, f"""
🧸 Виклик на Дуель!

👤 Гравець: {message.from_user.first_name}
🎇 User: {message.from_user.username}
⚔ Перемог: {per[0]}
💰 Ставка: {float(res_stavka87)} UAH""")
        await edit_mess(message.from_user.id, int(re_id.message_id))


      else:
        await state.finish()
        await bot.send_message(message.from_user.id, "У вас вже є одна створена гра.\nДочекайтесь гравця, або видаліть стару гру.", reply_markup=duel1kb)
    else:
      await bot.send_message(
            message.from_user.id,
            f"❌ Недостатньо коштів на балансі.\n💳 Баланс: {float(bal[0])} UAH")

#PROMOCODES
@dp.message_handler(state=Promo.promocode)
@dp.throttled(anti_flood, rate=1)
async def promocode_i(message: types.Message, state: FSMContext):
  user = message.from_user.id
  async with state.proxy() as data:
    data['promocode'] = message.text
  promo = await get_promo(data['promocode'])

  try:
    if promo[1] == 'N':
      bon = await get_bonus(user)
      res_bon = float(bon[0]) + float(promo[2])
      await edit_bonus(user, res_bon)
      await dell_promocode(promo[0])
      await state.finish()
      await bot.send_message(user, f"🎁 Вітаємо!\nПромокод активовано.\nВам зараховано {promo[2]} UAH бонусу.", reply_markup=profile_kb2)
      for admin in admins:
        await bot.send_message(admin, f"{message.from_user.id}\npromo: {data['promocode']}\n{promo[2]} UAH бонусу.")
    else:
      respromo = await get_all_promok(data['promocode'])
      promsus = []
      for q in respromo:
        promsus.append(q[1])

      if message.from_user.id not in promsus:
        await add_promok(data['promocode'], message.from_user.id)
        bon = await get_bonus(user)
        res_bon = float(bon[0]) + float(promo[2])
        await edit_bonus(user, res_bon)
        await state.finish()
        await bot.send_message(user, f"🎁 Вітаємо!\nПромокод активовано.\nВам зараховано {promo[2]} UAH бонусу.", reply_markup=profile_kb2)
        for admin in admins:
          await bot.send_message(admin, f"{message.from_user.id}\npromo: {data['promocode']}\n{promo[2]} UAH бонусу.")
      else:
        await state.finish()
        await bot.send_message(user, "🩸 Промокода не існує або його вже використали.", reply_markup=profile_kb2)

  except:
    await state.finish()
    await bot.send_message(user, "🩸 Промокода не існує або його вже використали.", reply_markup=profile_kb2)



#Обробка заявки на виплату.
@dp.message_handler(state=Widwart.suma_w)
@dp.throttled(anti_flood, rate=1)
async def wid(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['suma_w'] = message.text

    bal = await get_balance2(message.from_user.id)
    try:
      sum_zap = float(data['suma_w'])

      if sum_zap >= 100.0:

        if sum_zap <= float(bal[0]):
          await bot.send_message(
              message.from_user.id,
              "💳 Введіть номер вашої карти.\nПриклад: 1111 2222 3333 4444",
              reply_markup=c_kb)
          await Widwart.next()

        else:
          await bot.send_message(
              message.from_user.id,
              f"❌ Недостатньо коштів на балансі.\nУ вас на балансі {float(bal[0])} UAH",
              reply_markup=c_kb)
      else:
        await bot.send_message(
            message.from_user.id,
            f"❌ Мінімальна сума для виплати: 100 UAH\nУ вас на балансі {float(bal[0])} UAH",
            reply_markup=c_kb)
    except:
      await bot.send_message(message.from_user.id,
                             f"❌ Ви ввели некоректні дані!",
                             reply_markup=c_kb)


@dp.message_handler(state=Widwart)
@dp.throttled(anti_flood, rate=0.8)
async def karta(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    bal = await get_balance2(message.from_user.id)
    data['karta_w'] = message.text
    karta_res = data['karta_w']
    try:
      try:
        res_karta = ''.join(karta_res.split(' '))
      except:
        pass
      if len(res_karta) >= 15:

        if int(res_karta):
          res_bal = float(bal[0]) - float(data['suma_w'])
          await edit_balance2(message.from_user.id, float(res_bal))
          #print(message.from_user.id)
          await edit_balance_w(float(data['suma_w']))
          if message.from_user.id in admins:
            keyb = menu_admins
          else:
            keyb = menu_kb
          statistic = await get_statis()
          widharts1 = float(statistic[0][1]) + float(data['suma_w'])
          widharts2 = float(statistic[0][3]) + float(data['suma_w'])
          await edit_widhart(str(widharts1))
          await edit_towidhart(str(widharts2))
          await bot.send_message(
              message.from_user.id,
              f"✅ Ви подали заявку на виплату {data['suma_w']} UAH. Карта:\n<code>{message.text}</code>\n💳 Баланс: {float(res_bal)}\n\n🙂 Після виплати, залишіть будьласко відгук в чаті гравців разом з скріншотом.\n🤖 Це нам допомагагає рухатись далі!",
              parse_mode='html',
              reply_markup=keyb)
          await state.finish()

          await bot.send_message(pro_vyplat, f"Заявка на виплату!\nКористувач: {message.from_user.username}\nID: {message.from_user.id}\n{message.from_user.first_name}\nСума: {float(data['suma_w'])}\nКарта: {message.text}")
        else:
          await bot.send_message(
              message.from_user.id,
              f"❌ Ви ввели некоректні дані!\nНомер карти має складатись тільки з цифр!\n💳 Введіть номер вашої карти.\nПриклад: 1111 2222 3333 4444",
              reply_markup=profile_kb)
      else:
        await bot.send_message(
            message.from_user.id,
            f"❌ Ви ввели некоректні дані!\nДовжина номера карти, не може бути менше 16!\n💳 Введіть номер вашої карти.\nПриклад: 1111 2222 3333 4444",
            reply_markup=c_kb)
    except:
      await bot.send_message(message.from_user.id, f"❌ Ви ввели некоректні дані!\nНомер карти має складатись тільки з цифр!\n💳 Введіть номер вашої карти.\nПриклад: 1111 2222 3333 4444", reply_markup=c_kb)


@dp.message_handler(state=ZminBal.id_z)
@dp.throttled(anti_flood, rate=0.8)
async def zmin(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['id_z'] = message.text
    await bot.send_message(message.from_user.id,
                           "Введіть скільки додати до суми балансу.")
    await ZminBal.next()


@dp.message_handler(state=ZminBal.suma_z)
@dp.throttled(anti_flood, rate=0.8)
async def zmin2(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['suma_z'] = message.text
    try:

      await create_balances(int(data['id_z']))
      bal = await get_balance2(int(data['id_z']))

      res = float(bal[0]) + float(data['suma_z'])
      await edit_balance2(int(data['id_z']), str(res))
      bal2 = await get_balance2(int(data['id_z']))
      name = await get_username(int(data['id_z']))
      ref_all = await get_ref_all()
      for ref_to in ref_all:
        try:
          if int(ref_to[0]) not in blocki:
            if str(ref_to[1]) == str(data['id_z']):
              await create_bonus(ref_to[0], 0)
              balans = await get_bonus(user_id=ref_to[0])
              resb = float(balans[0]) + 5
              await edit_bonus(ref_to[0], resb)
              if 1 == 1:
                await bot.send_message(
                    ref_to[0],
                    f"💌 Ваш реферал поповнив собі рахунок на суму: {float(data['suma_z'])} UAH!\n🎁 Ви отримали 5 UAH!\n"
                )


        except:
          pass
      bal2 = await get_balance2(int(data['id_z']))
      name = await get_username(int(data['id_z']))

      try:
        await bot.send_message(message.from_user.id,
                             f"Баланс користувача {name[0]} - {float(bal2[0])} UAH.",
                             reply_markup=menu_admins)
      except:
        await bot.send_message(message.from_user.id,
                             f"Баланс користувача - {float(bal2[0])} UAH.",
                             reply_markup=menu_admins)
      statistic = await get_statis()
      widharts1 = float(statistic[0][0]) + float(data['suma_z'])
      widharts2 = float(statistic[0][2]) + float(data['suma_z'])
      await edit_deposit(str(widharts1))
      await edit_todeposit(str(widharts2))
      await bot.send_message(int(data['id_z']), f"✴Ваш баланс поповнено на суму: {float(data['suma_z'])} UAH!\nДякуємо що ви знами!")
      await state.finish()

    except:
      await state.finish()




@dp.message_handler(state=InfoUser.id_user)
@dp.throttled(anti_flood, rate=0.8)
async def info_user(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['id_user'] = message.text

    if message.from_user.id in admins:
      bon = await get_bonus(data['id_user'])
      res = await get_all_from_userid(data['id_user'])
      resper = await get_peremog(data['id_user'])
      bal = await get_balance2(data['id_user'])
      user = message.from_user.id
      verp = await get_veref(data['id_user'])
      await bot.send_message(message.from_user.id,
                               f"""
        🎇 Username: @{res[0][1]}

        🆔: {res[0][0]}

        💳 Баланс: {float(bal[0])} UAH

        🎁 Бонус: {float(bon[0])} UAH

        👣 Реферали: {res[0][3]}

        ⚔ Перемог в дуелі: {resper[0]}

        Phone: {verp[2]}""",
                               parse_mode='HTML',
                               reply_markup=menu_admins)
      await state.finish()

      await state.finish()
    if message.from_user.id in admins2:
      bon = await get_bonus(data['id_user'])
      res = await get_all_from_userid(data['id_user'])
      resper = await get_peremog(data['id_user'])
      bal = await get_balance2(data['id_user'])
      user = message.from_user.id
      verp = await get_veref(data['id_user'])
      await bot.send_message(message.from_user.id,
                               f"""
        🎇 Username: @{res[0][1]}

        🆔: {res[0][0]}

        💳 Баланс: {float(bal[0])} UAH

        🎁 Бонус: {float(bon[0])} UAH

        👣 Реферали: {res[0][3]}

        ⚔ Перемог в дуелі: {resper[0]}

        Phone: {verp[2]}""",
                               parse_mode='HTML',
                               reply_markup=menu_admins)
      await state.finish()

      await state.finish()
#########




@dp.message_handler(state=OrelStorage.suma_stavka)
@dp.throttled(anti_flood, rate=0.8)
async def sum_orel(message: types.Message, state: FSMContext):
  if message.text in ['50 UAH 🔮', '25 UAH 🔮', '10 UAH 🔮', '5 UAH 🔮', '1 UAH 🔮', '0 UAH 🔮']:
    res_stavka = ''.join(message.text.split(' ')[:-2])
    #print(f"{message.from_user.id} Слоти - ставка: {res_stavka} UAH")



    async with state.proxy() as data:
      data['suma_stavka'] = res_stavka





    bal = await get_balance2(message.from_user.id)
    bon = await get_bonus(message.from_user.id)
    if float(res_stavka) <= float(bal[0]):
      await bot.send_message(
              message.from_user.id,
                f"🔮 Ставка {res_stavka} UAH принята!\nВиберіть результат.",
                reply_markup=orel_reshka_kb)
      await OrelStorage.next()


    else:
      if float(res_stavka) <= float(bon[0]):
        await bot.send_message(
              message.from_user.id,
                  f"🔮 Ставка {res_stavka} UAH принята!\nВиберіть результат.",
                  reply_markup=orel_reshka_kb)
        await OrelStorage.next()
      else:
        bon2 = await get_bonus(message.from_user.id)
        await state.finish()
        await bot.send_message(
                    message.from_user.id,
                    f"❌ Недостатньо коштів на балансі.\n💳 Баланс: {float(bal[0])} UAH\n🎁 Бонус: {float(bon2[0])} UAH", reply_markup=menu_kb)

@dp.message_handler(state=Rosa.text_rosa)
@dp.throttled(anti_flood, rate=0.8)
async def adminka_rosa(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['text_rosa'] = message.text

  user_all = await get_users_all()
  us_all = []
  d_user = 0
  k_user = 0
  for q in user_all:
    try:
      await bot.send_message(q[0], data['text_rosa'])
      k_user += 1
    except:
      #await edit_balance2(q[0], 3)
      d_user += 1
  await state.finish()
  await bot.send_message(
      message.from_user.id,
      f"{k_user} користувачів отримали ваше повідомлення!\n{d_user} Не отримали.",
      reply_markup=menu_admins)


@dp.message_handler(state=OrelStorage.orel_or)
@dp.throttled(anti_flood, rate=0.8)
async def gra01(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    sums = data['suma_stavka']
  print(sums)
  if int(sums) == 0:
    orel_reshka = [1, 2, 3, 4]

  if int(sums) == 1:
    orel_reshka = [1, 2, 3, 4]

  if int(sums) == 5:
    orel_reshka = [1, 2, 3, 4]

  if int(sums) == 10:
    orel_reshka = [1, 2, 3, 4]

  if int(sums) == 25:
    orel_reshka = [1, 3, 2, 4, 4]

  if int(sums) == 50:
    orel_reshka = [1, 3, 2, 4, 4]

  async with state.proxy() as data:
    data['orel_or'] = str(message.text)

    result = choice(orel_reshka)
    if result == 1:
      res = "🔵"
    elif result == 2:
      res = "🟢"
    elif result == 3:
      res = "🔴"
    elif result == 4:
      if data['orel_or'] == "🔵":
        res = choice(['🟢', '🔴'])

      if data['orel_or'] == "🟢":
        res = choice(['🔵', '🔴'])

      if data['orel_or'] == "🔴":
        res = choice(['🔵', '🟢'])



    if str(data['orel_or']) == res:


      balance = await get_balance2(message.from_user.id)
      bon2 = await get_bonus(message.from_user.id)


      m_st = int(data['suma_stavka']) * 2


      bal = float(balance[0]) + float(m_st)
      mb = await get_balance_m()
      ress = mb[0] - float(m_st)
      await edit_balance_m(ress)


      await edit_balance2(user_id=message.from_user.id, bal=float(bal))
      balance2 = await get_balance2(message.from_user.id)
      bon2 = await get_bonus(message.from_user.id)
      await message.answer(f"Результат: {res} X3!\n🙂 Ви виграли {float(m_st)+float(sums)} UAH !\n💳 Баланс: {float(balance2[0])} UAH\n🎁 Бонус: {float(bon2[0])} UAH", reply_markup=stavka_kb)
      print(f"{message.from_user.id} Lucky - ставка: {data['suma_stavka']} UAH    +{data['suma_stavka']} = {balance2[0]}") 
      await state.finish()
      await OrelStorage.suma_stavka.set()




    if str(data['orel_or']) != str(res) and data['orel_or'] in ["🔴", "🟢", "🔵"]:

      balance2 = await get_balance2(message.from_user.id)
      bon = await get_bonus(message.from_user.id)

      mbl = await get_balance_m()
      res_mbl = int(mbl[0]) + int(sums)
      res_balance_user = float(balance2[0]) - float(data['suma_stavka'])
      res_balance_user2 = float(bon[0]) - float(data['suma_stavka'])


      await edit_balance_m(res_mbl)

      if float(bon[0]) >= float(data['suma_stavka']):
        await edit_bonus(message.from_user.id, res_balance_user2)
      else:
        if float(balance2[0]) >= float(data['suma_stavka']):
          await edit_balance2(message.from_user.id, res_balance_user)




      await state.finish()
      balance2 = await get_balance2(message.from_user.id)
      bon2 = await get_bonus(message.from_user.id)
      await message.answer(f"Результат: {res}\n😞 Удача не на вашому боці.\n💳 Баланс: {float(balance2[0])} UAH\n🎁 Бонус: {float(bon2[0])} UAH", reply_markup=stavka_kb)
      print(f"{message.from_user.id} Lucky - ставка: {data['suma_stavka']} UAH    -{data['suma_stavka']} = {balance2[0]}") 
      await state.finish()
      await OrelStorage.suma_stavka.set()
    if str(data['orel_or']) != str(res) and data['orel_or'] not in ["🔴", "🟢", "🔵"]:
      #print(data['orel_or'])
      await state.finish()
      if message.from_user.id in admins:
        keyb = menu_admins
      else:
        keyb = menu_kb
      await bot.send_message(message.from_user.id, "Невідоме значення.", reply_markup=keyb)

@dp.message_handler(state=perekaz.id_o)
@dp.throttled(anti_flood, rate=0.8)
async def perekaz_id(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['id_o'] = message.text
  try:
    if int(data['id_o']) > 5:
      await bot.send_message(message.from_user.id, f"🆔: {data['id_o']}\nВведіть суму переказу.", reply_markup=c_kb)
      await perekaz.next()
    else:
      if message.from_user.id in admins:
        await bot.send_message(message.from_user.id, '❌ Помилка в ID одержувача!', reply_markup=menu_admins)
        await state.finish()
      else:
        await bot.send_message(message.from_user.id, '❌ Помилка в ID одержувача!', reply_markup=menu_kb)
      await state.finish()
  except:
    if message.from_user.id in admins:
      await bot.send_message(message.from_user.id, '❌ Помилка в ID одержувача!', reply_markup=menu_admins)
      await state.finish()
    else:
      await bot.send_message(message.from_user.id, '❌ Помилка в ID одержувача!', reply_markup=menu_kb)
      await state.finish()

@dp.message_handler(state=perekaz.suma_p)
@dp.throttled(anti_flood, rate=0.8)
async def perekaz_summ(message: types.Message, state: FSMContext):
  try:
    async with state.proxy() as data:
      id_oo = data['id_o']
    async with state.proxy() as data:
      data['suma_p'] = message.text
    bal1 = await get_balance2(message.from_user.id)
    bal2 = await get_balance2(data['id_o'])

    if float(bal1[0]) >= float(data['suma_p']):
      if int(message.from_user.id) != int(data['id_o']):
        res1 = float(bal1[0]) - float(data['suma_p'])
        await edit_balance2(message.from_user.id, res1)

        res2 = float(bal2[0]) + float(data['suma_p'])
        await edit_balance2(id_oo, str(res2))
        bal3 = await get_balance2(id_oo)

        bal4 = await get_balance2(message.from_user.id)
        await state.finish()
        if message.from_user.id in admins:
          re_kb1 = menu_admins
        else:
          re_kb1 = menu_kb
        if id_oo in admins:
          re_kb2 = menu_admins
        else:
          re_kb2 = menu_kb
        for admin in admins:
          await bot.send_message(admin, f"""
    Переказ коштів
    {message.from_user.id}   {float(data['suma_p'])} UAH
          >>>
    {id_oo}""")
        await bot.send_message(id_oo, f"""
    ✅  Вам надіслано переказ! ✴

    🆔 Відправника: {message.from_user.id}
    Сума переказу: {float(data['suma_p'])} UAH

    💳 Баланс: {float(bal3[0])} UAH


    """)
        await bot.send_message(message.from_user.id, f"""
    ✅  Переказ надіслано! ✴

    🆔 Отримувача: {data['id_o']}
    Сума переказу: {float(data['suma_p'])} UAH

    💳 Баланс: {float(bal4[0])} UAH


    """, reply_markup=re_kb1)
      else:
        if message.from_user.id in admins:
          re_kb = menu_admins
        else:
          re_kb = menu_kb

        await state.finish()
        await bot.send_message(message.from_user.id, f"❌ Ви не можете переказати кошти собі!", reply_markup=re_kb)
    else:
      bal4 = await get_balance2(message.from_user.id)
      if message.from_user.id in admins:
        re_kb = menu_admins
      else:
        re_kb = menu_kb
      if id_oo in admins:
        re_kb2 = menu_admins
      else:
        re_kb2 = menu_kb
      await state.finish()
      await bot.send_message(message.from_user.id, f"❌ Недостатньо коштів на балансі.\n💳 Баланс: {float(bal4[0])} UAH", reply_markup=re_kb)
  except:
    if message.from_user.id in admins:
      re_kb = menu_admins

    else:
      re_kb = menu_kb
    if id_oo in admins:
      re_kb2 = menu_admins
    else:
      re_kb2 = menu_kb
    #await state.finish()
    await bot.send_message(message.from_user.id, '❌ Помилка в ID одержувача або сумі поповненння!', reply_markup=re_kb)
    await state.finish()






keep_alive()
if __name__ == '__main__':
  executor.start_polling(dp, on_startup=on_startup, skip_updates=False)
