import math
from neo4j_country_db.country_migration import country_migration_db
from keybords import cost_living
from agents.standard_of_living import st


class CountryMigrationAgent:
    climat = ["холодным", " умереным", "жарким"]
    speed_life = ["быстрым", "медленым"]
    country_choose = dict()
    user = None
    coefficients = {'friendlyToForeigners': 1,
                    'globalRank': 1,
                    'assessmentOfFamilyLife': 0.2,
                    'attitudeTowardsLGBT': 0.1,
                    'freedomOfSpeech': 1,
                    'communicationOnEnglish': 0.05,
                    'freeWifi': 0.02,
                    'speedOfInternetMbps': 0.01,
                    'speedOfLife': 0.2,
                    'workPlaces': 1,
                    'nightLifeEntertainment': 0.1}

    def expCalcStandart(self, value):
        return value ** math.e

    def climat_city(self):
        climat_country = {"1": dict(), "2": dict(), "3": dict()}
        c = country_migration_db.findClimat()
        for i in c:
            if i['decemberAverageTemperature'] == 0: i['decemberAverageTemperature'] = -1
            y = (((i['averageDurationOfWinter'] * i['decemberAverageTemperature']) / 2) + i[
                'juneAverageTemperature']) / 2
            if i['averageDurationOfWinter'] == 0: y = (i['decemberAverageTemperature'] + i[
                'juneAverageTemperature']) / 2
            if float(y) <= 10:
                climat_country["1"][i['name']] = y

            elif 10 < float(y) <= 20:
                climat_country["2"][i['name']] = y

            elif 20 < float(y):
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
        y = (((info['averageDurationOfWinter'] * info['decemberAverageTemperature']) / 2) + info[
            'juneAverageTemperature']) / 2
        if info['averageDurationOfWinter'] == 0: y = (info['decemberAverageTemperature'] + info[
            'juneAverageTemperature']) / 2
        answer = f'Страна, котомую мы для вас подобрали - {info["name"]}\n' \
                 f'Немного параметров о стране:\n' \
                 f'Население страны:  {info["count"]}\n' \
                 f'Официальный язык: {info["nameLan"]}\n' \
                 f'Процент загрязненности окружающей среды: {z}%\n' \
                 f'Процент комфортности проживания в стране: {info["comfortableToSpendTimeInTheCity"]}\n' \
                 f'Отношение к иностранцам (от 1 до 3): {info["friendlyToForeigners"]}\n' \
                 f'Место в глобальном рейтинге: {info["globalRank"]}\n' \
                 f'Комфорт жизни с семьей (от 1 до 3): {info["assessmentOfFamilyLife"]}\n' \
                 f'Уровень свободы слова (от 1 до 3): {info["freeWifi"]}\n' \
                 f'Доступность беспталного WiFi (от 1 до 3): {info["speedOfInternetMbps"]}\n' \
                 f'Национальная валюта: {info["nameMoney"]}\n' \
                 f'Курс к долару: {info["oneDollarEquals"]}\n'

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

        self.country_choose = dict(sorted(self.country_choose.items(), key=lambda item: item[1], reverse=True))

    def price_living(self, params):
        cost_living.cl.get_information()
        answe = dict()
        if params['flat'] == "на окраине":
            answe['rent'] = f'{params["family"]}-к {params["flat"]}'
        else:
            answe['rent'] = f'{params["family"]}-к {params["flat"]}'
        answe['country'] = 'Рейтинг стран'
        answe['members'] = int(params["family"])
        answe['child_preschool'] = 0
        if int(params["family"]) == 1:
            answe['child_school'] = 0
        else:
            answe['child_school'] = 1
        answe['smoking'] = 0
        answe['transportation'] = params['transport']
        rez = cost_living.cl.count_cost_living(answe['child_preschool'], answe['child_school'], answe['members'],
                                               answe['smoking'],
                                               answe['transportation'], answe['rent'], answe['country'])
        return {z[0][:-1]: float(z[1][:-2]) for z in [i.split("--") for i in rez.split('\n')][:-1]}

    def standart_living(self):
        rez = st.get_country_rating()
        return {z[0][:-1]: float(z[1]) for z in [i.split("--") for i in rez.split('\n')][:-1]}

    def calculate(self, params):
        price = self.price_living(params)
        standart = self.standart_living()
        rez_data = list()
        temp_rez = dict()
        if params['water'] == "True":
            country_water = self.water_city()
        else:
            country_water = self.all_country()
        country_tempricha = self.climat_city()[params['climat']]
        temp2 = list()
        for i in country_tempricha.keys():
            temp2.append(i)
        country_tempricha = set(temp2)
        temp3 = set()
        if country_water and country_tempricha:
            temp3 = country_water.intersection(country_tempricha)
        for i in temp3:
            rez_data.append(country_migration_db.findinfocountry(i)[0])
            temp_rez[i] = 0

        temp3 = list(temp3)

        for i in rez_data:
            if params['isBig'] == "1" and min(100, self.expCalcStandart(
                    i['speedOfLife'] * self.coefficients['speedOfLife']) * self.expCalcStandart(
                    i['count'] * 1e-7)) < 10:
                temp3.remove(i['name'])
            elif params['isBig'] == "2" and min(100, self.expCalcStandart(
                    i['speedOfLife'] * self.coefficients['speedOfLife']) * self.expCalcStandart(
                    i['count'] * 1e-7)) > 10:
                temp3.remove(i['name'])

        rez_data.clear()
        temp_rez.clear()
        for i in temp3:
            rez_data.append(country_migration_db.findinfocountry(i)[0])
            temp_rez[i] = 0
        for i in rez_data:
            if params['family'] == "3":
                temp_rez[i['name']] += (
                    self.expCalcStandart(self.coefficients['assessmentOfFamilyLife'] * i['assessmentOfFamilyLife']))
            elif params['family'] == "1":
                temp_rez[i['name']] += self.expCalcStandart(
                    (self.coefficients['nightLifeEntertainment'] * i['nightLifeEntertainment']))

            temp_rez[i['name']] += (
                self.expCalcStandart(self.coefficients['communicationOnEnglish'] * i['communicationOnEnglish']))

            temp_rez[i['name']] += (self.expCalcStandart(self.coefficients['freeWifi'] * i['freeWifi']))
            temp_rez[i['name']] += ((1 / standart[i['name']]))
            temp_rez[i['name']] += (self.expCalcStandart(0.1 * (1 / i['globalRank'])))
            if params['lgbt'] == "True":
                temp_rez[i['name']] += (
                    self.expCalcStandart(self.coefficients['attitudeTowardsLGBT'] * i['attitudeTowardsLGBT']))
        tem_price = dict()
        if params['price'] == '3600':
            for i in temp_rez.keys():
                if price[i] < 3600:
                    tem_price[i] = price[i]
        elif params['price'] == '3600_5200':
            for i in temp_rez.keys():
                if 3600 < price[i] < 5200:
                    tem_price[i] = price[i]
        elif params['price'] == '5200':
            for i in temp_rez.keys():
                if price[i] > 5200:
                    tem_price[i] = price[i]
        elif params['price'] == '1300':
            for i in temp_rez.keys():
                if price[i] < 1300:
                    tem_price[i] = price[i]
        elif params['price'] == '1300_1800':
            for i in temp_rez.keys():
                if 1300 < price[i] < 1800:
                    tem_price[i] = price[i]
        elif params['price'] == '1800':
            for i in temp_rez.keys():
                if price[i] > 1800:
                    tem_price[i] = price[i]

        temp_rez = dict(sorted(temp_rez.items(), key=lambda item: item[1], reverse=True))
        # print(temp_rez)

        tttt = None
        if tem_price == dict():
            for i in temp_rez.keys():
                tem_price[i] = price[i]

            if params['price'] == '3600':
                a = 99999
                b = -99999
                for i, r in tem_price.items():
                    if abs(3600 - r) < a and temp_rez[i] > b:
                        a = abs(1300 - r)
                        b = temp_rez[i]
                        tttt = i

            elif params['price'] == '5200' or params['price'] == '3600_5200':
                a = 99999
                b = -99999
                for i, r in tem_price.items():
                    if abs(5200 - r) < a and temp_rez[i] > b:
                        a = abs(5200 - r)
                        b = temp_rez[i]
                        tttt = i
            elif params['price'] == '1300':
                a = 99999
                b = -99999
                for i, r in tem_price.items():
                    if abs(1300 - r) < a and temp_rez[i] > b:
                        a = abs(1300 - r)
                        tttt = i

            elif params['price'] == '1800' or params['price'] == '1300_1800':
                a = 99999
                b = -99999
                for i, r in tem_price.items():
                    if abs(1800 - r) < a and temp_rez[i] > b:
                        a = abs(1300 - r)
                        tttt = i

        else:
            a = -9999999
            for i in tem_price.keys():
                if temp_rez[i] > a:
                    a = temp_rez[i]
                    tttt = i
        # print(tem_price)


        if tttt:
            rezult = f'На основании ваших ответов мы смогли вам подобрать {tttt}. Это прекрасная страна с ' \
                     f'{self.climat[int(params["climat"]) - 1]} климатом и ' \
                     f'{self.speed_life[int(params["isBig"]) - 1]} темпом жизни.\n' \
                     f'Расходы на все базовые потребности в месяц составят {tem_price[tttt]} $. '
            # print(tttt)
            return rezult

        else:
            return "Мы не смогли подобрать вам страну по заданным параметрам ;("


cm = CountryMigrationAgent()
if __name__ == "__main__":
    print(cm.calculate({'water': 'False', 'isBig': '2', 'climat': "2", 'family': '1', 'transport': 'общественный транспорт',
                     'flat': 'на окраине', 'price': '1800', "lgbt": "True"}))
'на окраине'
'своя машина'
'общественный транспорт'