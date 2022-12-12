from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

cb_type = CallbackData("type", "action")
i_btn_water = InlineKeyboardButton("Отдых у моря/океана", callback_data=cb_type.new("Beach Holidays"))
i_btn_ski = InlineKeyboardButton("Отдых на горнолыжном курорте", callback_data=cb_type.new("Ski Resort Holidays"))
i_btn_default = InlineKeyboardButton("Туристическая поездка", callback_data=cb_type.new("Tourism trip"))
ikb_type = InlineKeyboardMarkup(inline_keyboard=[[i_btn_water], [i_btn_ski], [i_btn_default]])

cb_countries = CallbackData("countries", "action")
i_btn_canada = InlineKeyboardButton("Канада", callback_data=cb_countries.new("Canada"))
i_btn_uae = InlineKeyboardButton("ОАЭ", callback_data=cb_countries.new("United Arab Emirates"))
i_btn_usa = InlineKeyboardButton("США", callback_data=cb_countries.new("United States of America"))
i_btn_italy = InlineKeyboardButton("Италия", callback_data=cb_countries.new("Italy"))
i_btn_spain = InlineKeyboardButton("Испания", callback_data=cb_countries.new("Spain"))
i_btn_portugal = InlineKeyboardButton("Португалия", callback_data=cb_countries.new("Portugal"))
i_btn_argentina = InlineKeyboardButton("Аргентина", callback_data=cb_countries.new("Argentina"))
i_btn_poland = InlineKeyboardButton("Польша", callback_data=cb_countries.new("Poland"))
i_btn_czech = InlineKeyboardButton("Чехия", callback_data=cb_countries.new("Czech"))
i_btn_germany = InlineKeyboardButton("Германия", callback_data=cb_countries.new("Germany"))
i_btn_slovakia = InlineKeyboardButton("Словакия", callback_data=cb_countries.new("Slovakia"))
i_btn_hungary = InlineKeyboardButton("Венгрия", callback_data=cb_countries.new("Hungary"))
i_btn_uk = InlineKeyboardButton("Великобритания", callback_data=cb_countries.new("United Kingdom"))
i_btn_finland = InlineKeyboardButton("Финляндия", callback_data=cb_countries.new("Finland"))
i_btn_norway = InlineKeyboardButton("Норвегия", callback_data=cb_countries.new("Norway"))
i_btn_sweden = InlineKeyboardButton("Швеция", callback_data=cb_countries.new("Sweden"))
i_btn_france = InlineKeyboardButton("Франция", callback_data=cb_countries.new("France"))
i_btn_brazil = InlineKeyboardButton("Бразилия", callback_data=cb_countries.new("Brazil"))
i_btn_panama = InlineKeyboardButton("Панама", callback_data=cb_countries.new("Panama"))
i_btn_egypt = InlineKeyboardButton("Египет", callback_data=cb_countries.new("Egypt"))
ikb_countries = InlineKeyboardMarkup(inline_keyboard=[[i_btn_canada, i_btn_uae, i_btn_usa],
                                                      [i_btn_italy, i_btn_spain, i_btn_portugal],
                                                      [i_btn_argentina, i_btn_poland, i_btn_czech],
                                                      [i_btn_germany, i_btn_slovakia, i_btn_hungary],
                                                      [i_btn_uk, i_btn_finland, i_btn_norway],
                                                      [i_btn_sweden, i_btn_france, i_btn_brazil],
                                                      [i_btn_panama, i_btn_egypt]])
