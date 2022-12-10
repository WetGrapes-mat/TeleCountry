from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

cb_faculty = CallbackData("faculty", "action")
i_btn_arts = InlineKeyboardButton("Искусство", callback_data=cb_faculty.new(1))
i_btn_it = InlineKeyboardButton("IT", callback_data=cb_faculty.new(2))
i_btn_education = InlineKeyboardButton("Общее образование", callback_data=cb_faculty.new(3))
i_btn_science = InlineKeyboardButton("Науки", callback_data=cb_faculty.new(4))
i_btn_social = InlineKeyboardButton("Социальные науки", callback_data=cb_faculty.new(5))
i_btn_engineering = InlineKeyboardButton("Инженерия", callback_data=cb_faculty.new(6))
i_btn_medicine = InlineKeyboardButton("Медицина", callback_data=cb_faculty.new(7))
i_btn_law = InlineKeyboardButton("Юриспруденция", callback_data=cb_faculty.new(8))
i_btn_forestry = InlineKeyboardButton("Агробиология", callback_data=cb_faculty.new(9))
i_btn_economics = InlineKeyboardButton("Экономика и бизнес", callback_data=cb_faculty.new(10))
i_btn_architecture = InlineKeyboardButton("Архитектура", callback_data=cb_faculty.new(11))
ikb_faculty = InlineKeyboardMarkup(inline_keyboard=[[i_btn_arts, i_btn_it, i_btn_education, i_btn_science,
                                                     i_btn_social, i_btn_engineering, i_btn_medicine, i_btn_law,
                                                     i_btn_forestry, i_btn_economics, i_btn_architecture]])


cb_program = CallbackData("program", "action")
i_btn_foundation = InlineKeyboardButton("Довузовские курсы", callback_data=cb_program.new(1))
i_btn_underdegree = InlineKeyboardButton("Бакалавриат", callback_data=cb_program.new(2))
i_btn_magistracy = InlineKeyboardButton("Магистратура", callback_data=cb_program.new(3))
i_btn_mba = InlineKeyboardButton("MBA", callback_data=cb_program.new(4))
ikb_program = InlineKeyboardMarkup(inline_keyboard=[[i_btn_foundation, i_btn_underdegree, i_btn_magistracy, i_btn_mba]])

cb_hostel = CallbackData("hostel", "action")
i_btn_yes_hostel = InlineKeyboardButton("Нужно", callback_data=cb_hostel.new(True))
i_btn_no_hostel = InlineKeyboardButton("Не нужно", callback_data=cb_hostel.new(False))
ikb_hostel = InlineKeyboardMarkup(inline_keyboard=[[i_btn_yes_hostel, i_btn_no_hostel]])

# добавить ввод стоимости обучения с клавиатуры
cb_cost = CallbackData("cost", "action")
