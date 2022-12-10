from neo4j_country_db.requests import Request


class MostDangerousPlaces(Request):
    def __init__(self):
        super().__init__()


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
        return [{"country":info["country"],
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
                        "(neighbor)-[:belongs_to_military_political_block]->(neighbor_block:MilitaryPoliticalBlock),"
                        "(country)-[:military_power]->(army:MilitaryPower),"
                        "(neighbor)-[:military_power]->(neighbor_army:MilitaryPower)"
                        "return"
                        "country.name as country,"
                        "block.name as countryBlock,"
                        "army.amountOfPeople as countryArmy,"
                        "neighbor.name as neighbor,"
                        "neighbor_block.name as neighborBlock,"
                        "neighbor_army.amountOfPeople as neighborArmy")
        return [{"country": info["country"],
                 "countryBlock": info["countryBlock"],
                 "countryArmy": info["countryArmy"],
                 "neighbor":info["neighbor"],
                 "neighborBlock": info["neighborBlock"],
                 "neighborArmy": info["neighborArmy"]} for info in result]

most_dangerous_places_db = MostDangerousPlaces()

if __name__ == "__main__":
    pass
