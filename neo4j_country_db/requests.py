from neo4j import GraphDatabase


class Request:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def findCitiesWithAccessToWater(self):
        with self.driver.session() as session:
            city = session.execute_write(self._accessToSeaOrOceanCities)
            print(city)

    def findCapitalName(self):
        with self.driver.session() as session:
            capitalName = session.execute_write(self._findCapital)
            print(capitalName)
            return capitalName

    def findFullInformationAboutCity(self, city_name):
        with self.driver.session() as session:
            city = session.execute_write(self._fullInformationAboutCity, city_name)
            print(city)

    @staticmethod
    def _accessToSeaOrOceanCities(tx):
        result = tx.run("MATCH (city:City {accessToSeaOrOcean:true}) "  # Проверяем доступ к морю у найденного города
                        "RETURN city.name")  # Возвращаем название города
        return result.single()[0]

    @staticmethod
    def _findCapital(tx):
        result = tx.run("MATCH (country:Country) "
                        "MATCH (country)-[capital:capital]->(city:City)"  # Ищем город по связи capital
                        "RETURN city.name")
        return result.single()[0]

    @staticmethod
    def _fullInformationAboutCity(tx, city_name):
        result = tx.run("MATCH (city:City {name:$city_name}) "
                        "RETURN city.name, city.accessToSeaOrOcean, city.isBig",
                        city_name=city_name)
        return [{"city.name": info["city.name"], "city.accessToSeaOrOcean":info["city.accessToSeaOrOcean"],
                 "city.isBig": info["city.isBig"]} for info in result]


if __name__ == "__main__":
    rq = Request("bolt://localhost:7999", "neo4j", "admin")
    rq.findCitiesWithAccessToWater()
    capital = rq.findCapitalName()
    rq.findFullInformationAboutCity(capital)
    rq.close()
