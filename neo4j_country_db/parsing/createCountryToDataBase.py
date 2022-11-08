from neo4j import GraphDatabase
from parsingInfoForDataBase import crimeThingForCountry, climatForCountry, costOfLivingForCountry, healthForCountry


def formParams(dict):
    params = '{'
    for key, value in dict.items():
        params += '%s: %s, ' % (key, str(value))
    params = params[:-2] + '}'
    return params


class CountryCreator:

    def __init__(self):
        self.driver = GraphDatabase.driver("bolt://localhost:7999", auth=("neo4j", "admin"))

    def close(self):
        self.driver.close()

    def createBase(self, countryName,
                   citiesDict, languageName,
                   # currency
                   currencyName, currencyEqualsToDollar,
                   # military
                   milPolBlock, amountOfPeopleInArmy,
                   # healthcare
                   numberOfDoctorsPer100kPopulation, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                   # climat
                   juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                   averageDurationOfWinter, averageRainfallPerMonth, averageNumberOfFoggyDaysPerYear,
                   averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,
                   # security
                   situationInTheCountry, freedomOfSpeech,
                   assessmentOfFamilyLife, attitudeTowardsLGBT,
                   # population
                   populationCount, procentOfMales, procentOfFemales, populationDensityPerSquareKilometer,
                   speedOfLife, workPlaces, nightLifeEntertainment,
                   # citizenship
                   citizenshipGlobalRank,
                   # communication
                   communicationOnEnglish,
                   # transport
                   averageTravelTimeToWork, developmentLevelOfPublicTransport,
                   # internet
                   speedOfInternetMbps, freeWifi,
                   # education
                   rankingOfNationalEducationSystem
                   ):
        with self.driver.session() as session:
            base = session.execute_write(self._createBase, countryName,
                                         citiesDict, languageName,
                                         # currency
                                         currencyName, currencyEqualsToDollar,
                                         # military
                                         milPolBlock, amountOfPeopleInArmy,
                                         # healthcare
                                         numberOfDoctorsPer100kPopulation, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                                         # climat
                                         juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                                         averageDurationOfWinter, averageRainfallPerMonth,
                                         averageNumberOfFoggyDaysPerYear,
                                         averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,
                                         # security
                                         situationInTheCountry, freedomOfSpeech,
                                         assessmentOfFamilyLife, attitudeTowardsLGBT,
                                         # # population
                                         populationCount, procentOfMales, procentOfFemales, populationDensityPerSquareKilometer,
                                         speedOfLife, workPlaces, nightLifeEntertainment,
                                         # citizenship
                                         citizenshipGlobalRank,
                                         # communication
                                         communicationOnEnglish,
                                         # transport
                                         averageTravelTimeToWork, developmentLevelOfPublicTransport,
                                         # internet
                                         speedOfInternetMbps, freeWifi,
                                         # education
                                         rankingOfNationalEducationSystem
                                         )
            return base

    @staticmethod
    def _createBase(tx, countryName,
                    citiesDict, languageName,
                    # currency
                    currencyName, currencyEqualsToDollar,
                    #military
                    milPolBlock, amountOfPeopleInArmy,
                    # healthcare
                    numberOfDoctorsPer100kPopulation, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                    # climat
                    juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                    averageDurationOfWinter, averageRainfallPerMonth, averageNumberOfFoggyDaysPerYear,
                    averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,
                    #
                    # security
                    situationInTheCountry, freedomOfSpeech,
                    assessmentOfFamilyLife, attitudeTowardsLGBT,
                    #
                    #population
                    populationCount, procentOfMales, procentOfFemales, populationDensityPerSquareKilometer,
                    speedOfLife, workPlaces, nightLifeEntertainment,
                    # citizenship
                    citizenshipGlobalRank,
                    # communication
                    communicationOnEnglish,
                    # transport
                    averageTravelTimeToWork, developmentLevelOfPublicTransport,
                    # internet
                    speedOfInternetMbps, freeWifi,
                    #education
                    rankingOfNationalEducationSystem
                    ):
        # country
        resultStr = 'create (country:Country {name:"%s"})' % (str(countryName))
        # Crime
        crime = crimeThingForCountry(countryName)
        crimeParams = formParams(crime)
        resultStr += '\ncreate (crime:CrimeThing %s)\n' % crimeParams
        resultStr += 'create (country)-[:crime_indices]->(crime)\n'
        # Climat
        climat = climatForCountry(countryName)
        climatParams = '{'
        for key, value in climat.items():
            climatParams += '%s: %s, ' % (key, str(value))
        climatParams += 'juneAverageTemperature: %s, ' % juneAverageTemperature
        climatParams += 'decemberAverageTemperature: %s, ' % decemberAverageTemperature
        climatParams += 'averageHumidity: %s, ' % averageHumidity
        climatParams += 'averageDurationOfWinter: %s, ' % averageDurationOfWinter
        climatParams += 'averageRainfallPerMonth: %s, ' % averageRainfallPerMonth
        climatParams += 'averageNumberOfFoggyDaysPerYear: %s, ' % averageNumberOfFoggyDaysPerYear
        climatParams += 'averageNumberOfRainyDaysPerYear: %s, ' % averageNumberOfRainyDaysPerYear
        climatParams += 'averageNumberOfClearDays: %s, ' % averageNumberOfClearDays
        climatParams = climatParams[:-2] + '}'
        resultStr += 'create (climat:Climat %s)\n' % (climatParams)
        resultStr += 'create (country)-[:climat]->(climat)\n'
        # economic situation
        resultStr += 'create (economicSituation:EconomicSituation)'
        economicList = costOfLivingForCountry(countryName)
        restaurantsParams = formParams(economicList[0])
        marketsParams = formParams(economicList[1])
        transportationParams = formParams(economicList[2])
        utilitiesParams = formParams(economicList[3])
        sportsParams = formParams(economicList[4])
        childcareParams = formParams(economicList[5])
        clothingParams = formParams(economicList[6])
        rentParams = formParams(economicList[7])
        buyParams = formParams(economicList[8])
        salariesParams = formParams(economicList[9])
        resultStr += '\ncreate (restaurantsPrices:RestaurantsPrices %s)' % restaurantsParams
        resultStr += '\ncreate (economicSituation)-[:prices_in_restaurants]->(restaurantsPrices)'
        resultStr += '\ncreate (marketsPrices:MarketsPrices %s)' % marketsParams
        resultStr += '\ncreate (economicSituation)-[:prices_in_markets]->(marketsPrices)'
        resultStr += '\ncreate (transportationPrices:TransportationPrices %s)' % transportationParams
        resultStr += '\ncreate (economicSituation)-[:transportation_prices]->(transportationPrices)'
        resultStr += '\ncreate (utilitiesPrices:UtilitiesPrices %s)' % utilitiesParams
        resultStr += '\ncreate (economicSituation)-[:utilities_prices]->(utilitiesPrices)'
        resultStr += '\ncreate (sportsPrices:SportsPrices %s)' % sportsParams
        resultStr += '\ncreate (economicSituation)-[:sports_prices]->(sportsPrices)'
        resultStr += '\ncreate (childcarePrices:ChildcarePrices %s)' % childcareParams
        resultStr += '\ncreate (economicSituation)-[:childcare_prices]->(childcarePrices)'
        resultStr += '\ncreate (clothingPrices:ClothingPrices %s)' % clothingParams
        resultStr += '\ncreate (economicSituation)-[:clothing_prices]->(clothingPrices)'
        resultStr += '\ncreate (rentPrices:RentPrices %s)' % rentParams
        resultStr += '\ncreate (economicSituation)-[:rent_prices]->(rentPrices)'
        resultStr += '\ncreate (buyPrices:BuyPrices %s)' % buyParams
        resultStr += '\ncreate (economicSituation)-[:buy_prices]->(buyPrices)'
        resultStr += '\ncreate (salaries:Salaries %s)' % salariesParams
        resultStr += '\ncreate (economicSituation)-[:salaries]->(salaries)'
        resultStr += '\ncreate (country)-[:economic_situation]->(economicSituation)'
        # healthcare
        healthDict = healthForCountry(countryName)
        healthParams = '{'
        for key, value in healthDict.items():
            healthParams += '%s: %s, ' % (key, str(value))
        healthParams += 'numberOfDoctorsPer100kPopulation: %s, ' % numberOfDoctorsPer100kPopulation
        healthParams += 'menAverageLifeExpectancy: %s, ' % menAverageLifeExpectancy
        healthParams += 'womenAverageLifeExpectancy: %s, ' % womenAverageLifeExpectancy
        healthParams = healthParams[:-2] + '}'
        resultStr += 'create (health:HealthCare %s)\n' % healthParams
        resultStr += 'create (country)-[:healthcare]->(health)\n'

        # cities
        index = 1
        for city in citiesDict:
            resultStr += '\ncreate (city%d:City {name:"%s", isBig:"%s"})' % (index, city, str(citiesDict[city][0]))
            resultStr += '\ncreate (country)-[:has_city]->(city%d)' % index
            if index == 1:
                resultStr += '\ncreate (country)-[:capital]->(city%d)' % index
            if citiesDict[city][1] is not None:
                resultStr += '\ncreate(ocean%d:Ocean {name:"%s"})' % (index, str(citiesDict[city][1]))
                resultStr += '\ncreate (ocean%d)-[:washes]->(city%d)' % (index, index)
            index += 1

        # language
        resultStr += '\ncreate (language:Language {name:"%s"})' % (str(languageName))
        resultStr += '\ncreate (country)-[:official_language]->(language)'
        # currency
        resultStr += '\ncreate (currency:Currency {name:"%s", oneDollarEquals:%s})' % (str(currencyName), currencyEqualsToDollar)
        resultStr += '\ncreate (country)-[:currency]->(currency)'
        # military political block
        resultStr += '\ncreate (militaryPoliticalBlock:MilitaryPoliticalBlock {name:"%s"})' % (str(milPolBlock))
        resultStr += '\ncreate (country)-[:belongs_to_military_political_block]->(militaryPoliticalBlock)'
        # military Power
        resultStr += '\ncreate (militaryPower:MilitaryPower {amountOfPeople:"%d"})' % amountOfPeopleInArmy
        resultStr += '\ncreate (country)-[:military_power]->(militaryPower)'
        # security
        resultStr += '\ncreate (security:Security {situationInTheCountry:%d, freedomOfSpeech:%d,' \
                     ' assessmentOfFamilyLife:%d, attitudeTowardsLGBT:%d})' % (situationInTheCountry, freedomOfSpeech,
                                                                         assessmentOfFamilyLife, attitudeTowardsLGBT)
        resultStr += '\ncreate (country)-[:security]->(security)'

        # population
        resultStr += '\ncreate (population:Population {count:%i, procentOfMales:%s, procentOfFemales:%s, populationDensityPerSquareKilometer:%d,' \
                     ' speedOfLife:%d, workPlaces:%d, nightLifeEntertainment:%d})' \
                     % (populationCount, procentOfMales, procentOfFemales, populationDensityPerSquareKilometer, speedOfLife, workPlaces, nightLifeEntertainment)
        resultStr += '\ncreate (country)-[:population]->(population)'
        #
        # citizenship
        resultStr += '\ncreate (citizenship:Citizenship {globalRank:%d})' % (citizenshipGlobalRank)
        resultStr += '\ncreate (country)-[:citizenship]->(citizenship)'
        # communication
        resultStr += '\ncreate (communication:Communication {communicationOnEnglish:%d})' % (communicationOnEnglish)
        resultStr += '\ncreate (country)-[:communication]->(communication)'
        # transport
        resultStr += '\ncreate (transport:Transport {averageTravelTimeToWork:%d, developmentLevelOfPublicTransport:%d})' \
                     % (averageTravelTimeToWork, developmentLevelOfPublicTransport)

        resultStr += '\ncreate (country)-[:transport]->(transport)'

        # internet
        resultStr += '\ncreate (internet:Internet {speedOfInternetMbps:%d, freeWifi:%d})' % (speedOfInternetMbps, freeWifi)
        resultStr += '\ncreate (country)-[:internet]->(internet)'

        # education
        resultStr += '\ncreate (education:Education {rankingOfNationalEducationSystem:%d})' % rankingOfNationalEducationSystem
        resultStr += '\ncreate (country)-[:education]->(education)'
        result = tx.run(resultStr)


    def createManMadeDisaster(self, countryName, nameOfDisaster, typeOfMMD, aomuntOfDeadPeople,
                  aomuntOfInjuredPeople, territoryOfPollution):
        with self.driver.session() as session:
            manMadeDisaster = session.execute_write(self._createManMadeDisaster, countryName, nameOfDisaster, typeOfMMD,
                                                    aomuntOfDeadPeople, aomuntOfInjuredPeople, territoryOfPollution)
            return manMadeDisaster

    @staticmethod
    def _createManMadeDisaster(tx, countryName, nameOfDisaster, typeOfMMD, aomuntOfDeadPeople,
                               aomuntOfInjuredPeople, territoryOfPollution):
        resultStr = 'match (country:Country {name:"%s"}' % countryName
        resultStr += '\nmatch (country)->[:climat]->(climat)'
        resultStr += 'create (manMadeDisaster:ManMadeDisaster {name:"%s", typeOfMMD:"%s", aomuntOfDeadPeople:"%d",' \
                     '                                         aomuntOfInjuredPeople:"%d", territoryOfPollution:"%d km^2"})' % (nameOfDisaster, typeOfMMD, aomuntOfDeadPeople,
                                                                                                                                aomuntOfInjuredPeople, territoryOfPollution)
        resultStr += 'create (climat)-[:man_made_disaster]->(manMadeDisaster)'

        result = tx.run(resultStr)

    def createOceans(self):
        with self.driver.session() as session:
            oceans = session.execute_write(self._createOceans)
            return oceans

    @staticmethod
    def _createOceans(tx):
        request = '''
        match (city1:City {name:"Quebec"})
        match (city2:City {name:"Vancouver"})
        create (ocean1:Ocean {name: "Pacific"})
        create (ocean2:Ocean {name: "Atlantic"})
        create (ocean2)-[:washes]->(city1)
        create (ocean1)-[:washes]->(city2)\n'''
        result = tx.run(request)

    def createBorders(self):
        with self.driver.session() as session:
            borders = session.execute_write(self._createBorders)
            return borders

    @staticmethod
    def _createBorders(tx):
        request = '''
        match (canada:Country {name:"Canada"})
        match (poland:Country {name:"Poland"})
        match (germany:Country {name:"Germany"})
        match (czech:Country {name:"Czech"})
        match (slovakia:Country {name:"Slovakia"})
        
        create (poland)-[:borders_with]->(czech)
        create (czech)-[:borders_with]->(poland)
        
        create (poland)-[:borders_with]->(germany)
        create (germany)-[:borders_with]->(poland)
        
        create (czech)-[:borders_with]->(germany)
        create (germany)-[:borders_with]->(czech)
        
        create (slovakia)-[:borders_with]->(poland)
        create (poland)-[:borders_with]->(slovakia)
        
        create (slovakia)-[:borders_with]->(czech)
        create (czech)-[:borders_with]->(slovakia)  
        
        \n'''
        result = tx.run(request)


if __name__ == "__main__":
    cc = CountryCreator()

    #############################   CANADA   #############################

    # Country
    countryName = "Canada"
    officialLanguage = "English"

    # cities    name   isBig  washesBy
    cities = {'Ottawa': [True, None], 'Toronto': [True, None], 'Montreal': [True, None],
              'Quebec': [True, 'Atlantic ocean'], 'Vancouver': [True, 'Pacific ocean']}

    # education
    universities = {'Ottawa': ['Carleton University', 'University of Ottawa'],
                    'Toronto': ['York University', 'University of Toronto'],
                    'Montreal': ['Montreal university', 'Polytechnique Montreal'],
                    'Quebec': ['Laval University', 'TELUQ University'],
                    'Vancouver': ['University of British Columbia', 'University Canada West']}
    faculties = {'Carleton University': ['Faculty of Arts and Social Sciences', 'Faculty of Engineering and Design',
                                         'Faculty of Public Affairs', 'Faculty of Science'], }

    # currency
    currencyName = 'CAD'
    currencyEqualsToDollar = 0.73

    # military
    milPolBlock = "NATO"
    amountOfPeopleInArmy = 92000

    # healthcare
    numberOfDoctorsPer100kPopulation = 241
    menAverageLifeExpectancy = 78.8
    womenAverageLifeExpectancy = 84.1

    # climat
    juneAverageTemperature = 20
    decemberAverageTemperature = 4.5
    averageHumidity = 73
    averageDurationOfWinter = 3.5
    averageRainfallPerMonth = 104
    averageNumberOfFoggyDaysPerYear = 47
    averageNumberOfRainyDaysPerYear = 63
    averageNumberOfClearDays = 119

    # Man-made disasters
    nameMMD = '0'
    typeOfMMD = '0'
    aomuntOfDeadPeople = 0
    aomuntOfInjuredPeople = 0
    territoryOfPollution = 0
    # manMadeDisaster = {'name': 'Авария на ЧАЭС', 'typeOfMMD': 'Авария на АЭС', 'aomuntOfDeadPeople': 37500,
    #                    'aomuntOfInjuredPeople': 5000000, 'territoryOfPollution': 145000}


    # security
    situationInTheCountry = 3  # [1, 3] 1-bad, 3-good
    freedomOfSpeech = 3  # [1, 3]
    assessmentOfFamilyLife = 3  # [1, 3]
    attitudeTowardsLGBT = 3  # [1, 3]

    # population
    populationCount = 38010000
    procentOfMales = 49.6
    procentOfFemales = 50.4
    populationDensityPerSquareKilometer = 4.2
    speedOfLife = 3  # [1, 3]
    workPlaces = 3  # [1, 3]
    nightLifeEntertainment = 3  # [1, 3]

    # citizenship
    citizenshipGlobalRank = 7

    # communication
    communicationOnEnglish = 3  # [1, 3]

    # transport
    averageTravelTimeToWork = 54
    developmentLevelOfPublicTransport = 3  # [1, 3]

    # internet
    speedOfInternetMbps = 52.4  # Мегабиты в секунду
    freeWifi = 2  # [1, 3]

    # education
    rankingOfNationalEducationSystem = 83.2

    cc.createBase(countryName, cities, officialLanguage,
                  # currency
                  currencyName, currencyEqualsToDollar,
                  # military
                  milPolBlock, amountOfPeopleInArmy,
                  # healthcare
                  numberOfDoctorsPer100kPopulation, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                  # climat
                  juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                  averageDurationOfWinter, averageRainfallPerMonth, averageNumberOfFoggyDaysPerYear,
                  averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,
                  # security
                  situationInTheCountry, freedomOfSpeech,
                  assessmentOfFamilyLife, attitudeTowardsLGBT,
                  # population
                  populationCount, procentOfMales, procentOfFemales, populationDensityPerSquareKilometer,
                  speedOfLife, workPlaces, nightLifeEntertainment,
                  # citizenship
                  citizenshipGlobalRank,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,
                  # education
                  rankingOfNationalEducationSystem
                  )
    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()
    #############################   CANADA   #############################


    #############################   POLAND   #############################

    # Country
    countryName = "Poland"
    officialLanguage = "Polish"

    # cities    name   isBig
    cities = {'Warsaw': [True, None], 'Krakow': [True, None], 'Lodz': [True, None],
              'Wroclaw': [True, None], 'Bialystok': [True, None]}

    # education
    universities = {'Warsaw': ['University of Economics and Humanities in Warsaw', 'University of Engineering and Health'],  # https://univerpl.com.ua/ru/universiteti-varshavi/
                    'Krakow': ['Jagiellonian University', 'Krakow Academy named after A.F. Modzhevsky'],  # https://univerpl.com.ua/ru/universiteti-krakova/
                    'Lodz': ['Łódź University of Technology', 'University of Lodz'],
                    'Wroclaw': ['Wrocław University of Science and Technology', 'University of Wrocław'],
                    'Bialystok': ['Bialystok Technical University', 'Medical University of Białystok']}
    faculties = {'University of Engineering and Health': ['Internet programs', 'IT in administration',
                                                          'internal security', 'public finance'], }

    # currency
    currencyName = 'PLN'
    currencyEqualsToDollar = 0.21

    # military
    milPolBlock = "NATO"
    amountOfPeopleInArmy = 125500

    # healthcare
    numberOfDoctorsPer100kPopulation = 227
    menAverageLifeExpectancy = 74  # years
    womenAverageLifeExpectancy = 82  # years

    # climat
    juneAverageTemperature = 21.9  # °C
    decemberAverageTemperature = 0  # °C
    averageHumidity = 71.25  # %
    averageDurationOfWinter = 3  # month
    averageRainfallPerMonth = 600  # mm (?)
    averageNumberOfFoggyDaysPerYear = 156  # days
    averageNumberOfRainyDaysPerYear = 136  # days
    averageNumberOfClearDays = 73  # days

    # Man-made disasters
    nameMMD = 'Warsaw gas explosion'
    typeOfMMD = 'gas explosion'
    yearOfMMD = 1979
    aomuntOfDeadPeople = 49
    aomuntOfInjuredPeople = 135
    territoryOfPollution = 0
    # manMadeDisaster = {'name': 'Авария на ЧАЭС', 'typeOfMMD': 'Авария на АЭС', 'aomuntOfDeadPeople': 37500,
    #                    'aomuntOfInjuredPeople': 5000000, 'territoryOfPollution': 145000}

    # security
    situationInTheCountry = 3  # [1, 3] 1-bad, 3-good
    freedomOfSpeech = 3  # [1, 3]
    assessmentOfFamilyLife = 2  # [1, 3]
    attitudeTowardsLGBT = 1  # [1, 3]

    # population
    populationCount = 37780000
    procentOfMales = 48.2
    procentOfFemales = 51.8
    populationDensityPerSquareKilometer = 121.2
    speedOfLife = 2  # [1, 3]
    workPlaces = 3  # [1, 3]
    nightLifeEntertainment = 2  # [1, 3]

    # citizenship
    citizenshipGlobalRank = 3

    # communication
    communicationOnEnglish = 3  # [1, 3]

    # transport
    averageTravelTimeToWork = 45
    developmentLevelOfPublicTransport = 3  # [1, 3]

    # internet
    speedOfInternetMbps = 85  # Мегабиты в секунду
    freeWifi = 2  # [1, 3]

    # education
    rankingOfNationalEducationSystem = 52.6

    cc.createBase(countryName, cities, officialLanguage,
                  # currency
                  currencyName, currencyEqualsToDollar,
                  # military
                  milPolBlock, amountOfPeopleInArmy,
                  # healthcare
                  numberOfDoctorsPer100kPopulation, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                  # climat
                  juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                  averageDurationOfWinter, averageRainfallPerMonth, averageNumberOfFoggyDaysPerYear,
                  averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,
                  # security
                  situationInTheCountry, freedomOfSpeech,
                  assessmentOfFamilyLife, attitudeTowardsLGBT,
                  # population
                  populationCount, procentOfMales, procentOfFemales, populationDensityPerSquareKilometer,
                  speedOfLife, workPlaces, nightLifeEntertainment,
                  # citizenship
                  citizenshipGlobalRank,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,
                  # education
                  rankingOfNationalEducationSystem
                  )
    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()

    #############################   POLAND   #############################

    #############################   CZECH   ##############################

    # Country
    countryName = "Czech"
    officialLanguage = "Czech"

    # cities    name   isBig
    cities = {'Prague': [True, None], 'Brno': [True, None], 'Pilsen': [True, None],
              'Ostrava': [True, None], 'Olomouc': [True, None]}

    # education
    universities = {'Prague': ['Czech Technical University in Prague', 'Charles University'],
                    'Brno': ['Brno University of Technology', 'Masaryk University'],
                    'Pilsen': ['University of West Bohemia', 'Charles University'],
                    'Ostrava': ['University of Ostrava', 'Ostrava University of Technology'],
                    'Olomouc': ['Olomouc University', 'Palacký University Olomouc']}
    faculties = {'Czech Technical University in Prague': ['Architecture and construction', 'Software Engineering and Technology',
                                                          'Applied Informatics', 'Design'], }

    # currency
    currencyName = 'CZK'
    currencyEqualsToDollar = 0.04

    # military
    milPolBlock = "NATO"
    amountOfPeopleInArmy = 24900

    # healthcare
    numberOfDoctorsPer100kPopulation = 369
    menAverageLifeExpectancy = 73.9  # years
    womenAverageLifeExpectancy = 80.7  # years

    # climat
    juneAverageTemperature = 18  # °C
    decemberAverageTemperature = 0  # °C
    averageHumidity = 77  # %
    averageDurationOfWinter = 4  # month
    averageRainfallPerMonth = 525  # mm (?)
    averageNumberOfFoggyDaysPerYear = 157  # days
    averageNumberOfRainyDaysPerYear = 135  # days
    averageNumberOfClearDays = 73  # days

    # Man-made disasters
    nameMMD = ''
    typeOfMMD = ''
    yearOfMMD = 0
    aomuntOfDeadPeople = 0
    aomuntOfInjuredPeople = 0
    territoryOfPollution = 0
    # manMadeDisaster = {'name': 'Авария на ЧАЭС', 'typeOfMMD': 'Авария на АЭС', 'aomuntOfDeadPeople': 37500,
    #                    'aomuntOfInjuredPeople': 5000000, 'territoryOfPollution': 145000}

    # security
    situationInTheCountry = 3  # [1, 3] 1-bad, 3-good
    freedomOfSpeech = 3  # [1, 3]
    assessmentOfFamilyLife = 3  # [1, 3]
    attitudeTowardsLGBT = 2  # [1, 3]

    # population
    populationCount = 10700000
    procentOfMales = 49.1
    procentOfFemales = 50.9
    populationDensityPerSquareKilometer = 135.8
    speedOfLife = 2  # [1, 3]
    workPlaces = 3  # [1, 3]
    nightLifeEntertainment = 3  # [1, 3]

    # citizenship
    citizenshipGlobalRank = 4

    # communication
    communicationOnEnglish = 2  # [1, 3]

    # transport
    averageTravelTimeToWork = 20
    developmentLevelOfPublicTransport = 3  # [1, 3]

    # internet
    speedOfInternetMbps = 65  # Мегабиты в секунду
    freeWifi = 2  # [1, 3]

    # education
    rankingOfNationalEducationSystem = 54.8

    cc.createBase(countryName, cities, officialLanguage,
                  # currency
                  currencyName, currencyEqualsToDollar,
                  # military
                  milPolBlock, amountOfPeopleInArmy,
                  # healthcare
                  numberOfDoctorsPer100kPopulation, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                  # climat
                  juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                  averageDurationOfWinter, averageRainfallPerMonth, averageNumberOfFoggyDaysPerYear,
                  averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,
                  # security
                  situationInTheCountry, freedomOfSpeech,
                  assessmentOfFamilyLife, attitudeTowardsLGBT,
                  # population
                  populationCount, procentOfMales, procentOfFemales, populationDensityPerSquareKilometer,
                  speedOfLife, workPlaces, nightLifeEntertainment,
                  # citizenship
                  citizenshipGlobalRank,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,
                  # education
                  rankingOfNationalEducationSystem
                  )
    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()

    #############################   CZECH   #############################

    #############################   GERMANY   #############################

    # Country
    countryName = "Germany"
    officialLanguage = "Deutsch"

    # cities    name   isBig
    cities = {'Berlin': [True, None], 'Hamburg': [True, None], 'Bremen': [True, None],
              'Dresden': [True, None], 'Nuremberg': [True, None]}

    # education
    universities = {'Berlin': ['Czech Technical University in Prague', 'Charles University'],
                    'Hamburg': ['Brno University of Technology', 'Masaryk University'],
                    'Bremen': ['University of West Bohemia', 'Charles University'],
                    'Dresden': ['University of Ostrava', 'Ostrava University of Technology'],
                    'Nuremberg': ['Olomouc University', 'Palacký University Olomouc']}
    faculties = {'Czech Technical University in Prague': ['Architecture and construction', 'Software Engineering and Technology',
                                                          'Applied Informatics', 'Design']}

    # currency
    currencyName = 'EUR'
    currencyEqualsToDollar = 1

    # military
    milPolBlock = "NATO"
    amountOfPeopleInArmy = 182832

    # healthcare
    numberOfDoctorsPer100kPopulation = 413
    menAverageLifeExpectancy = 77.2  # years
    womenAverageLifeExpectancy = 82.4  # years

    # climat
    juneAverageTemperature = 21  # °C
    decemberAverageTemperature = 0  # °C
    averageHumidity = 79  # %
    averageDurationOfWinter = 3  # month
    averageRainfallPerMonth = 625  # mm (?)
    averageNumberOfFoggyDaysPerYear = 89  # days
    averageNumberOfRainyDaysPerYear = 140  # days
    averageNumberOfClearDays = 136  # days

    # Man-made disasters
    nameMMD = ''
    typeOfMMD = ''
    yearOfMMD = 0
    aomuntOfDeadPeople = 0
    aomuntOfInjuredPeople = 0
    territoryOfPollution = 0
    # manMadeDisaster = {'name': 'Авария на ЧАЭС', 'typeOfMMD': 'Авария на АЭС', 'aomuntOfDeadPeople': 37500,
    #                    'aomuntOfInjuredPeople': 5000000, 'territoryOfPollution': 145000}

    # security
    situationInTheCountry = 3  # [1, 3] 1-bad, 3-good
    freedomOfSpeech = 3  # [1, 3]
    assessmentOfFamilyLife = 3  # [1, 3]
    attitudeTowardsLGBT = 3  # [1, 3]

    # population
    populationCount = 83130000
    procentOfMales = 49
    procentOfFemales = 51
    populationDensityPerSquareKilometer = 240
    speedOfLife = 2  # [1, 3]
    workPlaces = 3  # [1, 3]
    nightLifeEntertainment = 3  # [1, 3]

    # citizenship
    citizenshipGlobalRank = 3

    # communication
    communicationOnEnglish = 2  # [1, 3]

    # transport
    averageTravelTimeToWork = 42.1
    developmentLevelOfPublicTransport = 3  # [1, 3]

    # internet
    speedOfInternetMbps = 49  # Мегабиты в секунду
    freeWifi = 2  # [1, 3]

    # education
    rankingOfNationalEducationSystem = 70.5

    cc.createBase(countryName, cities, officialLanguage,
                  # currency
                  currencyName, currencyEqualsToDollar,
                  # military
                  milPolBlock, amountOfPeopleInArmy,
                  # healthcare
                  numberOfDoctorsPer100kPopulation, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                  # climat
                  juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                  averageDurationOfWinter, averageRainfallPerMonth, averageNumberOfFoggyDaysPerYear,
                  averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,
                  # security
                  situationInTheCountry, freedomOfSpeech,
                  assessmentOfFamilyLife, attitudeTowardsLGBT,
                  # population
                  populationCount, procentOfMales, procentOfFemales, populationDensityPerSquareKilometer,
                  speedOfLife, workPlaces, nightLifeEntertainment,
                  # citizenship
                  citizenshipGlobalRank,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,
                  # education
                  rankingOfNationalEducationSystem
                  )
    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()

    #############################   GERMANY   #############################

    #############################   SLOVAKIA   #############################

    # Country
    countryName = "Slovakia"
    officialLanguage = "Slovak"

    # cities    name   isBig
    cities = {'Bratislava': [True, None], 'Kosice': [True, None], 'Nitra': [True, None],
              'Presov': [True, None], 'Banska Bystrica': [True, None]}

    # education
    universities = {'Bratislava': ['Czech Technical University in Prague', 'Charles University'],
                    'Kosice': ['Brno University of Technology', 'Masaryk University'],
                    'Nitra': ['University of West Bohemia', 'Charles University'],
                    'Presov': ['University of Ostrava', 'Ostrava University of Technology'],
                    'Banska Bystrica': ['Olomouc University', 'Palacký University Olomouc']}
    faculties = {
        'Czech Technical University in Prague': ['Architecture and construction', 'Software Engineering and Technology',
                                                 'Applied Informatics', 'Design']}

    # currency
    currencyName = 'EUR'
    currencyEqualsToDollar = 1

    # military
    milPolBlock = "NATO"
    amountOfPeopleInArmy = 26200

    # healthcare
    numberOfDoctorsPer100kPopulation = 300
    menAverageLifeExpectancy = 75.8  # years
    womenAverageLifeExpectancy = 75.8  # years

    # climat
    juneAverageTemperature = 19.6  # °C
    decemberAverageTemperature = 1.7  # °C
    averageHumidity = 75  # %
    averageDurationOfWinter = 3.5  # month
    averageRainfallPerMonth = 580  # mm (?)
    averageNumberOfFoggyDaysPerYear = 70  # days
    averageNumberOfRainyDaysPerYear = 142  # days
    averageNumberOfClearDays = 153  # days

    # Man-made disasters
    nameMMD = ''
    typeOfMMD = ''
    yearOfMMD = 0
    aomuntOfDeadPeople = 0
    aomuntOfInjuredPeople = 0
    territoryOfPollution = 0
    # manMadeDisaster = {'name': 'Авария на ЧАЭС', 'typeOfMMD': 'Авария на АЭС', 'aomuntOfDeadPeople': 37500,
    #                    'aomuntOfInjuredPeople': 5000000, 'territoryOfPollution': 145000}

    # security
    situationInTheCountry = 3  # [1, 3] 1-bad, 3-good
    freedomOfSpeech = 3  # [1, 3]
    assessmentOfFamilyLife = 3  # [1, 3]
    attitudeTowardsLGBT = 2  # [1, 3]

    # population
    populationCount = 5447000
    procentOfMales = 49
    procentOfFemales = 51
    populationDensityPerSquareKilometer = 114
    speedOfLife = 2  # [1, 3]
    workPlaces = 2  # [1, 3]
    nightLifeEntertainment = 3  # [1, 3]

    # citizenship
    citizenshipGlobalRank = 9

    # communication
    communicationOnEnglish = 1  # [1, 3]

    # transport
    averageTravelTimeToWork = 44.3
    developmentLevelOfPublicTransport = 2  # [1, 3]

    # internet
    speedOfInternetMbps = 45.47  # Мегабиты в секунду
    freeWifi = 2  # [1, 3]

    # education
    rankingOfNationalEducationSystem = 70.5

    cc.createBase(countryName, cities, officialLanguage,
                  # currency
                  currencyName, currencyEqualsToDollar,
                  # military
                  milPolBlock, amountOfPeopleInArmy,
                  # healthcare
                  numberOfDoctorsPer100kPopulation, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                  # climat
                  juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                  averageDurationOfWinter, averageRainfallPerMonth, averageNumberOfFoggyDaysPerYear,
                  averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,
                  # security
                  situationInTheCountry, freedomOfSpeech,
                  assessmentOfFamilyLife, attitudeTowardsLGBT,
                  # population
                  populationCount, procentOfMales, procentOfFemales, populationDensityPerSquareKilometer,
                  speedOfLife, workPlaces, nightLifeEntertainment,
                  # citizenship
                  citizenshipGlobalRank,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,
                  # education
                  rankingOfNationalEducationSystem
                  )
    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()

    #############################   SLOVAKIA   #############################

    cc.createBorders()
    cc.close()
