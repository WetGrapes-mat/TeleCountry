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
                   rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images, requirements,
                   hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers
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
                                         rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images, requirements,
                                         hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers
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
                    rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images, requirements,
                    hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers
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
            resultStr += '\ncreate (city%d:City {name:"%s", isBig:"%s", isResort:"%s"})' % (index, city, str(citiesDict[city][0]), str(citiesDict[city][1]))
            resultStr += '\ncreate (country)-[:has_city]->(city%d)' % index
            if index == 1:
                resultStr += '\ncreate (country)-[:capital]->(city%d)' % index
            if citiesDict[city][2] is not None:
                resultStr += '\ncreate(water%d:Water {name:"%s"})' % (index, str(citiesDict[city][2]))
                resultStr += '\ncreate (water%d)-[:washes]->(city%d)' % (index, index)
            index += 1
        # education
        resultStr += '\ncreate (education:Education {rankingOfNationalEducationSystem:%d})' % rankingOfNationalEducationSystem
        resultStr += '\ncreate (country)-[:education]->(education)\n'

        index = 1
        for sight in sights.keys():
            resultStr += '\ncreate (sight%d:Sight {name:"%s", description:"%s", image:"%s"})' % (
                index, sight, sights[sight][0], sights[sight][1])
            resultStr += '\ncreate (country)-[:sight]->(sight%d)' % (index)
            index += 1

        index = 1
        for beach in beaches.keys():
            resultStr += '\ncreate (beach%d:Beach {name:"%s", description:"%s", image:"%s"})' % (
            index, beach, beaches[beach][0], beaches[beach][1])
            resultStr += '\ncreate (country)-[:beach]->(beach%d)' % (index)
            index += 1

        index = 1
        for mountain in mountains.keys():
            resultStr += '\ncreate (mountain%d:Mountain {name:"%s", description:"%s", image:"%s"})' % (
                index, mountain, mountains[mountain][0], mountains[mountain][1])
            resultStr += '\ncreate (country)-[:mountain]->(mountain%d)' % (index)
            index += 1

        index = 1
        for lake in lakes.keys():
            resultStr += '\ncreate (lake%d:Lake {name:"%s", description:"%s", image:"%s"})' % (
                index, lake, lakes[lake][0], lakes[lake][1])
            resultStr += '\ncreate (country)-[:lake]->(lake%d)' % (index)
            index += 1

        index = 1
        for river in rivers.keys():
            resultStr += '\ncreate (river%d:River {name:"%s", description:"%s", image:"%s"})' % (
                index, river, rivers[river][0], rivers[river][1])
            resultStr += '\ncreate (country)-[:river]->(river%d)' % (index)
            index += 1

        index = 1
        for skiResort in skiResorts.keys():
            resultStr += '\ncreate (skiResort%d:SkiResort {name:"%s", description:"%s", image:"%s"})' % (
                index, skiResort, skiResorts[skiResort][0], skiResorts[skiResort][1])
            resultStr += '\ncreate (country)-[:skiResort]->(skiResort%d)' % (index)
            index += 1


        index = 1
        fac = 1
        univ_ind = 1
        prog = 1

        for city in citiesDict:
            if city in universities.keys():
                for univ in universities[city]:
                    try:
                        link = links[univ]
                        cost = costs[univ]
                        image = images[univ]
                        req = requirements[univ]
                        host = hostel[univ]
                        scolar = scolarship[univ]
                    except:
                        link = "a"
                        cost = 1000
                        image = 'clear'
                        req = 'No requirements'
                        host = 'No'
                        scolar = 'No'
                    resultStr += '\ncreate (univ%d:University {name:"%s",link:"%s",cost:%d,hostel:"%s",scolarship:"%s",image:"%s",requirements:"%s"})' % (
                    univ_ind, univ, link, cost, host, scolar, image, req)
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
        resultStr += '\ncreate (currency:Currency {name:"%s", oneDollarEquals:%s})' % (str(currencyName), currencyEqualsToDollar)
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

    # cities    name   isBig isResort washesBy
    cities = {'Ottawa': [True, True, None], 'Toronto': [True, False, None], 'Montreal': [True, True, None],
              'Quebec': [True, True, 'Atlantic ocean'], 'Vancouver': [True, True, 'Pacific ocean'], 'Victoria': [False, True, 'Salish sea']}
    sights = {'Parliament building of Canada': ["The architectural complex, which hosts working meetings of the Canadian government, looks like a medieval castle from the outside. "
                                                "It is located in a convenient location for travelers - in the heart of Ottawa. "
                                                "The gray stone from which the building is built seems gloomy at first glance. "
                                                "However, the overall composition of the building is so precise and accurate that the complex inspires involuntary respect. "
                                                "It seems that the architects who built the complex in 1860 were fanatically devoted to the idea of symmetry in architecture."
                                                "The pointed towers are located strictly symmetrically with respect to the central column, on which the clock runs, visible from everywhere. "
                                                "The strength of the building is evidenced by the fact that the gray stone is also covered with copper plates. "
                                                "However, in 1916 the building did not survive the devastating fire. "
                                                "Reconstruction work was carried out in an organized manner, but they dragged on until 1922.", 'parliament_building_of_Canada_sight'],
              'Oratory of St. Joseph': ["Among those sights that you must visit in Canada is the Oratory of St. Joseph. Construction work began in 1904. "
                                        "The initiative of the project belongs to André Bessette. "
                                        "The original version of the oratorio was a small chapel that nestled comfortably on the slopes of Mont Royal next to Notre Dame College. "
                                        "The church quickly became popular, the number of parishioners increased every year. "
                                        "Therefore, already in 1917, a church for 1000 people was built here."
                                        "The church keeps the memory of many miracles performed by Brother Andre Bessette. "
                                        "It is significant that Pope John Paul II recognized the miracles that are attributed to brother Andrew. "
                                        "The recognition took place in 1982, and already in 2010 the canonization of brother Andrei took place. "
                                        "He was canonized by Pope Benedict XVII.", 'oratory_sight'],
              'Niagara Falls': ["Niagara Falls is included in the list of natural attractions in Canada. "
                                "In addition, it is considered one of the wonders of the world. "
                                "The waterfall is located on the border of Canada and America. "
                                "With a terrifying roar, tons of water flows powerfully rush every second. "
                                "The waterfall is located in a dense cloud of spray, since the water pressure here is quite strong. "
                                'This is fully true, since a giant water stream falls from a 50-meter height. '
                                'Millions of travelers come here to see this unique natural phenomenon with their own eyes.', 'niagara_falls_sight']}
    beaches = {'Wasaga Beach': ["The longest freshwater beach in the world, attracting tourists with its 12 km of sandy coastline. "
                                "The warm, shallow waters of the beach are ideal for swimming, while the soft white sand is ideal for picnicking, "
                                "relaxing and watching the beautiful sunset. This urban beach, which is somewhat reminiscent of the famous beaches in Florida: "
                                "Daytona Beach and Fort Lauderdale.", 'wasaga_beach'],
               "Brady’s Beach": ["Bradis Beach is located in a very secluded area on the Pacific Ocean. The only way to get here is by ferry, plane or timber barge. "
                                 "Yes, the path is not easy, but the rest here is worth such a voyage. Try to be there during the Music by The Sea festival. "
                                 "By August, the water here warms up to temperatures suitable for a refreshing swim. "
                                 "The advantages of this beach are that it is surrounded by the Pacific Rim National Park, the ocean, and the territory of the Indians. "
                                 "Excellent diving. Proximity to Barkley Sound islands inhabited by sea lions and bald eagles.", "brady_beach"],
               'Ingonish Beach': ["Ingonish Beach is the only beach in the Cape Breton Highlands National Park, with a unique opportunity to swim in both fresh and sea water. "
                                  "This sandy beach is washed away in winter and washed back by waves every spring, and a natural barrier separates the lake from the waters of the Atlantic Ocean. "
                                  "In addition to swimming, here you will be offered to go on a boat trip to go fishing and, of course, watch the whales in their habitat.", 'ingonish_beach']}
    mountains = {'Robson': ['The highest point of the Rocky Mountains; it is also the highest point of the Canadian Rockies. '
                           'The mountain is located within the Robson Provincial Park in British Columbia.', 'robson_mountain'],
                 'Temple': ['Mountain in Banff National Park in the Canadian Rockies, the 7th highest peak in Alberta. '
                            'The Temple is located in the Bow River Valley between Paradise Creek and Moraine Creek and is the highest point in the Lake Louise region.',
                            'temple_mountain'],
                 'Snow House': ['A mountain on the continental divide of the Columbia Icefield on the border of Banff and Jasper National Parks. '
                                'Located in the Canadian Rockies on the border of British Columbia and Alberta. The height of the peak is 3456 m.',
                                'snow_house_mountain'],
                 'Assiniboine': ['Pyramidal mountain located on the American Continental Divide on the border of the Canadian provinces of Alberta and British Columbia. '
                                 'The height is 3618 m above sea level.', 'assiniboine_mountain']}
    skiResorts = {'Whistler Blackcomb': ['At the heart of Whistler and Blackcomb is the charming village of Whistler. '
                                         "You don't even have to ski to enjoy your trip to Whistler, but if you do, you'll find "
                                         'seemingly limitless terrain that can accommodate any level of skier, from first timers to extreme skiers. '
                                         "You'll find beautiful wide-open bowls at Mount Whistler and incredible groomed runs on both mountains. "
                                         "On Blackcomb, the Horstmann Glacier offers year-round skiing.", 'whistler_blackcomb_resort'],
                  'Lake Louise': ["Lake Louise, in the heart of the Rocky Mountains and less than an hour from the city of Banff, is one of Canada's most famous resorts. "
                                  "From the slopes, majestic scenery stretches over the Luke Valley and the surrounding mountains and beyond to the palatial Fairmont Chateau Lake Louise. "
                                  "This is a mountain for all skiers, from extreme skiers to families coming here to learn about the sport. "
                                  "In a resort with 4,200 acres of rocky terrain, the resort offers a combination of wide-open bowls, steepness, flumes and plenty of groomed trails."
                                  "The Lake Louise Ski Resort doesn't have an onsite location, but it does have fantastic daytime facilities at the base, as well as restaurants serving delicious food, "
                                  "as well as other restaurants in the mountains. Skiers can take a dip in the nearby village of Lake Louise or the town of Banff.", 'lake_louise_resort'],
                  'Revelstoke': ["Located in the interior of British Columbia, about 2.5 hours from the city of Kelowna, Revelstoke is a bit harder to get to some resorts, but well worth it. "
                                 "The mountain sees a large number of powder days; few crowds; and offers great terrain, from open bowls to tree trails and starter areas. "
                                 "Add to that the affordable accommodation options in Revelstoke; ski slopes, ski slopes on the mountain; and fabulous mountain scenery and it's hard to beat this resort. "
                                 "This is not the place for a glamorous five-star experience or shopping experience. It is a mountain of skiers and a great place for families.", 'revelstoke_resort']}
    lakes = {'Louise': ["A natural wonder of Banff National Park. Lies surrounded by the Rocky Mountains and the bright greenery of the forest, at an altitude of 1646 meters. "
                        "The unusual emerald color of the water is due to the presence of rock particles brought into the lake by glaciers. The area of the lake is 0.8 km2. "
                        "On the shore there is a 5-star hotel, a number of campsites and tourist centers, nearby is the famous ski resort. "
                        "Hiking and cycling routes are organized around the reservoir. Canoe excursions are available.", 'louise_lake'],
             'Moraine': ["One of the most beautiful and photographed lakes in the world. Business card of Canada. "
                         "Its stunning landscapes can be found in many magazines and catalogs, on Canadian currency, Windows screensaver, etc. "
                         "It lies in the Valley of the Ten Peaks of the famous Banff Park, at an altitude of 1885 meters. "
                         "Origin - glacial. The area is 0.5 km2. Routes have been laid out for tourists, it is better to move along them with an experienced guide. "
                         "A hotel was built on the shore, there is a boat rental.", 'moraine_kale'],
             'Superior': ['The largest in terms of area in the composition of the Great Five and among the fresh lakes of the world. '
                          'Located in Canada and the USA. It occupies an area of 82.7 thousand km2. The shores are indented, there are large bays, islands. '
                          'There are many parks on the lake, a marine reserve has been created. The water is cold, even in summer it does not exceed 4 ° C, in winter it does not freeze due to frequent storms. '
                          'The lake is rich in fish. Navigable. The major port is Thunder Bay. The southern part of the reservoir is known as the graveyard of ships.', 'superior_lake']}
    rivers = {'Yukon': ["One of the largest rivers of the North American continent originates in Lake Marsh. "
                        "Most of the Yukon is located in the United States, but the source is located in the Canadian province of the same name. "
                        'A tributary of the Yukon, the Klondike, is famous for the gold rush of the 20th century. '
                        'Almost the entire river is located in the subarctic climate zone, but in the Canadian part of the Yukon it is much warmer than in the north.'
                        'The total length of the river is 3190 km.', 'yukon_river'],
              'Colombia': ["The source of the river is Lake Columbia in the Rocky Mountains. "
                           "Due to its fast current and large elevation difference, Colombia is actively used to generate electricity. "
                           "In total, there are 14 hydroelectric power stations on it. The river is a spawning ground for many species of salmon. "
                           "Dams and hydroelectric power stations prevent the advancement of both adults and fry, but all power plants have fish passages, "
                           "and fry are in some cases transported to the ocean by the US Army. "
                           "The total length of the river is 2000 km.", 'colombia_river'],
              'Churchill': ["Thanks to an artificial canal built in the 20th century, most of the water from the Churchill River goes to Saskatchewan to increase hydroelectric power generation. "
                            "The river originates in the central part of the province of Saskatchewan and carries its waters east to Hudson Bay. "
                            "The rich flora and fauna of the river basin was the reason for its nomination for inclusion in the List of Protected Rivers of Canada.", 'churchill_river']}
    universities = {'Ottawa': ['Carleton University', 'University of Ottawa'],
                    'Toronto': ['York University', 'University of Toronto'],
                    'Montreal': ['Montreal University', 'Polytechnique Montreal'],
                    'Quebec': ['Laval University', 'TELUQ University'],
                    'Vancouver': ['University of British Columbia', 'University Canada West']}
    faculties = {'Carleton University': ['Faculty of Arts', 'Faculty of Computer Engineering and Software', 'Faculty of Education',
                                         'Faculty of Public Affairs', 'Faculty of Science', 'Faculty of Social Sciences'],
                 'University of Ottawa': ['Faculty of Arts', 'Faculty of Engineering', 'Faculty of Education',
                                          'Faculty of Science', 'Faculty of Medicine', 'Faculty of Law', 'Faculty of Social Sciences'],
                 'York University': ['Faculty of Education', 'Faculty of Arts', 'Faculty of Medicine, Faculty of Science'],
                 'University of Toronto': ['Faculty of Arts', 'Faculty of Science', 'Faculty of Medicine', 'Faculty of Design'],
                 'Montreal University': ['Faculty of Arts', 'Faculty of Science', 'Faculty of Law', 'Faculty of Medicine',
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
                'Montreal University': ['Magistracy', 'Undergraduate'],
                'Polytechnique Montreal': ['Magistracy', 'Undergraduate'],
                'Laval University': ['Magistracy', 'Undergraduate'],
                'TELUQ University': ['Magistracy', 'Undergraduate'],
                'University of British Columbia': ['Magistracy', 'Undergraduate', 'MBA'],
                'University Canada West': ['Magistracy', 'Undergraduate']}
    links = {'Carleton University': 'https://carleton.ca',
             'University of Ottawa': 'https://www.uottawa.ca/en',
             'York University': 'https://www.yorku.ca',
             'University of Toronto': 'https://www.utoronto.ca',
             'Montreal University': 'https://www.umontreal.ca/en',
             'Polytechnique Montreal': 'https://www.polymtl.ca',
             'Laval University': 'https://www.ulaval.ca/en',
             'TELUQ University': 'https://www.teluq.ca',
             'University of British Columbia': 'https://www.ubc.ca',
             'University Canada West': 'https://www.ucanwest.ca'}
    images = {'Carleton University': 'carleton_university',
              'University of Ottawa': 'university_of_ottawa',
              'York University': 'york_university',
              'University of Toronto': 'university_of_toronto',
              'Montreal University': 'montreal_university',
              'Polytechnique Montreal': 'politechnique_montreal',
              'Laval University': 'laval_university',
              'TELUQ University': 'teluq_university',
              'University of British Columbia': 'university_of_british_columbia',
              'University Canada West': 'university_canada_west'}
    hostel = {'Carleton University': 'Yes',
              'University of Ottawa': 'Yes',
              'York University': 'Yes',
              'University of Toronto': 'Yes',
              'Montreal University': 'Yes',
              'Polytechnique Montreal': 'No',
              'Laval University': 'No',
              'TELUQ University': 'No',
              'University of British Columbia': 'Yes',
              'University Canada West': 'university_canada_west'}
    scolarship = {'Abu Dhabi University': 'Yes',
                  'Khalifa University': 'Yes',
                  'Murdoch University Dubai': 'Yes',
                  'American University of Sharjah': 'Yes'}
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
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images, requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers
                  )

    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()
    #############################   CANADA   #############################



    cc.createBorders()
    cc.close()
