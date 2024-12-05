from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command, BaseFilter
from aiogram import Router, F, Bot
from aiogram.fsm.state import State, StatesGroup
from aiogram import exceptions
from aiogram.fsm.context import FSMContext
import re, io


import database.requests as rq
import telegram_bot.keyboards as kb


messages = []

class isAdmin(BaseFilter):
    def init(self) -> None:
        pass

    async def __call__(self, message: Message, bot: Bot) -> bool:
        username = f'@{message.from_user.username}'
        if username is None:
            username = message.from_user.id

        user = await rq.check_role(socialNetworkId=username)

        if user is None:
            return False
        elif not user is None and user.role == 'admin':
            return True

adminRouter = Router()
adminRouter.message.filter(isAdmin())


class adminState(StatesGroup):
    add_user = State()
    remove_user = State()


@adminRouter.message(Command('admin'))
async def cmd_start(message: Message):
    msg = await message.answer('Здравствуйте, выберите действие.',reply_markup=kb.adminAction)
    messages.append(msg)

@adminRouter.callback_query(F.data == 'add_employee')
async def add_employee(callback: CallbackQuery, state: FSMContext):

    for msg in messages:
        if(callback.message.from_user.id == msg.from_user.id and msg.chat.id == callback.message.chat.id):
            try:
                await callback.message.chat.delete_message(msg.message_id)
            except exceptions.TelegramBadRequest:
                messages.remove(msg)
        elif (msg.from_user.id == 7904510825 and msg.chat.id == callback.message.chat.id):
            try:
                await callback.message.chat.delete_message(msg.message_id)
            except exceptions.TelegramBadRequest:
                messages.remove(msg)

    
    msgs = []

    for msg in messages:
        msgs.append(msg)

    for msg in msgs:
        if((callback.message.from_user.id == msg.from_user.id and msg.chat.id == callback.message.chat.id) or (msg.from_user.id == 7904510825 and msg.chat.id == callback.message.chat.id)):
            messages.remove(msg)

    msg = await callback.message.answer('Введите telegram юзернейм или id пользователя',reply_markup=kb.cancelActionAdmin)
    await state.set_state(adminState.add_user)
    messages.append(msg)


@adminRouter.callback_query(F.data == 'cancel_action_admin')
async def filter_applications(callback: CallbackQuery,state: FSMContext):

    for msg in messages:
        if(callback.message.from_user.id == msg.from_user.id and msg.chat.id == callback.message.chat.id):
            try:
                await callback.message.chat.delete_message(msg.message_id)
            except exceptions.TelegramBadRequest:
                messages.remove(msg)
        elif (msg.from_user.id == 7904510825 and msg.chat.id == callback.message.chat.id):
            try:
                await callback.message.chat.delete_message(msg.message_id)
            except exceptions.TelegramBadRequest:
                messages.remove(msg)

    
    msgs = []

    for msg in messages:
        msgs.append(msg)

    for msg in msgs:
        if((callback.message.from_user.id == msg.from_user.id and msg.chat.id == callback.message.chat.id) or (msg.from_user.id == 7904510825 and msg.chat.id == callback.message.chat.id)):
            messages.remove(msg)


    await state.clear()
    msg = await callback.message.answer('Выберите действие',reply_markup=kb.adminAction)
    messages.append(msg)


@adminRouter.callback_query(F.data == 'remove_employee')
async def add_employee(callback: CallbackQuery, state: FSMContext):
    for msg in messages:
        if(callback.message.from_user.id == msg.from_user.id and msg.chat.id == callback.message.chat.id):
            try:
                await callback.message.chat.delete_message(msg.message_id)
            except exceptions.TelegramBadRequest:
                messages.remove(msg)
        elif (msg.from_user.id == 7904510825 and msg.chat.id == callback.message.chat.id):
            try:
                await callback.message.chat.delete_message(msg.message_id)
            except exceptions.TelegramBadRequest:
                messages.remove(msg)

    
    msgs = []

    for msg in messages:
        msgs.append(msg)

    for msg in msgs:
        if((callback.message.from_user.id == msg.from_user.id and msg.chat.id == callback.message.chat.id) or (msg.from_user.id == 7904510825 and msg.chat.id == callback.message.chat.id)):
            messages.remove(msg)

    msg = await callback.message.answer('Введите telegram юзернейм или id пользователя',reply_markup=kb.cancelActionAdmin)
    await state.set_state(adminState.remove_user)
    messages.append(msg)


@adminRouter.message(adminState.add_user)
async def add_employee(message: Message, state: FSMContext):

    for msg in messages:
        if(message.from_user.id == msg.from_user.id and msg.chat.id == message.chat.id):
            try:
                await message.chat.delete_message(msg.message_id)
            except exceptions.TelegramBadRequest:
                messages.remove(msg)
        elif (msg.from_user.id == 7904510825 and msg.chat.id == message.chat.id):
            try:
                await message.chat.delete_message(msg.message_id)
            except exceptions.TelegramBadRequest:
                messages.remove(msg)

    
    msgs = []

    for msg in messages:
        msgs.append(msg)

    for msg in msgs:
        if((message.from_user.id == msg.from_user.id and msg.chat.id == message.chat.id) or (msg.from_user.id == 7904510825 and msg.chat.id == message.chat.id)):
            messages.remove(msg)

    

    if message.text.__len__() > 0:
        if message.text[0] != '@':
            user =  await rq.check_role(socialNetworkId='@' + message.text)
        else:
            user =  await rq.check_role(socialNetworkId=message.text)

        if user is None:
            if message.text[0] != '@':
                await rq.add_employee(socialNetworkId= '@' + message.text,role='employee')
                msg = await message.answer('Сотрудник успешно добавлен!',reply_markup=kb.adminAction)
                messages.append(msg)
                messages.append(message)
                await state.clear()
            else:
                await rq.add_employee(socialNetworkId=message.text,role='employee')
                msg = await message.answer('Сотрудник успешно добавлен!',reply_markup=kb.adminAction)
                messages.append(msg)
                messages.append(message)
                await state.clear()
        else: 
            msg = await message.answer('Сотрудник уже зарегистрирован',reply_markup=kb.cancelActionAdmin)
            messages.append(msg)
            messages.append(message)
    else:
        msg = await message.answer('Введите корректные данные',reply_markup=kb.cancelActionAdmin)
        messages.append(msg)
        messages.append(message)



@adminRouter.message(adminState.remove_user)
async def remove_employee(message: Message, state: FSMContext):

    for msg in messages:
        if(message.from_user.id == msg.from_user.id and msg.chat.id == message.chat.id):
            try:
                await message.chat.delete_message(msg.message_id)
            except exceptions.TelegramBadRequest:
                messages.remove(msg)
        elif (msg.from_user.id == 7904510825 and msg.chat.id == message.chat.id):
            try:
                await message.chat.delete_message(msg.message_id)
            except exceptions.TelegramBadRequest:
                messages.remove(msg)

    
    msgs = []

    for msg in messages:
        msgs.append(msg)

    for msg in msgs:
        if((message.from_user.id == msg.from_user.id and msg.chat.id == message.chat.id) or (msg.from_user.id == 7904510825 and msg.chat.id == message.chat.id)):
            messages.remove(msg)

    if message.text.__len__() > 0:
        if message.text[0] != '@':
            user =  await rq.check_role(socialNetworkId='@' + message.text)
        else:
            user =  await rq.check_role(socialNetworkId=message.text)
        

        if user is None:
            msg = await message.answer('Такого сотрудника нет',reply_markup=kb.cancelActionAdmin)
            messages.append(msg)
            messages.append(message)
        else:
            if message.text[0] != '@':
                await rq.remove_employee(socialNetworkId='@' + message.text,role='employee')
                msg = await message.answer('Сотрудник успешно удалён!',reply_markup=kb.adminAction)
                messages.append(msg)
                messages.append(message)
                await state.clear()
            else:
                await rq.remove_employee(socialNetworkId=message.text,role='employee')
                msg = await message.answer('Сотрудник успешно удалён!',reply_markup=kb.adminAction)
                messages.append(msg)
                messages.append(message)
                await state.clear()
    else:
        msg = await message.answer('Введите корректные данные',reply_markup=kb.cancelActionAdmin)
        messages.append(msg)
        messages.append(message)