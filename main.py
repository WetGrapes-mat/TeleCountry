from aiogram.utils import executor
from create_bot import dp
from handlers import cost_living, country_education, country_migration, country_travel, \
    most_dangerous_places, standard_of_living, other


async def on_startup(_):
    print('Бот онлайн')

cost_living.register_handlers(dp)
country_education.register_handlers(dp)
country_migration.register_handlers(dp)
country_travel.register_handlers(dp)
most_dangerous_places.register_handlers(dp)
standard_of_living.register_handlers(dp)
other.register_handlers_other(dp)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


