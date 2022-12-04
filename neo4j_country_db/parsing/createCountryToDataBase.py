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
        self.driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "3777"))

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
                   rankingOfNationalEducationSystem, universities, faculties
                   ):
        with self.driver.session() as session:
            base = session.execute_write(self._createBase, countryName,
                                         citiesDict, languageName,
                                         # currency
                                         currencyName, currencyEqualsToDollar,
                                         # military
                                         milPolBlock, amountOfPeopleInArmy,
                                         # healthcare
                                         numberOfDoctorsPer100kPopulation, menAverageLifeExpectancy,
                                         womenAverageLifeExpectancy,
                                         # climat
                                         juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                                         averageDurationOfWinter, averageRainfallPerMonth,
                                         averageNumberOfFoggyDaysPerYear,
                                         averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,
                                         # security
                                         situationInTheCountry, freedomOfSpeech,
                                         assessmentOfFamilyLife, attitudeTowardsLGBT,
                                         # # population
                                         populationCount, procentOfMales, procentOfFemales,
                                         populationDensityPerSquareKilometer,
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
                                         rankingOfNationalEducationSystem, universities, faculties
                                         )
            return base

    @staticmethod
    def _createBase(tx, countryName,
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
                    #
                    # security
                    situationInTheCountry, freedomOfSpeech,
                    assessmentOfFamilyLife, attitudeTowardsLGBT,
                    #
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
                    rankingOfNationalEducationSystem, universities, faculties
                    ):
        # country
        resultStr = 'create (country:Country {name:"%s"})' % (str(countryName))
        # Crime
        crime = crimeThingForCountry(countryName)
        crimeParams = formParams(crime)
        resultStr += '\ncreate (crime:CrimeThing %s)\n' % crimeParams
        resultStr += 'create (country)-[:crime_indexes]->(crime)\n'
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
        resultStr += 'create (climat:Climat %s)\n' % climatParams
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
        resultStr += 'create (country)-[:healthcare]->(health)'

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
        # education
        resultStr += '\ncreate (education:Education {rankingOfNationalEducationSystem:%d})' % rankingOfNationalEducationSystem
        resultStr += '\ncreate (country)-[:education]->(education)\n'

        index = 1
        fac = 1
        ind = 1
        for city in citiesDict:
            for univ in universities[city]:
                resultStr += '\ncreate (univ%d:University {name:"%s"})' % (ind, univ)
                for faculty in faculties[univ]:
                    resultStr += '\ncreate (faculty%d:Faculty {name:"%s"})' % (fac, faculty)
                    resultStr += '\ncreate (univ%d)-[:faculty]->(faculty%d)' % (ind, fac)
                    fac += 1
                resultStr += '\ncreate (city%d)-[:university]->(univ%d)' % (index, ind)
                ind += 1
            index += 1

        # language
        resultStr += '\ncreate (language:Language {name:"%s"})' % (str(languageName))
        resultStr += '\ncreate (country)-[:official_language]->(language)'
        # currency
        resultStr += '\ncreate (currency:Currency {name:"%s", oneDollarEquals:%s})' % (
        str(currencyName), currencyEqualsToDollar)
        resultStr += '\ncreate (country)-[:currency]->(currency)'
        # military political block
        resultStr += '\ncreate (militaryPoliticalBlock:MilitaryPoliticalBlock {name:"%s"})' % (str(milPolBlock))
        resultStr += '\ncreate (country)-[:belongs_to_military_political_block]->(militaryPoliticalBlock)'
        # military Power
        resultStr += '\ncreate (militaryPower:MilitaryPower {amountOfPeople:%d})' % amountOfPeopleInArmy
        resultStr += '\ncreate (country)-[:military_power]->(militaryPower)'
        # security
        resultStr += '\ncreate (security:Security {situationInTheCountry:%d, freedomOfSpeech:%d,' \
                     ' assessmentOfFamilyLife:%d, attitudeTowardsLGBT:%d})' % (situationInTheCountry, freedomOfSpeech,
                                                                               assessmentOfFamilyLife,
                                                                               attitudeTowardsLGBT)
        resultStr += '\ncreate (country)-[:security]->(security)'

        # population
        resultStr += '\ncreate (population:Population {count:%i, procentOfMales:%s, procentOfFemales:%s, populationDensityPerSquareKilometer:%d,' \
                     ' speedOfLife:%d, workPlaces:%d, nightLifeEntertainment:%d})' \
                     % (populationCount, procentOfMales, procentOfFemales, populationDensityPerSquareKilometer,
                        speedOfLife, workPlaces, nightLifeEntertainment)
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
        resultStr += '\ncreate (internet:Internet {speedOfInternetMbps:%d, freeWifi:%d})' % (
        speedOfInternetMbps, freeWifi)
        resultStr += '\ncreate (country)-[:internet]->(internet)'
        print(resultStr)
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
        resultStr += 'create (manMadeDisaster:ManMadeDisaster {name:"%s", typeOfMMD:"%s", aomuntOfDeadPeople:%d,' \
                     '                                         aomuntOfInjuredPeople:%d, territoryOfPollution:"%d km^2"})' % (
                     nameOfDisaster, typeOfMMD, aomuntOfDeadPeople,
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
        match (hungary:Country {name:"Hungary"})
        match (uk:Country {name:"United Kingdom"})
        match (finland:Country {name:"Finland"})
        match (sweden:Country {name:"Sweden"})
        match (norway:Country {name:"Norway"})
        
        
        create (poland)-[:borders_with]->(czech)
        create (poland)-[:borders_with]->(germany)
        create (poland)-[:borders_with]->(slovakia)

        create (czech)-[:borders_with]->(poland)
        create (czech)-[:borders_with]->(germany)
        create (czech)-[:borders_with]->(slovakia)
        
        create (germany)-[:borders_with]->(poland)        
        create (germany)-[:borders_with]->(czech)
        
        create (slovakia)-[:borders_with]->(poland)      
        create (slovakia)-[:borders_with]->(czech)
        create (slovakia)-[:borders_with]->(hungary) 
        
        create (hungary)-[:borders_with]->(slovakia)
        
        create (finland)-[:borders_with]->(sweden)
        create (finland)-[:borders_with]->(norway)
        
        create (sweden)-[:borders_with]->(finland)
        create (sweden)-[:borders_with]->(norway)
        
        create (norway)-[:borders_with]->(finland)
        create (norway)-[:borders_with]->(sweden)

         
        
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
    faculties = {'Carleton University': ['Faculty of Arts', 'Faculty of Computer Engineering and Software', 'Faculty of Education',
                                         'Faculty of Public Affairs', 'Faculty of Science', 'Faculty of Social Sciences'],
                 'University of Ottawa': ['Faculty of Arts', 'Faculty of Engineering', 'Faculty of Education',
                                          'Faculty of Science', 'Faculty of Medicine', 'Faculty of Law', 'Faculty of Social Sciences'],
                 'York University': ['Faculty of Education', 'Faculty of Arts', 'Faculty of Medicine, Faculty of Science'],
                 'University of Toronto': ['Faculty of Arts', 'Faculty of Science', 'Faculty of Medicine', 'Faculty of Design'],
                 'Montreal university': ['Faculty of Arts', 'Faculty of Science', 'Faculty of Law', 'Faculty of Medicine',
                                         'Faculty of Education', 'Faculty of Design', 'Faculty of Kinesiology'],
                 'Polytechnique Montreal': ['Faculty of Computer Engineering and Software', 'Faculty of Science', 'Faculty of Biomedicine'],
                 'Laval University': ['Faculty of Arts', 'Faculty of Law', 'Faculty of Education', 'Faculty of Forestry', 'Faculty of Medicine'],
                 'TELUQ University': ['Faculty of Arts', 'Faculty of Science', 'Faculty of Medicine', 'Faculty of Design'],
                 'University of British Columbia': ['Faculty of Business', 'Faculty of Forestry', 'Faculty of Education',
                                                    'Faculty of Science', 'Faculty of Medicine', 'Faculty of Law', 'Faculty of Kinesiology'],
                 'University Canada West': ['Faculty of Arts', 'Faculty of Computer Engineering and Software', 'Faculty of Education',
                                            'Faculty of Public Affairs', 'Faculty of Science', 'Faculty of Social Sciences']}

    # currency
    currencyName = 'CAD'
    currencyEqualsToDollar = 1.33

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
                  rankingOfNationalEducationSystem, universities, faculties
                  )

    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()
    #############################   CANADA   #############################

    #############################   POLAND   #############################

    # Country
    countryName = "Poland"
    officialLanguage = "Polish"

    # cities    name    isBig WashesBy
    cities = {'Warsaw': [True, None], 'Krakow': [True, None], 'Lodz': [True, None],
              'Wroclaw': [True, None], 'Bialystok': [True, None]}

    # education
    universities = {
        'Warsaw': ['University of Economics and Human Sciences', 'University of Engineering and Health'],
        # https://univerpl.com.ua/ru/universiteti-varshavi/
        'Krakow': ['Jagiellonian University', 'Krakow Academy named after A.F. Modzhevsky'],
        # https://univerpl.com.ua/ru/universiteti-krakova/
        'Lodz': ['Łódź University of Technology', 'University of Lodz'],
        'Wroclaw': ['Wrocław University of Science and Technology', 'University of Wrocław'],
        'Bialystok': ['Bialystok Technical University', 'University of Bialystok']}

    faculties = {'University of Economics and Human Sciences': ['Faculty of Management', 'Faculty of Finance',
                                                                'Faculty of Psychology', 'Faculty of Computer Engineering and Software',
                                                                'Faculty of Political Science', 'Faculty of Dietetics'],
                 'University of Engineering and Health': ['Faculty of Administration and Social Sciences', 'Faculty of Architecture',
                                                          'Faculty of Engineering', 'Faculty of Chemistry',
                                                          'Faculty of Civil Engineering', 'Faculty of Electrical Engineering'],
                 'Jagiellonian University': ['Faculty of Law and Administration', 'Faculty of Medicine',
                                             'Faculty of Pharmacy', 'Faculty of Health Science', 'Faculty of Philosophy',
                                             'Faculty of History', 'Faculty of Philology'],
                 'Krakow Academy named after A.F. Modzhevsky': ['Faculty of Design of Aircraft', 'Faculty of Space Infrastructure',
                                                                'Faculty of Information Security', 'Faculty of Computer Science'],
                 'Łódź University of Technology': ['Faculty of Mechanical Engineering', 'Faculty of Electrical Engineering',
                                                   'Faculty of Chemistry', 'Faculty of Biotechnology',
                                                   'Faculty of Architecture', 'Faculty of Physics', 'Faculty of Management'],
                 'University of Lodz': ['Faculty of Biology', 'Faculty of Chemistry', 'Faculty of Economics',
                                        'Faculty of Sociology', 'Faculty of Philology', 'Faculty of Psychology',
                                        'Faculty of Computer Science', 'Faculty of Management'],
                 'Wrocław University of Science and Technology': ['Faculty of Architecture', 'Faculty of Chemistry',
                                                                  'Faculty of Electrical Engineering', 'Faculty of Management',
                                                                  'Faculty of Mechanical Engineering'],
                 'University of Wrocław': ['Faculty of Biotechnology', 'Faculty of Chemistry', 'Faculty of Physics',
                                           'Faculty of Computer Science', 'Faculty of Social Sciences', 'Faculty of Biology'],
                 'Bialystok Technical University': ['Faculty of Architecture', 'Faculty of Computer Science', 'Faculty of Electrical Engineering',
                                                    'Faculty of Engineering Management', 'Faculty of Mechanical Engineering'],
                 'University of Bialystok': ['Faculty of Biology', 'Faculty of Chemistry', 'Faculty of Economics and Finance',
                                             'Faculty of Philology', 'Faculty of Physics', 'Faculty of History',
                                             'Faculty of Computer Science', 'Faculty of Management']}

    # currency
    currencyName = 'PLN'
    currencyEqualsToDollar = 4.52

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
    averageRainfallPerMonth = 50  # mm (?)
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
                  rankingOfNationalEducationSystem, universities, faculties
                  )
    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()

    #############################   POLAND   #############################

    #############################   CZECH   ##############################

    # Country
    countryName = "Czech"
    officialLanguage = "Czech"

    # cities     name   isBig WashesBy
    cities = {'Prague': [True, None], 'Brno': [True, None], 'Pilsen': [True, None],
              'Ostrava': [True, None], 'Olomouc': [True, None]}

    # education
    universities = {'Prague': ['Czech Technical University in Prague', 'Prague City University'],
                    'Brno': ['Brno University of Technology', 'Masaryk University'],
                    'Pilsen': ['University of West Bohemia', 'Charles University'],
                    'Ostrava': ['University of Ostrava', 'Ostrava University of Technology'],
                    'Olomouc': ['Palacký University Olomouc', 'Moravian University Olomouc']}

    faculties = {'Czech Technical University in Prague': ['Faculty of Architecture', 'Faculty of Biomedical Engineering',
                                                          'Faculty of Electrical Engineering', 'Faculty of Information Technology',
                                                          'Faculty of Mechanical Engineering', 'Faculty of Transportation Sciences'],
                 'Prague City University': ['Faculty of Design', 'Faculty of Art', 'Faculty of Management',
                                            'Faculty of Computig'],
                 'Brno University of Technology': ['Faculty of Architecture', 'Faculty of Management', 'Faculty of Business',
                                                   'Faculty of Civil Engineering', 'Faculty of Electrical Engineering', 'Faculty of Chemistry',
                                                   'Faculty of Information Technology', 'Faculty of Mechanical Engineering', 'Faculty of Arts'],
                 'Masaryk University': ['Faculty of Law', 'Faculty of Medicine', 'Faculty of Science', 'Faculty of Arts',
                                        'Faculty of Economics', 'Faculty of Informatics'],
                 'University of West Bohemia': ['Faculty of Science', 'Faculty of Arts', 'Faculty of Economics',
                                                'Faculty of Electrical Engineering', 'Faculty of Law', 'Faculty of Mechanical Engineering'],
                 'Charles University': ['Faculty of Law', 'Faculty of Medicine', 'Faculty of Arts', 'Faculty of Science',
                                        'Faculty of Mathematics and Physics', 'Faculty of Social Sciences'],
                 'University of Ostrava': ['Faculty of Science', 'Faculty of Arts', 'Faculty of Music',
                                           'Faculty of Music', 'Faculty of Social Studies', 'Faculty of Medicine'],
                 'Ostrava University of Technology': ['Faculty of Mechanical Engineering', 'Faculty of Economics',
                                                      'Faculty of Electrical Engineering', 'Faculty of Computer Science',
                                                      'Faculty of Civil Engineering', 'Faculty of Safety Engineering'],
                 'Palacký University Olomouc': ['Faculty of Medicine', 'Faculty of Arts', 'Faculty of Science',
                                                'Faculty of Education', 'Faculty of Law', 'Faculty of Health Sciences'],
                 'Moravian University Olomouc': ['Faculty of Economics', 'Faculty of Social Studies',
                                                 'Faculty of Electrical Engineering',
                                                 'Faculty of Mechanical Engineering']}



    # currency
    currencyName = 'CZK'
    currencyEqualsToDollar = 23.39

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
    averageRainfallPerMonth = 43.75  # mm (?)
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
                  rankingOfNationalEducationSystem, universities, faculties
                  )
    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()

    #############################   CZECH   #############################

    #############################   GERMANY   #############################

    # Country
    countryName = "Germany"
    officialLanguage = "Deutsch"

    # cities     name   isBig WashesBy
    cities = {'Berlin': [True, None], 'Hamburg': [True, None], 'Bremen': [True, None],
              'Dresden': [True, None], 'Nuremberg': [True, None]}

    # education
    universities = {'Berlin': ['Humboldt University of Berlin', 'Technical University of Berlin'],
                    'Hamburg': ['University of Hamburg', 'HafenCity University Hamburg'],
                    'Bremen': ['University of Bremen', 'Jacobs University Bremen'],
                    'Dresden': ['Dresden University of Technology', 'Dresden University of Applied Sciences'],
                    'Nuremberg': ['Nuremberg Institute of Technology', 'Academy of Fine Arts']}
    faculties = {'Humboldt University of Berlin': ['Faculty of Law', 'Faculty of Mathematics', 'Faculty of Arts',
                                                   'Faculty of Economics', 'Faculty of Language'],
                 'Technical University of Berlin': ['Faculty of Education', 'Faculty of Mathematics', 'Faculty of Science',
                                                    'Faculty of Electrical Engineering', 'Faculty of Computer Science',
                                                    'Faculty of Mechanical Engineering', 'Faculty of Economics'],
                 'University of Hamburg': ['Faculty of Law', 'Faculty of Business', 'Faculty of Economics',
                                           'Faculty of Social Sciences', 'Faculty of Medicine', 'Faculty of Education',
                                           'Faculty of Mathematics', 'Faculty of Business'],
                 'HafenCity University Hamburg': ['Faculty of Architecture', 'Faculty of Engineering', 'Faculty of Mathematics',
                                                  'Faculty of Mechanical Engineering'],
                 'University of Bremen': ['Faculty of Biology', 'Faculty of Chemistry', 'Faculty of Mathematics',
                                          'Faculty of Computer Science', 'Faculty of Law', 'Faculty of Social Sciences'],
                 'Jacobs University Bremen': ['Faculty of Computer Science', 'Faculty of Physics', 'Faculty of Mathematics',
                                              'Faculty of Business', 'Faculty of Social Sciences', 'Faculty of Psychology'],
                 'Dresden University of Technology': ['Faculty of Biology', 'Faculty of Mathematics', 'Faculty of Psychology',
                                                      'Faculty of Physics', 'Faculty of Chemistry', 'Faculty of Education',
                                                      'Faculty of Arts', 'Faculty of Computer Science', 'Faculty of Electrical Engineering'],
                 'Dresden University of Applied Sciences': ['Faculty of Biology', 'Faculty of Chemistry', 'Faculty of Mathematics',
                                                            'Faculty of Physics', 'Faculty of Psychology'],
                 'Nuremberg Institute of Technology': ['Faculty of Chemistry', 'Faculty of Mathematics', 'Faculty of Architecture',
                                                       'Faculty of Design', 'Faculty of Computer Science', 'Faculty of Electrical Engineering'],
                 'Academy of Fine Arts': ['Faculty of Design', 'Faculty of Arts', 'Faculty of Psychology',
                                          'Faculty of Architecture', 'Faculty of Law']}

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
    averageRainfallPerMonth = 52.08  # mm (?)
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
                  rankingOfNationalEducationSystem, universities, faculties
                  )
    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()

    #############################   GERMANY   #############################

    #############################   SLOVAKIA   #############################

    # Country
    countryName = "Slovakia"
    officialLanguage = "Slovak"

    # cities     name      isBig WashesBy
    cities = {'Bratislava': [True, None], 'Kosice': [True, None], 'Nitra': [True, None],
              'Presov': [True, None], 'Banska Bystrica': [True, None]}

    # education
    universities = {'Bratislava': ['Slovak University of Technology in Bratislava', 'Comenius University Bratislava'],
                    'Kosice': ['University of Veterinary Medicine in Kosice', 'Pavol Josef Safarik University'],
                    'Nitra': ['Slovak University of Agriculture in Nitra', 'Constantine the Philosopher University'],
                    'Presov': ['University of Presov', 'International Business College ISM Slovakia in Presov'],
                    'Banska Bystrica': ['Matej Bel University in Banská Bystrica', 'Academy of Arts in Banská Bystrica']}
    faculties = {'Slovak University of Technology in Bratislava': ['Faculty of Civil Engineering', 'Faculty of Electrical Engineering',
                                                                   'Faculty of Mechanical Engineering', 'Faculty of Chemistry',
                                                                   'Faculty of Architecture', 'Faculty of Science'],
                 'Comenius University Bratislava': ['Faculty of Medicine', 'Faculty of Law', 'Faculty of Arts',
                                                    'Faculty of Natural Sciences', 'Faculty of Education', 'Faculty of Medicine'],
                 'University of Veterinary Medicine in Kosice': ['Faculty of Medicine', 'Faculty of Veterinary Medicine',
                                                                 'Faculty of Veterinary Surgery'],
                 'Pavol Josef Safarik University': ['Faculty of Medicine', 'Faculty of Biology', 'Faculty of Surgery'],
                 'Slovak University of Agriculture in Nitra': ['Faculty of Agrobiology', 'Faculty of Biotechnology',
                                                               'Faculty of Economics', 'Faculty of Engineering',
                                                               'Faculty of Management'],
                 'Constantine the Philosopher University': ['Faculty of Arts', 'Faculty of Natural Sciences',
                                                            'Faculty of Informatics'],
                 'University of Presov': ['Faculty of Arts', 'Faculty of Management', 'Faculty of Business',
                                          'Faculty of Education', 'Faculty of Sports', 'Faculty of Health Care'],
                 'International Business College ISM Slovakia in Presov': ['Faculty of Management', 'Faculty of Business',
                                                                           'Faculty of Law', 'Faculty of Economics'],
                 'Matej Bel University in Banská Bystrica': ['Faculty of Economics', 'Faculty of Natural Science',
                                                             'Faculty of Arts', 'Faculty of Education',
                                                             'Faculty of Law'],
                 'Academy of Arts in Banská Bystrica': ['Faculty of Dramatic Arts', 'Faculty of Performing Arts',
                                                        'Faculty of Fine Arts']}

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
    averageRainfallPerMonth = 48.3  # mm (?)
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
                  rankingOfNationalEducationSystem, universities, faculties
                  )
    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()

    #############################   SLOVAKIA   #############################

    #############################   HUNGARY   #############################

    # Country
    countryName = "Hungary"
    officialLanguage = "Hungarian"

    # cities     name      isBig WashesBy
    cities = {'Budapest': [True, None], 'Debrecen': [True, None], 'Szeged': [True, None],
              'Miskolc': [True, None], 'Pecs': [True, None]}

    # education
    universities = {'Budapest': ['Eötvös Loránd University', 'Semmelweis University'],
                    'Debrecen': ['University of Debrecen', 'Debrecen University of Reformed Theology'],
                    'Szeged': ['University of Szeged'],
                    'Miskolc': ['University of Miskolc'],
                    'Pecs': ['University of Pecs']}
    faculties = {'Eötvös Loránd University': ['Faculty of Economic', 'Faculty of Education', 'Faculty of Humanities',
                                              'Faculty of Informatics', 'Faculty of Law', 'Faculty of Science',
                                              'Faculty of Social Science'],
                 'Semmelweis University': ['Faculty of Medicine', 'Faculty of Health', 'Faculty of Dentistry'],
                 'University of Debrecen': ['Faculty of Dentistry', 'Faculty of Economics', 'Faculty of Business',
                                            'Faculty of Engineering', 'Faculty of Law', 'Faculty of Informatics',
                                            'Faculty of Medicine', 'Faculty of Music'],
                 'Debrecen University of Reformed Theology': ['Faculty of Reformed Theology', 'Faculty of Medicine',
                                                              'Faculty of Health', 'Faculty of Dentistry'],
                 'University of Szeged': ['Faculty of Agriculture', 'Faculty of Social Sciences', 'Faculty of Dentistry',
                                          'Faculty of Economics', 'Faculty of Business', 'Faculty of Engineering'],
                 'University of Miskolc': ['Faculty of Engineering', 'Faculty of Informatics',
                                           'Faculty of Mechanical Engineering', 'Faculty of Economics',
                                           'Faculty of Arts', 'Faculty of Law'],
                 'University of Pecs': ['Faculty of Economics', 'Faculty of Business',
                                        'Faculty of Education', 'Faculty of Engineering',
                                        'Faculty of Information Technology', 'Faculty of Law']}

    # currency
    currencyName = 'HUF'
    currencyEqualsToDollar = 390.46

    # military
    milPolBlock = "NATO"
    amountOfPeopleInArmy = 31080

    # healthcare
    numberOfDoctorsPer100kPopulation = 332
    menAverageLifeExpectancy = 71  # years
    womenAverageLifeExpectancy = 78.8  # years

    # climat
    juneAverageTemperature = 24  # °C
    decemberAverageTemperature = 1  # °C
    averageHumidity = 68.1  # %
    averageDurationOfWinter = 3.5  # month
    averageRainfallPerMonth = 46.9  # mm (?)
    averageNumberOfFoggyDaysPerYear = 76  # days
    averageNumberOfRainyDaysPerYear = 135  # days
    averageNumberOfClearDays = 154  # days

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
    populationCount = 9_710_000
    procentOfMales = 47.62
    procentOfFemales = 52.38
    populationDensityPerSquareKilometer = 107
    speedOfLife = 2  # [1, 3]
    workPlaces = 2  # [1, 3]
    nightLifeEntertainment = 2  # [1, 3]

    # citizenship
    citizenshipGlobalRank = 4

    # communication
    communicationOnEnglish = 2  # [1, 3]

    # transport
    averageTravelTimeToWork = 29
    developmentLevelOfPublicTransport = 2  # [1, 3]

    # internet
    speedOfInternetMbps = 42.11  # Мегабиты в секунду
    freeWifi = 2  # [1, 3]

    # education
    rankingOfNationalEducationSystem = 51.3

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
                  rankingOfNationalEducationSystem, universities, faculties
                  )
    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()

    #############################   HUNGARY   #############################

    #############################   UNITED KINGDOM   #############################

    # Country
    countryName = "United Kingdom"
    officialLanguage = "English"

    # cities     name      isBig WashesBy
    cities = {'London': [True, None], 'Edinburgh': [True, "Northern ocean"], 'Birmingham': [True, None],
              'Manchester': [True, None], 'Belfast': [True, "Irish sea"]}

    # education
    universities = {'London': ['University College London', 'Imperial College London'],
                    'Edinburgh': ['University of Edinburgh', 'Heriot-Watt University'],
                    'Birmingham': ['University of Birmingham', 'Aston University'],
                    'Manchester': ['University of Manchester', 'University of Salford'],
                    'Belfast': ["Queen's University Belfast"]}
    faculties = {'University College London': ['Faculty of Arts', 'Faculty of Engineering', 'Faculty of Law',
                                               'Faculty of Medicine', 'Faculty of Architecture', 'Faculty of Mathematics',
                                               'Faculty of Physics'],
                 'Imperial College London': ['Faculty of Engineering', 'Faculty of Medicine', 'Faculty of Mathematics',
                                             'Faculty of Chemistry', 'Faculty of Physics'],
                 'University of Edinburgh': ['Faculty of Law', 'Faculty of Arts', 'Faculty of Medicine',
                                             'Faculty of Veterinary Medicine', 'Faculty of Education', 'Faculty of Science'],
                 'Heriot-Watt University': ['Faculty of Engineering', 'Faculty of Social Sciences', 'Faculty of Design',
                                            'Faculty of Business', 'Faculty of Computer Sciences'],
                 'University of Birmingham': ['Faculty of Arts', 'Faculty of Design', 'Faculty of Media',
                                              'Faculty of Business', 'Faculty of Law', 'Faculty of Social Sciences',
                                              'Faculty of Education', 'Faculty of Computing', 'Faculty of Engineering'],
                 'Aston University': ['Faculty of Business', 'Faculty of Social Sciences', 'Faculty of Engineering',
                                      'Faculty of Physics', 'Faculty of Life Science'],
                 'University of Manchester': ['Faculty of Biology', 'Faculty of Medicine', 'Faculty of Health',
                                              'Faculty of Science', 'Faculty of Engineering', 'Faculty of Humanities'],
                 'University of Salford': ['Faculty of Science', 'Faculty of Engineering', 'Faculty of Arts',
                                           'Faculty of Health', 'Faculty of Business'],
                 "Queen's University Belfast": ['Faculty of Arts', 'Faculty of Humanities', 'Faculty of Social Science',
                                                'Faculty of Engineering', 'Faculty of Physics', 'Faculty of Medicine']}

    # currency
    currencyName = 'GBP'
    currencyEqualsToDollar = 0.84

    # military
    milPolBlock = "NATO"
    amountOfPeopleInArmy = 188000

    # healthcare
    numberOfDoctorsPer100kPopulation = 264
    menAverageLifeExpectancy = 79.0  # years
    womenAverageLifeExpectancy = 82.9  # years

    # climat
    juneAverageTemperature = 21  # °C
    decemberAverageTemperature = 8  # °C
    averageHumidity = 79  # %
    averageDurationOfWinter = 4  # month
    averageRainfallPerMonth = 59.3  # mm (?)
    averageNumberOfFoggyDaysPerYear = 56 # days
    averageNumberOfRainyDaysPerYear = 149  # days
    averageNumberOfClearDays = 160  # days

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
    populationCount = 67_330_000
    procentOfMales = 48
    procentOfFemales = 52
    populationDensityPerSquareKilometer = 277.12
    speedOfLife = 3  # [1, 3]
    workPlaces = 2  # [1, 3]
    nightLifeEntertainment = 3  # [1, 3]

    # citizenship
    citizenshipGlobalRank = 4

    # communication
    communicationOnEnglish = 3  # [1, 3]

    # transport
    averageTravelTimeToWork = 58.8
    developmentLevelOfPublicTransport = 3  # [1, 3]

    # internet
    speedOfInternetMbps = 50.4  # Мегабиты в секунду
    freeWifi = 3  # [1, 3]

    # education
    rankingOfNationalEducationSystem = 83.6

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
                  rankingOfNationalEducationSystem, universities, faculties
                  )
    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()

    #############################   UNITED KINGDOM   #############################

    #############################   FINLAND   #############################

    # Country
    countryName = "Finland"
    officialLanguage = "Finnish"

    # cities     name      isBig WashesBy
    cities = {'Helsinki': [True, "The Gulf of Finland"], 'Turku': [True, "Baltic Sea"], 'Tampere': [True, None],
              'Oulu': [True, "Baltic Gulf"], 'Rovaniemi': [True, None]}

    # education
    universities = {'Helsinki': ['University of Helsinki', 'Hanken School of Economics'],
                    'Turku': ['University of Turku', 'Abo Akademi University'],
                    'Tampere': ['University of Tampere'],
                    'Oulu': ['University of Oulu', 'Oulu University of Applied Sciences'],
                    'Rovaniemi': ['University of Lapland', 'Lapland University of Applied Sciences']}
    faculties = {'University of Helsinki': ['Faculty of Agriculture', 'Faculty of Arts', 'Faculty of Biology',
                                            'Faculty of Education', 'Faculty of Law', 'Faculty of Medicine',
                                            'Faculty of Science', 'Faculty of Theology', 'Faculty of Veterinary Medicine'],
                 'Hanken School of Economics': ['Faculty of Economics', 'Faculty of Management', 'Faculty of Business'],
                 'University of Turku': ['Faculty of Education', 'Faculty of Humanities', 'Faculty of Law',
                                         'Faculty of Medicine', 'Faculty of Science', 'Faculty of Technology'],
                 'Abo Akademi University': ['Faculty of Arts', 'Faculty of Psychology', 'Faculty of Theology',
                                            'Faculty of Education', 'Faculty of Science', 'Faculty of Engineering',
                                            'Faculty of Social Sciences', 'Faculty of Business', 'Faculty of Economics'],
                 'University of Tampere': ['Faculty of Architecture', 'Faculty of Education', 'Faculty of Engineering',
                                           'Faculty of Science', 'Faculty of Information Technology', 'Faculty of Management',
                                           'Faculty of Business', 'Faculty of Medicine'],
                 'University of Oulu': ['Faculty of Biochemistry', ' Faculty of Medicine', ' Faculty of Science',
                                        'Faculty of Humanities', 'Faculty of Electrical Engineering'],
                 'Oulu University of Applied Sciences': ['Faculty of Biochemistry', 'Faculty of Education', 'Faculty of Medicine',
                                                         'Faculty of Science', 'Faculty of Technology', 'Faculty of Business'],
                 'University of Lapland': ['Faculty of Art', 'Faculty of Design', 'Faculty of Education',
                                           'Faculty of Law', 'Faculty of Social Sciences'],
                 'Lapland University of Applied Sciences': ['Faculty of Social Sciences', 'Faculty of Technology', 'Faculty of Electrical Engineering',
                                                            'Faculty of Information Technology', 'Faculty of Mechanical Engineering']}

    # currency
    currencyName = 'FIM'
    currencyEqualsToDollar = 5.73

    # military
    milPolBlock = "Finnish Defense Forces"
    amountOfPeopleInArmy = 23800

    # healthcare
    numberOfDoctorsPer100kPopulation = 302
    menAverageLifeExpectancy = 79.2  # years
    womenAverageLifeExpectancy = 84.0  # years

    # climat
    juneAverageTemperature = 22  # °C
    decemberAverageTemperature = -6  # °C
    averageHumidity = 77  # %
    averageDurationOfWinter = 5  # month
    averageRainfallPerMonth = 80  # mm (?)
    averageNumberOfFoggyDaysPerYear = 82  # days
    averageNumberOfRainyDaysPerYear = 139  # days
    averageNumberOfClearDays = 144  # days

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
    situationInTheCountry = 2  # [1, 3] 1-bad, 3-good
    freedomOfSpeech = 3  # [1, 3]
    assessmentOfFamilyLife = 2  # [1, 3]
    attitudeTowardsLGBT = 3  # [1, 3]

    # population
    populationCount = 5_542_000
    procentOfMales = 49
    procentOfFemales = 51
    populationDensityPerSquareKilometer = 18
    speedOfLife = 3  # [1, 3]
    workPlaces = 3  # [1, 3]
    nightLifeEntertainment = 2  # [1, 3]

    # citizenship
    citizenshipGlobalRank = 2

    # communication
    communicationOnEnglish = 3  # [1, 3]

    # transport
    averageTravelTimeToWork = 45
    developmentLevelOfPublicTransport = 2  # [1, 3]

    # internet
    speedOfInternetMbps = 79.40  # Мегабиты в секунду
    freeWifi = 2  # [1, 3]

    # education
    rankingOfNationalEducationSystem = 82.8

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
                  rankingOfNationalEducationSystem, universities, faculties
                  )
    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()

    #############################   FINLAND   #############################

    #############################   NORWAY   #############################

    # Country
    countryName = "Norway"
    officialLanguage = "Norwegian"

    # cities     name      isBig WashesBy
    cities = {'Oslo': [True, None], 'Drammen': [True, None], 'Bergen': [True, "Northern ocean"],
              'Trondheim': [True, "Trondheimsfjorden"], 'Stavanger': [True, "Northern ocean"]}

    # education
    universities = {'Oslo': ['University of Oslo', 'Oslo Metropolitan University'],
                    'Drammen': ['The International Theatre Academy Norway'],
                    'Bergen': ['University of Bergen', 'Norwegian School of Economics'],
                    'Trondheim': ['Norwegian University of Science and Technology', 'Queen Maud University College for Early Childhood Education'],
                    'Stavanger': ['University of Stavanger']}
    faculties = {'University of Oslo': ['Faculty of Health', 'Faculty of Education', 'Faculty of Social Sciences',
                                        'Faculty of Technology', 'Faculty of Arts', 'Faculty of Design'],
                 'Oslo Metropolitan University': ['Faculty of Health', 'Faculty of Education', 'Faculty of Social Sciences',
                                                  'Faculty of Technology', 'Faculty of Arts', 'Faculty of Design'],
                 'The International Theatre Academy Norway': ['Faculty of Arts', 'Faculty of Music', 'Faculty of Design',
                                                              'Faculty of Social Sciences'],
                 'University of Bergen': ['Faculty of Fine Art', 'Faculty of Music', 'Faculty of Design',
                                          'Faculty of Humanities', 'Faculty of Law', 'Faculty of Natural Sciences',
                                          'Faculty of Medicine', 'Faculty of Social Sciences'],
                 'Norwegian School of Economics': ['Faculty of Economics', 'Faculty of Management', 'Faculty of Business',
                                                   'Faculty of Social Science'],
                 'Norwegian University of Science and Technology': ['Faculty of Architecture', 'Faculty of Design',
                                                                    'Faculty of Humanities', 'Faculty of Information Technology',
                                                                    'Faculty of Electrical Engineering', 'Faculty of Medicine'],
                 'Queen Maud University College for Early Childhood Education': ['Faculty of Childhood Education', 'Faculty of Care',
                                                                                 'Faculty of Health', 'Faculty of Arts'],
                 'University of Stavanger': ['Faculty of Arts', 'Faculty of Education', 'Faculty of Science',
                                             'Faculty of Technology', 'Faculty of Health']}

    # currency
    currencyName = 'NOK'
    currencyEqualsToDollar = 10.14

    # military
    milPolBlock = "NATO"
    amountOfPeopleInArmy = 29000

    # healthcare
    numberOfDoctorsPer100kPopulation = 442
    menAverageLifeExpectancy = 81.1  # years
    womenAverageLifeExpectancy = 84.1  # years

    # climat
    juneAverageTemperature = 20  # °C
    decemberAverageTemperature = -3  # °C
    averageHumidity = 77  # %
    averageDurationOfWinter = 3.3  # month
    averageRainfallPerMonth = 73  # mm (?)
    averageNumberOfFoggyDaysPerYear = 65  # days
    averageNumberOfRainyDaysPerYear = 133  # days
    averageNumberOfClearDays = 167  # days

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
    situationInTheCountry = 2  # [1, 3] 1-bad, 3-good
    freedomOfSpeech = 3  # [1, 3]
    assessmentOfFamilyLife = 3  # [1, 3]
    attitudeTowardsLGBT = 3  # [1, 3]

    # population
    populationCount = 5_408_000
    procentOfMales = 50.57
    procentOfFemales = 49.43
    populationDensityPerSquareKilometer = 15
    speedOfLife = 3  # [1, 3]
    workPlaces = 3  # [1, 3]
    nightLifeEntertainment = 2  # [1, 3]

    # citizenship
    citizenshipGlobalRank = 3

    # communication
    communicationOnEnglish = 3  # [1, 3]

    # transport
    averageTravelTimeToWork = 70
    developmentLevelOfPublicTransport = 2  # [1, 3]

    # internet
    speedOfInternetMbps = 23.5  # Мегабиты в секунду
    freeWifi = 1  # [1, 3]

    # education
    rankingOfNationalEducationSystem = 80.5

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
                  rankingOfNationalEducationSystem, universities, faculties
                  )
    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()

    #############################   NORWAY   #############################

    #############################   SWEDEN   #############################

    # Country
    countryName = "Sweden"
    officialLanguage = "Swedish"

    # cities     name      isBig WashesBy
    cities = {'Stockholm': [True, "Baltic Sea"], 'Orebro': [True, None], 'Linkoping': [True, None],
              'Jonkoping': [True, "Vättern"], 'Goteborg': [True, "Kattegat"]}

    # education
    universities = {'Stockholm': ['Karolinska Institute', 'Stockholm University'],
                    'Orebro': ['Orebro University'],
                    'Linkoping': ['Linkoping University'],
                    'Jonkoping': ['Jonkoping University'],
                    'Goteborg': ['University of Gothenburg', 'Chalmers University of Technology']}
    faculties = {'Karolinska Institute': ['Faculty of Dentistry', 'Faculty of Medicine', 'Faculty of Anatomy',
                                          'Faculty of Biology', 'Faculty of Psychology'],
                 'Stockholm University': ['Faculty of Humanities', 'Faculty of Law', 'Faculty of Social Sciences',
                                          'Faculty of ', 'Faculty of Science'],
                 'Orebro University': ['Faculty of Business', 'Faculty of Science', 'Faculty of Engineering',
                                       'Faculty of Humanities', 'Faculty of Social Sciences', 'Faculty of Medicine',
                                       'Faculty of Health'],
                 'Linkoping University': ['Faculty of Arts', 'Faculty of Science', 'Faculty of Education',
                                          'Faculty of Medicine', 'Faculty of Health', 'Faculty of Science',
                                          'Faculty of Engineering'],
                 'Jonkoping University': ['Faculty of Computing', 'Faculty of Engineering', 'Faculty of Mathematics',
                                          'Faculty of Physics', 'Faculty of Chemistry'],
                 'University of Gothenburg': ['Faculty of Information Technology', 'Faculty of Humanities', 'Faculty of Education',
                                              'Faculty of Arts', 'Faculty of Science', 'Faculty of Social Sciences'],
                 'Chalmers University of Technology': ['Faculty of Architecture', 'Faculty of Information Technology', 'Faculty of Physics',
                                                       'Faculty of Mathematics', 'Faculty of Chemistry', 'Faculty of Engineering']}

    # currency
    currencyName = 'CHF'
    currencyEqualsToDollar = 0.95

    # military
    milPolBlock = "None"
    amountOfPeopleInArmy = 140304

    # healthcare
    numberOfDoctorsPer100kPopulation = 411
    menAverageLifeExpectancy = 80.8  # years
    womenAverageLifeExpectancy = 84.0  # years

    # climat
    juneAverageTemperature = 21  # °C
    decemberAverageTemperature = -2  # °C
    averageHumidity = 75  # %
    averageDurationOfWinter = 4.0  # month
    averageRainfallPerMonth = 51  # mm (?)
    averageNumberOfFoggyDaysPerYear = 70  # days
    averageNumberOfRainyDaysPerYear = 136  # days
    averageNumberOfClearDays = 159  # days

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
    situationInTheCountry = 2  # [1, 3] 1-bad, 3-good
    freedomOfSpeech = 3  # [1, 3]
    assessmentOfFamilyLife = 3  # [1, 3]
    attitudeTowardsLGBT = 3  # [1, 3]

    # population
    populationCount = 10_420_000
    procentOfMales = 50
    procentOfFemales = 50
    populationDensityPerSquareKilometer = 25
    speedOfLife = 2  # [1, 3]
    workPlaces = 3  # [1, 3]
    nightLifeEntertainment = 2  # [1, 3]

    # citizenship
    citizenshipGlobalRank = 2

    # communication
    communicationOnEnglish = 3  # [1, 3]

    # transport
    averageTravelTimeToWork = 41
    developmentLevelOfPublicTransport = 2  # [1, 3]

    # internet
    speedOfInternetMbps = 55.18  # Мегабиты в секунду
    freeWifi = 2  # [1, 3]

    # education
    rankingOfNationalEducationSystem = 84.3

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
                  rankingOfNationalEducationSystem, universities, faculties
                  )
    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()

    #############################   SWEDEN   #############################

    cc.createBorders()
    cc.close()
