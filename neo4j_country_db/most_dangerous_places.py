from neo4j_country_db.requests import Request


class MostDangerousPlaces(Request):
    def __init__(self):
        super().__init__()


most_dangerous_places_db = MostDangerousPlaces()

if __name__ == "__main__":
    pass
