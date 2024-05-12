import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import CommandObject, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from aiogram.utils.formatting import Bold, Text
from database import connection
from settings import HOST, TG_TOKEN

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TG_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


class UserStatus(StatesGroup):
    ANON = State()
    REGISTRED = State()


@dp.message(CommandStart(
    deep_link=True
))
async def start(message: Message, command: CommandObject, state: FSMContext):
    args = command.args
    if args:
        username = message.from_user.username
        cur = connection.cursor()
        cur.execute(
            "UPDATE users a "
            f"SET tg_username = '{username}' "
            f"WHERE tg_token='{args}' "
            "RETURNING a.*")
        result = cur.fetchone()
        if result:
            connection.commit()
            await message.answer('Аккаунт привязан!')
            await message.answer(
                'Вы можете отправить любое сообщение'
                ' и я сообщу вам количество символов в нем.'
            )
            await state.set_state(UserStatus.REGISTRED)
        return
    await message.answer(
        f'Зарегистрируйтесь для работы с ботом по ссылке: {HOST}/user'
    )
    await state.set_state(UserStatus.ANON)


@dp.message(UserStatus.REGISTRED, F.text)
async def send_message_len(message: Message):
    content = Text(
        Bold('Символов в сообщении: '),
        len(message.text.strip().replace('\n', '').replace(' ', ''))
    )
    await message.answer(
        **content.as_kwargs()
    )


@dp.message(F.text)
async def not_auth(message: Message, state: FSMContext):
    username = message.from_user.username
    cur = connection.cursor()
    cur.execute(
        "SELECT tg_username "
        "FROM users "
        f"WHERE tg_username='{username}'"
    )
    result = cur.fetchone()
    if result:
        await state.set_state(UserStatus.REGISTRED)
        await send_message_len(message)
    else:
        await message.answer(
            f'Зарегистрируйтесь для работы с ботом по ссылке: {HOST}user'
        )


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
