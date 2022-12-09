from neo4j_country_db.country_migration import country_migration_db


class CountryMigrationAgent:
    country_choose = dict()

    def climat_city(self):
        climat_country = {"1":dict(), "2":dict(), "3":dict()}
        c = country_migration_db.findClimat()
        for i in c:
            z = (i['airPollution'] + i['waterPollution'] + i['dirtyAndUntidy'])//3
            x = i['comfortableToSpendTimeInTheCity']
            if i['decemberAverageTemperature'] == 0: i['decemberAverageTemperature'] = -1
            y = (((i['averageDurationOfWinter'] * i['decemberAverageTemperature'])/2) + i['juneAverageTemperature'])/2

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
        size_city = []
        c = country_migration_db.findisb(choise)
        for i in c:
            size_city.append(i['nameCity'])
        return size_city

    def water_city(self):
        water_city = []
        water_country = []
        c = country_migration_db.findOcean()
        for i in c:
            water_city.append(i['nameCity'])
            water_country.append(i['nameCountry'])

        return water_city, set(water_country)

    def city_in_country(self, country):
        c = country_migration_db.findcity(country)
        result = []
        for i in c:
            result.append(i['nameCity'])
        return result

    def count_patams(self, params):
        temp1 = country_migration_db.findenglish()
        for i in temp1:
            if i['communicationOnEnglish'] >= int(params['english']):
                try:
                    self.country_choose[i['nameCountry']] += i['communicationOnEnglish']
                except:
                    self.country_choose[i['nameCountry']] = i['communicationOnEnglish']
        temp2 = country_migration_db.findtransport()
        for i in temp2:
            if i['developmentLevelOfPublicTransport'] >= int(params['transport']):
                try:
                    self.country_choose[i['nameCountry']] += i['developmentLevelOfPublicTransport']
                except:
                    self.country_choose[i['nameCountry']] = i['developmentLevelOfPublicTransport']

        temp3 = country_migration_db.findlifetype()
        for i in temp3:
            if i['workPlaces'] >= int(params['workplace']):
                try:
                    self.country_choose[i['nameCountry']] += i['workPlaces']
                except:
                    self.country_choose[i['nameCountry']] = i['workPlaces']
            if i['nightLifeEntertainment'] >= int(params['nightlife']):
                try:
                    self.country_choose[i['nameCountry']] += i['nightLifeEntertainment']
                except:
                    self.country_choose[i['nameCountry']] = i['nightLifeEntertainment']

        temp4 = country_migration_db.findlgbt()
        for i in temp4:
            if i['attitudeTowardsLGBT'] >= int(params['lgbt']):
                try:
                    self.country_choose[i['nameCountry']] += i['attitudeTowardsLGBT']
                except:
                    self.country_choose[i['nameCountry']] = i['attitudeTowardsLGBT']

        self.country_choose = dict(sorted(self.country_choose.items(), key=lambda item: item[1], reverse = True))


    def calculate(self, params):
        city = []
        country = None
        rezult = {}
        if params['water'] == "True":
            city, country = self.water_city()
            city_s = self.size_city(str(params['isBig']))
            temp1 = list(set(city).intersection(set(city_s)))
            if temp1:
                city = temp1
            else:
                city, country = self.water_city()
                print('был тут')
        else:
            city = self.size_city(str(params['isBig']))
        climat = self.climat_city()[params['climat']]
        temp2 = list()
        for i in climat.keys():
            temp2 += self.city_in_country(i)
        city = list(set(city).intersection(set(temp2)))
        self.count_patams(params)
        print(self.country_choose)
        for co, am in self.country_choose.items():
            if co in country:
                temp5 = list(set(city).intersection(set(self.city_in_country(co))))
                if temp5:
                    rezult[co] = temp5
        temp6 = list(rezult.items())
        if len(temp6) >= 3:
            return f"Для переезда наиболее подходящим будет {temp6[0][0]} можете расмотреть следущие города {', '.join(temp6[0][1])}, " \
                   f"так же неплохим варинтом будет {temp6[1][0]} тут стоит обратьить внимание на {', '.join(temp6[1][1])}. " \
                   f"И последний вариант который мы смогли вам подобраьт {temp6[2][0]}"
        elif len(temp6) == 2:
            return f"Для переезда наиболее подходящим будет {temp6[0][0]} можете расмотреть следущие города {', '.join(temp6[0][1])}, " \
                   f"так же неплохим варинтом будет {temp6[1][0]} тут стоит обратьить внимание на {', '.join(temp6[1][1])}."
        elif len(temp6) == 1:
            return f"Для переезда наиболее подходящим будет {temp6[0][0]} можете расмотреть следущие города {', '.join(temp6[0][1])}. "
        else:
            return f"К сожелению страны с задаными вами параметрами не нашлось."






#
# {'water': 'True', 'isBig': 'True', 'climat': '1', 'transport': '5', 'english': '5', 'workplace': '4', 'nightlife': '4', 'lgbt': '1'}
# {'Germany': 3, 'United Kingdom': 3, 'Finland': 3, 'Norway': 3, 'Sweden': 3, 'Canada': 3, 'Czech': 2, 'Slovakia': 2, 'Hungary': 2, 'Poland': 1}






agent = CountryMigrationAgent()
if __name__ == "__main__":

    print(agent.calculate({'water': 'True', 'isBig': 'True', 'climat': '1', 'transport': '5', 'english': '5', 'workplace': '4', 'nightlife': '4', 'lgbt': '1'}))
