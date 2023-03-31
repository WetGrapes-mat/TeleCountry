from neo4j_country_db.requests import Request


class CountryTravel(Request):
    def __init__(self):
        super().__init__()


country_travel_db = CountryTravel()

if __name__ == "__main__":
    pass
