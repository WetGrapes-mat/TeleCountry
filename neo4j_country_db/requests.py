from neo4j import GraphDatabase


class Request:

    def __init__(self):
        self.driver = GraphDatabase.driver("bolt://localhost:7999", auth=("neo4j", "admin"))

    def close(self):
        self.driver.close()

    def findCitiesWithAccessToWater(self, haveAccessToWater):
        with self.driver.session() as session:
            city = session.execute_write(self._accessToSeaOrOceanCities, haveAccessToWater)
            return city

    def findCapitalName(self):
        with self.driver.session() as session:
            capitalName = session.execute_write(self._findCapital)
            return capitalName

    def findFullInformationAboutCity(self, city_name):
        with self.driver.session() as session:
            city = session.execute_write(self._fullInformationAboutCity, city_name)
            return city

    @staticmethod
    def _accessToSeaOrOceanCities(tx, haveAccessToWater):
        result = tx.run("MATCH (city:City {accessToSeaOrOcean:$haveAccessToWater}) "  # Проверяем доступ к морю у найденного города
                        "RETURN city.name",
                        haveAccessToWater=haveAccessToWater)  # Возвращаем название города
        return [cityName["city.name"] for cityName in result]

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


rq = Request()

if __name__ == "__main__":
    rq = Request()
    print(rq.findCitiesWithAccessToWater(False))
    capital = rq.findCapitalName()
    rq.findFullInformationAboutCity(capital)
    rq.close()
