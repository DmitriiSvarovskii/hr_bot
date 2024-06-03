from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup
)

from src.lexicons import answers


def create_kb_answer() -> ReplyKeyboardMarkup:
    button1 = KeyboardButton(text=answers.answers['a'])
    button2 = KeyboardButton(text=answers.answers['b'])
    button3 = KeyboardButton(text=answers.answers['cancel'])
    keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=[[button1, button2], [button3]],
        resize_keyboard=True
    )
    return keyboard
