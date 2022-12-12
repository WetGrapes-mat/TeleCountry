from neo4j_country_db.standard_of_living import standart_living_db
from agents import cost_living
import math

coefficients = {"purchasingPowerInclRentIndex": 0.03333,
                "costOfLivingIndex": 0.03333,
                "safetyIndex": 0.33333,
                "healthIndex": 0.3333,
                "pollutionIndex": 0.3333,
                "climateIndex": 0.03333,
                "air_quality_index": 0.07,
                "drinking_water_quality_accessibility_index": 0.02,
                "water_pollution_index": 0.02,
                "garbage_disposal_satisfaction_index": 0.01,
                "clean_and_tidy_index": 0.01,
                "noise_and_light_pollution_index": 0.01,
                "green_and_parks_quality_index": 0.01,
                "comfortable_to_spend_time_index": 0.01,
                "level_of_crime_index": 0.03,
                "crime_increasing_index": 0.01,
                "safe_alone_daylight_index": 0.01,
                "safe_alone_night_index": 0.01,
                "worried_home_broken_index": 0.01,
                "worried_mugged_robbed_index": 0.01,
                "worried_car_stolen_index": 0.01,
                "worried_things_car_stolen_index": 0.01,
                "worried_attacked_index": 0.01,
                "worried_insulted_index": 0.01,
                "worried_skin_ethnic_religion_index": 0.01,
                "problem_drugs_index": 0.01,
                "problem_property_crimes_index": 0.01,
                "problem_violent_crimes_index": 0.01,
                "problem_corruption_bribery_index": 0.01,
                "hum_index": -0.0003,
                "skill_and_competency_index": 0.01,
                "speed_index": 0.01,
                "modern_equipment_index": 0.01,
                "accuracy_and_completeness_index": 0.01,
                "friendliness_and_courtesy_index": 0.01,
                "responsiveness_waitings_index": 0.01,
                "location_index": 0.01,
                "cost_index": 0.02,
                }


class StandartLiving:
    def __init__(self):
        super().__init__()
        self.info = []
        self.cl = cost_living.CostLiving()
        self.coefficients = coefficients

    def get_information(self):
        self.info = standart_living_db.findAllInfo()
        standart_living_db.close()

    def get_countries(self):
        countries = standart_living_db.findCountryNames()
        standart_living_db.close()
        return countries

    def to_fixed(self, numObj: float):
        digits = 2
        return f"{numObj:.{digits}f}"

    def expCalcStandart(self, value):
        return value**math.e

    def calculatePollutionIndex(self, i: int):
        overall = 0.0
        overall += self.expCalcStandart(self.info[i]["air_quality"] * self.coefficients["air_quality_index"])
        overall += self.expCalcStandart(self.info[i]["drinking_water_quality_accessibility"] * self.coefficients[
            "drinking_water_quality_accessibility_index"])
        overall -= self.expCalcStandart(self.info[i]["water_pollution"] * self.coefficients["water_pollution_index"])
        overall += self.expCalcStandart(
            self.info[i]["garbage_disposal_satisfaction"] * self.coefficients["garbage_disposal_satisfaction_index"])
        overall += self.expCalcStandart(self.info[i]["clean_and_tidy"] * self.coefficients["clean_and_tidy_index"])
        overall -= self.expCalcStandart(
            self.info[i]["noise_and_light_pollution"] * self.coefficients["noise_and_light_pollution_index"])
        overall += self.expCalcStandart(
            self.info[i]["green_and_parks_quality"] * self.coefficients["green_and_parks_quality_index"])
        overall += self.expCalcStandart(
            self.info[i]["comfortable_to_spend_time"] * self.coefficients["comfortable_to_spend_time_index"])

        # print("Ecology: " + self.info[i]["Country"] + str((overall * 25) ** (1 / (0.68307 * math.e))))
        return max(0.0, ((overall * 25) ** (1 / (0.68307 * math.e))))

    def calculateSafetyIndex(self, i: int):
        overall = 31.8
        overall -= self.expCalcStandart(self.info[i]["level_of_crime"] * self.coefficients["level_of_crime_index"])
        overall -= self.expCalcStandart(self.info[i]["crime_increasing"] * self.coefficients["crime_increasing_index"])
        overall += self.expCalcStandart(
            self.info[i]["safe_alone_daylight"] * self.coefficients["safe_alone_daylight_index"])
        overall += self.expCalcStandart(
            self.info[i]["safe_alone_night"] * self.coefficients["safe_alone_night_index"])
        overall -= self.expCalcStandart(
            self.info[i]["worried_home_broken"] * self.coefficients["worried_home_broken_index"])
        overall -= self.expCalcStandart(
            self.info[i]["worried_mugged_robbed"] * self.coefficients["worried_mugged_robbed_index"])
        overall -= self.expCalcStandart(
            self.info[i]["worried_car_stolen"] * self.coefficients["worried_car_stolen_index"])
        overall -= self.expCalcStandart(
            self.info[i]["worried_things_car_stolen"] * self.coefficients["worried_things_car_stolen_index"])
        overall -= self.expCalcStandart(self.info[i]["worried_attacked"] * self.coefficients["worried_attacked_index"])
        overall -= self.expCalcStandart(self.info[i]["worried_insulted"] * self.coefficients["worried_insulted_index"])
        overall -= self.expCalcStandart(
            self.info[i]["worried_skin_ethnic_religion"] * self.coefficients["worried_skin_ethnic_religion_index"])
        overall -= self.expCalcStandart(self.info[i]["problem_drugs"] * self.coefficients["problem_drugs_index"])
        overall -= self.expCalcStandart(
            self.info[i]["problem_property_crimes"] * self.coefficients["problem_property_crimes_index"])
        overall -= self.expCalcStandart(
            self.info[i]["problem_violent_crimes"] * self.coefficients["problem_violent_crimes_index"])
        overall -= self.expCalcStandart(
            self.info[i]["problem_corruption_bribery"] * self.coefficients["problem_corruption_bribery_index"])
        overall = max(0.0, overall)

        # print("Safety: " + self.info[i]["Country"] + str((overall * 25) ** (1 / (0.538365 * math.e))))
        return min(100.0, (overall * 25) ** (1 / (0.538365 * math.e)))

    def calculateClimateIndex(self, i: int):
        index = 1
        if (self.info[i]["averageHumidity"]) < 40 or (self.info[i]["averageHumidity"]) > 60:
            index = math.exp(self.expCalcStandart(((abs(self.info[i]["averageHumidity"] - 50)) - 10))
                               * self.coefficients["hum_index"])
        # print("Climat: " + self.info[i]["Country"] + str(index*100))
        return index*100

    def calculateHealthIndex(self, i: int):
        overall = 0
        overall += self.expCalcStandart(
            self.info[i]["skill_and_competency"] * self.coefficients["skill_and_competency_index"])
        overall += self.expCalcStandart(self.info[i]["speed"] * self.coefficients["speed_index"])
        overall += self.expCalcStandart(self.info[i]["modern_equipment"] * self.coefficients["modern_equipment_index"])
        overall += self.expCalcStandart(
            self.info[i]["accuracy_and_completeness"] * self.coefficients["accuracy_and_completeness_index"])
        overall += self.expCalcStandart(
            self.info[i]["friendliness_and_courtesy"] * self.coefficients["friendliness_and_courtesy_index"])
        overall += self.expCalcStandart(
            self.info[i]["responsiveness_waitings"] * self.coefficients["responsiveness_waitings_index"])
        overall += self.expCalcStandart(
            self.info[i]["location"] * self.coefficients["location_index"])
        overall += self.expCalcStandart(
            self.info[i]["cost"] * self.coefficients["cost_index"])

        # print("Health: " + self.info[i]["Country"] + str((overall * 25) ** (1 / (0.465526 * math.e))))
        return min(100.0, (overall * 25) ** (1 / (0.465526 * math.e)))

    def calculateCostOfLivingIndex(self, i: int):
        self.cl.get_information()
        cost = {}
        cost = self.cl.count_function(0, 0, 1, 0, "своя машина", "1-к в центре", cost, i)
        index = list(cost.values())[0] / 1424
        # print("Cost of living: " + self.info[i]["Country"] + str(index * 100))
        return index * 100

    def calculatePurchaisingPowerIndex(self, i: int):
        self.cl.get_information()
        cost = {}
        cost = self.cl.count_function(0, 0, 1, 0, "своя машина", "1-к в центре", cost, i)
        index = (list(cost.values())[0] / self.info[i]["salary"]) / ((1424 + 3844) / 5982)
        # print("Purchasing index: " + self.info[i]["Country"] + str(index * 100))
        return index * 100

    def finalCalculation(self, i):
        # print("Result " + str((self.calculatePurchaisingPowerIndex(i) * self.coefficients["purchasingPowerInclRentIndex"])
        #                           + (self.calculateCostOfLivingIndex(i) * self.coefficients["costOfLivingIndex"])
        #                           + (self.calculateSafetyIndex(i) * self.coefficients["safetyIndex"])
        #                           + (self.calculateHealthIndex(i) * self.coefficients["healthIndex"])
        #                           + (self.calculatePollutionIndex(i) * self.coefficients["pollutionIndex"])
        #                           + (self.calculateClimateIndex(i) * self.coefficients["climateIndex"])))
        return max(0.0, min(100, ((self.calculatePurchaisingPowerIndex(i) * self.coefficients["purchasingPowerInclRentIndex"])
                                  + (self.calculateCostOfLivingIndex(i) * self.coefficients["costOfLivingIndex"])
                                  + (self.calculateSafetyIndex(i) * self.coefficients["safetyIndex"])
                                  + (self.calculateHealthIndex(i) * self.coefficients["healthIndex"])
                                  + (self.calculatePollutionIndex(i) * self.coefficients["pollutionIndex"])
                                  + (self.calculateClimateIndex(i) * self.coefficients["climateIndex"]))))

    def get_country_rating(self):
        self.get_information()
        result = {}
        for i in range(len(self.info)):
            curr_country = self.finalCalculation(i)
            result[self.info[i]["Country"]] = curr_country
        string_result = ""
        sorted_values = sorted(result.values())
        for i in sorted_values:
            for key, value in result.items():
                if i == value:
                    string_result += f'{key} -- {self.to_fixed(i)}\n'
        return string_result

st = StandartLiving()