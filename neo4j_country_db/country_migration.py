from neo4j_country_db.requests import Request


class CountryMigration(Request):
    def __init__(self):
        super().__init__()

    def findClimat(self):
        with self.driver.session() as session:
            city = session.execute_write(self._climat)
            return city

    def findOcean(self):
        with self.driver.session() as session:
            city = session.execute_write(self._ocean)
            return city

    def findisb(self, isb):
        with self.driver.session() as session:
            city = session.execute_write(self._isbig, isb)
            return city

    def findenglish(self):
        with self.driver.session() as session:
            city = session.execute_write(self._english)
            return city

    def findglobalrank(self):
        with self.driver.session() as session:
            city = session.execute_write(self._globalrank)
            return city

    def findtransport(self):
        with self.driver.session() as session:
            city = session.execute_write(self._transport)
            return city

    def findlgbt(self):
        with self.driver.session() as session:
            city = session.execute_write(self._lgbt)
            return city

    def findlifetype(self):
        with self.driver.session() as session:
            city = session.execute_write(self._life_type)
            return city

    def findcity(self, country):
        with self.driver.session() as session:
            city = session.execute_write(self._country, country)
            return city

    def findinfocountry(self, country):
        with self.driver.session() as session:
            city = session.execute_write(self._final, country)
            return city

    def findallcountry(self):
        with self.driver.session() as session:
            city = session.execute_write(self._allcountry)
            return city

    @staticmethod
    def _climat(tx):
        result = tx.run("MATCH (n:Country) -[:climat]->(c:Climat) return n as Country ,"
                        "n.name as name,"
                        "c.averageDurationOfWinter as averageDurationOfWinter,"
                        "c.juneAverageTemperature as juneAverageTemperature,"
                        "c.decemberAverageTemperature as decemberAverageTemperature,"
                        "c.airPollution as airPollution,"
                        "c.waterPollution as waterPollution,"
                        "c.dirtyAndUntidy as dirtyAndUntidy, "
                        "c.comfortableToSpendTimeInTheCity as comfortableToSpendTimeInTheCity")
        return [{'name': info["name"], 'averageDurationOfWinter': info['averageDurationOfWinter'],
                 'juneAverageTemperature': info['juneAverageTemperature'],
                 'decemberAverageTemperature': info['decemberAverageTemperature'],
                 'airPollution': info['airPollution'],
                 'waterPollution': info['waterPollution'],
                 'dirtyAndUntidy': info['dirtyAndUntidy'],
                 'comfortableToSpendTimeInTheCity': info['comfortableToSpendTimeInTheCity']} for info in result]

    @staticmethod
    def _ocean(tx):
        result = tx.run("match (h:Country)-[:washes]-() return  "
                        "h.name as nameCountry")
        return set([info["nameCountry"] for info in result])

    @staticmethod
    def _isbig(tx, isb):
        result = tx.run("match (h:Country)-[:has_city]->(n:City {isBig: $isb}) return "
                        "h.name as nameCountry", isb=isb)
        return set([info["nameCountry"] for info in result])

    @staticmethod
    def _allcountry(tx):
        result = tx.run("match (h:Country) return "
                        "h.name as nameCountry")
        return set([info["nameCountry"] for info in result])

    @staticmethod
    def _country(tx, name):
        result = tx.run("match (h:Country {name: $name})-[:has_city]->(n:City) return "
                        "h.name as nameCountry,"
                        "n.name as nameCity", name=name)
        return [{'nameCountry': info["nameCountry"], 'nameCity': info['nameCity']} for info in result]

    @staticmethod
    def _final(tx, name):
        result = tx.run("match (h:Country {name: $name}) - [:climat] - (c:Climat), "
                        "(h)-[:citizenship]-(ci:Citizenship), "
                        "(h)-[:security]-(s:Security),"
                        "(h)-[:communication]- (com:Communication),"
                        "(h)-[:internet]-(i:Internet),"
                        "(h)-[:currency]-(cur:Currency),"
                        "(h)-[:population]-(po:Population),"
                        "(h)-[:official_language]-(l:Language)return "
                        "h.name as nameCountry,"
                        "c.comfortableToSpendTimeInTheCity as comfortableToSpendTimeInTheCity,"
                        "ci.friendlyToForeigners as friendlyToForeigners ,"
                        "ci.globalRank as globalRank,"
                        "s.assessmentOfFamilyLife as assessmentOfFamilyLife,"
                        "s.attitudeTowardsLGBT as attitudeTowardsLGBT,"
                        "s.freedomOfSpeech as freedomOfSpeech,"
                        "com.communicationOnEnglish as communicationOnEnglish,"
                        "i.freeWifi as freeWifi,"
                        "i.speedOfInternetMbps as speedOfInternetMbps,"
                        "cur.name as nameMoney,"
                        "cur.oneDollarEquals as oneDollarEquals, "
                        "po.count as count,"
                        "po.speedOfLife as speedOfLife,"
                        "po.nightLifeEntertainment as nightLifeEntertainment,"
                        "po.workPlaces as workPlaces,"
                        "l.name as nameLan", name=name)
        return [{'name': info["nameCountry"],
                 'comfortableToSpendTimeInTheCity': info['comfortableToSpendTimeInTheCity'],
                 'friendlyToForeigners': info['friendlyToForeigners'],
                 'globalRank': info['globalRank'],
                 'assessmentOfFamilyLife': info['assessmentOfFamilyLife'],
                 'attitudeTowardsLGBT': info['attitudeTowardsLGBT'],
                 'freedomOfSpeech': info['freedomOfSpeech'],
                 'communicationOnEnglish': info['communicationOnEnglish'],
                 'freeWifi': info['freeWifi'],
                 'speedOfInternetMbps': info['speedOfInternetMbps'],
                 'nameMoney': info['nameMoney'],
                 'oneDollarEquals': info['oneDollarEquals'],
                 'count': info['count'],
                 'speedOfLife': info['speedOfLife'],
                 'workPlaces': info['workPlaces'],
                 'nightLifeEntertainment': info['nightLifeEntertainment'],
                 'nameLan': info['nameLan']} for info in result]

    @staticmethod
    def _english(tx):
        result = tx.run("match (h:Country)-[:communication]->(n:Communication) return "
                        "h.name as nameCountry,"
                        "n.communicationOnEnglish as communicationOnEnglish")
        return [{'nameCountry': info["nameCountry"], 'communicationOnEnglish': info['communicationOnEnglish']} for info
                in result]

    @staticmethod
    def _globalrank(tx):
        # чем больше тем хуже
        result = tx.run("match (h:Country)-[:citizenship]->(n:Citizenship) return "
                        "h.name as nameCountry,"
                        "n.globalRank as globalRank")
        return [{'nameCountry': info["nameCountry"], 'globalRank': info['globalRank']} for info
                in result]

    @staticmethod
    def _transport(tx):
        result = tx.run("match (h:Country)-[:transport]->(n:Transport) return "
                        "h.name as nameCountry,"
                        "n.developmentLevelOfPublicTransport as developmentLevelOfPublicTransport")
        return [{'nameCountry': info["nameCountry"],
                 'developmentLevelOfPublicTransport': info['developmentLevelOfPublicTransport']} for info
                in result]

    @staticmethod
    def _lgbt(tx):
        result = tx.run("match (h:Country)-[:security]->(n:Security) return "
                        "h.name as nameCountry,"
                        "n.attitudeTowardsLGBT as attitudeTowardsLGBT")
        return [{'nameCountry': info["nameCountry"],
                 'attitudeTowardsLGBT': info['attitudeTowardsLGBT']} for info
                in result]

    @staticmethod
    def _life_type(tx):
        result = tx.run("match (h:Country)-[:population]->(n:Population) return "
                        "h.name as nameCountry,"
                        "n.nightLifeEntertainment as nightLifeEntertainment,"
                        "n.speedOfLife as speedOfLife,"
                        "n.workPlaces as workPlaces")
        return [{'nameCountry': info["nameCountry"],
                 'nightLifeEntertainment': info['nightLifeEntertainment'],
                 'speedOfLife': info['speedOfLife'],
                 'workPlaces': info['workPlaces']} for info
                in result]


country_migration_db = CountryMigration()

if __name__ == "__main__":
    c = country_migration_db.findClimat()
    for i in c:
        z = (i['airPollution'] + i['waterPollution'] + i['dirtyAndUntidy']) // 3
        x = i['comfortableToSpendTimeInTheCity']
        if i['decemberAverageTemperature'] == 0: i['decemberAverageTemperature'] = -1
        y = (((i['averageDurationOfWinter'] * i['decemberAverageTemperature']) / 2) + i['juneAverageTemperature']) / 2
        if i['averageDurationOfWinter'] == 0: y = (i['decemberAverageTemperature'] + i['juneAverageTemperature']) / 2

        print(i['name'], z, "грязь\n", x, "комфорт\n", y, "температура")
    print('+++++++++++++')
    # c = country_migration_db.findcity("Canada")
    c = country_migration_db.findisb('True')
    w = country_migration_db.findOcean()
    print(w)

    print(c)
    print(country_migration_db.findinfocountry("Canada"))
    print(country_migration_db.findinfocountry("United Arab Emirates"))
