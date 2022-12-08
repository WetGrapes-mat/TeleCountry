from neo4j import GraphDatabase
from parsingInfoForDataBase import crimeThingForCountry, climatForCountry, costOfLivingForCountry, healthForCountry
from config import LOCALHOST, LOGIN, PASSWORD


def formParams(dict):
    params = '{'
    for key, value in dict.items():
        params += '%s: %s, ' % (key, str(value))
    params = params[:-2] + '}'
    return params


class CountryCreator:

    def __init__(self):
        self.driver = GraphDatabase.driver(LOCALHOST, auth=(LOGIN, PASSWORD))

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
                   rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images, requirements
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
                                         rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images, requirements
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
                    rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images, requirements
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
        univ_ind = 1
        prog = 1

        for city in citiesDict:
            for univ in universities[city]:
                try:
                    link = links[univ]
                    cost = costs[univ]
                    image = images[univ]
                    req = requirements[univ]
                except:
                    link = "a"
                    cost = 1000
                    image = 'clear'
                    req = 'No requirements'
                resultStr += '\ncreate (univ%d:University {name:"%s", link:"%s", cost:%d, image:"%s", requirements:"%s"})' % (univ_ind, univ, link, cost, image, req)
                for faculty in faculties[univ]:
                    resultStr += '\nmerge (faculty%d:Faculty {name:"%s"})' % (fac, faculty)
                    resultStr += '\nmerge (univ%d)-[:faculty]->(faculty%d)' % (univ_ind, fac)
                    fac += 1
                try:
                    for program in programs[univ]:
                        resultStr += '\ncreate (program%d:Program {name:"%s"})' % (prog, program)
                        resultStr += '\ncreate (univ%d)-[:program]->(program%d)' % (univ_ind, prog)
                        prog += 1
                except:
                    pass

                # resultStr += '\ncreate (cost%d:Cost {value:%d})' % (c, cost)
                # resultStr += '\ncreate (univ%d)-[:cost]->(cost%d)' % (ind, c)

                resultStr += '\ncreate (city%d)-[:university]->(univ%d)' % (index, univ_ind)
                resultStr += '\ncreate (country)-[:university]->(univ%d)' % univ_ind
                univ_ind += 1
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

    def clear_db(self):
        with self.driver.session() as session:
            clr = session.execute_write(self._clear_db)
            return clr

    @staticmethod
    def _clear_db(tx):
        request = "match (n) detach delete n"
        tx.run(request)


if __name__ == "__main__":
    cc = CountryCreator()

    cc.clear_db()

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
    programs = {'Carleton University': ['Magistracy', 'Undergraduate'],
                'University of Ottawa': ['Magistracy', 'Undergraduate'],
                'York University': ['Magistracy', 'Undergraduate'],
                'University of Toronto': ['Foundation', 'Undergraduate', 'MBA'],
                'Montreal university': ['Magistracy', 'Undergraduate'],
                'Polytechnique Montreal': ['Magistracy', 'Undergraduate'],
                'Laval University': ['Magistracy', 'Undergraduate'],
                'TELUQ University': ['Magistracy', 'Undergraduate'],
                'University of British Columbia': ['Magistracy', 'Undergraduate', 'MBA'],
                'University Canada West': ['Magistracy', 'Undergraduate']}
    links = {'Carleton University': 'https://carleton.ca',
             'University of Ottawa': 'https://www.uottawa.ca/en',
             'York University': 'https://www.yorku.ca',
             'University of Toronto': 'https://www.utoronto.ca',
             'Montreal university': 'https://www.umontreal.ca/en',
             'Polytechnique Montreal': 'https://www.polymtl.ca',
             'Laval University': 'https://www.ulaval.ca/en',
             'TELUQ University': 'https://www.teluq.ca',
             'University of British Columbia': 'https://www.ubc.ca',
             'University Canada West': 'https://www.ucanwest.ca'}
    images = {'Carleton University': 'carleton_university',
              'University of Ottawa': 'university_of_ottawa',
              'York University': 'york_university',
              'University of Toronto': 'university_of_toronto',
              'Montreal university': 'montreal_university',
              'Polytechnique Montreal': 'politechnique_montreal',
              'Laval University': 'laval_university',
              'TELUQ University': 'teluq_university',
              'University of British Columbia': 'university_of_british_columbia',
              'University Canada West': 'university_canada_west'}
    requirements = {'Carleton University': 'Four years of English. '
                                           'Three or more years of mathematics. '
                                           'Two or more years of science. '
                                           'Three or more years of social science.',
                    'University of Ottawa': 'An admissions application (you can apply online). '
                                            'A $75 application fee. '
                                            'All official undergraduate transcripts (3.0 GPA - minimum requirement)'
                                            'A Graduate School Admission Essay/Personal Statement - This is a two-page essay focused on professional career development.',
                    'York University': 'For Ontario high school students, the minimum admission requirement is the completion of the Ontario Secondary School Diploma (OSSD) or equivalent and six 4U/M courses, including ENG4U. '
                                       'Students may also be required to fulfill Faculty or program-specific prerequisites.'
                                       'Francophone applicants may present FRA4U.You must successfully complete the OSSD, including six 4U/M courses and all of the prerequisites for your programs, and maintain the average used for conditional admission.',
                    'University of Toronto': 'Entry requirements for international students are based on current high school grades. '
                                             'The average score sufficient for admission should be at least 75-80% of the maximum possible. '
                                             'The age limit is at least 17 years old. '
                                             'English at IELTS level minimum 6.5 or TOEFL iBT 100+',
                    'Montreal university': 'To secure admission at UdeM, international students are required to have a minimum GPA of 3.0 i.e 85% for UG programs, and a GPA of 3.3 i.e 88% for PG programs.y',
                    'Polytechnique Montreal': 'A certified or official French or English translation is required for any documentation not written in French or English. A copy of original documents as well as their official translations must be provided.'
                                              ' All documentation provided becomes property of Polytechnique Montréal and will not be returned to the applicant.',
                    'Laval University': 'You must hold the minimum diploma required for the level of studies you are pursuing and demonstrate an adequate level of French proficiency.',
                    'TELUQ University': 'When applying for admission to Tele-Universite TELUQ in Canada you should prepare all required documents. '
                                        'Request a list of necessary documents directly from a university, as it may vary for different countries. '
                                        'Using our live chat, you can also ask for sample documents.',
                    'University of British Columbia': 'Graduation from high school. '
                                                      'Minimum of 70% in Grade 11 or Grade 12 English (or their equivalents)'
                                                      'At least six academic/non-academic Grade 12 courses (recommended, but not required)',
                    'University Canada West': "Usually, the university accepts a bachelor's degree in BBA/BCom or its equivalent and a minimum of three years of documented professional or management experience with evidence of career progression. "
                                              "The English language requirement includes an overall IELTS score of 6.5 with at least 6.0 in Writing."}


    costs = {'Carleton University': 18911,
             'University of Ottawa': 19041,
             'York University': 20102,
             'University of Toronto': 34045,
             'Montreal university': 18400,
             'Polytechnique Montreal': 23000,
             'Laval University': 18151,
             'TELUQ University': 17256,
             'University of British Columbia': 38946,
             'University Canada West': 19624}
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
    rankingOfNationalEducationSystem = 17

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
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images, requirements
                  )

    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()
    #############################   CANADA   #############################

    cc.createBorders()
    cc.close()
