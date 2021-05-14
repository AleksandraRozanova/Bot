import telebot

bot = telebot.TeleBot('1773022199:AAFICnJg_0DLHYhNrQchvq4cy4v7fqjqc6k')


@bot.message_handler(commands=['start'])
def process_start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Ламинат')
    keyboard.row('Линолиум')
    msg = bot.send_message(message.chat.id, text='Нажмите любую кнопку в меню', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def step1(message):
    if message.text == "400036731":
        bot.send_message(message.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Balterio Fortissimo New click AC 5/33 (1257х190,5х12 мм)"
                                               "\n Тон/Рулон: 135 Дуб Фуджи (1,4368 кв.м.)"
                                               "\n Артикул: 400036731"
                                               "\n Штрихкод: 5415125712014")
        bot.send_photo(message.from_user.id,   "https://www.stroycity.ru/images/laminat/Balterio/Fortissimo/decor/135_FOR.jpg")
    elif message.text == "400036733":
        bot.send_message(message.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Balterio Fortissimo New click AC 5/33 (1257х190,5х12 мм)"
                                               "\n Тон/Рулон: 138 Дуб Килиманджаро (1,4368 кв.м.)"
                                               "\n Артикул: 400036733"
                                               "\n Штрихкод: 5415125712038")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/laminat/Balterio/Fortissimo/decor/138_FOR.jpg")
    elif message.text == "400036732":
        bot.send_message(message.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Balterio Fortissimo New click AC 5/33 (1257х190,5х12 мм)"
                                               "\n Тон/Рулон: 136 Дуб Гималайя  (1,4368 кв.м.)"
                                               "\n Артикул: 400036732"
                                               "\n Штрихкод: 5415125712021")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/laminat/Balterio/Fortissimo/decor/136_FOR.jpg")
    elif message.text == "400036734":
        bot.send_message(message.from_user.id, "Название: Ламинат"
                                            "\n Коллекция: Balterio Fortissimo New click AC 5/33 (1257х190,5х12 мм)"
                                            "\n Тон/Рулон: 139 Дуб Этна  (1,4368 кв.м.)"
                                            "\n Артикул: 400036734"
                                            "\n Штрихкод: 5415125712045")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/laminat/Balterio/Fortissimo/decor/139_FOR.jpg")
    elif message.text == "D1821":
        bot.send_message(message.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Floorwood Epica АС 5/33 (1380х193х8мм)"
                                               "\n Тон/Рулон: D1821 Дуб Винсент ( 2,131 кв.м.)"
                                               "\n Артикул: D1821"
                                               "\n Штрихкод: 4660024290342")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/laminat/Floorwood/Epica/Decors/D1821.jpg")
    elif message.text == "D1822":
        bot.send_message(message.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Floorwood Epica АС 5/33 (1380х193х8мм)"
                                               "\n Тон/Рулон: D1822 Дуб Ануари ( 2,131 кв.м.)"
                                               "\n Артикул: D1822"
                                               "\n Штрихкод: 4660024290359")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/laminat/Floorwood/Epica/Decors/D1822.jpg")
    elif message.text == "D1824":
        bot.send_message(message.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Floorwood Epica АС 5/33 (1380х193х8мм)"
                                               "\n Тон/Рулон: D1824 Дуб Грюйер ( 2,131 кв.м.)"
                                               "\n Артикул: D1824"
                                               "\n Штрихкод: 4660024290373")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/laminat/Floorwood/Epica/Decors/D1824.jpg")
    elif message.text == "S172494":
        bot.send_message(message.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Faus Elegance AC6/33 (1182,6х395,7х8 мм)"
                                               "\n Тон/Рулон: S172494 Divino Oak (2,34 кв.м.)"
                                               "\n Артикул: S172494"
                                               "\n Штрихкод: 8426924172494")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/laminat/FAUS/Elegance/decor/S172494%20Divino%20Oak.jpg")
    elif message.text == "S172524":
        bot.send_message(message.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Faus Elegance AC6/33 (1182,6х395,7х8 мм)"
                                               "\n Тон/Рулон: S172524 Romance Oak (2,34 кв.м.)"
                                               "\n Артикул: S172524"
                                               "\n Штрихкод: 8426924172524")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/laminat/FAUS/Elegance/decor/S172524%20Romance%20Oak.jpg")
    elif message.text == "S172620":
        bot.send_message(message.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Faus Elegance AC6/33 (1182,6х395,7х8 мм)"
                                               "\n Тон/Рулон: S173620 Colonial Oak (2,34 кв.м.)"
                                               "\n Артикул: S173620"
                                               "\n Штрихкод: 8426924173620")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/laminat/FAUS/Elegance/decor/S173620%20Colonial%20Oak.jpg")
    elif message.text == "6642":
        bot.send_message(message.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Floorwood Estet 4V АС 5/33 (1382х195х12мм)"
                                               "\n Тон/Рулон: 6642 Дуб Бэкстер (1,347 кв.м.)"
                                               "\n Артикул: 6642"
                                               "\n Штрихкод: 4665304110464")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/laminat/Floorwood/Estet/Decors/Dub_bekster_1024.jpg")
    elif message.text == "7681":
        bot.send_message(message.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Floorwood Estet 4V АС 5/33 (1382х195х12мм)"
                                               "\n Тон/Рулон: 7681 Дуб Иберо грей (1,347 кв.м.)"
                                               "\n Артикул: 7681"
                                               "\n Штрихкод: 4665304110600")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/laminat/Floorwood/Estet/Decors/Dub_ibero_grey_1024.jpg")
    elif message.text == "6741":
        bot.send_message(message.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Floorwood Estet 4V АС 5/33 (1382х195х12мм)"
                                               "\n Тон/Рулон: 6741 Дуб Савой (1,347 кв.м.)"
                                               "\n Артикул: 6741"
                                               "\n Штрихкод: 4665304110594")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/laminat/Floorwood/Estet/Decors/Dub_savoy_1024.jpg")
    elif message.text == "6687":
        bot.send_message(message.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Floorwood Estet 4V АС 5/33 (1382х195х12мм)"
                                               "\n Тон/Рулон: 6687 Дуб Ленсингтон (1,347 кв.м.)"
                                               "\n Артикул: 6687"
                                               "\n Штрихкод: 4665304110471")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/laminat/Floorwood/Estet/Decors/Dub_lensington_1024.jpg")
    elif message.text == "6693":
        bot.send_message(message.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Floorwood Estet 4V АС 5/33 (1382х195х12мм)"
                                               "\n Тон/Рулон: 6693 Дуб Энтони (1,347 кв.м.)"
                                               "\n Артикул: 6693"
                                               "\n Штрихкод: 4665304110488")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/laminat/Floorwood/Estet/Decors/Dub_entoni_1024.jpg")
    elif message.text == "400031189":
        bot.send_message(message.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Vitality Deluxe 4V АС4/32 (1261х190,5х8 мм)"
                                               "\n Тон/Рулон: 316 Дуб шато ( 2,162 кв.м.)"
                                               "\n Артикул: 400031189"
                                               "\n Штрихкод: 5414084756688")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/laminat/Balterio/Vitality%20Deluxe/decor/316.jpg")
    elif message.text == "400031197":
        bot.send_message(message.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Vitality Deluxe 4V АС4/32 (1261х190,5х8 мм)"
                                               "\n Тон/Рулон: 328 Дуб Амбарный ( 2,162 кв.м.)"
                                               "\n Артикул: 400031197"
                                               "\n Штрихкод: 5414084756725")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/laminat/Balterio/Vitality%20Deluxe/decor/328-1024.jpg")
    elif message.text == "400031214":
        bot.send_message(message.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Vitality Deluxe 4V АС4/32 (1261х190,5х8 мм)"
                                               "\n Тон/Рулон: 491 Дуб отбеленный ( 2,162 кв.м.)"
                                               "\n Артикул: 400031214"
                                               "\n Штрихкод: 5414084756800")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/laminat/Balterio/Vitality%20Deluxe/decor/491-1024.jpg")
    elif message.text == "400031220":
        bot.send_message(message.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Vitality Deluxe 4V АС4/32 (1261х190,5х8 мм)"
                                               "\n Тон/Рулон: 544 Орех Селект ( 2,162 кв.м.)"
                                               "\n Артикул: 400031220"
                                               "\n Штрихкод: 5414084756848")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/laminat/Balterio/Vitality%20Deluxe/decor/544-1024.jpg")
    elif message.text == "400031235":
        bot.send_message(message.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Vitality Deluxe 4V АС4/32 (1261х190,5х8 мм)"
                                               "\n Тон/Рулон: 583 Дуб Лакированный натуральный ( 2,162 кв.м.)"
                                               "\n Артикул: 400031235"
                                               "\n Штрихкод: 5414084756985")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/laminat/Balterio/Vitality%20Deluxe/decor/583-1024.jpg")
    elif message.text == "400031246":
        bot.send_message(message.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Vitality Deluxe 4V АС4/32 (1261х190,5х8 мм)"
                                               "\n Тон/Рулон: 619 Дуб белый промасленный ( 2,162 кв.м.)"
                                               "\n Артикул: 400031246"
                                               "\n Штрихкод: 5414084757067")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/laminat/Balterio/Vitality%20Deluxe/decor/619-1024.jpg")
    elif message.text == "400031324":
        bot.send_message(message.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Vitality Deluxe 4V АС4/32 (1261х190,5х8 мм)"
                                               "\n Тон/Рулон: 796 Дуб Песчаный ( 2,162 кв.м.)"
                                               "\n Артикул: 400031324"
                                               "\n Штрихкод: 5414084757180")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/laminat/Balterio/Vitality%20Deluxe/decor/796-1024.jpg")
    elif message.text == "400031326":
        bot.send_message(message.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Vitality Deluxe 4V АС4/32 (1261х190,5х8 мм)"
                                               "\n Тон/Рулон: 797 Дуб Золотой закат ( 2,162 кв.м.)"
                                               "\n Артикул: 400031326"
                                               "\n Штрихкод: 5414084757227")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/laminat/Balterio/Vitality%20Deluxe/decor/797-1024.jpg")
    elif message.text == "400031330":
        bot.send_message(message.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Vitality Deluxe 4V АС4/32 (1261х190,5х8 мм)"
                                               "\n Тон/Рулон: 900 Дуб серовато-дымчатый ( 2,162 кв.м.)"
                                               "\n Артикул: 400031330"
                                               "\n Штрихкод: 5414084757265")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/laminat/Balterio/Vitality%20Deluxe/decor/900-1024.jpg")
    elif message.text == "400031339":
        bot.send_message(message.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Vitality Deluxe 4V АС4/32 (1261х190,5х8 мм)"
                                               "\n Тон/Рулон: 903 Дуб Шамо ( 2,162 кв.м.)"
                                               "\n Артикул: 400031339"
                                               "\n Штрихкод: 5414084757388")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/laminat/Balterio/Vitality%20Deluxe/decor/903-1024.jpg")
    elif message.text == "400030851":
        bot.send_message(message.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Balterio Impressio AC 4/32 (1261х244х8 мм)"
                                               "\n Тон/Рулон: 928 Дуб Wadi Rum ( 2,4615 кв.м.)"
                                               "\n Артикул: 400030851"
                                               "\n Штрихкод: 5414084716309")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/laminat/Balterio/Impressio/decor/928_IMP.jpg")
    elif message.text == "400030853":
        bot.send_message(message.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Balterio Impressio AC 4/32 (1261х244х8 мм)"
                                               "\n Тон/Рулон: 930 Дуб Фраппучино ( 2,4615 кв.м.)"
                                               "\n Артикул: 400030853"
                                               "\n Штрихкод: 5414084716347")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/laminat/Balterio/Impressio/decor/930_IMP.jpg")
    elif message.text == "400031419":
        bot.send_message(message.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Balterio Impressio AC 4/32 (1261х244х8 мм)"
                                               "\n Тон/Рулон: 106 Дуб Гарда ( 2,4615 кв.м.)"
                                               "\n Артикул: 400031419"
                                               "\n Штрихкод: 5414084766038")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/laminat/Balterio/Impressio/decor/106_IMP.jpg")
    elif message.text == "400030852":
        bot.send_message(message.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Balterio Impressio AC 4/32 (1261х244х8 мм)"
                                               "\n Тон/Рулон: 929 Дуб Коричнево-Дымчатый ( 2,4615 кв.м.)"
                                               "\n Артикул: 400030852"
                                               "\n Штрихкод: 5414084716323")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/laminat/Balterio/Impressio/decor/929_IMP.jpg")
    elif message.text == "400030855":
        bot.send_message(message.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Balterio Impressio AC 4/32 (1261х244х8 мм)"
                                               "\n Тон/Рулон: 915 Дуб с Подпалиной ( 2,4615 кв.м.)"
                                               "\n Артикул: 400030855"
                                               "\n Штрихкод: 5414084717023")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/laminat/Balterio/Impressio/decor/915_IMP.jpg")
    elif message.text == "400031421":
        bot.send_message(message.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Balterio Impressio AC 4/32 (1261х244х8 мм)"
                                               "\n Тон/Рулон: 142 Дуб Каспий ( 2,4615 кв.м.)"
                                               "\n Артикул: 400031421"
                                               "\n Штрихкод: 5414084766052")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/laminat/Balterio/Impressio/decor/142_IMP.jpg")
    elif message.text == "400030857":
        bot.send_message(message.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Balterio Impressio AC 4/32 (1261х244х8 мм)"
                                               "\n Тон/Рулон: 917 Дуб Саванна ( 2,4615 кв.м.)"
                                               "\n Артикул: 400030857"
                                               "\n Штрихкод: 5414084717047")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/laminat/Balterio/Impressio/decor/917_IMP.jpg")
    elif message.text == "400036087":
        bot.send_message(message.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Balterio Impressio AC 4/32 (1261х244х8 мм)"
                                               "\n Тон/Рулон: 917 Дуб Саванна ( 2,4615 кв.м.)"
                                               "\n Артикул: 400030857"
                                               "\n Штрихкод: 5414084717047")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/laminat/Balterio/Impressio/decor/184_IMP.jpg")
    elif message.text == "V4240.483C931G300":
        bot.send_message(message.from_user.id, "Название: Линолеум"
                                               "\n Коллекция: IVC CITYLIFE 931 Venturi Spark/001 Ravena 3м"
                                               "\n Тон/Рулон: 116,10 кв.м"
                                               "\n Артикул: V4240.483C931G300")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/linoleum/!Leoline%202020/CITYLIFE/Decors/Venturi%20931%20%D0%A0%D0%B0%D0%B2%D0%B5%D0%BD%D0%BD%D0%B0%20001.jpg")
    elif message.text == "V4240.483C931G301":
        bot.send_message(message.from_user.id, "Название: Линолеум"
                                               "\n Коллекция: IVC CITYLIFE 931 Venturi Spark/001 Ravena 3м"
                                               "\n Тон/Рулон: 119,34 кв.м"
                                               "\n Артикул: V4240.483C931G301")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/linoleum/!Leoline%202020/CITYLIFE/Decors/Venturi%20931%20%D0%A0%D0%B0%D0%B2%D0%B5%D0%BD%D0%BD%D0%B0%20001.jpg")
    elif message.text == "V4240.483C931G302":
        bot.send_message(message.from_user.id, "Название: Линолеум"
                                               "\n Коллекция: IVC CITYLIFE 931 Venturi Spark/001 Ravena 3м"
                                               "\n Тон/Рулон: 120,00 кв.м"
                                               "\n Артикул: V4240.483C931G302")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/linoleum/!Leoline%202020/CITYLIFE/Decors/Venturi%20931%20%D0%A0%D0%B0%D0%B2%D0%B5%D0%BD%D0%BD%D0%B0%20001.jpg")
    elif message.text == "V8314.483C591G300":
        bot.send_message(message.from_user.id, "Название: Линолеум"
                                               "\n Коллекция: IVC CITYLIFE 591 Samson Spark/3 Samson 3м"
                                               "\n Тон/Рулон: 105,30 кв.м"
                                               "\n Артикул: V8314.483C591G300")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/linoleum/!Leoline%202020/CITYLIFE/Decors/Samson%20591%20%D0%A1%D0%B0%D0%BC%D1%81%D0%BE%D0%BD%203.jpg")
    elif message.text == "V8314.483C591G400":
        bot.send_message(message.from_user.id, "Название: Линолеум"
                                               "\n IVC CITYLIFE 591 Samson Spark/3 Samson 4м"
                                               "\n Тон/Рулон: 150,00 кв.м"
                                               "\n Артикул: V8314.483C591G400")
        bot.send_photo(message.from_user.id, "https://www.stroycity.ru/images/linoleum/!Leoline%202020/CITYLIFE/Decors/Samson%20591%20%D0%A1%D0%B0%D0%BC%D1%81%D0%BE%D0%BD%203.jpg")


    menu1 = telebot.types.InlineKeyboardMarkup()
    menu1.add(telebot.types.InlineKeyboardButton(text='Floorwood', callback_data='Floorwood'))
    menu1.add(telebot.types.InlineKeyboardButton(text='Balterio', callback_data='Balterio'))
    menu1.add(telebot.types.InlineKeyboardButton(text='Vitality', callback_data='Vitality'))
    menu1.add(telebot.types.InlineKeyboardButton(text='Faus', callback_data='Faus'))
    if message.text == 'Ламинат':
        msg = bot.send_message(message.chat.id, text='Выберите коллекцию', reply_markup=menu1)

    menu2 = telebot.types.InlineKeyboardMarkup()
    menu2.add(
        telebot.types.InlineKeyboardButton(text='Venturi Spark/001 Ravena', callback_data='Venturi Spark/001 Ravena'))
    menu2.add(telebot.types.InlineKeyboardButton(text='Samson Spark/3 Samson', callback_data='Samson Spark/3 Samson'))
    if message.text == 'Линолиум':
        msg = bot.send_message(message.chat.id, text='Выберите коллекцию', reply_markup=menu2)


@bot.callback_query_handler(func=lambda call: True)
def step2(call):
    menu3 = telebot.types.InlineKeyboardMarkup()
    menu3.add(telebot.types.InlineKeyboardButton(text='Floorwood Estet', callback_data='Floorwood Estet'))
    menu3.add(telebot.types.InlineKeyboardButton(text='Floorwood Epica', callback_data='Floorwood Epica'))

    menu4 = telebot.types.InlineKeyboardMarkup()
    menu4.add(telebot.types.InlineKeyboardButton(text='Faus Elegance', callback_data='Faus Elegance'))

    menu5 = telebot.types.InlineKeyboardMarkup()
    menu5.add(telebot.types.InlineKeyboardButton(text='Vitality Deluxe', callback_data='Vitality Deluxe'))

    menu6 = telebot.types.InlineKeyboardMarkup()
    menu6.add(telebot.types.InlineKeyboardButton(text='Balterio Impressio', callback_data='Balterio Impressio'))
    menu6.add(telebot.types.InlineKeyboardButton(text='Balterio Fortissimo', callback_data='Balterio Fortissimo'))

    if call.data == 'Floorwood':
        msg = bot.send_message(call.message.chat.id, 'Выберете тип', reply_markup=menu3)

    elif call.data == 'Faus':
        msg = bot.send_message(call.message.chat.id, 'Выберете тип', reply_markup=menu4)

    elif call.data == 'Vitality':
        msg = bot.send_message(call.message.chat.id, 'Выберете тип', reply_markup=menu5)

    elif call.data == 'Balterio':
        msg = bot.send_message(call.message.chat.id, 'Выберете тип', reply_markup=menu6)

    menu7 = telebot.types.InlineKeyboardMarkup()
    menu7.add(telebot.types.InlineKeyboardButton(text='116,10 кв.м', callback_data='116,10 кв.м'))
    menu7.add(telebot.types.InlineKeyboardButton(text='119,34 кв.м', callback_data='119,34 кв.м'))
    menu7.add(telebot.types.InlineKeyboardButton(text='120,00 кв.м', callback_data='120,00 кв.м'))

    menu8 = telebot.types.InlineKeyboardMarkup()
    menu8.add(telebot.types.InlineKeyboardButton(text='105,30 кв.м', callback_data='105,30 кв.м'))
    menu8.add(telebot.types.InlineKeyboardButton(text='150,00 кв.м', callback_data='150,00 кв.м'))

    if call.data == 'Venturi Spark/001 Ravena':
        msg = bot.send_message(call.message.chat.id, 'Выберете размер', reply_markup=menu7)
    elif call.data == 'Samson Spark/3 Samson':
        msg = bot.send_message(call.message.chat.id, 'Выберете размер', reply_markup=menu8)

    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    if call.data == '116,10 кв.м':
        bot.send_message(call.from_user.id, "Название: Линолеум"
                                            "\n Коллекция: IVC CITYLIFE 931 Venturi Spark/001 Ravena 3м"
                                            "\n Тон/Рулон: 116,10 кв.м"
                                            "\n Артикул: V4240.483C931G300")
        bot.send_photo(call.from_user.id, "https://www.stroycity.ru/images/linoleum/!Leoline%202020/CITYLIFE/Decors/Venturi%20931%20%D0%A0%D0%B0%D0%B2%D0%B5%D0%BD%D0%BD%D0%B0%20001.jpg")
    elif call.data == '119,34 кв.м':
        bot.send_message(call.from_user.id, "Название: Линолеум"
                                               "\n Коллекция: IVC CITYLIFE 931 Venturi Spark/001 Ravena 3м"
                                               "\n Тон/Рулон: 119,34 кв.м"
                                               "\n Артикул: V4240.483C931G301")
        bot.send_photo(call.from_user.id,  "https://www.stroycity.ru/images/linoleum/!Leoline%202020/CITYLIFE/Decors/Venturi%20931%20%D0%A0%D0%B0%D0%B2%D0%B5%D0%BD%D0%BD%D0%B0%20001.jpg")
    elif call.data == '120,00 кв.м':
        bot.send_message(call.from_user.id, "Название: Линолеум"
                                               "\n Коллекция: IVC CITYLIFE 931 Venturi Spark/001 Ravena 3м"
                                               "\n Тон/Рулон: 120,00 кв.м"
                                               "\n Артикул: V4240.483C931G302")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/linoleum/!Leoline%202020/CITYLIFE/Decors/Venturi%20931%20%D0%A0%D0%B0%D0%B2%D0%B5%D0%BD%D0%BD%D0%B0%20001.jpg")
    elif call.data == '105,30 кв.м':
        bot.send_message(call.from_user.id, "Название: Линолеум"
                                               "\n Коллекция: IVC CITYLIFE 591 Samson Spark/3 Samson 3м"
                                               "\n Тон/Рулон: 105,30 кв.м"
                                               "\n Артикул: V8314.483C591G300")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/linoleum/!Leoline%202020/CITYLIFE/Decors/Samson%20591%20%D0%A1%D0%B0%D0%BC%D1%81%D0%BE%D0%BD%203.jpg")
    elif call.data == '150,00 кв.м':
        bot.send_message(call.from_user.id, "Название: Линолеум"
                                               "\n IVC CITYLIFE 591 Samson Spark/3 Samson 4м"
                                               "\n Тон/Рулон: 150,00 кв.м"
                                               "\n Артикул: V8314.483C591G400")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/linoleum/!Leoline%202020/CITYLIFE/Decors/Samson%20591%20%D0%A1%D0%B0%D0%BC%D1%81%D0%BE%D0%BD%203.jpg")

    menu9 = telebot.types.InlineKeyboardMarkup()
    menu9.add(telebot.types.InlineKeyboardButton(text='Дуб Бэкстер', callback_data='Дуб Бэкстер'))
    menu9.add(telebot.types.InlineKeyboardButton(text='Дуб Иберо грей', callback_data='Дуб Иберо грей'))
    menu9.add(telebot.types.InlineKeyboardButton(text='Дуб Савой', callback_data='Дуб Савой'))
    menu9.add(telebot.types.InlineKeyboardButton(text='Дуб Ленсингтон', callback_data='Дуб Ленсингтон'))
    menu9.add(telebot.types.InlineKeyboardButton(text='Дуб Энтони', callback_data='Дуб Энтони'))

    menu10 = telebot.types.InlineKeyboardMarkup()
    menu10.add(telebot.types.InlineKeyboardButton(text='Дуб Винсент', callback_data='Faus Elegance'))
    menu10.add(telebot.types.InlineKeyboardButton(text='Дуб Ануари ', callback_data='Дуб Ануари '))
    menu10.add(telebot.types.InlineKeyboardButton(text='Дуб Грюйер', callback_data='Дуб Грюйер'))

    menu11 = telebot.types.InlineKeyboardMarkup()
    menu11.add(telebot.types.InlineKeyboardButton(text='Divino Oak', callback_data='Divino Oak'))
    menu11.add(telebot.types.InlineKeyboardButton(text='Romance Oak', callback_data='Romance Oak'))
    menu11.add(telebot.types.InlineKeyboardButton(text='Colonial Oak', callback_data='Colonial Oak'))

    menu12 = telebot.types.InlineKeyboardMarkup()
    menu12.add(telebot.types.InlineKeyboardButton(text='Дуб шато', callback_data='Дуб шато'))
    menu12.add(telebot.types.InlineKeyboardButton(text='Дуб Амбарный', callback_data='Дуб Амбарный'))
    menu12.add(telebot.types.InlineKeyboardButton(text='Дуб отбеленный', callback_data='Дуб отбеленный'))
    menu12.add(telebot.types.InlineKeyboardButton(text='Орех Селект', callback_data='Орех Селект'))
    menu12.add(telebot.types.InlineKeyboardButton(text='Дуб Лакированный натуральный',
                                                  callback_data='Дуб Лакированный натуральный'))
    menu12.add(telebot.types.InlineKeyboardButton(text='Дуб белый промасленный', callback_data='Дуб белый промасленный'))
    menu12.add(telebot.types.InlineKeyboardButton(text='Дуб Песчаный', callback_data='Дуб Песчаный'))
    menu12.add(telebot.types.InlineKeyboardButton(text='Дуб Золотой закат', callback_data='Дуб Золотой закат'))
    menu12.add(telebot.types.InlineKeyboardButton(text='Дуб серовато-дымчатый', callback_data='Дуб серовато-дымчатый'))
    menu12.add(telebot.types.InlineKeyboardButton(text='Дуб Шамо', callback_data='Дуб Шамо'))

    menu13 = telebot.types.InlineKeyboardMarkup()
    menu13.add(telebot.types.InlineKeyboardButton(text='Дуб Wadi Rum', callback_data='Дуб Wadi Rum'))
    menu13.add(telebot.types.InlineKeyboardButton(text='Дуб Фраппучино', callback_data='Дуб Фраппучино'))
    menu13.add(telebot.types.InlineKeyboardButton(text='Дуб Гарда', callback_data='Дуб Гарда'))
    menu13.add(telebot.types.InlineKeyboardButton(text='Дуб Коричнево-Дымчатый', callback_data='Дуб Коричнево-Дымчатый'))
    menu13.add(telebot.types.InlineKeyboardButton(text='Дуб с Подпалиной', callback_data='Дуб с Подпалиной'))
    menu13.add(telebot.types.InlineKeyboardButton(text='Дуб Каспий', callback_data='Дуб Каспий'))
    menu13.add(telebot.types.InlineKeyboardButton(text='Дуб Саванна', callback_data='Дуб Саванна'))
    menu13.add(telebot.types.InlineKeyboardButton(text='Дуб Слоновая кость', callback_data='Дуб Слоновая кость'))

    menu14 = telebot.types.InlineKeyboardMarkup()
    menu14.add(telebot.types.InlineKeyboardButton(text='Дуб Фуджи', callback_data='Дуб Фуджи'))
    menu14.add(telebot.types.InlineKeyboardButton(text='Дуб Килиманджаро', callback_data='Дуб Килиманджаро'))
    menu14.add(telebot.types.InlineKeyboardButton(text='Дуб Гималайя', callback_data='Дуб Гималайя'))
    menu14.add(telebot.types.InlineKeyboardButton(text='Дуб Этна', callback_data='Дуб Этна'))

    if call.data == 'Floorwood Estet':
        msg = bot.send_message(call.message.chat.id, 'Выберете материал', reply_markup=menu9)

    elif call.data == 'Floorwood Epica':
        msg = bot.send_message(call.message.chat.id, 'Выберете материал', reply_markup=menu10)

    elif call.data == 'Faus Elegance':
        msg = bot.send_message(call.message.chat.id, 'Выберете материал', reply_markup=menu11)

    elif call.data == 'Vitality Deluxe':
        msg = bot.send_message(call.message.chat.id, 'Выберете материал', reply_markup=menu12)

    elif call.data == 'Balterio Impressio':
        msg = bot.send_message(call.message.chat.id, 'Выберете материал', reply_markup=menu13)

    elif call.data == 'Balterio Fortissimo':
        msg = bot.send_message(call.message.chat.id, 'Выберете материал', reply_markup=menu14)

    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    if call.data == 'Дуб Бэкстер':
        bot.send_message(call.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Floorwood Estet 4V АС 5/33 (1382х195х12мм)"
                                               "\n Тон/Рулон: 6642 Дуб Бэкстер (1,347 кв.м.)"
                                               "\n Артикул: 6642"
                                               "\n Штрихкод: 4665304110464")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/laminat/Floorwood/Estet/Decors/Dub_bekster_1024.jpg")
    elif call.data == 'Дуб Иберо грей':
        bot.send_message(call.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Floorwood Estet 4V АС 5/33 (1382х195х12мм)"
                                               "\n Тон/Рулон: 7681 Дуб Иберо грей (1,347 кв.м.)"
                                               "\n Артикул: 7681"
                                               "\n Штрихкод: 4665304110600")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/laminat/Floorwood/Estet/Decors/Dub_ibero_grey_1024.jpg")
    elif call.data == 'Дуб Савой':
        bot.send_message(call.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Floorwood Estet 4V АС 5/33 (1382х195х12мм)"
                                               "\n Тон/Рулон: 6741 Дуб Савой (1,347 кв.м.)"
                                               "\n Артикул: 6741"
                                               "\n Штрихкод: 4665304110594")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/laminat/Floorwood/Estet/Decors/Dub_savoy_1024.jpg")
    elif call.data == 'Дуб Ленсингтон':
        bot.send_message(call.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Floorwood Estet 4V АС 5/33 (1382х195х12мм)"
                                               "\n Тон/Рулон: 6687 Дуб Ленсингтон (1,347 кв.м.)"
                                               "\n Артикул: 6687"
                                               "\n Штрихкод: 4665304110471")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/laminat/Floorwood/Estet/Decors/Dub_lensington_1024.jpg")
    elif call.data == 'Дуб Энтони':
        bot.send_message(call.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Floorwood Estet 4V АС 5/33 (1382х195х12мм)"
                                               "\n Тон/Рулон: 6693 Дуб Энтони (1,347 кв.м.)"
                                               "\n Артикул: 6693"
                                               "\n Штрихкод: 4665304110488")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/laminat/Floorwood/Estet/Decors/Dub_entoni_1024.jpg")

    elif call.data == 'Дуб Винсент':
        bot.send_message(call.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Floorwood Epica АС 5/33 (1380х193х8мм)"
                                               "\n Тон/Рулон: D1821 Дуб Винсент ( 2,131 кв.м.)"
                                               "\n Артикул: D1821"
                                               "\n Штрихкод: 4660024290342")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/laminat/Floorwood/Epica/Decors/D1821.jpg")
    elif call.data == 'Дуб Ануари':
        bot.send_message(call.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Floorwood Epica АС 5/33 (1380х193х8мм)"
                                               "\n Тон/Рулон: D1822 Дуб Ануари ( 2,131 кв.м.)"
                                               "\n Артикул: D1822"
                                               "\n Штрихкод: 4660024290359")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/laminat/Floorwood/Epica/Decors/D1822.jpg")
    elif call.data == 'Дуб Грюйер':
        bot.send_message(call.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Floorwood Epica АС 5/33 (1380х193х8мм)"
                                               "\n Тон/Рулон: D1824 Дуб Грюйер ( 2,131 кв.м.)"
                                               "\n Артикул: D1824"
                                               "\n Штрихкод: 4660024290373")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/laminat/Floorwood/Epica/Decors/D1824.jpg")

    elif call.data == 'Divino Oak':
        bot.send_message(call.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Faus Elegance AC6/33 (1182,6х395,7х8 мм)"
                                               "\n Тон/Рулон: S172494 Divino Oak (2,34 кв.м.)"
                                               "\n Артикул: S172494"
                                               "\n Штрихкод: 8426924172494")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/laminat/FAUS/Elegance/decor/S172494%20Divino%20Oak.jpg")
    elif call.data == 'Romance Oak':
        bot.send_message(call.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Faus Elegance AC6/33 (1182,6х395,7х8 мм)"
                                               "\n Тон/Рулон: S172524 Romance Oak (2,34 кв.м.)"
                                               "\n Артикул: S172524"
                                               "\n Штрихкод: 8426924172524")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/laminat/FAUS/Elegance/decor/S172524%20Romance%20Oak.jpg")
    elif call.data == 'Colonial Oak':
        bot.send_message(call.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Faus Elegance AC6/33 (1182,6х395,7х8 мм)"
                                               "\n Тон/Рулон: S173620 Colonial Oak (2,34 кв.м.)"
                                               "\n Артикул: S173620"
                                               "\n Штрихкод: 8426924173620")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/laminat/FAUS/Elegance/decor/S173620%20Colonial%20Oak.jpg")

    elif call.data == 'Дуб шато':
        bot.send_message(call.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Vitality Deluxe 4V АС4/32 (1261х190,5х8 мм)"
                                               "\n Тон/Рулон: 316 Дуб шато ( 2,162 кв.м.)"
                                               "\n Артикул: 400031189"
                                               "\n Штрихкод: 5414084756688")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/laminat/Balterio/Vitality%20Deluxe/decor/316.jpg")
    elif call.data == 'Дуб Амбарный':
        bot.send_message(call.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Vitality Deluxe 4V АС4/32 (1261х190,5х8 мм)"
                                               "\n Тон/Рулон: 328 Дуб Амбарный ( 2,162 кв.м.)"
                                               "\n Артикул: 400031197"
                                               "\n Штрихкод: 5414084756725")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/laminat/Balterio/Vitality%20Deluxe/decor/328-1024.jpg")
    elif call.data == 'Дуб отбеленный':
        bot.send_message(call.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Vitality Deluxe 4V АС4/32 (1261х190,5х8 мм)"
                                               "\n Тон/Рулон: 491 Дуб отбеленный ( 2,162 кв.м.)"
                                               "\n Артикул: 400031214"
                                               "\n Штрихкод: 5414084756800")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/laminat/Balterio/Vitality%20Deluxe/decor/491-1024.jpg")
    elif call.data == 'Орех Селект':
        bot.send_message(call.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Vitality Deluxe 4V АС4/32 (1261х190,5х8 мм)"
                                               "\n Тон/Рулон: 544 Орех Селект ( 2,162 кв.м.)"
                                               "\n Артикул: 400031220"
                                               "\n Штрихкод: 5414084756848")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/laminat/Balterio/Vitality%20Deluxe/decor/544-1024.jpg")
    elif call.data == 'Дуб Лакированный натуральный':
        bot.send_message(call.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Vitality Deluxe 4V АС4/32 (1261х190,5х8 мм)"
                                               "\n Тон/Рулон: 583 Дуб Лакированный натуральный ( 2,162 кв.м.)"
                                               "\n Артикул: 400031235"
                                               "\n Штрихкод: 5414084756985")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/laminat/Balterio/Vitality%20Deluxe/decor/583-1024.jpg")
    elif call.data == 'Дуб белый промасленный':
        bot.send_message(call.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Vitality Deluxe 4V АС4/32 (1261х190,5х8 мм)"
                                               "\n Тон/Рулон: 619 Дуб белый промасленный ( 2,162 кв.м.)"
                                               "\n Артикул: 400031246"
                                               "\n Штрихкод: 5414084757067")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/laminat/Balterio/Vitality%20Deluxe/decor/619-1024.jpg")
    elif call.data == 'Дуб Песчаный':
        bot.send_message(call.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Vitality Deluxe 4V АС4/32 (1261х190,5х8 мм)"
                                               "\n Тон/Рулон: 796 Дуб Песчаный ( 2,162 кв.м.)"
                                               "\n Артикул: 400031324"
                                               "\n Штрихкод: 5414084757180")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/laminat/Balterio/Vitality%20Deluxe/decor/796-1024.jpg")
    elif call.data == 'Дуб Золотой закат':
        bot.send_message(call.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Vitality Deluxe 4V АС4/32 (1261х190,5х8 мм)"
                                               "\n Тон/Рулон: 797 Дуб Золотой закат ( 2,162 кв.м.)"
                                               "\n Артикул: 400031326"
                                               "\n Штрихкод: 5414084757227")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/laminat/Balterio/Vitality%20Deluxe/decor/797-1024.jpg")
    elif call.data == 'Дуб серовато-дымчатый':
        bot.send_message(call.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Vitality Deluxe 4V АС4/32 (1261х190,5х8 мм)"
                                               "\n Тон/Рулон: 900 Дуб серовато-дымчатый ( 2,162 кв.м.)"
                                               "\n Артикул: 400031330"
                                               "\n Штрихкод: 5414084757265")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/laminat/Balterio/Vitality%20Deluxe/decor/900-1024.jpg")
    elif call.data == 'Дуб Шамо':
        bot.send_message(call.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Vitality Deluxe 4V АС4/32 (1261х190,5х8 мм)"
                                               "\n Тон/Рулон: 903 Дуб Шамо ( 2,162 кв.м.)"
                                               "\n Артикул: 400031339"
                                               "\n Штрихкод: 5414084757388")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/laminat/Balterio/Vitality%20Deluxe/decor/903-1024.jpg")

    elif call.data == 'Дуб Wadi Rum':
        bot.send_message(call.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Balterio Impressio AC 4/32 (1261х244х8 мм)"
                                               "\n Тон/Рулон: 928 Дуб Wadi Rum ( 2,4615 кв.м.)"
                                               "\n Артикул: 400030851"
                                               "\n Штрихкод: 5414084716309")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/laminat/Balterio/Impressio/decor/928_IMP.jpg")
    elif call.data == 'Дуб Фраппучино':
        bot.send_message(call.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Balterio Impressio AC 4/32 (1261х244х8 мм)"
                                               "\n Тон/Рулон: 930 Дуб Фраппучино ( 2,4615 кв.м.)"
                                               "\n Артикул: 400030853"
                                               "\n Штрихкод: 5414084716347")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/laminat/Balterio/Impressio/decor/930_IMP.jpg")
    elif call.data == 'Дуб Гарда':
        bot.send_message(call.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Balterio Impressio AC 4/32 (1261х244х8 мм)"
                                               "\n Тон/Рулон: 106 Дуб Гарда ( 2,4615 кв.м.)"
                                               "\n Артикул: 400031419"
                                               "\n Штрихкод: 5414084766038")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/laminat/Balterio/Impressio/decor/106_IMP.jpg")
    elif call.data == 'Дуб Коричнево-Дымчатый':
        bot.send_message(call.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Balterio Impressio AC 4/32 (1261х244х8 мм)"
                                               "\n Тон/Рулон: 929 Дуб Коричнево-Дымчатый ( 2,4615 кв.м.)"
                                               "\n Артикул: 400030852"
                                               "\n Штрихкод: 5414084716323")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/laminat/Balterio/Impressio/decor/929_IMP.jpg")
    elif call.data == 'Дуб с Подпалиной':
        bot.send_message(call.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Balterio Impressio AC 4/32 (1261х244х8 мм)"
                                               "\n Тон/Рулон: 915 Дуб с Подпалиной ( 2,4615 кв.м.)"
                                               "\n Артикул: 400030855"
                                               "\n Штрихкод: 5414084717023")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/laminat/Balterio/Impressio/decor/915_IMP.jpg")
    elif call.data == 'Дуб Каспий':
        bot.send_message(call.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Balterio Impressio AC 4/32 (1261х244х8 мм)"
                                               "\n Тон/Рулон: 142 Дуб Каспий ( 2,4615 кв.м.)"
                                               "\n Артикул: 400031421"
                                               "\n Штрихкод: 5414084766052")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/laminat/Balterio/Impressio/decor/142_IMP.jpg")
    elif call.data == 'Дуб Саванна':
        bot.send_message(call.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Balterio Impressio AC 4/32 (1261х244х8 мм)"
                                               "\n Тон/Рулон: 917 Дуб Саванна ( 2,4615 кв.м.)"
                                               "\n Артикул: 400030857"
                                               "\n Штрихкод: 5414084717047")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/laminat/Balterio/Impressio/decor/917_IMP.jpg")
    elif call.data == 'Дуб Слоновая кость':
        bot.send_message(call.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Balterio Impressio AC 4/32 (1261х244х8 мм)"
                                               "\n Тон/Рулон: 184 Дуб Слоновая кость ( 2,4615 кв.м.)"
                                               "\n Артикул: 400036087"
                                               "\n Штрихкод: 5415125701834")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/laminat/Balterio/Impressio/decor/184_IMP.jpg")

    elif call.data == 'Дуб Фуджи':
        bot.send_message(call.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Balterio Fortissimo New click AC 5/33 (1257х190,5х12 мм)"
                                               "\n Тон/Рулон: 135 Дуб Фуджи (1,4368 кв.м.)"
                                               "\n Артикул: 400036731"
                                               "\n Штрихкод: 5415125712014")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/laminat/Balterio/Fortissimo/decor/135_FOR.jpg")
    elif call.data == 'Дуб Килиманджаро':
        bot.send_message(call.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Balterio Fortissimo New click AC 5/33 (1257х190,5х12 мм)"
                                               "\n Тон/Рулон: 138 Дуб Килиманджаро (1,4368 кв.м.)"
                                               "\n Артикул: 400036733"
                                               "\n Штрихкод: 5415125712038")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/laminat/Balterio/Fortissimo/decor/138_FOR.jpg")
    elif call.data == 'Дуб Гималайя':
        bot.send_message(call.from_user.id, "Название: Ламинат"
                                               "\n Коллекция: Balterio Fortissimo New click AC 5/33 (1257х190,5х12 мм)"
                                               "\n Тон/Рулон: 136 Дуб Гималайя  (1,4368 кв.м.)"
                                               "\n Артикул: 400036732"
                                               "\n Штрихкод: 5415125712021")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/laminat/Balterio/Fortissimo/decor/136_FOR.jpg")
    elif call.data == 'Дуб Этна':
        bot.send_message(call.from_user.id, "Название: Ламинат"
                                            "\n Коллекция: Balterio Fortissimo New click AC 5/33 (1257х190,5х12 мм)"
                                            "\n Тон/Рулон: 139 Дуб Этна  (1,4368 кв.м.)"
                                            "\n Артикул: 400036734"
                                            "\n Штрихкод: 5415125712045")
        bot.send_photo(call.from_user.id,
                       "https://www.stroycity.ru/images/laminat/Balterio/Fortissimo/decor/139_FOR.jpg")


bot.polling(none_stop=True)
