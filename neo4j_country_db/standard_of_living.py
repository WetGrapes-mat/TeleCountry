from neo4j_country_db.requests import Request


class StandartLivingRequest(Request):

    def findAllInfo(self):
        with self.driver.session() as session:
            info = session.execute_write(self._findAllInfo)
            return info

    def findCountryNames(self):
        with self.driver.session() as session:
            info = session.execute_write(self._findCounryNames)
            return info

    @staticmethod
    def _findCounryNames(tx):
        result = tx.run("""match(n:Country) return n.name as Country""")
        return [info["Country"] for info in result]

    @staticmethod
    def _findAllInfo(tx):
        result = tx.run("""match (c:Country)-[:healthcare]-(hc), 
        (c)-[:crime_indexes]-(ci), 
        (c)-[:climat]-(clim), 
        return c.name as Country, 
        hc.accuracyAndCompletenessInFillingOutReports as
        hc.convenienceOfLocationForYou as
        hc.equipmentForModernDiagnosisAndTreatment as modern_equipment
        hc.friendlinessAndCourtesyOfTheStaff as
        hc.satisfactionWithCostToYou as
        hc.satisfactionWithResponsivenessInMedicalInstitutions as
        hc.skillAndCompetencyOfMedicalStaff as skill_and_competency
        hc.speedInCompletingExaminationAndReports as speed
        """)
        return [{"Country": info["Country"],
                 "averageMonthlyNetSalary": info["averageMonthlyNetSalary"],
                 "dress": info["dress"],
                 "jeans": info["jeans"],
                 "pairOfMenLeatherBusinessShoes": info["pairOfMenLeatherBusinessShoes"],
                 "pairOfNikeRunningShoes": info["pairOfNikeRunningShoes"],
                 "cappuccino": info["cappuccino"],
                 "domesticBeerRestaurant": info["domesticBeerRestaurant"],
                 "importedBeerRestaurant": info["importedBeerRestaurant"],
                 "mcMealAtMcDonalds": info["mcMealAtMcDonalds"],
                 "mealFor2PeopleMidRestaurant": info["mealFor2PeopleMidRestaurant"],
                 "mealInexpensiveRestaurant": info["mealInexpensiveRestaurant"],
                 "water": info["water"],
                 "internationalPrimarySchool": info["internationalPrimarySchool"],
                 "preschool": info["preschool"],
                 "pricePerSquareMeterToBuyApartmentInCityCentre": info["pricePerSquareMeterToBuyApartmentInCityCentre"],
                 "pricePerSquareMeterToBuyApartmentOutsideOfCentre": info["pricePerSquareMeterToBuyApartmentOutsideOfCentre"],
                 "mobileTariffLocal": info["mobileTariffLocal"],
                 "internet": info["internet"],
                 "basic": info["basic"],
                 "apartment1RoomInCityCentre": info["apartment1RoomInCityCentre"],
                 "apartment1RoomOutsideOfCentre": info["apartment1RoomOutsideOfCentre"],
                 "apartment3RoomsInCityCentre": info["apartment3RoomsInCityCentre"],
                 "apartment3RoomsOutsideOfCentre": info["apartment3RoomsOutsideOfCentre"],
                 "cinema": info["cinema"],
                 "fitnessClub": info["fitnessClub"],
                 "tennisCourt": info["tennisCourt"],
                 "gasoline": info["gasoline"],
                 "monthlyPass": info["monthlyPass"],
                 "oneWayTicketLocal": info["oneWayTicketLocal"],
                 "taxi1hourWaiting": info["taxi1hourWaiting"],
                 "taxi1km": info["taxi1km"],
                 "taxiStart": info["taxiStart"],
                 "toyotaCorollaSedan": info["toyotaCorollaSedan"],
                 "volkswagenGolf": info["volkswagenGolf"],
                 "apples": info["apples"],
                 "banana": info["banana"],
                 "beefRound": info["beefRound"],
                 "bottleOfWine": info["bottleOfWine"],
                 "chickenFillets": info["chickenFillets"],
                 "cigarettesPack": info["cigarettesPack"],
                 "domesticBeer": info["domesticBeer"],
                 "eggs": info["eggs"],
                 "importedBeer": info["importedBeer"],
                 "lettuce": info["lettuce"],
                 "loafOfFreshWhiteBread": info["loafOfFreshWhiteBread"],
                 "localCheese": info["localCheese"],
                 "milk": info["milk"],
                 "onion": info["onion"],
                 "oranges": info["oranges"],
                 "potato": info["potato"],
                 "rice": info["rice"],
                 "tomato": info["tomato"],
                 "waterBigBottle": info["waterBigBottle"]} for info in result]


standart_living_db = StandartLivingRequest()

if __name__ == "__main__":
    pass

