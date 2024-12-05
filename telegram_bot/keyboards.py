from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Заполнить анкету',callback_data='input_application')]])

cancelButton = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Отменить обращение',callback_data='cancel_application')]])


refreshApplication = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Переоформить',callback_data='re_execute'),InlineKeyboardButton(text='Отменить обращение',callback_data='cancel')]])

refreshApplicationByEmpl = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Переоформить',callback_data='re_execute_empl'),InlineKeyboardButton(text='Отменить обращение',callback_data='cancel_empl')]])

getApplication = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Посмотреть заявки',callback_data='check_application')],
                                                       [InlineKeyboardButton(text='Добавить заявку',callback_data='add_application_by_employee'),
                                                        InlineKeyboardButton(text='Удалить заявку',callback_data='delete_application_by_employee')
                                                        ]])

getFilteredApplication = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сортировать по региону',callback_data='get_by_region_application')],
    [InlineKeyboardButton(text='Получить все',callback_data='get_application')],
    [InlineKeyboardButton(text='Отмена',callback_data='cancel_employee')]
    ])

cancelActionEmployee = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Отмена',callback_data='cancel_action_employee')]])

cancelActionAdmin = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Отмена',callback_data='cancel_action_admin')]])

adminAction = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Добавить сотрудника',callback_data='add_employee'),InlineKeyboardButton(text='Удалить сотрудника',callback_data='remove_employee')]])