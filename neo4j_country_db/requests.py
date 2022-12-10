from neo4j import GraphDatabase


class Request:

    def __init__(self):
        self.driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "12345678"))

    def close(self):
        self.driver.close()

    def findAllPrices(self):
        with self.driver.session() as session:
            info = session.execute_write(self._findAllPrices)
            return info


#================Это пример (потом удалиться)==============
    def findCitiesWithAccessToWater(self, haveAccessToWater):
        with self.driver.session() as session:
            city = session.execute_write(self._accessToSeaOrOceanCities, haveAccessToWater)
            return city

    def findCapitalName(self, list_city):
        with self.driver.session() as session:
            capitalName = session.execute_write(self._findCapital, list_city)
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
    def _findCapital(tx, list_city):
        result = tx.run("MATCH(country: Country) -[capital: capital]->  (city:City) "
                        "WHERE(city.name) IN $list_city "
                        "RETURN city.name", list_city=list_city)

        # print(result.single())
        return [cityName["city.name"] for cityName in result]
        # return result.single()[0]


    @staticmethod
    def _fullInformationAboutCity(tx, city_name):
        result = tx.run("MATCH (city:City {name:$city_name}) "
                        "RETURN city.name, city.accessToSeaOrOcean, city.isBig",
                        city_name=city_name)
        return [{"city.name": info["city.name"], "city.accessToSeaOrOcean":info["city.accessToSeaOrOcean"],
                 "city.isBig": info["city.isBig"]} for info in result]

#=========================================================
rq = Request()

if __name__ == "__main__":
    rq = Request()
    print(rq.findCitiesWithAccessToWater(False))
    capital = rq.findCapitalName(['Оттава', 'Квебек', 'Монреаль', 'Торонто'])
    print(capital)
    rq.findFullInformationAboutCity(capital)
    rq.close()
