from neo4j_country_db.requests import Request


class MostDangerousPlacesRequest(Request):
    def __init__(self):
        super().__init__()

    def findHazard(self):
        with self.driver.session() as session:
            info = session.execute_write(self._hazard)
            return info

    def findCta(self):
        with self.driver.session() as session:
            info = session.execute_write(self._CTa)
            return info

    def findSa(self):
        with self.driver.session() as session:
            info = session.execute_write(self._Sa)
            return info

    def findCountryNames(self):
        with self.driver.session() as session:
            info = session.execute_write(self._findCounryNames)
            return info

    # возвращает словарь, содержащий СРЕДНЕЕ ЗНАЧЕНИЕ КРИМИНАЛА, округляется до тысячных
    @staticmethod
    def _CTa(tx):
        result = tx.run("match (country:Country) -[:crime_indexes]-> (crime:CrimeThing) "
                        "return "
                        "country.name as country, "
                        "ROUND((crime.crimeIncreasingInThePast3Years + "
                        "crime.levelOfCrime + "
                        "crime.problemCorruptionAndBribery +"
                        "crime.problemPeopleUsingOrDealingDrugs + "
                        "crime.problemPropertyCrimesSuchAsVandalismAndTheft + "
                        "crime.problemViolentCrimesSuchAsAssaultAndArmedRobbery +"
                        "crime.safetyWalkingAloneDuringDaylight +"
                        "crime.safetyWalkingAloneDuringNight +"
                        "crime.worriesAttacked +"
                        "crime.worriesBeingInsulted +"
                        "crime.worriesBeingMuggedOrRobbed +"
                        "crime.worriesBeingSubjectToAPhysicalAttack + "
                        "crime.worriesCarStolen +"
                        "crime.worriesHomeBrokenAndThingsStolen +"
                        "crime.worriesThingsFromCarStolen) /14.0, 3) as avg")
        return [{"country": info["country"],
                 "CTa": info["avg"]} for info in result]

    # возвращает словарь, содержащий СРЕДНЕЕ ЗНАЧЕНИЕ ЗАЩИТЫ
    @staticmethod
    def _Sa(tx):
        result = tx.run("match (country:Country) -[:security]-> (security:Security) "
                        "return "
                        "country.name as country, "
                        "ROUND((security.assessmentOfFamilyLife + "
                        "security.attitudeTowardsLGBT + "
                        "security.freedomOfSpeech +"
                        "security.situationInTheCountry) / 4.0, 3) as avg")
        return [{"country": info["country"],
                 "Sa": info["avg"]} for info in result]

    # возвращает СЛОВАРЬ
    @staticmethod
    def _hazard(tx):
        result = tx.run("match (country:Country)-[:borders_with]->(neighbor:Country), "
                        "(country)-[:belongs_to_military_political_block]->(block:MilitaryPoliticalBlock),"                        
                        "(country)-[:military_power]->(army:MilitaryPower) "                        
                        "return "
                        "country.name as country,"
                        "block.name as countryBlock,"
                        "army.amountOfPeople as countryArmy,"
                        "neighbor.name as neighbor")
        return [{"country": info["country"],
                 "countryBlock": info["countryBlock"],
                 "countryArmy": info["countryArmy"],
                 "neighbor":info["neighbor"]} for info in result]

    # поиск всех стран для вывода в бот
    @staticmethod
    def _findCounryNames(tx):
        result = tx.run("""
            match (country:Country) return country.name as Country            
            """)
        return [info["Country"] for info in result]


most_dangerous_places_db = MostDangerousPlacesRequest()

if __name__ == "__main__":
    pass
