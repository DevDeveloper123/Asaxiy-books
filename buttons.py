from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

def numbers_button():

    markup = InlineKeyboardMarkup(row_width=6)

    markup.insert(
        InlineKeyboardButton(text='1', callback_data='1')
    )
    markup.insert(
        InlineKeyboardButton(text='2', callback_data='2')
    )
    markup.insert(
        InlineKeyboardButton(text='3', callback_data='3')
    )
    markup.insert(
        InlineKeyboardButton(text='4', callback_data='4')
    )
    markup.insert(
        InlineKeyboardButton(text='5', callback_data='5')
    )
    markup.insert(
        InlineKeyboardButton(text='6', callback_data='6')
    )
    markup.insert(
        InlineKeyboardButton(text='7', callback_data='7')
    )
    markup.insert(
        InlineKeyboardButton(text='8', callback_data='8')
    )
    markup.insert(
        InlineKeyboardButton(text='9', callback_data='9')
    )
    markup.insert(
        InlineKeyboardButton(text='10', callback_data='10')
    )
    markup.insert(
        InlineKeyboardButton(text='11', callback_data='11')
    )
    markup.insert(
        InlineKeyboardButton(text='12', callback_data='12')
    )
    markup.insert(
        InlineKeyboardButton(text='<<', callback_data='<<'),
    )
    markup.insert(
        InlineKeyboardButton(text='>>', callback_data='>>'),
    )
    return markup