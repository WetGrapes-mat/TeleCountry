from neo4j_country_db.requests import Request


class CountryMigration(Request):
    def __init__(self):
        super().__init__()


country_migration_db = CountryMigration()

if __name__ == "__main__":
    pass
