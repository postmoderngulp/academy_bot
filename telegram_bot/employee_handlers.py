from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command, BaseFilter
from aiogram import Router, F, Bot, types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import re, io, os
from aiogram import exceptions
from openpyxl import Workbook
from aiogram.types import FSInputFile


import database.requests as rq
import telegram_bot.keyboards as kb


chat_id = -1002158934954


class isEmployee(BaseFilter):
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
        elif not user is None and user.role == 'employee':
            return True


employeeRouter = Router()
employeeRouter.message.filter(isEmployee())

messages = []





class EmployeeState(StatesGroup):
    region = State()
    startAge = State()
    endAge = State()
    socialNetworkId = State()
    fullname = State()
    age = State()
    address = State()
    phoneNumber = State()
    photo = State()
    photoUser = State()
    messages = State()
    cancel = State()



@employeeRouter.message(Command('employee'))
async def cmd_start(message: Message):
    msg = await message.answer('Здравствуйте, здесь вы можете посмотреть заявки на обучение.',reply_markup=kb.getApplication)
    messages.append(msg)
    


@employeeRouter.callback_query(F.data == 'check_application')
async def filter_applications(callback: CallbackQuery):
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

    msg = await callback.message.answer('Получите необходимые вам заявки',reply_markup=kb.getFilteredApplication)
    messages.append(msg)



@employeeRouter.callback_query(F.data == 'cancel_employee')
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
    msg = await callback.message.answer('Посмотреть заявки на обучение',reply_markup=kb.getApplication)
    messages.append(msg)



@employeeRouter.callback_query(F.data == 'cancel_action_employee')
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
    msg = await callback.message.answer('Посмотреть заявки на обучение',reply_markup=kb.getApplication)
    messages.append(msg)



@employeeRouter.callback_query(F.data == "cancel_empl")
async def cancel(callback: CallbackQuery,state: FSMContext):
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
    
    msg = await callback.message.answer('Обращение отменено',reply_markup=kb.getApplication)
    messages.append(msg)    



@employeeRouter.callback_query(F.data == 'get_by_region_application')
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

    await state.set_state(EmployeeState.region)
    msg = await callback.message.answer('Введите регион или город',reply_markup=kb.cancelActionEmployee)
    messages.append(msg)



@employeeRouter.message(EmployeeState.region)
async def filter_applications(message: Message,state: FSMContext):
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

    if message.text.__len__() >= 1:
        applications =  await rq.get_applications_byRegion(message.text.lower())
        if applications.__len__() > 0:
            workbook = Workbook()
            sheet = workbook.active
            sheet.title = "Aplications Data"

            # Sample data
            data = [
                ('ФИО', 'Возраст', 'Регион','Телефон'),
             ]

            for application in applications:
                data.append((application.fullname,application.age,application.address,str(application.phoneNumber)))

            # Write data to the Excel sheet
            for row in data:
                sheet.append(row)

            # Save the workbook to a file
            excel_filename = 'Заявки на обучение.xlsx'
            workbook.save(excel_filename)

            # Create an InputFile instance from the file path
            file = FSInputFile(excel_filename)

            # Sending the document
            msg = await message.answer_document(file,reply_markup=kb.getApplication)
            
            messages.append(msg)
            messages.append(message)

            # Clean up the created file
            os.remove(excel_filename)
            await state.clear()
        else:
            msg = await message.answer('Заявок с таким регионом нет',reply_markup=kb.cancelActionEmployee)
            messages.append(msg)
            messages.append(message)
    else:
        msg = await message.answer('Пожалуйста, введите город или регион корректно')
        messages.append(msg)
        messages.append(message)
    


@employeeRouter.callback_query(F.data == 'delete_application_by_employee')
async def delete_application(callback: CallbackQuery,state: FSMContext):
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

    msg = await callback.message.answer('Введите id социальной сети пользователя, заявку которого нужно удалить',reply_markup=kb.cancelActionEmployee)
    await state.set_state(EmployeeState.socialNetworkId)
    messages.append(msg)




@employeeRouter.message(EmployeeState.socialNetworkId)
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

    if message.text[0] != '@':
        application =  await rq.check_application_byId(socialNetworkId='@' + message.text)
    else:
        application =  await rq.check_application_byId(socialNetworkId=message.text)

    if not application:
        msg = await message.answer('Такой заявки нет',reply_markup=kb.getApplication)
        messages.append(msg)
    else:
        if message.text[0] != '@':
            await rq.delete_application(socialNetworkId='@' + message.text)
            msg = await message.answer('Заявка успешно удалена!',reply_markup=kb.getApplication)
            messages.append(msg)
            await state.clear()
        else:
            await rq.delete_application(message.text)
            msg = await message.answer('Заявка успешно удалена!',reply_markup=kb.getApplication)
            messages.append(msg)
            await state.clear()



@employeeRouter.callback_query(F.data == 'add_application_by_employee')
async def add_application(callback: CallbackQuery,state: FSMContext):
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

    msg = await callback.message.answer('Введите номер телефона пользователя',reply_markup=kb.cancelActionEmployee)
    messages.append(msg)
    await state.set_state(EmployeeState.phoneNumber)


@employeeRouter.message(EmployeeState.phoneNumber)
async def phone_number_handler(message: Message,state: FSMContext):

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

    pattern = re.compile(r'^(8\d{10}|7\d{10}|\+8\d{10}|\+7\d{10})$')

    if pattern.match(message.text):
        if message.from_user.username is None:
            username = message.from_user.id
        else:
            username = f'@{message.from_user.username}'

        await state.update_data(socialNetworkId=username)

        checked = await rq.check_application(message.text)
        my_application = await rq.check_my_application(message.text,username)
        if my_application:
            msg = await message.answer('Ранее заявка на обучение уже подавалась, хотите переоформить?',reply_markup=kb.refreshApplicationByEmpl)
            messages.append(msg)
            if message.text.__len__() > 0:
                messages.append(message)  
        elif checked and not my_application:
            msg = await message.answer('Заявка с таким номером телефона уже создана другим пользователем',reply_markup=kb.getApplication)
            messages.append(msg)
            if message.text.__len__() > 0:
                messages.append(message) 
            await state.clear()
        else:
            await state.update_data(phoneNumber = message.text)
            await state.set_state(EmployeeState.fullname)
            msg = await message.answer('Пожалуйста, введите ФИО',reply_markup=kb.cancelActionEmployee)
            messages.append(msg)
            if message.text.__len__() > 0:
                messages.append(message) 
    else:
        msg = await message.answer('Пожалуйста, введите номер телефона в корректном формате. Например, +79211234567',reply_markup=kb.cancelActionEmployee)
        messages.append(msg)
        if message.text.__len__() > 0:
                messages.append(message) 




@employeeRouter.callback_query(F.data == "re_execute_empl")
async def re_execute(callback: CallbackQuery,state: FSMContext):

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

    data = await state.get_data()
    
    await rq.delete_application(str(data['socialNetworkId']))
    
    await state.clear()
    await state.set_state(EmployeeState.phoneNumber)
    
    msg = await callback.message.answer('Введите номер телефона',reply_markup=kb.cancelActionEmployee)
    messages.append(msg)






@employeeRouter.message(EmployeeState.fullname)
async def name_handler(message: Message,state: FSMContext):
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

    listSplit =  message.text.split()
    len = listSplit.__len__()
    val = "".join(listSplit).isalpha()

    if val and len >= 3 :
        await state.update_data(fullname = message.text)
        await state.set_state(EmployeeState.age)
        msg = await message.answer('Введите возраст',reply_markup=kb.cancelActionEmployee)
        messages.append(msg)
        if message.text.__len__() > 0:
                messages.append(message) 
    else:
        msg = await message.answer('Пожалуйста, введите полное ФИО, соблюдая все пробелы, пример:\nКутузов Владислав Александрович',reply_markup=kb.cancelActionEmployee)
        messages.append(msg)
        if message.text.__len__() > 0:
                messages.append(message) 

    



@employeeRouter.message(EmployeeState.age)
async def age_handler(message: Message,state: FSMContext):
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

    if message.text.isdigit() and int(message.text) > 0:
        await state.update_data(age = message.text)
        await state.set_state(EmployeeState.address)
        msg = await message.answer('Введите город или регион проживания',reply_markup=kb.cancelActionEmployee)
        messages.append(msg)
        if message.text.__len__() > 0:
                messages.append(message) 
    else:
        msg = await message.answer('Пожалуйста, введите полный возраст, в виде числа',reply_markup=kb.cancelActionEmployee)
        messages.append(msg)
        if message.text.__len__() > 0:
                messages.append(message) 
    


@employeeRouter.message(EmployeeState.address)
async def address_handler(message: Message,state: FSMContext):
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

    if message.text.__len__() >= 1:
        await state.update_data(address = message.text)
        await state.set_state(EmployeeState.photo)
        msg = await message.answer('Пожалуйста, отправьте фото паспорта',reply_markup=kb.cancelActionEmployee)
        messages.append(msg)
        if message.text.__len__() > 0:
                messages.append(message) 
    else:
        msg = await message.answer('Пожалуйста, введите город или регион проживания',reply_markup=kb.cancelActionEmployee)
        messages.append(msg)
        if message.text.__len__() > 0:
                messages.append(message) 


@employeeRouter.message(EmployeeState.photo)
async def doc_photo_handler(message: Message,state: FSMContext):

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

    if not message.photo:
        msg = await message.answer('Пожалуйста, отправьте именно фото паспорта',reply_markup=kb.cancelActionEmployee)
        messages.append(msg)
        messages.append(message) 
    else:
        await state.update_data(photo = message.photo[-1])
        await state.set_state(EmployeeState.photoUser)

        msg = await message.answer('Отправьте фото паспорта на фоне с пользователем',reply_markup=kb.cancelActionEmployee)
        messages.append(msg)
        messages.append(message) 




@employeeRouter.message(EmployeeState.photoUser)
async def user_photo_handler(message: Message,state: FSMContext):
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

    if not message.photo:
        msg = await message.answer('Пожалуйста, отправьте именно фото паспорта на фоне с вами',reply_markup=kb.cancelActionEmployee)
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

        
        await rq.set_application(socialNetworkId=data['socialNetworkId'],fullname=str(data['fullname']).lower(),age=int(data['age']),address=str(data['address']).lower(),phoneNumber=int(data['phoneNumber']),docPhoto=photo_image_bytes,userPhoto=userPhoto_image_bytes)

        messages.append(message) 

        

        media = [
            types.InputMediaPhoto(media=data['photo'].file_id,caption=f'Новый запрос на обучение:\nФИО: {data["fullname"]}\nВозраст: {data["age"]}\nМесто проживания: {data["address"]}\nТелефон: {data["phoneNumber"]}\nID соц.сети: {str(data['socialNetworkId'])}',has_spoiler=True),
            types.InputMediaPhoto(media=data['photoUser'].file_id,has_spoiler=True)
        ]
    
        await message.bot.send_media_group(chat_id,media)

        await message.answer('Заявка успешно создана!',reply_markup=kb.getApplication)
    
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

        await state.clear()


@employeeRouter.callback_query(F.data == 'get_application')
async def get_application(callback: CallbackQuery,state: FSMContext):
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

    applications =  await rq.get_applications()
    if applications.__len__() > 0:
        # Sample data
        data = [
            ('ФИО', 'Возраст', 'Регион','Телефон'),
        ]
        
        for application in applications:
            data.append((application.fullname,application.age,application.address,str(application.phoneNumber)))

    
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Aplications Data"


        # Write data to the Excel sheet
        for row in data:
            sheet.append(row)

        # Save the workbook to a file
        excel_filename = 'Заявки на обучение.xlsx'
        workbook.save(excel_filename)

        # Create an InputFile instance from the file path
        file = FSInputFile(excel_filename)

        # Sending the document
        msg = await callback.message.answer_document(file,reply_markup=kb.getApplication)
        messages.append(msg)

        # Clean up the created file
        os.remove(excel_filename)
        await state.clear()
    else:
        msg = await callback.message.answer("Заявок нет",reply_markup=kb.cancelActionEmployee)
        messages.append(msg)    
    
