from neo4j_country_db.country_migration import country_migration_db


class CountryMigrationAgent:
    country_choose = dict()
    user = None

    def climat_city(self):
        climat_country = {"1":dict(), "2":dict(), "3":dict()}
        c = country_migration_db.findClimat()
        for i in c:
            z = (i['airPollution'] + i['waterPollution'] + i['dirtyAndUntidy'])//3
            x = i['comfortableToSpendTimeInTheCity']
            if i['decemberAverageTemperature'] == 0: i['decemberAverageTemperature'] = -1
            y = (((i['averageDurationOfWinter'] * i['decemberAverageTemperature']) / 2) + i[
                'juneAverageTemperature']) / 2
            if i['averageDurationOfWinter'] == 0: y = (i['decemberAverageTemperature'] + i[
                'juneAverageTemperature']) / 2

            if float(y) <= 10:
                climat_country["1"][i['name']] = y

            elif 10 < float(y) <= 20:
                climat_country["2"][i['name']] = y

            elif  20 < float(y):
                climat_country["3"][i['name']] = y

        for i, c in climat_country.items():
            climat_country[i] = dict(sorted(c.items(), key=lambda item: item[1]))
        return climat_country

    def size_city(self, choise):
        c = country_migration_db.findisb(choise)
        return c

    def water_city(self):
        c = country_migration_db.findOcean()
        return c

    def all_country(self):
        c = country_migration_db.findallcountry()
        return c

    def answer_preparation(self, country):
        info = country_migration_db.findinfocountry(country)[0]

        z = (info['airPollution'] + info['waterPollution'] + info['dirtyAndUntidy']) // 3
        if info['decemberAverageTemperature'] == 0: info['decemberAverageTemperature'] = -1
        y = (((info['averageDurationOfWinter'] * info['decemberAverageTemperature']) / 2) +info[
            'juneAverageTemperature']) / 2
        if info['averageDurationOfWinter'] == 0: y = (info['decemberAverageTemperature'] + info[
            'juneAverageTemperature']) / 2
        answer = f'Страна котомую мы для вас подобрали {info["name"]}\n' \
                 f'Немного параметров о стране:\n' \
                 f'Население страны {info["count"]}\n' \
                 f'Официальный язык {info["nameLan"]}\n' \
                 f'Процент закрзясненности окружающей среды {z}%\n' \
                 f'Процент комфортности проживания в стране {info["comfortableToSpendTimeInTheCity"]}\n' \
                 f'Отношение к иностранцам (от 1 до 3) {info["friendlyToForeigners"]}\n' \
                 f'Мество в глобальном рейтинге {info["globalRank"]}\n' \
                 f'Комфорт жизни с семьей (от 1 до 3) {info["assessmentOfFamilyLife"]}\n' \
                 f'Уровени свободы слова (от 1 до 3) {info["freedomOfSpeech"]}\n' \
                 f'Доспуность беспталного WiFi (от 1 до 3) {info["speedOfInternetMbps"]}\n' \
                 f'Национальная валюта {info["nameMoney"]}\n' \
                 f'Курс к долару {info["oneDollarEquals"]}\n'

        return answer



    def city_in_country(self, country):
        c = country_migration_db.findcity(country)
        result = []
        for i in c:
            result.append(i['nameCity'])
        return result

    def count_patams(self, params):
        temp1 = country_migration_db.findenglish()
        self.user = (int(params['transport']) + int(params['english']) + int(params['workplace']) +
                     int(params['nightlife']) + int(params['lgbt']))
        for i in temp1:
            try:
                self.country_choose[i['nameCountry']] += i['communicationOnEnglish']
            except:
                self.country_choose[i['nameCountry']] = i['communicationOnEnglish']
        temp2 = country_migration_db.findtransport()
        for i in temp2:
            try:
                self.country_choose[i['nameCountry']] += i['developmentLevelOfPublicTransport']
            except:
                self.country_choose[i['nameCountry']] = i['developmentLevelOfPublicTransport']

        temp3 = country_migration_db.findlifetype()
        for i in temp3:
            try:
                self.country_choose[i['nameCountry']] += i['workPlaces']
            except:
                self.country_choose[i['nameCountry']] = i['workPlaces']
            try:
                self.country_choose[i['nameCountry']] += i['nightLifeEntertainment']
            except:
                self.country_choose[i['nameCountry']] = i['nightLifeEntertainment']

        temp4 = country_migration_db.findlgbt()
        for i in temp4:
            try:
                self.country_choose[i['nameCountry']] += i['attitudeTowardsLGBT']
            except:
                self.country_choose[i['nameCountry']] = i['attitudeTowardsLGBT']

        self.country_choose = dict(sorted(self.country_choose.items(), key=lambda item: item[1], reverse = True))


    def calculate(self, params):
        # country_water = None
        # country_IsBig = None
        # country_tempricha = None
        rezult = None
        if params['water'] == "True":
            country_water = self.water_city()
        else:
            country_water = self.all_country()
        country_IsBig = self.size_city(str(params['isBig']))
        country_tempricha = self.climat_city()[params['climat']]
        temp2 = list()
        for i in country_tempricha.keys():
            temp2.append(i)
        country_tempricha = set(temp2)
        temp3 = set()
        if country_water and country_IsBig and country_tempricha:
            temp3 = country_water.intersection(country_IsBig.intersection(country_tempricha))
        self.count_patams(params)
        print(self.country_choose)
        temp_r = 9999999
        for co, am in self.country_choose.items():
            if co in temp3:
                if abs(am - self.user) < temp_r:
                    temp_r = abs(am - self.user)
                    rezult = co
        if rezult:
            return f"{self.answer_preparation(rezult)} "
        else:
            return f"К сожелению страны с задаными вами параметрами не нашлось."






#
# {'water': 'True', 'isBig': 'True', 'climat': '1', 'transport': '5', 'english': '5', 'workplace': '4', 'nightlife': '4', 'lgbt': '1'}
# {'Germany': 3, 'United Kingdom': 3, 'Finland': 3, 'Norway': 3, 'Sweden': 3, 'Canada': 3, 'Czech': 2, 'Slovakia': 2, 'Hungary': 2, 'Poland': 1}






agent = CountryMigrationAgent()
if __name__ == "__main__":
    print(agent.water_city())
    print(agent.climat_city())
    print({'water': 'True', 'isBig': 'True', 'climat': '1', 'transport': '5', 'english': '5', 'workplace': '4', 'nightlife': '4', 'lgbt': '1'})

    print(agent.calculate({'water': 'True', 'isBig': 'False', 'climat': '3', 'transport': '1', 'english': '1', 'workplace': '1', 'nightlife': '1', 'lgbt': '1'}))
