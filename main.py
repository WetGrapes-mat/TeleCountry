from aiogram.utils import executor
from create_bot import dp
from handlers import cost_living, country_education, country_migration, country_travel, \
    most_dangerous_places, standard_of_living, other
from neo4j_country_db import cost_living_db, country_education_db, country_migration_db, country_travel_db, \
    most_dangerous_places_db, standard_of_living_db


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
    cost_living_db.close()
    country_education_db.close()
    country_migration_db.close()
    country_travel_db.close()
    most_dangerous_places_db.close()
    standard_of_living_db.close()


