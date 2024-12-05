from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram import Router, F, Bot, types
from aiogram import exceptions
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import re, io
import asyncio


import database.requests as rq
import telegram_bot.keyboards as kb

chat_id = -1002158934954
bot_username = '@academy_application_bot'
userRouter = Router()
messages = []

class Supply(StatesGroup):
    fullname = State()
    age = State()
    address = State()
    phoneNumber = State()
    photo = State()
    photoUser = State()
    idUser = State()
    messages = State()


@userRouter.message(CommandStart())
async def cmd_start(message: Message):
    msg = await message.answer('Здравствуйте!\nЕсли вы готовы начать свое обучение или получить больше информации, пожалуйста, заполните нашу анкету.\nЭто займёт всего несколько минут.',reply_markup=kb.main)
    messages.append(msg)



@userRouter.callback_query(F.data == "input_application")
async def input_application(callback: CallbackQuery,state: FSMContext):

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

    if callback.message.chat.type == 'private':
        await state.set_state(Supply.phoneNumber)
        msg = await callback.message.answer('Введите ваш номер телефона',reply_markup=kb.cancelButton)    
        messages.append(msg)


@userRouter.message(F.text == "Отменить обращение")
async def cancel(message: Message,state: FSMContext):
    messages.append(message)

    for msg in messages:
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
            
    await state.clear()
    
    msg = await message.answer('Обращение отменено',reply_markup=kb.main)
    messages.append(msg)


@userRouter.callback_query(F.data == "cancel_application")
async def cancel(callback: CallbackQuery,state: FSMContext):

    for msg in messages:
        if((callback.message.from_user.id == msg.from_user.id and msg.chat.id == callback.message.chat.id) or (msg.from_user.id == 7904510825 and msg.chat.id == callback.message.chat.id)):
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

    msg = await callback.message.answer('Обращение отменено',reply_markup=kb.main)  
    messages.append(msg)


@userRouter.callback_query(F.data == "cancel")
async def cancel(callback: CallbackQuery,state: FSMContext):

    for msg in messages:
        if((callback.message.from_user.id == msg.from_user.id and msg.chat.id == callback.message.chat.id) or (msg.from_user.id == 7904510825 and msg.chat.id == callback.message.chat.id)):
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
    
    msg = await callback.message.answer('Обращение отменено',reply_markup=kb.main)
    messages.append(msg)    


 


@userRouter.callback_query(F.data == "re_execute")
async def re_execute(callback: CallbackQuery,state: FSMContext):

    for msg in messages:
        if((callback.message.from_user.id == msg.from_user.id and msg.chat.id == callback.message.chat.id) or (msg.from_user.id == 7904510825 and msg.chat.id == callback.message.chat.id)):
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

    data = await state.get_data()
    
    await rq.delete_application(str(data['idUser']))
    
    await state.clear()
    await state.set_state(Supply.phoneNumber)
    
    msg = await callback.message.answer('Введите ваш номер телефона',reply_markup=kb.cancelButton)
    messages.append(msg)
    


    


@userRouter.message(Supply.phoneNumber)
async def phone_number_handler(message: Message,state: FSMContext):

    for msg in messages:
        if((message.from_user.id == msg.from_user.id and msg.chat.id == message.chat.id) or (msg.from_user.id == 7904510825 and msg.chat.id == message.chat.id)):
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

    pattern = re.compile(r'^(8\d{10}|7\d{10}|\+8\d{10}|\+7\d{10})$')

    if pattern.match(message.text):

        if message.from_user.username is None:
            username = message.from_user.id
        else:
            username = f'@{message.from_user.username}'

        await state.update_data(idUser=username)

        checked = await rq.check_application(message.text)
        my_application = await rq.check_my_application(message.text,username)
        if my_application:
            msg = await message.answer('Ранее вы уже подавали заявку на обучение, хотите переоформить?',reply_markup=kb.refreshApplication)
            messages.append(msg)
            if message.text.__len__() > 0:
                messages.append(message)  
        elif checked and not my_application:
            msg = await message.answer('Заявка с таким номером телефона уже создана другим пользователем',reply_markup=kb.main)
            messages.append(msg)
            if message.text.__len__() > 0:
                messages.append(message) 
            await state.clear()
        else:
            await state.update_data(phoneNumber = message.text)
            await state.set_state(Supply.fullname)
            msg = await message.answer('Пожалуйста, введите ваше ФИО',reply_markup=kb.cancelButton)
            messages.append(msg)
            if message.text.__len__() > 0:
                messages.append(message) 
    else:
        msg = await message.answer('Пожалуйста, введите ваш номер телефона в корректном формате. Например, +79211234567',reply_markup=kb.cancelButton)
        messages.append(msg)
        if message.text.__len__() > 0:
                messages.append(message) 


@userRouter.message(Supply.fullname)
async def name_handler(message: Message,state: FSMContext):
    for msg in messages:
        if((message.from_user.id == msg.from_user.id and msg.chat.id == message.chat.id) or (msg.from_user.id == 7904510825 and msg.chat.id == message.chat.id)):
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

    listSplit =  message.text.split()
    len = listSplit.__len__()
    val = "".join(listSplit).isalpha()

    if val and len >= 3 :
        await state.update_data(fullname = message.text)
        await state.set_state(Supply.age)
        msg = await message.answer('Введите ваш возраст',reply_markup=kb.cancelButton)
        messages.append(msg)
        if message.text.__len__() > 0:
                messages.append(message) 
    else:
        msg = await message.answer('Пожалуйста, введите ваше полное ФИО, соблюдая все пробелы, пример:\nКутузов Владислав Александрович',reply_markup=kb.cancelButton)
        messages.append(msg)
        if message.text.__len__() > 0:
                messages.append(message) 

    



@userRouter.message(Supply.age)
async def age_handler(message: Message,state: FSMContext):
    for msg in messages:
        if((message.from_user.id == msg.from_user.id and msg.chat.id == message.chat.id) or (msg.from_user.id == 7904510825 and msg.chat.id == message.chat.id)):
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

    if message.text.isdigit() and int(message.text) > 0:
        await state.update_data(age = message.text)
        await state.set_state(Supply.address)
        msg = await message.answer('Введите ваш город или регион проживания',reply_markup=kb.cancelButton)
        messages.append(msg)
        if message.text.__len__() > 0:
                messages.append(message) 
    else:
        msg = await message.answer('Пожалуйста, введите ваш полный возраст, в виде числа',reply_markup=kb.cancelButton)
        messages.append(msg)
        if message.text.__len__() > 0:
                messages.append(message) 
    


@userRouter.message(Supply.address)
async def address_handler(message: Message,state: FSMContext):
    for msg in messages:
        if((message.from_user.id == msg.from_user.id and msg.chat.id == message.chat.id) or (msg.from_user.id == 7904510825 and msg.chat.id == message.chat.id)):
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

    if message.text.__len__() >= 1:
        await state.update_data(address = message.text)
        await state.set_state(Supply.photo)
        msg = await message.answer('Пожалуйста, отправьте фото паспорта',reply_markup=kb.cancelButton)
        messages.append(msg)
        if message.text.__len__() > 0:
                messages.append(message) 
    else:
        msg = await message.answer('Пожалуйста, введите ваш город или регион проживания',reply_markup=kb.cancelButton)
        messages.append(msg)
        if message.text.__len__() > 0:
                messages.append(message) 


@userRouter.message(Supply.photo)
async def doc_photo_handler(message: Message,state: FSMContext):

    for msg in messages:
        if((message.from_user.id == msg.from_user.id and msg.chat.id == message.chat.id) or (msg.from_user.id == 7904510825 and msg.chat.id == message.chat.id)):
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

    if not message.photo:
        msg = await message.answer('Пожалуйста, отправьте именно фото паспорта',reply_markup=kb.cancelButton)
        messages.append(msg)
        messages.append(message) 
    else:
        await state.update_data(photo = message.photo[-1])
        await state.set_state(Supply.photoUser)

        msg = await message.answer('Отправьте фото паспорта на фоне с вами',reply_markup=kb.cancelButton)
        messages.append(msg)
        messages.append(message) 




@userRouter.message(Supply.photoUser)
async def user_photo_handler(message: Message,state: FSMContext):
    for msg in messages:
        if((message.from_user.id == msg.from_user.id and msg.chat.id == message.chat.id) or (msg.from_user.id == 7904510825 and msg.chat.id == message.chat.id)):
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

    if not message.photo:
        msg = await message.answer('Пожалуйста, отправьте именно фото паспорта на фоне с вами',reply_markup=kb.cancelButton)
        messages.append(msg)
        messages.append(message) 
    else:
        await state.update_data(photoUser = message.photo[-1])
        data = await state.get_data()

        photo_id =  data['photo'].file_id
        userPhoto_id =  data['photoUser'].file_id


        photoFile = await message.bot.get_file(photo_id)
        userPhotoFile = await message.bot.get_file(userPhoto_id)

        photo_file_data = await message.bot.download_file(photoFile.file_path)
        userPhoto_file_data = await message.bot.download_file(userPhotoFile.file_path)
    

        photo_image_bytes = io.BytesIO(photo_file_data.getvalue()).getvalue()
        userPhoto_image_bytes = io.BytesIO(userPhoto_file_data.getvalue()).getvalue()

        
        await rq.set_application(socialNetworkId=data['idUser'],fullname=str(data['fullname']).lower(),age=int(data['age']),address=str(data['address']).lower(),phoneNumber=int(data['phoneNumber']),docPhoto=photo_image_bytes,userPhoto=userPhoto_image_bytes)

        messages.append(message) 

        for msg in messages:
            if((message.from_user.id == msg.from_user.id and msg.chat.id == message.chat.id) or (msg.from_user.id == 7904510825 and msg.chat.id == message.chat.id)):
                try:
                    await message.chat.delete_message(msg.message_id)
                except exceptions.TelegramBadRequest:
                    messages.remove(msg)
    

        

        media = [
            types.InputMediaPhoto(media=data['photo'].file_id,caption=f'Новый запрос на обучение:\nФИО: {data["fullname"]}\nВозраст: {data["age"]}\nМесто проживания: {data["address"]}\nТелефон: {data["phoneNumber"]}\nID соц.сети: {str(data['idUser'])}',has_spoiler=True),
            types.InputMediaPhoto(media=data['photoUser'].file_id,has_spoiler=True)
        ]
    
        await message.bot.send_media_group(chat_id,media)

        await message.answer('Ваша заявка на обучение успешно отправлена!\nМы свяжемся с вами в ближайшее время.',reply_markup=kb.main)
    
        msgss = []

        for msg in messages:
            msgss.append(msg)

        for msg in msgss:
            if((message.from_user.id == msg.from_user.id and msg.chat.id == message.chat.id) or (msg.from_user.id == 7904510825 and msg.chat.id == message.chat.id)):
                messages.remove(msg)
        
        await state.clear()






@userRouter.message(F.text == '84941867-84cf-409f-b48f-b366c92286f7')
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

    

    if message.from_user.username is None:
        username = message.from_user.id
    else:
        username = f'@{message.from_user.username}'

    user =  await rq.check_role(socialNetworkId=username)
    
    if message.text.__len__() > 0:
        if user is None:
            await rq.add_admin(socialNetworkId=username,role='admin')
            msg = await message.answer('Права администратора выданы!',reply_markup=kb.adminAction)
            messages.append(msg)
            messages.append(message)
            await state.clear()
        elif user.role == 'admin':
            msg = await message.answer('Вы уже обладаете правами администратора',reply_markup=kb.cancelActionAdmin)
            messages.append(msg)
            messages.append(message)
    else:
        msg = await message.answer('Введите корректные данные',reply_markup=kb.cancelActionAdmin)
        messages.append(msg)
        messages.append(message)
