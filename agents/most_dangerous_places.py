from neo4j_country_db.most_dangerous_places import most_dangerous_places_db
from itertools import groupby


class MostDangerousPlaces:
    def __init__(self):
        super().__init__()
        self.hazard = []
        self.Sa = []
        self.CTa = []

    def get_countries(self):
        countries = most_dangerous_places_db.findCountryNames()
        most_dangerous_places_db.close()
        return countries

    def count_HR(self):
        countries_list = []
        for i in range(len(self.CTa)):
            country = {}
            country["country"] = self.CTa[i]["country"]
            country["HR"] = (self.CTa[i]["CTa"] + self.Sa[i]["Sa"])/2
            countries_list.append(country)
        return countries_list

    def function_for_count(self, i: int, HR_list: list):
        country = {}
        hz = 0
        CTa = 0
        Sa = 0
        country_name = self.hazard[i]["country"]
        for k in range(len(HR_list)):
            if country_name == HR_list[k]["country"]:
                hz = HR_list[k]["HR"]
        country_block = self.hazard[i]["countryBlock"]
        country_army = self.hazard[i]["countryArmy"]
        neighbor = self.hazard[i]["neighbor"]

        for j in range(len(self.hazard)):
            if self.hazard[j]["country"] == neighbor \
                    and self.hazard[j]["countryBlock"] != country_block \
                    and self.hazard[j]["countryArmy"] > country_army:
                hz += 1

        for s in range(len(self.CTa)):
            if country_name == self.CTa[s]["country"]:
                CTa = self.CTa[s]["CTa"]

        for s in range(len(self.Sa)):
            if country_name == self.Sa[s]["country"]:
                Sa = self.Sa[s]["Sa"]

        country["country"] = country_name
        country["hz"] = hz
        country["CTa"] = CTa
        country["Sa"] = Sa
        return country

    def count(self, answer: str):
        string_result = ""
        country_list = []
        HR_list = self.count_HR()

        if answer == "Рейтинг":
            for i in range(len(self.hazard)):
                country = self.function_for_count(i, HR_list)
                country_list.append(country)
        else:
            for i in range(len(self.hazard)):
                if self.hazard[i]["country"] == answer:
                    country = self.function_for_count(i, HR_list)
                    country_list.append(country)
                    break

        country_list = [el for el, _ in groupby(country_list)]

        values = [country_list[i]["hz"] for i in range(len(country_list))]
        values.sort(reverse=True)

        for i in values:
            for c in country_list:
                if i == c["hz"]:
                    string_result += f'{c["country"]} ~ HR: {c["hz"]} ~ CTa: {c["CTa"]} ~ Sa: {c["Sa"]}\n'

        string_result += "\n"
        string_result += "HR  - рейтинг опасности (hazard rating)\n" \
                         "CTa - среднее значение Crime Thing\n" \
                         "Sa  - среднее значение Security\n"
        string_result += "\n"

        return string_result

    def get_all_information(self):
        self.hazard = most_dangerous_places_db.findHazard()
        self.Sa = most_dangerous_places_db.findSa()
        self.CTa = most_dangerous_places_db.findCta()
        most_dangerous_places_db.close()

