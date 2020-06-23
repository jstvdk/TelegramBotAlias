from aiogram.types import Message, CallbackQuery
from keyboards.inline.game_buttons import host_keyboard, host_help
from loader import dp
from app import redis_control
from data_base_working import get_word

CURRENT_WORD = 0   # variable for saving current game word
HOST_NAME = 0   # variable for saving narrator name


@dp.message_handler(commands=['start_alias'])
async def start_game(message: Message):
    await message.answer(text='Виберіть ведучого що б почати гру, якщо під час гри виникнуть запитання, напишіть /help',
                         reply_markup=host_keyboard)


@dp.message_handler(commands=['my_stats'])
async def my_stats(message: Message):
    try:
        convert_score = redis_control.get(message.from_user.first_name).decode('utf-8')
        await message.answer(text=f"Кількість правильних відповідей {message.from_user.first_name} = {convert_score}")
    except AttributeError:
        await message.answer(text='У вас ще немає статистики')


@dp.message_handler(commands=['help'])
async def helper(message: Message):
    global HOST_NAME
    await message.answer(text=f"{HOST_NAME} пояснює слово, для зміни ведучого напишіть /start", reply_markup=host_help)


# ___ callback section ___________

@dp.callback_query_handler(text=['be_host'])
async def get_host(call: CallbackQuery):
    global HOST_NAME
    HOST_NAME = call.from_user.first_name
    global CURRENT_WORD
    CURRENT_WORD = get_word()
    await call.answer(text=CURRENT_WORD, show_alert=True)
    await call.message.edit_reply_markup()


@dp.callback_query_handler(text='show_word')
async def show_word(call: CallbackQuery):
    global HOST_NAME
    global CURRENT_WORD
    if call.from_user.first_name == HOST_NAME:
        await call.answer(text=CURRENT_WORD, show_alert=True)
    else:
        await call.answer(text="Ач який розумний найшовся, думай сам", show_alert=True)


@dp.callback_query_handler(text='next_word')
async def show_word(call: CallbackQuery):
    global HOST_NAME
    global CURRENT_WORD
    if call.from_user.first_name == HOST_NAME:
        CURRENT_WORD = get_word()
        await call.answer(text=CURRENT_WORD, show_alert=True)
    else:
        await call.answer(text="А це не в твоїй юрисдикції, фурфантя ти мале", show_alert=True)


# function that check if word is correct
@dp.message_handler()
async def check_word(message: Message):
    global HOST_NAME
    cur_word = message.text
    if cur_word.lower() == CURRENT_WORD:
        if message.from_user.first_name in redis_control:
            redis_control.incr(message.from_user.first_name, 1)
        else:
            redis_control.set(message.from_user.first_name, 1)
        convert_score = redis_control.get(message.from_user.first_name).decode('utf-8')

        await message.answer(text=f'Вітаємо {message.from_user.first_name}! Це правильне слово. '
                                  f'Кількість відгаданних слів = {convert_score} \n'
                                  f'Для нової гри напишіть /start')
        HOST_NAME = 0
