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
        (c)-[:economic_situation]-(r)-[:salaries]-(s),
        (c)-[:climat]-(clim)
        return c.name as Country, 
        hc.accuracyAndCompletenessInFillingOutReports as accuracy_and_completeness,
        hc.convenienceOfLocationForYou as location,
        hc.equipmentForModernDiagnosisAndTreatment as modern_equipment,
        hc.friendlinessAndCourtesyOfTheStaff as friendliness_and_courtesy,
        hc.satisfactionWithCostToYou as cost,
        hc.satisfactionWithResponsivenessInMedicalInstitutions as responsiveness_waitings,
        hc.skillAndCompetencyOfMedicalStaff as skill_and_competency,
        hc.speedInCompletingExaminationAndReports as speed,
        ci.crimeIncreasingInThePast3Years as crime_increasing,
        ci.levelOfCrime as level_of_crime,
        ci.problemCorruptionAndBribery as problem_corruption_bribery,
        ci.problemPeopleUsingOrDealingDrugs as problem_drugs,
        ci.worriesHomeBrokenAndThingsStolen as worried_home_broken,
        ci.problemViolentCrimesSuchAsAssaultAndArmedRobbery as problem_violent_crimes,
        ci.safetyWalkingAloneDuringDaylight as safe_alone_daylight,
        ci.safetyWalkingAloneDuringNight as safe_alone_night,
        ci.worriesAttacked as worried_attacked,
        ci.worriesBeingInsulted as worried_insulted,
        ci.worriesBeingMuggedOrRobbed as worried_mugged_robbed,
        ci.worriesBeingSubjectToAPhysicalAttack as worried_skin_ethnic_religion,
        ci.worriesCarStolen as worried_car_stolen,
        ci.worriesThingsFromCarStolen as worried_things_car_stolen,
        ci.problemPropertyCrimesSuchAsVandalismAndTheft as problem_property_crimes,
        clim.airQuality as air_quality,
        clim.averageHumidity as averageHumidity,
        clim.drinkingWaterQualityAndAccessibility as drinking_water_quality_accessibility,
        clim.waterPollution as water_pollution,
        clim.garbageDisposalSatisfaction as garbage_disposal_satisfaction,
        clim.cleanAndTidy as clean_and_tidy,
        clim.noiseAndLightPollution as noise_and_light_pollution,
        clim.qualityOfGreenAndParks as green_and_parks_quality,
        clim.comfortableToSpendTimeInTheCity as comfortable_to_spend_time,
        s.averageMonthlyNetSalary as salary
        """)
        return [{"Country": info["Country"],
                 "accuracy_and_completeness": info["accuracy_and_completeness"],
                 "location": info["location"],
                 "modern_equipment": info["modern_equipment"],
                 "friendliness_and_courtesy": info["friendliness_and_courtesy"],
                 "cost": info["cost"],
                 "responsiveness_waitings": info["responsiveness_waitings"],
                 "skill_and_competency": info["skill_and_competency"],
                 "speed": info["speed"],
                 "crime_increasing": info["crime_increasing"],
                 "level_of_crime": info["level_of_crime"],
                 "problem_corruption_bribery": info["problem_corruption_bribery"],
                 "problem_drugs": info["problem_drugs"],
                 "worried_home_broken": info["worried_home_broken"],
                 "problem_violent_crimes": info["problem_violent_crimes"],
                 "safe_alone_daylight": info["safe_alone_daylight"],
                 "safe_alone_night": info["safe_alone_night"],
                 "worried_attacked": info["worried_attacked"],
                 "worried_insulted": info["worried_insulted"],
                 "worried_mugged_robbed": info["worried_mugged_robbed"],
                 "worried_skin_ethnic_religion": info["worried_skin_ethnic_religion"],
                 "worried_car_stolen": info["worried_car_stolen"],
                 "worried_things_car_stolen": info["worried_things_car_stolen"],
                 "problem_property_crimes": info["problem_property_crimes"],
                 "air_quality": info["air_quality"],
                 "averageHumidity": info["averageHumidity"],
                 "drinking_water_quality_accessibility": info["drinking_water_quality_accessibility"],
                 "water_pollution": info["water_pollution"],
                 "garbage_disposal_satisfaction": info["garbage_disposal_satisfaction"],
                 "clean_and_tidy": info["clean_and_tidy"],
                 "noise_and_light_pollution": info["noise_and_light_pollution"],
                 "green_and_parks_quality": info["green_and_parks_quality"],
                 "salary": info["salary"],
                 "comfortable_to_spend_time": info["comfortable_to_spend_time"]} for info in result]


standart_living_db = StandartLivingRequest()

if __name__ == "__main__":
    pass
