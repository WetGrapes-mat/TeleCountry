from neo4j import GraphDatabase


class CountryCreator:

    def __init__(self):
        self.driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "admin"))

    def close(self):
        self.driver.close()

    def createCountry(self, countryName, languageName,
                      cityName1, cityName2, cityName3, cityName4, cityName5,
                      isBig1, isBig2, isBig3, isBig4, isBig5):
        with self.driver.session() as session:
            city = session.execute_write(self._createCountry, countryName, languageName,
                                         cityName1, cityName2, cityName3, cityName4, cityName5,
                                         isBig1, isBig2, isBig3, isBig4, isBig5)
            return city

    @staticmethod
    def _createCountry(tx, countryName, languageName, cityName1, cityName2, cityName3, cityName4, cityName5,
                                                      isBig1, isBig2, isBig3, isBig4, isBig5):
        result = tx.run("CREATE (country:Country {name:$countryName}) "
                        "CREATE (language:Language {name:$languageName}) "

                        "CREATE (city.City {name:$cityName1, isBig:$isBig1}) "
                        "CREATE (city.City {name:$cityName2, isBig:$isBig2}) "
                        "CREATE (city.City {name:$cityName3, isBig:$isBig3}) "
                        "CREATE (city.City {name:$cityName4, isBig:$isBig4}) "
                        "CREATE (city.City {name:$cityName5, isBig:$isBig5}) "

                        "SET country-[has_city]->city"

                        ,
                        countryName=countryName,
                        languageName=languageName,
                        cityName1=cityName1, cityName2=cityName2, cityName3=cityName3, cityName4=cityName4,
                        cityName5=cityName5,
                        isBig1=isBig1, isBig2=isBig2, isBig3=isBig3, isBig4=isBig4, isBig5=isBig5
                        )
        return result.single()[0]


if __name__ == "__main__":
    cc = CountryCreator()
    cc.createCountry("Беларусь", "Русский", "Минск", "Брест", "Витебск", "Гродно", "Орша",
                     "True", "True", "True", "True", "False"
                     )
    cc.close()
