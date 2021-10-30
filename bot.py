import logging
from buttons import numbers_button
from aiogram import Bot, Dispatcher, executor, types
from parse import Asaxiy
from config import TOKEN

logging.basicConfig(level=logging.INFO)

page_number = 1

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):

    await message.answer('Добро пожаловать в asaxiy.uz телеграм бот!!!\n\nкниги - /books\nпомощь - /help')

@dp.message_handler(commands='books')
async def knigi(message: types.Message):
    markup = numbers_button()
    books = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_title()

    await message.answer(f"Книги\n\n1.  {books[0]}\n2.  {books[1]}\n3.  {books[2]}\n4.  {books[3]}\n5.  {books[4]}\n6.  {books[5]}\n7.  {books[6]}\n8.  {books[7]}\n9.  {books[8]}\n10.  {books[9]}\n11.  {books[10]}\n12.  {books[11]}", reply_markup=markup)

@dp.callback_query_handler(text='>>')
async def right(message: types.Message):
    global page_number
    page_number += 1

    markup = numbers_button()
    books = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_title()

    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, f"Книги\n\n1.  {books[0]}\n2.  {books[1]}\n3.  {books[2]}\n4.  {books[3]}\n5.  {books[4]}\n6.  {books[5]}\n7.  {books[6]}\n8.  {books[7]}\n9.  {books[8]}\n10.  {books[9]}\n11.  {books[10]}\n12.  {books[11]}", reply_markup=markup)

@dp.callback_query_handler(text='<<')
async def down(message: types.Message):
    global page_number
    page_number -= 1

    markup = numbers_button()
    books = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_title()

    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, f"Книги\n\n1.  {books[0]}\n2.  {books[1]}\n3.  {books[2]}\n4.  {books[3]}\n5.  {books[4]}\n6.  {books[5]}\n7.  {books[6]}\n8.  {books[7]}\n9.  {books[8]}\n10.  {books[9]}\n11.  {books[10]}\n12.  {books[11]}", reply_markup=markup)

@dp.callback_query_handler(text='1')
async def button_1(message: types.Message):

    title = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_title()[0]
    price = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_price()[0]
    photo = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_photo()[0]

    await bot.send_message(text=f'Картинка - {photo}\nИмя - {title}\nЦена - {price}', chat_id=message.from_user.id)

@dp.callback_query_handler(text='2')
async def button_2(message: types.Message):

    title = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_title()[1]
    price = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_price()[1]
    photo = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_photo()[1]

    await bot.send_message(text=f'Картинка - {photo}\nИмя - {title}\nЦена - {price}', chat_id=message.from_user.id)

@dp.callback_query_handler(text='3')
async def button_3(message: types.Message):

    title = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_title()[2]
    price = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_price()[2]
    photo = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_photo()[2]

    await bot.send_message(text=f'Картинка - {photo}\nИмя - {title}\nЦена - {price}', chat_id=message.from_user.id)

@dp.callback_query_handler(text='4')
async def button_4(message: types.Message):

    title = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_title()[3]
    price = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_price()[3]
    photo = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_photo()[3]

    await bot.send_message(text=f'Картинка - {photo}\nИмя - {title}\nЦена - {price}', chat_id=message.from_user.id)

@dp.callback_query_handler(text='5')
async def button_5(message: types.Message):

    title = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_title()[4]
    price = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_price()[4]
    photo = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_photo()[4]

    await bot.send_message(text=f'Картинка - {photo}\nИмя - {title}\nЦена - {price}', chat_id=message.from_user.id)

@dp.callback_query_handler(text='6')
async def button_6(message: types.Message):

    title = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_title()[5]
    price = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_price()[5]
    photo = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_photo()[5]

    await bot.send_message(text=f'Картинка - {photo}\nИмя - {title}\nЦена - {price}', chat_id=message.from_user.id)

@dp.callback_query_handler(text='7')
async def button_7(message: types.Message):

    title = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_title()[6]
    price = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_price()[6]
    photo = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_photo()[6]

    await bot.send_message(text=f'Картинка - {photo}\nИмя - {title}\nЦена - {price}', chat_id=message.from_user.id)

@dp.callback_query_handler(text='8')
async def button_8(message: types.Message):

    title = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_title()[7]
    price = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_price()[7]
    photo = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_photo()[7]

    await bot.send_message(text=f'Картинка - {photo}\nИмя - {title}\nЦена - {price}', chat_id=message.from_user.id)

@dp.callback_query_handler(text='9')
async def button_9(message: types.Message):

    title = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_title()[8]
    price = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_price()[8]
    photo = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_photo()[8]

    await bot.send_message(text=f'Картинка - {photo}\nИмя - {title}\nЦена - {price}', chat_id=message.from_user.id)

@dp.callback_query_handler(text='10')
async def button_10(message: types.Message):

    title = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_title()[9]
    price = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_price()[9]
    photo = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_photo()[9]

    await bot.send_message(text=f'Картинка - {photo}\nИмя - {title}\nЦена - {price}', chat_id=message.from_user.id)

@dp.callback_query_handler(text='11')
async def button_11(message: types.Message):

    title = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_title()[10]
    price = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_price()[10]
    photo = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_photo()[10]

    await bot.send_message(text=f'Картинка - {photo}\nИмя - {title}\nЦена - {price}', chat_id=message.from_user.id)

@dp.callback_query_handler(text='12')
async def button_12(message: types.Message):

    title = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_title()[11]
    price = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_price()[11]
    photo = Asaxiy(f'https://asaxiy.uz/product/knigi?page={page_number}&per-page=12').get_photo()[11]

    await bot.send_message(text=f'Картинка - {photo}\nИмя - {title}\nЦена - {price}', chat_id=message.from_user.id)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)