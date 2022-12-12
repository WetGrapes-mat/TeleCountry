from neo4j_country_db.requests import Request


class CountryResorts(Request):
    def __init__(self):
        super().__init__()

    def find_resort(self, country):
        with self.driver.session() as session:
            res = session.execute_write(self._resort, country)
            return res

    @staticmethod
    def _resort(tx, name):
        result = tx.run("match (country:Country {name: $name}) -[:beach]-> (beach:Beach)"
                        "return "
                        "country.name as country, "
                        "beach.name as beachName, "
                        "beach.description as descr, "
                        "beach.image as photo", name=name)
        return [{"country": info["country"],
                 "resortName": info["beachName"],
                 "description": info["descr"],
                 "photo": info["photo"]} for info in result]


class CountrySkiResorts(Request):
    def __init__(self):
        super().__init__()

    def find_ski_resort(self, country):
        with self.driver.session() as session:
            res = session.execute_write(self._resort, country)
            return res

    @staticmethod
    def _resort(tx, name):
        result = tx.run("match (country:Country {name: $name}) -[:skiResort]-> (resort:SkiResort)"
                        "return "
                        "country.name as country, "
                        "resort.name as skiName, "
                        "resort.description as descr, "
                        "resort.image as photo", name=name)
        return [{"country": info["country"],
                 "skiResortName": info["skiName"],
                 "description": info["descr"],
                 "photo": info["photo"]} for info in result]


class CountryTourism(Request):
    def __init__(self):
        super().__init__()

    def find_sight(self, country):
        with self.driver.session() as session:
            res = session.execute_write(self._resort, country)
            return res

    @staticmethod
    def _resort(tx, name):
        result = tx.run("match (country:Country {name: $name}) -[:sight]-> (sight:Sight)"
                        "return "
                        "country.name as country, "
                        "sight.name as sightName, "
                        "sight.description as descr, "
                        "sight.image as photo", name=name)
        return [{"country": info["country"],
                 "sightName": info["sightName"],
                 "description": info["descr"],
                 "photo": info["photo"]} for info in result]


country_resorts_db = CountryResorts()
country_ski_resorts_db = CountrySkiResorts()
country_tourism_db = CountryTourism()


if __name__ == "__main__":
    print(country_ski_resorts_db.find_ski_resort('Canada'))

    print(country_resorts_db.find_resort('Canada'))

    print(country_tourism_db.find_sight('Canada'))

