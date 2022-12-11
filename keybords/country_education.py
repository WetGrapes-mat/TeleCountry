from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from neo4j_country_db import country_education_db as db

cb_faculty = CallbackData("faculty", "action")
i_btn_arts = InlineKeyboardButton("Искусство", callback_data=cb_faculty.new("Faculty of Arts"))
i_btn_it = InlineKeyboardButton("IT", callback_data=cb_faculty.new("Faculty of Computer Engineering and Software"))
i_btn_education = InlineKeyboardButton("Общее образование", callback_data=cb_faculty.new("Faculty of Education"))
i_btn_science = InlineKeyboardButton("Науки", callback_data=cb_faculty.new("Faculty of Science"))
i_btn_social = InlineKeyboardButton("Социальные науки", callback_data=cb_faculty.new("Faculty of Social Sciences"))
i_btn_engineering = InlineKeyboardButton("Инженерия", callback_data=cb_faculty.new("Faculty of Engineering"))
i_btn_medicine = InlineKeyboardButton("Медицина", callback_data=cb_faculty.new("Faculty of Medicine"))
i_btn_law = InlineKeyboardButton("Юриспруденция", callback_data=cb_faculty.new("Faculty of Law"))
i_btn_forestry = InlineKeyboardButton("Агробиология", callback_data=cb_faculty.new("Faculty of Forestry"))
i_btn_economics = InlineKeyboardButton("Экономика и бизнес", callback_data=cb_faculty.new("Faculty of Business"))
i_btn_architecture = InlineKeyboardButton("Архитектура", callback_data=cb_faculty.new("Faculty of Architecture"))
ikb_faculty = InlineKeyboardMarkup(inline_keyboard=[[i_btn_arts, i_btn_it, i_btn_education], [i_btn_science,
                                                     i_btn_social, i_btn_engineering], [i_btn_medicine, i_btn_law,
                                                     i_btn_forestry], [i_btn_economics, i_btn_architecture]])


cb_program = CallbackData("program", "action")
i_btn_foundation = InlineKeyboardButton("Довузовские курсы", callback_data=cb_program.new("Foundation"))
i_btn_underdegree = InlineKeyboardButton("Бакалавриат", callback_data=cb_program.new("Undergraduate"))
i_btn_magistracy = InlineKeyboardButton("Магистратура", callback_data=cb_program.new("Magistracy"))
i_btn_mba = InlineKeyboardButton("MBA", callback_data=cb_program.new("MBA"))
i_btn_doctoral = InlineKeyboardButton("Докторантура", callback_data=cb_program.new("Doctoral"))
ikb_program = InlineKeyboardMarkup(inline_keyboard=[[i_btn_foundation, i_btn_underdegree], [i_btn_magistracy, i_btn_mba],
                                                     [i_btn_doctoral]])

cb_hostel = CallbackData("hostel", "action")
i_btn_yes_hostel = InlineKeyboardButton("Нужно", callback_data=cb_hostel.new("Yes"))
i_btn_no_hostel = InlineKeyboardButton("Не нужно", callback_data=cb_hostel.new("No"))
ikb_hostel = InlineKeyboardMarkup(inline_keyboard=[[i_btn_yes_hostel, i_btn_no_hostel]])

delta = (db.find_max_cost() - db.find_min_cost()) // 3
cb_cost = CallbackData("cost", "action")
i_btn_1 = InlineKeyboardButton("1", callback_data=cb_cost.new(db.find_min_cost() + delta))
i_btn_2 = InlineKeyboardButton("2", callback_data=cb_cost.new(db.find_min_cost() + 2 * delta))
i_btn_3 = InlineKeyboardButton("3", callback_data=cb_cost.new(db.find_max_cost()))
ikb_cost = InlineKeyboardMarkup(inline_keyboard=[[i_btn_1, i_btn_2, i_btn_3]])
