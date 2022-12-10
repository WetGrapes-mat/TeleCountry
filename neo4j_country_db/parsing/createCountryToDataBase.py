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
                   citizenshipGlobalRank, friendlyToForeigners,
                   # communication
                   communicationOnEnglish,
                   # transport
                   averageTravelTimeToWork, developmentLevelOfPublicTransport,
                   # internet
                   speedOfInternetMbps, freeWifi,
                   # education
                   rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                   requirements,
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
                                         citizenshipGlobalRank, friendlyToForeigners,
                                         # communication
                                         communicationOnEnglish,
                                         # transport
                                         averageTravelTimeToWork, developmentLevelOfPublicTransport,
                                         # internet
                                         speedOfInternetMbps, freeWifi,
                                         # education
                                         rankingOfNationalEducationSystem, universities, faculties, programs, costs,
                                         links, images, requirements,
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
                    citizenshipGlobalRank, friendlyToForeigners,
                    # communication
                    communicationOnEnglish,
                    # transport
                    averageTravelTimeToWork, developmentLevelOfPublicTransport,
                    # internet
                    speedOfInternetMbps, freeWifi,
                    # education
                    rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                    requirements,
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
            resultStr += '\ncreate (city%d:City {name:"%s", isBig:"%s", isResort:"%s"})' % (
                index, city, str(citiesDict[city][0]), str(citiesDict[city][1]))
            resultStr += '\ncreate (country)-[:has_city]->(city%d)' % index
            if index == 1:
                resultStr += '\ncreate (country)-[:capital]->(city%d)' % index
            if citiesDict[city][2] is not None:
                resultStr += '\ncreate(water%d:Water {name:"%s"})' % (index, str(citiesDict[city][2]))
                resultStr += '\ncreate (water%d)-[:washes]->(city%d)' % (index, index)
            index += 1

        # resort
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

        # education
        resultStr += '\ncreate (education:Education {rankingOfNationalEducationSystem:%d})' % rankingOfNationalEducationSystem
        resultStr += '\ncreate (country)-[:education]->(education)\n'

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
                            resultStr += '\nmerge (program%d:Program {name:"%s"})' % (prog, program)
                            resultStr += '\nmerge (univ%d)-[:program]->(program%d)' % (univ_ind, prog)
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
        resultStr += '\ncreate (citizenship:Citizenship {globalRank:%d, friendlyToForeigners:%d})' % (
            citizenshipGlobalRank, friendlyToForeigners)
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
              'Quebec': [True, True, 'Atlantic ocean'], 'Vancouver': [True, True, 'Pacific ocean'],
              'Victoria': [False, True, 'Salish sea']}
    # resort
    sights = {'Parliament building of Canada': [
        "The architectural complex, which hosts working meetings of the Canadian government, looks like a medieval castle from the outside. "
        "It is located in a convenient location for travelers - in the heart of Ottawa. "
        "The gray stone from which the building is built seems gloomy at first glance. "
        "However, the overall composition of the building is so precise and accurate that the complex inspires involuntary respect. "
        "It seems that the architects who built the complex in 1860 were fanatically devoted to the idea of symmetry in architecture."
        "The pointed towers are located strictly symmetrically with respect to the central column, on which the clock runs, visible from everywhere. "
        "The strength of the building is evidenced by the fact that the gray stone is also covered with copper plates. "
        "However, in 1916 the building did not survive the devastating fire. "
        "Reconstruction work was carried out in an organized manner, but they dragged on until 1922.",
        'parliament_building_of_Canada_sight'],
        'Oratory of St. Joseph': [
            "Among those sights that you must visit in Canada is the Oratory of St. Joseph. Construction work began in 1904. "
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
                          'Millions of travelers come here to see this unique natural phenomenon with their own eyes.',
                          'niagara_falls_sight']}
    beaches = {'Wasaga Beach': [
        "The longest freshwater beach in the world, attracting tourists with its 12 km of sandy coastline. "
        "The warm, shallow waters of the beach are ideal for swimming, while the soft white sand is ideal for picnicking, "
        "relaxing and watching the beautiful sunset. This urban beach, which is somewhat reminiscent of the famous beaches in Florida: "
        "Daytona Beach and Fort Lauderdale.", 'wasaga_beach'],
        "Brady’s Beach": [
            "Bradis Beach is located in a very secluded area on the Pacific Ocean. The only way to get here is by ferry, plane or timber barge. "
            "Yes, the path is not easy, but the rest here is worth such a voyage. Try to be there during the Music by The Sea festival. "
            "By August, the water here warms up to temperatures suitable for a refreshing swim. "
            "The advantages of this beach are that it is surrounded by the Pacific Rim National Park, the ocean, and the territory of the Indians. "
            "Excellent diving. Proximity to Barkley Sound islands inhabited by sea lions and bald eagles.",
            "brady_beach"],
        'Ingonish Beach': [
            "Ingonish Beach is the only beach in the Cape Breton Highlands National Park, with a unique opportunity to swim in both fresh and sea water. "
            "This sandy beach is washed away in winter and washed back by waves every spring, and a natural barrier separates the lake from the waters of the Atlantic Ocean. "
            "In addition to swimming, here you will be offered to go on a boat trip to go fishing and, of course, watch the whales in their habitat.",
            'ingonish_beach']}
    mountains = {
        'Robson': ['The highest point of the Rocky Mountains; it is also the highest point of the Canadian Rockies. '
                   'The mountain is located within the Robson Provincial Park in British Columbia.', 'robson_mountain'],
        'Temple': ['Mountain in Banff National Park in the Canadian Rockies, the 7th highest peak in Alberta. '
                   'The Temple is located in the Bow River Valley between Paradise Creek and Moraine Creek and is the highest point in the Lake Louise region.',
                   'temple_mountain'],
        'Snow House': [
            'A mountain on the continental divide of the Columbia Icefield on the border of Banff and Jasper National Parks. '
            'Located in the Canadian Rockies on the border of British Columbia and Alberta. The height of the peak is 3456 m.',
            'snow_house_mountain'],
        'Assiniboine': [
            'Pyramidal mountain located on the American Continental Divide on the border of the Canadian provinces of Alberta and British Columbia. '
            'The height is 3618 m above sea level.', 'assiniboine_mountain']}
    skiResorts = {'Whistler Blackcomb': ['At the heart of Whistler and Blackcomb is the charming village of Whistler. '
                                         "You don't even have to ski to enjoy your trip to Whistler, but if you do, you'll find "
                                         'seemingly limitless terrain that can accommodate any level of skier, from first timers to extreme skiers. '
                                         "You'll find beautiful wide-open bowls at Mount Whistler and incredible groomed runs on both mountains. "
                                         "On Blackcomb, the Horstmann Glacier offers year-round skiing.",
                                         'whistler_blackcomb_resort'],
                  'Lake Louise': [
                      "Lake Louise, in the heart of the Rocky Mountains and less than an hour from the city of Banff, is one of Canada's most famous resorts. "
                      "From the slopes, majestic scenery stretches over the Luke Valley and the surrounding mountains and beyond to the palatial Fairmont Chateau Lake Louise. "
                      "This is a mountain for all skiers, from extreme skiers to families coming here to learn about the sport. "
                      "In a resort with 4,200 acres of rocky terrain, the resort offers a combination of wide-open bowls, steepness, flumes and plenty of groomed trails."
                      "The Lake Louise Ski Resort doesn't have an onsite location, but it does have fantastic daytime facilities at the base, as well as restaurants serving delicious food, "
                      "as well as other restaurants in the mountains. Skiers can take a dip in the nearby village of Lake Louise or the town of Banff.",
                      'lake_louise_resort'],
                  'Revelstoke': [
                      "Located in the interior of British Columbia, about 2.5 hours from the city of Kelowna, Revelstoke is a bit harder to get to some resorts, but well worth it. "
                      "The mountain sees a large number of powder days; few crowds; and offers great terrain, from open bowls to tree trails and starter areas. "
                      "Add to that the affordable accommodation options in Revelstoke; ski slopes, ski slopes on the mountain; and fabulous mountain scenery and it's hard to beat this resort. "
                      "This is not the place for a glamorous five-star experience or shopping experience. It is a mountain of skiers and a great place for families.",
                      'revelstoke_resort']}
    lakes = {'Louise': [
        "A natural wonder of Banff National Park. Lies surrounded by the Rocky Mountains and the bright greenery of the forest, at an altitude of 1646 meters. "
        "The unusual emerald color of the water is due to the presence of rock particles brought into the lake by glaciers. The area of the lake is 0.8 km2. "
        "On the shore there is a 5-star hotel, a number of campsites and tourist centers, nearby is the famous ski resort. "
        "Hiking and cycling routes are organized around the reservoir. Canoe excursions are available.", 'louise_lake'],
        'Moraine': ["One of the most beautiful and photographed lakes in the world. Business card of Canada. "
                    "Its stunning landscapes can be found in many magazines and catalogs, on Canadian currency, Windows screensaver, etc. "
                    "It lies in the Valley of the Ten Peaks of the famous Banff Park, at an altitude of 1885 meters. "
                    "Origin - glacial. The area is 0.5 km2. Routes have been laid out for tourists, it is better to move along them with an experienced guide. "
                    "A hotel was built on the shore, there is a boat rental.", 'moraine_kale'],
        'Superior': [
            'The largest in terms of area in the composition of the Great Five and among the fresh lakes of the world. '
            'Located in Canada and the USA. It occupies an area of 82.7 thousand km2. The shores are indented, there are large bays, islands. '
            'There are many parks on the lake, a marine reserve has been created. The water is cold, even in summer it does not exceed 4 ° C, in winter it does not freeze due to frequent storms. '
            'The lake is rich in fish. Navigable. The major port is Thunder Bay. The southern part of the reservoir is known as the graveyard of ships.',
            'superior_lake']}
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
              'Churchill': [
                  "Thanks to an artificial canal built in the 20th century, most of the water from the Churchill River goes to Saskatchewan to increase hydroelectric power generation. "
                  "The river originates in the central part of the province of Saskatchewan and carries its waters east to Hudson Bay. "
                  "The rich flora and fauna of the river basin was the reason for its nomination for inclusion in the List of Protected Rivers of Canada.",
                  'churchill_river']}
    # universities
    universities = {'Ottawa': ['Carleton University', 'University of Ottawa'],
                    'Toronto': ['York University', 'University of Toronto'],
                    'Montreal': ['Montreal University', 'Polytechnique Montreal'],
                    'Quebec': ['Laval University', 'TELUQ University'],
                    'Vancouver': ['University of British Columbia', 'University Canada West']}
    faculties = {'Carleton University': ['Faculty of Arts', 'Faculty of Computer Engineering and Software',
                                         'Faculty of Education',
                                         'Faculty of Law', 'Faculty of Science',
                                         'Faculty of Social Sciences'],
                 'University of Ottawa': ['Faculty of Arts', 'Faculty of Engineering', 'Faculty of Education',
                                          'Faculty of Science', 'Faculty of Medicine', 'Faculty of Law',
                                          'Faculty of Social Sciences'],
                 'York University': ['Faculty of Education', 'Faculty of Arts',
                                     'Faculty of Medicine, Faculty of Science'],
                 'University of Toronto': ['Faculty of Arts', 'Faculty of Science', 'Faculty of Medicine'],
                 'Montreal University': ['Faculty of Arts', 'Faculty of Science', 'Faculty of Law',
                                         'Faculty of Medicine',
                                         'Faculty of Education', 'Faculty of Medicine'],
                 'Polytechnique Montreal': ['Faculty of Computer Engineering and Software', 'Faculty of Science',
                                            'Faculty of Biomedicine'],
                 'Laval University': ['Faculty of Arts', 'Faculty of Law', 'Faculty of Education',
                                      'Faculty of Forestry', 'Faculty of Medicine'],
                 'TELUQ University': ['Faculty of Arts', 'Faculty of Science', 'Faculty of Medicine'],
                 'University of British Columbia': ['Faculty of Business', 'Faculty of Forestry',
                                                    'Faculty of Education',
                                                    'Faculty of Science', 'Faculty of Medicine', 'Faculty of Law',
                                                    'Faculty of Medicine'],
                 'University Canada West': ['Faculty of Arts', 'Faculty of Computer Engineering and Software',
                                            'Faculty of Education',
                                            'Faculty of Law', 'Faculty of Science',
                                            'Faculty of Social Sciences']}
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
              'University Canada West': 'Yes'}
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
    friendlyToForeigners = 0

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
                  citizenshipGlobalRank, friendlyToForeigners,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,
                  # education
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers
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
    cities = {'Warsaw': [True, True, None], 'Krakow': [True, True, None], 'Lodz': [True, True, None],
              'Wroclaw': [True, True, None], 'Bialystok': [True, True, None]}

    # education
    universities = {
        'Warsaw': ['University of Economics and Human Sciences', 'University of Engineering and Health'],
        # https://univerpl.com.ua/ru/universiteti-varshavi/
        'Krakow': ['Jagiellonian University', 'Krakow Academy named after A.F. Modzhevsky'],
        # https://univerpl.com.ua/ru/universiteti-krakova/
        'Lodz': ['Łódź University of Technology', 'University of Lodz'],
        'Wroclaw': ['Wrocław University of Science and Technology', 'University of Wrocław'],
        'Bialystok': ['Bialystok Technical University', 'University of Bialystok']}

    faculties = {'University of Economics and Human Sciences': ['Faculty of Business', 'Faculty of Finance',
                                                                'Faculty of Psychology',
                                                                'Faculty of Computer Engineering and Software',
                                                                'Faculty of Political Science', 'Faculty of Dietetics'],
                 'University of Engineering and Health': ['Faculty of Administration and Social Sciences',
                                                          'Faculty of Architecture',
                                                          'Faculty of Engineering', 'Faculty of Chemistry',
                                                          'Faculty of Civil Engineering',
                                                          'Faculty of Electrical Engineering'],
                 'Jagiellonian University': ['Faculty of Law and Administration', 'Faculty of Medicine',
                                             'Faculty of Pharmacy', 'Faculty of Health Science',
                                             'Faculty of Philosophy',
                                             'Faculty of History', 'Faculty of Philology'],
                 'Krakow Academy named after A.F. Modzhevsky': ['Faculty of Arts',
                                                                'Faculty of Space Infrastructure',
                                                                'Faculty of Computer Engineering and Software'],
                 'Łódź University of Technology': [
                     'Faculty of Electrical Engineering',
                     'Faculty of Chemistry', 'Faculty of Biotechnology',
                     'Faculty of Architecture', 'Faculty of Physics',
                     'Faculty of Business'],
                 'University of Lodz': ['Faculty of Biology', 'Faculty of Chemistry',
                                        'Faculty of Sociology', 'Faculty of Philology', 'Faculty of Psychology',
                                        'Faculty of Computer Engineering and Software', 'Faculty of Business'],
                 'Wrocław University of Science and Technology': ['Faculty of Architecture', 'Faculty of Chemistry',
                                                                  'Faculty of Electrical Engineering',
                                                                  'Faculty of Business'],
                 'University of Wrocław': ['Faculty of Biotechnology', 'Faculty of Chemistry', 'Faculty of Physics',
                                           'Faculty of Computer Engineering and Software', 'Faculty of Social Sciences',
                                           'Faculty of Biology'],
                 'Bialystok Technical University': ['Faculty of Architecture',
                                                    'Faculty of Computer Engineering and Software',
                                                    'Faculty of Engineering',
                                                    'Faculty of Business'],
                 'University of Bialystok': ['Faculty of Social Sciences'
                                             'Faculty of Computer Engineering and Software', 'Faculty of Business']}

    programs = {'University of Economics and Human Sciences': ['Magistracy', 'Undergraduate', 'MBA'],
                'University of Engineering and Health': ['Magistracy'],
                'Jagiellonian University': ['Magistracy', 'Undergraduate', 'MBA'],
                'Krakow Academy named after A.F. Modzhevsky': ['Foundation', 'Undergraduate', 'MBA'],
                'Łódź University of Technology': ['Magistracy', 'Undergraduate'],
                'University of Lodz': ['Magistracy', 'Undergraduate'],
                'Wrocław University of Science and Technology': ['Magistracy', 'Undergraduate', 'MBA'],
                'University of Wrocław': ['Magistracy', 'Undergraduate'],
                'Bialystok Technical University': ['Magistracy', 'Undergraduate', 'MBA'],
                'University of Bialystok': ['Magistracy', 'Undergraduate']}
    links = {'University of Economics and Human Sciences': 'https://vizja.pl/en/',
             'University of Engineering and Health': 'https://entrant.eu/en/university/universytet-kosmetologiyi-ta-doglyadu-za-zdorov-yam/',
             'Jagiellonian University': 'https://en.uj.edu.pl/en_GB/start',
             'Krakow Academy named after A.F. Modzhevsky': 'https://en.ka.edu.pl/',
             'Łódź University of Technology': 'https://p.lodz.pl/',
             'University of Lodz': 'https://www.uni.lodz.pl/en',
             'Wrocław University of Science and Technology': 'https://pwr.edu.pl/en/',
             'University of Wrocław': 'https://uwr.edu.pl/',
             'Bialystok Technical University': 'https://pb.edu.pl/',
             'University of Bialystok': 'https://uwb.edu.pl/home'}
    images = {'University of Economics and Human Sciences': 'university_of_economics_and_human_sciences',
              'University of Engineering and Health': 'university_of_engineering_and_health',
              'Jagiellonian University': 'jagiellonian_university',
              'Krakow Academy named after A.F. Modzhevsky': 'krakow_academy_named_after_af_modzhevsky',
              'Łódź University of Technology': 'lodz_university_of_technology',
              'University of Lodz': 'university_of_lodz',
              'Wrocław University of Science and Technology': 'wroclaw_university_of_science_and_technology',
              'University of Wrocław': 'university_of_wroclaw',
              'Bialystok Technical University': 'bialystok_technical_university',
              'University of Bialystok': 'university_of_bialystok'}
    # общага
    hostel = {'University of Economics and Human Sciences': 'Yes',
              'University of Engineering and Health': 'Yes',
              'Jagiellonian University': 'Yes',
              'Krakow Academy named after A.F. Modzhevsky': 'No',
              'Łódź University of Technology': 'Yes',
              'University of Lodz': 'No',
              'Wrocław University of Science and Technology': 'No',
              'University of Wrocław': 'No',
              'Bialystok Technical University': 'Yes',
              'University of Bialystok': 'Yes'}
    # стипендия
    scolarship = {'University of Economics and Human Sciences': 'Yes',
                  'University of Engineering and Health': 'Yes',
                  'Jagiellonian University': 'Yes',
                  'Krakow Academy named after A.F. Modzhevsky': 'Yes',
                  'Łódź University of Technology': 'Yes',
                  'University of Lodz': 'Yes',
                  'Wrocław University of Science and Technology': 'Yes',
                  'University of Wrocław': 'Yes',
                  'Bialystok Technical University': 'Yes',
                  'University of Bialystok': 'Yes'
                  }
    # требования к поступлению
    requirements = {'University of Economics and Human Sciences': 'photo. '
                                                                  'passport. '
                                                                  'high school diploma and attachment to high school diploma with subjects and grades. '
                                                                  'bachelor diploma and transcript of studies (for Masters studies). '
                                                                  'certificate of language proficiency (if available)',
                    'University of Engineering and Health': 'minimum GPA of 2 in order to stand a good chance to get admission',
                    'Jagiellonian University': 'complete TOEFL exam with a minimum score of 87. c) TOEFL/IELTS scores if the applicants native language is not English.',
                    'Krakow Academy named after A.F. Modzhevsky': 'Request a list of necessary documents directly from a university, as it may vary for different countries.',
                    'Łódź University of Technology': 'Legalised original (or duplicate) of relevant education certificate(s). Documentary evidence of learning. Polish translation of the certificate (diploma). Passport.',
                    'University of Lodz': 'A high school diploma, a transcript of records showing the subjects/grades and a certificate of proficiency in English (unless the secondary education was taught in English)',
                    'Wrocław University of Science and Technology': 'Passport for inspection,'
                                                                    'your application form printed out from the application system and signed;'
                                                                    'transfer details of payment for your fees (application, tuition, student ID);'
                                                                    'your language certificate or another document serving as such'
                                                                    'for undergraduate programs: your secondary school diploma with a list of grades, for postgraduate programs: your Bachelor’s diploma with a full academic transcript. These documents should be legalized/apostilled and presented together with a certified translation into Polish or English made by a sworn translator.',
                    'University of Wrocław': 'High School graduation certificate or equivalent with decision about nostrification (learn more about nostrification procedure on our website)'
                                             'High School transcript of grades.'
                                             'Certificate confirming access to higher education in your country.',
                    'Bialystok Technical University': 'Secondary school certificate (12 years of education) being the equivalent of Polish secondary school certificate. English language international B2 certificate (upper intermediate) such as FCE, IELTS (min. 6 points),',
                    'University of Bialystok': 'Positive grades in two out of four subjects - Chemistry, Biology, Physics or Mathematics - must be shown on the certificate. or have passed the Matura Exam (High School Final Exam) in two out of four subjects: Chemistry, Biology, Physics or Mathematics.'}

    costs = {'University of Economics and Human Sciences': 2600,
             'University of Engineering and Health': 4300,
             'Jagiellonian University': 3500,
             'Krakow Academy named after A.F. Modzhevsky': 3200,
             'Łódź University of Technology': 2700,
             'University of Lodz': 2400,
             'Wrocław University of Science and Technology': 4100,
             'University of Wrocław': 3000,
             'Bialystok Technical University': 2400,
             'University of Bialystok': 13500}

    # resort
    sights = {'sight_name1': ["dicsr", '_sight'],
              'sight_name2': ["dicsr", '_sight'],
              'sight_name3': ["dicsr", '_sight']}
    beaches = {'beach_name1': ["dicsr", '_beach'],
               "beach_name2": ["dicsr", '_beach'],
               'beach_name3': ["dicsr", '_beach']}
    mountains = {'mountain_name1': ["dicsr", '_mountain'],
                 'mountain_name2': ["dicsr", '_mountain'],
                 'mountain_name3': ["dicsr", '_mountain'],
                 'mountain_name4': ["dicsr", '_mountain']}
    skiResorts = {'ski_resort_name1': ["dicsr", '_resort'],
                  'ski_resort_name2': ["dicsr", '_resort'],
                  'ski_resort_name3': ["dicsr", '_resort']}
    lakes = {'lake_name1': ["dicsr", '_lake'],
             'lake_name2': ["dicsr", '_lake'],
             'lake_name3': ["dicsr", '_lake']}
    rivers = {'river_name1': ["dicsr", '_river'],
              'river_name2': ["discr", '_river'],
              'river_name3': ["discr", '_river']}

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
    friendlyToForeigners = 1

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
                  citizenshipGlobalRank, friendlyToForeigners,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,
                  # education
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers
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
    cities = {'Prague': [True, True, None], 'Brno': [True, True, None], 'Pilsen': [True, True, None],
              'Ostrava': [True, True, None], 'Olomouc': [True, True, None]}

    # education
    universities = {'Prague': ['Czech Technical University in Prague', 'Prague City University'],
                    'Brno': ['Brno University of Technology', 'Masaryk University'],
                    'Pilsen': ['University of West Bohemia', 'Charles University'],
                    'Ostrava': ['University of Ostrava', 'Ostrava University of Technology'],
                    'Olomouc': ['Palacký University Olomouc', 'Moravian University Olomouc']}

    faculties = {
        'Czech Technical University in Prague': ['Faculty of Architecture', 'Faculty of Medicine',
                                                 'Faculty of Engineering',
                                                 'Faculty of Computer Engineering and Software'],
        'Prague City University': ['Faculty of Arts', 'Faculty of Business',
                                   'Faculty of Computer Engineering and Software'],
        'Brno University of Technology': ['Faculty of Architecture', 'Faculty of Computer Engineering and Software', 'Faculty of Business',
                                          'Faculty of Engineering',
                                          'Faculty of Computer Engineering and Software',
                                          'Faculty of Arts'],
        'Masaryk University': ['Faculty of Law', 'Faculty of Medicine', 'Faculty of Science', 'Faculty of Arts',
                               'Faculty of Business', 'Faculty of Computer Engineering and Software'],
        'University of West Bohemia': ['Faculty of Science', 'Faculty of Arts', 'Faculty of Business',
                                       'Faculty of Electrical Engineering', 'Faculty of Law'],
        'Charles University': ['Faculty of Law', 'Faculty of Medicine', 'Faculty of Arts',
                               'Faculty of Science' 'Faculty of Social Sciences'],
        'University of Ostrava': ['Faculty of Science', 'Faculty of Arts', 'Faculty of Social Sciences',
                                  'Faculty of Medicine'],
        'Ostrava University of Technology': ['Faculty of Business',
                                             'Faculty of Engineering', 'Faculty of Computer Engineering and Software'],
        'Palacký University Olomouc': ['Faculty of Medicine', 'Faculty of Arts', 'Faculty of Science',
                                       'Faculty of Education', 'Faculty of Law', 'Faculty of Health Sciences'],
        'Moravian University Olomouc': ['Faculty of Business', 'Faculty of Social Sciences']}

    programs = {'Czech Technical University in Prague': ['Magistracy', 'Undergraduate'],
                'Prague City University': ['Magistracy', 'Undergraduate', 'MBA'],
                'Brno University of Technology': ['Magistracy', 'Undergraduate'],
                'Masaryk University': ['Foundation', 'Undergraduate', 'MBA'],
                'University of West Bohemia': ['Magistracy', 'Undergraduate'],
                'Charles University': ['Magistracy', 'Undergraduate', 'MBA'],
                'University of Ostrava': ['Magistracy', 'Undergraduate'],
                'Ostrava University of Technology': ['Magistracy', 'Undergraduate'],
                'Palacký University Olomouc': ['Magistracy', 'Undergraduate', 'MBA'],
                'Moravian University Olomouc': ['Magistracy', 'Undergraduate']}
    links = {'Czech Technical University in Prague': 'https://www.cvut.cz/en',
             'Prague City University': 'https://www.praguecityuniversity.cz/',
             'Brno University of Technology': 'https://www.vut.cz/en/',
             'Masaryk University': 'https://www.muni.cz/en',
             'University of West Bohemia': 'https://www.zcu.cz/en/index.html',
             'Charles University': 'https://cuni.cz/uken-1.html',
             'University of Ostrava': 'https://www.osu.eu/',
             'Ostrava University of Technology': 'https://www.vsb.cz/en',
             'Palacký University Olomouc': 'https://www.upol.cz/en/',
             'Moravian University Olomouc': 'https://www.mvso.cz/en'}

    images = {'Czech Technical University in Prague': 'czech_technical_university_in_prague',
              'Prague City University': 'prague_city_university',
              'Brno University of Technology': 'brno_university_of_technology',
              'Masaryk University': 'masaryk_university',
              'University of West Bohemia': 'university_of_west_bohemia',
              'Charles University': 'charles_university',
              'University of Ostrava': 'university_of_ostrava',
              'Ostrava University of Technology': 'ostrava_university_of_technology',
              'Palacky University Olomouc': 'palacky_university_olomouc',
              'Moravian University Olomouc': 'moravian_university_olomouc'}
    # общага
    hostel = {'Czech Technical University in Prague': 'Yes',
              'Prague City University': 'Yes',
              'Brno University of Technology': 'Yes',
              'Masaryk University': 'Yes',
              'University of West Bohemia': 'Yes',
              'Charles University': 'No',
              'University of Ostrava': 'No',
              'Ostrava University of Technology': 'No',
              'Palacky University Olomouc': 'Yes',
              'Moravian University Olomouc': 'No'}
    # стипендия
    scolarship = {'Czech Technical University in Prague': 'Yes',
                  'Prague City University': 'Yes',
                  'Brno University of Technology': 'Yes',
                  'Masaryk University': 'Yes',
                  'University of West Bohemia': 'Yes',
                  'Charles University': 'Yes',
                  'University of Ostrava': 'Yes',
                  'Ostrava University of Technology': 'Yes',
                  'Palacky University Olomouc': 'Yes',
                  'Moravian University Olomouc': 'Yes'
                  }
    # требования к поступлению
    requirements = {
        'Czech Technical University in Prague': 'A certificate of successful graduation from a secondary school.'
                                                'A duly completed and submitted application for a study programme.'
                                                'Documentary evidence that fees and charges have been paid.'
                                                'Compliance with the requirements for the entrance procedures.',
        'Prague City University': 'Confirmation of English level upon entry. Letter of motivation. Portfolio (only School of Art & Design & Creative Media Production). Final interview.',
        'Brno University of Technology': 'Curriculum vitae. '
                                         'Statement of purpose '
                                         'Recommendation letter (if required) '
                                         'English language qualifications TOEFL (if required) ',
        'Masaryk University': 'diploma or statement of expected graduation. '
                              'diploma supplement/Transcript of records. '
                              'CV. '
                              'proof of English language level. '
                              'motivation letter. '
                              'own academic work/publication (e.g. bachelor, diploma thesis) '
                              'copy of passport.',
        'University of West Bohemia': 'Curriculum vitae. '
                                      'Statement of purpose '
                                      'Recommendation letter (if required) '
                                      'English language qualifications TOEFL (if required) ',
        'Charles University': 'Curriculum vitae. '
                              'Statement of purpose '
                              'Recommendation letter (if required) '
                              'English language qualifications TOEFL (if required) ',
        'University of Ostrava': 'Senior School Certificates. '
                                 'Official Transcripts. '
                                 'English Language Proficiency Scores. '
                                 'Norwegian Language Proficiency Scores. '
                                 'CV/Resume. '
                                 'Letter of Recommendations. '
                                 'Personal Statement. ',
        'Ostrava University of Technology': 'A certificate of successful graduation from a secondary school.'
                                            'A duly completed and submitted application for a study programme.'
                                            'Documentary evidence that fees and charges have been paid.'
                                            'Compliance with the requirements for the entrance procedures.',
        'Palacky University Olomouc': 'diploma or statement of expected graduation. '
                                      'diploma supplement/Transcript of records. '
                                      'CV. '
                                      'proof of English language level. '
                                      'motivation letter. '
                                      'own academic work/publication (e.g. bachelor, diploma thesis) '
                                      'copy of passport.',
        'Moravian University Olomouc': 'Student visa. '
                                       'Online Application form. '
                                       'TOEFL Certificate. '
                                       'World Education Services evaluation. '
                                       'Passport. '
                                       'Photographs. '
                                       'IELTS Certificate. '
                                       'Proof of fee payment. '
                                       'Health and Life Insurance'}

    costs = {'Czech Technical University in Prague': 4700,
             'Prague City University': 4500,
             'Brno University of Technology': 4900,
             'Masaryk University': 3900,
             'University of West Bohemia': 3700,
             'Charles University': 3750,
             'University of Ostrava': 4100,
             'Ostrava University of Technology': 4500,
             'Palacky University Olomouc': 3400,
             'Moravian University Olomouc': 3550}

    # resort
    sights = {'sight_name1': ["", '_sight'],
              'sight_name2': ["", '_sight'],
              'sight_name3': ["", '_sight']}
    beaches = {'beach_name1': ["", '_beach'],
               "beach_name2": ["", '_beach'],
               'beach_name3': ["", '_beach']}
    mountains = {'mountain_name1': ["", '_mountain'],
                 'mountain_name2': ["", '_mountain'],
                 'mountain_name3': ['', '_mountain'],
                 'mountain_name4': ['', '_mountain']}
    skiResorts = {'ski_resort_name1': ["", '_resort'],
                  'ski_resort_name2': ["", '_resort'],
                  'ski_resort_name3': ["", '_resort']}
    lakes = {'lake_name1': ["", '_lake'],
             'lake_name2': ["", '_lake'],
             'lake_name3': ['', '_lake']}
    rivers = {'river_name1': ["dicsr", '_river'],
              'river_name2': ["discr", '_river'],
              'river_name3': ["discr", '_river']}

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
    friendlyToForeigners = 2

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
                  citizenshipGlobalRank, friendlyToForeigners,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,
                  # education
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers
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
    cities = {'Berlin': [True, True, None], 'Hamburg': [True, True, None], 'Bremen': [True, True, None],
              'Dresden': [True, True, None], 'Nuremberg': [True, True, None]}

    # education
    universities = {'Berlin': ['Humboldt University of Berlin', 'Technical University of Berlin'],
                    'Hamburg': ['University of Hamburg', 'HafenCity University Hamburg'],
                    'Bremen': ['University of Bremen', 'Jacobs University Bremen'],
                    'Dresden': ['Dresden University of Technology', 'Dresden University of Applied Sciences'],
                    'Nuremberg': ['Nuremberg Institute of Technology', 'Academy of Fine Arts']}
    faculties = {'Humboldt University of Berlin': ['Faculty of Law', 'Faculty of Mathematics', 'Faculty of Arts',
                                                   'Faculty of Business', 'Faculty of Language'],
                 'Technical University of Berlin': ['Faculty of Education', 'Faculty of Mathematics',
                                                    'Faculty of Science',
                                                    'Faculty of Computer Engineering and Software' 'Faculty of Business'],
                 'University of Hamburg': ['Faculty of Law', 'Faculty of Business',
                                           'Faculty of Social Sciences', 'Faculty of Medicine', 'Faculty of Education',
                                           'Faculty of Mathematics', 'Faculty of Business'],
                 'HafenCity University Hamburg': ['Faculty of Architecture', 'Faculty of Engineering',
                                                  'Faculty of Mathematics'],
                 'University of Bremen': ['Faculty of Biology', 'Faculty of Chemistry', 'Faculty of Mathematics',
                                          'Faculty of Computer Engineering and Software', 'Faculty of Law',
                                          'Faculty of Social Sciences'],
                 'Jacobs University Bremen': ['Faculty of Computer Engineering and Software', 'Faculty of Physics',
                                              'Faculty of Mathematics',
                                              'Faculty of Business', 'Faculty of Social Sciences',
                                              'Faculty of Psychology'],
                 'Dresden University of Technology': ['Faculty of Biology', 'Faculty of Mathematics',
                                                      'Faculty of Psychology',
                                                      'Faculty of Physics', 'Faculty of Chemistry',
                                                      'Faculty of Education',
                                                      'Faculty of Arts', 'Faculty of Computer Engineering and Software',
                                                      'Faculty of Electrical Engineering'],
                 'Dresden University of Applied Sciences': ['Faculty of Biology', 'Faculty of Chemistry',
                                                            'Faculty of Mathematics',
                                                            'Faculty of Physics', 'Faculty of Psychology'],
                 'Nuremberg Institute of Technology': ['Faculty of Chemistry', 'Faculty of Mathematics',
                                                       'Faculty of Architecture',
                                                       'Faculty of Arts',
                                                       'Faculty of Computer Engineering and Software',
                                                       'Faculty of Electrical Engineering'],
                 'Academy of Fine Arts': ['Faculty of Arts', 'Faculty of Psychology',
                                          'Faculty of Architecture', 'Faculty of Law']}

    programs = {'Humboldt University of Berlin': ['Magistracy', 'Undergraduate', 'MBA'],
                'Technical University of Berlin': ['Magistracy', 'Undergraduate'],
                'University of Hamburg': ['Magistracy', 'Undergraduate'],
                'HafenCity University Hamburg': ['Foundation', 'Undergraduate', 'MBA'],
                'University of Bremen': ['Magistracy', 'Undergraduate'],
                'Jacobs University Bremen': ['Magistracy', 'Undergraduate', 'MBA'],
                'Dresden University of Technology': ['Magistracy', 'Undergraduate'],
                'Dresden University of Applied Sciences': ['Magistracy', 'Undergraduate'],
                'Nuremberg Institute of Technology': ['Magistracy', 'Undergraduate', 'MBA'],
                'Academy of Fine Arts': ['Magistracy', 'Undergraduate']}
    links = {'Humboldt University of Berlin': 'https://www.hu-berlin.de/en',
             'Technical University of Berlin': 'https://www.tu.berlin/en/',
             'University of Hamburg': 'https://www.uni-hamburg.de/en.html',
             'HafenCity University Hamburg': 'https://www.hcu-hamburg.de/',
             'University of Bremen': 'https://www.uni-bremen.de/',
             'Jacobs University Bremen': 'https://www.jacobs-university.de/',
             'Dresden University of Technology': 'https://tu-dresden.de/?set_language=en',
             'Dresden University of Applied Sciences': 'https://www.htw-dresden.de/',
             'Nuremberg Institute of Technology': 'https://www.th-nuernberg.eu/',
             'Academy of Fine Arts': 'https://www.academyoffinearts.in/'}

    images = {'Humboldt University of Berlin': 'humboldt_university_of_berlin',
              'Technical University of Berlin': 'technical_university_of_berlin',
              'University of Hamburg': 'university_of_hamburg',
              'HafenCity University Hamburg': 'hafencity_university_hamburg',
              'University of Bremen': 'university_of_bremen',
              'Jacobs University Bremen': 'jacobs_university_bremen',
              'Dresden University of Technology': 'dresden_university_of_technology',
              'Dresden University of Applied Sciences': 'dresden_university_of_applied_sciences',
              'Nuremberg Institute of Technology': 'nuremberg_institute_of_technology',
              'Academy of Fine Arts': 'academy_of_fine_arts'}
    # общага
    hostel = {'Humboldt University of Berlin': 'Yes',
              'Technical University of Berlin': 'Yes',
              'University of Hamburg': 'Yes',
              'HafenCity University Hamburg': 'Yes',
              'University of Bremen': 'Yes',
              'Jacobs University Bremen': 'No',
              'Dresden University of Technology': 'No',
              'Dresden University of Applied Sciences': 'No',
              'Nuremberg Institute of Technology': 'Yes',
              'Academy of Fine Arts': 'Yes'}
    # стипендия
    scolarship = {'Humboldt University of Berlin': 'Yes',
                  'Technical University of Berlin': 'Yes',
                  'University of Hamburg': 'Yes',
                  'HafenCity University Hamburg': 'Yes',
                  'University of Bremen': 'Yes',
                  'Jacobs University Bremen': 'Yes',
                  'Dresden University of Technology': 'Yes',
                  'Dresden University of Applied Sciences': 'Yes',
                  'Nuremberg Institute of Technology': 'Yes',
                  'Academy of Fine Arts': 'Yes'
                  }
    # требования к поступлению
    requirements = {'Humboldt University of Berlin': 'Academic records and transcripts.'
                                                     'Language Proficiency Proof.'
                                                     'A CV (from the commencement of education at school-level)'
                                                     'Fee Receipt produced by Uni-Assist.'
                                                     'Photocopy of Passport or an Identification Card ( Applicable only to EU Students)',
                    'Technical University of Berlin': 'Admission Requirement: To secure admission in TU berlin, Applicants are required to have a bachelors degree in a relevant field. Additionally, international students also have to demonstrate proficiency in English or German language depending upon the language of instruction of the program.',
                    'University of Hamburg': 'Higher education entrance eligibility- German Abitur. '
                                             'Academic transcripts. '
                                             'School leaving certificate. '
                                             'English language proficiency proof. '
                                             'German language proficiency proof. ',
                    'HafenCity University Hamburg': 'Language Proficiency Proof.'
                                                    'A CV (from the commencement of education at school-level)'
                                                    'Fee Receipt produced by Uni-Assist.'
                                                    'Photocopy of Passport or an Identification Card ( Applicable only to EU Students)',
                    'University of Bremen': 'Certificate of Bachelor degree or official academic transcript of Study Records of your Bachelor studies. '
                                            'Detailed and current curriculum vitae (CV), written in English. '
                                            'Letter of Motivation, explaining your interest for enrollment in the Master of Ecology program, written in English. ',
                    'Jacobs University Bremen': 'Academic transcripts. '
                                                'School leaving certificate. '
                                                'English language proficiency proof. '
                                                'German language proficiency proof.',
                    'Dresden University of Technology': 'Valid passport.'
                                                        'Two-recent Passport size photo.'
                                                        'University entrance qualification recognized by Germany (A-Levels or equivalent)'
                                                        'Proof of previous academic performance.'
                                                        'Proof of financial resources (8,700 EUR per year)'
                                                        'Letter of admission from the TU Dresden.',
                    'Dresden University of Applied Sciences': 'Valid passport.'
                                                              'Two-recent Passport size photo.'
                                                              'University entrance qualification recognized by Germany (A-Levels or equivalent)'
                                                              'Proof of previous academic performance.',
                    'Nuremberg Institute of Technology': 'Certificate of Bachelor degree or official academic transcript of Study Records of your Bachelor studies. '
                                                         'Detailed and current curriculum vitae (CV), written in English.',
                    'Academy of Fine Arts': 'Basic admissions materials. Application form or online application. '
                                            'Statement of Intent. One page essay explaining personal goals for graduate school or essay related to a topic as required by the Department. '
                                            'Resume. '
                                            'Portfolio/Demo Reel. '
                                            'Additional Materials. '
                                            'Complete Your Application. '
                    }

    costs = {'Humboldt University of Berlin': 3100,
             'Technical University of Berlin': 3500,
             'University of Hamburg': 2900,
             'HafenCity University Hamburg': 3200,
             'University of Bremen': 3150,
             'Jacobs University Bremen': 2750,
             'Dresden University of Technology': 3300,
             'Dresden University of Applied Sciences': 3150,
             'Nuremberg Institute of Technology': 3600,
             'Academy of Fine Arts': 2500}

    sights = {'sight_name1': ["", '_sight'],
              'sight_name2': ["", '_sight'],
              'sight_name3': ["", '_sight']}
    beaches = {'beach_name1': ["", '_beach'],
               "beach_name2": ["", '_beach'],
               'beach_name3': ["", '_beach']}
    mountains = {'mountain_name1': ["", '_mountain'],
                 'mountain_name2': ["", '_mountain'],
                 'mountain_name3': ['', '_mountain'],
                 'mountain_name4': ['', '_mountain']}
    skiResorts = {'ski_resort_name1': ["", '_resort'],
                  'ski_resort_name2': ["", '_resort'],
                  'ski_resort_name3': ["", '_resort']}
    lakes = {'lake_name1': ["", '_lake'],
             'lake_name2': ["", '_lake'],
             'lake_name3': ['', '_lake']}
    rivers = {'river_name1': ["dicsr", '_river'],
              'river_name2': ["discr", '_river'],
              'river_name3': ["discr", '_river']}

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
    friendlyToForeigners = 0

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
                  citizenshipGlobalRank, friendlyToForeigners,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,
                  # education
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers
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
    cities = {'Bratislava': [True, True, None], 'Kosice': [True, True, None], 'Nitra': [True, True, None],
              'Presov': [True, True, None], 'Banska Bystrica': [True, True, None]}

    # education
    universities = {'Bratislava': ['Slovak University of Technology in Bratislava', 'Comenius University Bratislava'],
                    'Kosice': ['University of Veterinary Medicine in Kosice', 'Pavol Josef Safarik University'],
                    'Nitra': ['Slovak University of Agriculture in Nitra', 'Constantine the Philosopher University'],
                    'Presov': ['University of Presov', 'International Business College ISM Slovakia in Presov'],
                    'Banska Bystrica': ['Matej Bel University in Banská Bystrica',
                                        'Academy of Arts in Banská Bystrica']}
    faculties = {'Slovak University of Technology in Bratislava': ['Faculty of Civil Engineering',
                                                                   'Faculty of Electrical Engineering',
                                                                   'Faculty of Mechanical Engineering',
                                                                   'Faculty of Chemistry',
                                                                   'Faculty of Architecture', 'Faculty of Science'],
                 'Comenius University Bratislava': ['Faculty of Medicine', 'Faculty of Law', 'Faculty of Arts',
                                                    'Faculty of Natural Sciences', 'Faculty of Education',
                                                    'Faculty of Medicine'],
                 'University of Veterinary Medicine in Kosice': ['Faculty of Medicine',
                                                                 'Faculty of Veterinary Medicine',
                                                                 'Faculty of Veterinary Surgery'],
                 'Pavol Josef Safarik University': ['Faculty of Medicine', 'Faculty of Biology', 'Faculty of Surgery'],
                 'Slovak University of Agriculture in Nitra': ['Faculty of Agrobiology', 'Faculty of Biotechnology',
                                                               'Faculty of Engineering',
                                                               'Faculty of Business'],
                 'Constantine the Philosopher University': ['Faculty of Arts', 'Faculty of Natural Sciences',
                                                            'Faculty of Informatics'],
                 'University of Presov': ['Faculty of Arts', 'Faculty of Business', 'Faculty of Business',
                                          'Faculty of Education', 'Faculty of Sports', 'Faculty of Health Care'],
                 'International Business College ISM Slovakia in Presov': ['Faculty of Business',
                                                                           'Faculty of Law'],
                 'Matej Bel University in Banská Bystrica': ['Faculty of Business', 'Faculty of Natural Science',
                                                             'Faculty of Arts', 'Faculty of Education',
                                                             'Faculty of Law'],
                 'Academy of Arts in Banská Bystrica': ['Faculty of Dramatic Arts', 'Faculty of Performing Arts',
                                                        'Faculty of Arts']}

    programs = {'Slovak University of Technology in Bratislava': ['Magistracy', 'Undergraduate'],
                'Comenius University Bratislava': ['Magistracy', 'Undergraduate'],
                'University of Veterinary Medicine in Kosice': ['Magistracy', 'Undergraduate'],
                'Pavol Josef Safarik University': ['Foundation', 'Undergraduate', 'MBA'],
                'Slovak University of Agriculture in Nitra': ['Magistracy', 'Undergraduate'],
                'Constantine the Philosopher University': ['Magistracy', 'Undergraduate'],
                'University of Presov': ['Magistracy', 'Undergraduate', 'MBA'],
                'International Business College ISM Slovakia in Presov': ['Magistracy', 'Undergraduate', 'MBA'],
                'Matej Bel University in Banská Bystrica': ['Magistracy', 'Undergraduate', 'MBA'],
                'Academy of Arts in Banská Bystrica': ['Magistracy', 'Undergraduate']}
    links = {'Slovak University of Technology in Bratislava': 'https://www.stuba.sk/english.html?page_id=132',
             'Comenius University Bratislava': 'https://uniba.sk/en/',
             'University of Veterinary Medicine in Kosice': 'https://www.uvlf.sk/en',
             'Pavol Josef Safarik University': 'https://www.upjs.sk/en/faculty-of-medicine/',
             'Slovak University of Agriculture in Nitra': 'https://www.uniag.sk/en/main-page',
             'Constantine the Philosopher University': 'https://www.ukf.sk/en/university',
             'University of Presov': 'https://www.unipo.sk/en/',
             'International Business College ISM Slovakia in Presov': 'https://free-apply.com/en/university/1070300002',
             'Matej Bel University in Banská Bystrica': 'https://www.umb.sk/ru/',
             'Academy of Arts in Banská Bystrica': 'https://www.aku.sk/en/'}

    images = {'Slovak University of Technology in Bratislava': 'slovak_university_of_technology_in_bratislava',
              'Comenius University Bratislava': 'comenius_university_bratislava',
              'University of Veterinary Medicine in Kosice': 'university_of_veterinary_medicine_in_kosice',
              'Pavol Josef Safarik University': 'pavol_josef_safarik_university',
              'Slovak University of Agriculture in Nitra': 'slovak_university_of_agriculture_in_nitra',
              'Constantine the Philosopher University': 'constantine_the_philosopher_university',
              'University of Presov': 'university_of_presov',
              'International Business College ISM Slovakia in Presov': 'international_business_college_ism_slovakia_in_presov',
              'Matej Bel University in Banská Bystrica': 'matej_bel_university_in_banska_bystrica',
              'Academy of Arts in Banská Bystrica': 'academy_of_arts_in_banska_bystrica'}
    # общага
    hostel = {'Slovak University of Technology in Bratislava': 'Yes',
              'Comenius University Bratislava': 'Yes',
              'University of Veterinary Medicine in Kosice': 'Yes',
              'Pavol Josef Safarik University': 'Yes',
              'Slovak University of Agriculture in Nitra': 'Yes',
              'Constantine the Philosopher University': 'No',
              'University of Presov': 'Yes',
              'International Business College ISM Slovakia in Presov': 'No',
              'Matej Bel University in Banská Bystrica': 'Yes',
              'Academy of Arts in Banská Bystrica': 'No'}
    # стипендия
    scolarship = {'Slovak University of Technology in Bratislava': 'Yes',
                  'Comenius University Bratislava': 'Yes',
                  'University of Veterinary Medicine in Kosice': 'Yes',
                  'Pavol Josef Safarik University': 'Yes',
                  'Slovak University of Agriculture in Nitra': 'Yes',
                  'Constantine the Philosopher University': 'Yes',
                  'University of Presov': 'Yes',
                  'International Business College ISM Slovakia in Presov': 'Yes',
                  'Matej Bel University in Banská Bystrica': 'Yes',
                  'Academy of Arts in Banská Bystrica': 'Yes'
                  }
    # требования к поступлению
    requirements = {'Slovak University of Technology in Bratislava': 'Higher Certificate '
                                                                     '40% in English. '
                                                                     '30% in either Mathematics or Mathematical Literacy. '
                                                                     '40% in Life Orientation. '
                                                                     '50% in four vocational subjects.',
                    'Comenius University Bratislava': 'Maintain a minimum IB of 24 in order to stand a good chance to get admission into Comenius University in Bratislava',
                    'University of Veterinary Medicine in Kosice': '5 GCSEs at grades 9 to 4 (A* to C), or equivalent, including English, maths and science',
                    'Pavol Josef Safarik University': 'Valid passport.'
                                                      'Two-recent Passport size photo.'
                                                      'University entrance qualification recognized by Germany (A-Levels or equivalent)'
                                                      'Proof of previous academic performance.',
                    'Slovak University of Agriculture in Nitra': 'Application form '
                                                                 'Decision on recognition of documents on completed secondary education which is issued by the Regional Office of Education in Nitra, Department of Vocational and Methodological Activities, J. Vuruma 1, 949 01 Nitra (procedure for processing the above documents). '
                                                                 'Curriculum Vitae. '
                                                                 'Proof of payment of the fee for admission procedure. ',
                    'Constantine the Philosopher University': 'Higher Certificate '
                                                              '40% in English. '
                                                              '30% in either Mathematics or Mathematical Literacy. '
                                                              '40% in Life Orientation. '
                                                              '50% in four vocational subjects.',
                    'University of Presov': 'A copy of the passport (page with photo and personal data). '
                                            'Autobiography in Slovak. '
                                            'The original certificate of study of subjects and grades for the 8th, 9th, 10th and first six months of the 11th grade, plus a translation into Slovak (if there is no certificate yet). '
                                            'Statement of health '
                                            'Valid health insurance policy. '
                                            'The original document on recognition of the equivalence of the previous education of a foreigner in Slovakia, issued by the Presevo regional department of the education department. '
                                            '6 photo cards 30 x 35 mm.',
                    'International Business College ISM Slovakia in Presov': 'Application form '
                                                                             'Decision on recognition of documents on completed secondary education which is issued by the Regional Office of Education in Nitra, Department of Vocational and Methodological Activities, J. Vuruma 1, 949 01 Nitra (procedure for processing the above documents). '
                                                                             'Curriculum Vitae. '
                                                                             'Proof of payment of the fee for admission procedure. ',
                    'Matej Bel University in Banská Bystrica': 'Valid passport.'
                                                               'Two-recent Passport size photo.'
                                                               'University entrance qualification recognized by Germany (A-Levels or equivalent)'
                                                               'Proof of previous academic performance.',
                    'Academy of Arts in Banská Bystrica': 'Higher Certificate '
                                                          '40% in English. '
                                                          '30% in either Mathematics or Mathematical Literacy. '
                                                          '40% in Life Orientation. '
                                                          '50% in four vocational subjects.'}

    costs = {'Slovak University of Technology in Bratislava': 900,
             'Comenius University Bratislava': 890,
             'University of Veterinary Medicine in Kosice': 950,
             'Pavol Josef Safarik University': 990,
             'Slovak University of Agriculture in Nitra': 930,
             'Constantine the Philosopher University': 2500,
             'University of Presov': 1000,
             'International Business College ISM Slovakia in Presov': 1100,
             'Matej Bel University in Banská Bystrica': 970,
             'Academy of Arts in Banská Bystrica': 830}

    sights = {'sight_name1': ["", '_sight'],
              'sight_name2': ["", '_sight'],
              'sight_name3': ["", '_sight']}
    beaches = {'beach_name1': ["", '_beach'],
               "beach_name2": ["", '_beach'],
               'beach_name3': ["", '_beach']}
    mountains = {'mountain_name1': ["", '_mountain'],
                 'mountain_name2': ["", '_mountain'],
                 'mountain_name3': ['', '_mountain'],
                 'mountain_name4': ['', '_mountain']}
    skiResorts = {'ski_resort_name1': ["", '_resort'],
                  'ski_resort_name2': ["", '_resort'],
                  'ski_resort_name3': ["", '_resort']}
    lakes = {'lake_name1': ["", '_lake'],
             'lake_name2': ["", '_lake'],
             'lake_name3': ['', '_lake']}
    rivers = {'river_name1': ["dicsr", '_river'],
              'river_name2': ["discr", '_river'],
              'river_name3': ["discr", '_river']}

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
    friendlyToForeigners = 1

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
                  citizenshipGlobalRank, friendlyToForeigners,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,
                  # education
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers
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
    cities = {'Budapest': [True, True, None], 'Debrecen': [True, True, None], 'Szeged': [True, True, None],
              'Miskolc': [True, True, None], 'Pecs': [True, True, None]}

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
                 'University of Debrecen': ['Faculty of Dentistry', 'Faculty of Business',
                                            'Faculty of Engineering', 'Faculty of Law', 'Faculty of Informatics',
                                            'Faculty of Medicine', 'Faculty of Music'],
                 'Debrecen University of Reformed Theology': ['Faculty of Reformed Theology', 'Faculty of Medicine',
                                                              'Faculty of Health', 'Faculty of Dentistry'],
                 'University of Szeged': ['Faculty of Agriculture', 'Faculty of Social Sciences',
                                          'Faculty of Dentistry', 'Faculty of Business', 'Faculty of Engineering'],
                 'University of Miskolc': ['Faculty of Engineering', 'Faculty of Informatics',
                                           'Faculty of Mechanical Engineering', 'Faculty of Business',
                                           'Faculty of Arts', 'Faculty of Law'],
                 'University of Pecs': ['Faculty of Business',
                                        'Faculty of Education', 'Faculty of Engineering',
                                        'Faculty of Computer Engineering and Software', 'Faculty of Law']}

    programs = {'Eötvös Loránd University': ['Magistracy', 'Undergraduate', 'MBA'],
                'Semmelweis University': ['Magistracy', 'Undergraduate', 'MBA'],
                'University of Debrecen': ['Magistracy', 'Undergraduate'],
                'Debrecen University of Reformed Theology': ['Foundation', 'Undergraduate'],
                'University of Szeged': ['Magistracy', 'Undergraduate'],
                'University of Miskolc': ['Magistracy', 'Undergraduate', 'MBA'],
                'University of Pecs': ['Magistracy', 'Undergraduate']}
    links = {'Eötvös Loránd University': 'https://www.elte.hu/en/',
             'Semmelweis University': 'https://semmelweis.hu/english/',
             'University of Debrecen': 'https://www.edu.unideb.hu/',
             'Debrecen University of Reformed Theology': 'https://drhe.hu/',
             'University of Szeged': 'https://u-szeged.hu/',
             'University of Miskolc': 'https://www.uni-miskolc.hu/',
             'University of Pecs': 'https://ajk.pte.hu/hu'}

    images = {'Eötvös Loránd University': 'eotvos_lorand_university',
              'Semmelweis University': 'semmelweis_university',
              'University of Debrecen': 'university_of_debrecen',
              'Debrecen University of Reformed Theology': 'debrecen_university_of_reformed_theology',
              'University of Szeged': 'university_of_szeged',
              'University of Miskolc': 'university_of_miskolc',
              'University of Pecs': 'university_of_pecs'}
    # общага
    hostel = {'Eötvös Loránd University': 'No',
              'Semmelweis University': 'Yes',
              'University of Debrecen': 'Yes',
              'Debrecen University of Reformed Theology': 'Yes',
              'University of Szeged': 'Yes',
              'University of Miskolc': 'Yes',
              'University of Pecs': 'No'}
    # стипендия
    scolarship = {'Eötvös Loránd University': 'Yes',
                  'Semmelweis University': 'Yes',
                  'University of Debrecen': 'Yes',
                  'Debrecen University of Reformed Theology': 'Yes',
                  'University of Szeged': 'Yes',
                  'University of Miskolc': 'Yes',
                  'University of Pecs': 'Yes'
                  }
    # требования к поступлению
    requirements = {'Eötvös Loránd University': 'discrpt',
                    'Semmelweis University': 'discrpt',
                    'University of Debrecen': 'discrpt',
                    'Debrecen University of Reformed Theology': 'discrpt',
                    'University of Szeged': 'discrpt',
                    'University of Miskolc': 'discrpt',
                    'University of Pecs': 'discrpt'}

    costs = {'Eötvös Loránd University': 4800,
             'Semmelweis University': 13000,
             'University of Debrecen': 6500,
             'Debrecen University of Reformed Theology': 5000,
             'University of Szeged': 3000,
             'University of Miskolc': 1000,
             'University of Pecs': 1650}

    sights = {'sight_name1': ["", '_sight'],
              'sight_name2': ["", '_sight'],
              'sight_name3': ["", '_sight']}
    beaches = {'beach_name1': ["", '_beach'],
               "beach_name2": ["", '_beach'],
               'beach_name3': ["", '_beach']}
    mountains = {'mountain_name1': ["", '_mountain'],
                 'mountain_name2': ["", '_mountain'],
                 'mountain_name3': ['', '_mountain'],
                 'mountain_name4': ['', '_mountain']}
    skiResorts = {'ski_resort_name1': ["", '_resort'],
                  'ski_resort_name2': ["", '_resort'],
                  'ski_resort_name3': ["", '_resort']}
    lakes = {'lake_name1': ["", '_lake'],
             'lake_name2': ["", '_lake'],
             'lake_name3': ["", '_lake']}
    rivers = {'river_name1': ["dicsr", '_river'],
              'river_name2': ["discr", '_river'],
              'river_name3': ["discr", '_river']}

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
    friendlyToForeigners = 0

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
                  citizenshipGlobalRank, friendlyToForeigners,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,
                  # education
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers
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
    cities = {'London': [True, True, None], 'Edinburgh': [True, True, "Northern ocean"], 'Birmingham': [True, True, None],
              'Manchester': [True, True, None], 'Belfast': [True, True, "Irish sea"]}

    # education
    universities = {'London': ['University College London', 'Imperial College London'],
                    'Edinburgh': ['University of Edinburgh', 'Heriot-Watt University'],
                    'Birmingham': ['University of Birmingham', 'Aston University'],
                    'Manchester': ['University of Manchester', 'University of Salford'],
                    'Belfast': ["Queen's University Belfast"]}
    faculties = {'University College London': ['Faculty of Arts', 'Faculty of Engineering', 'Faculty of Law',
                                               'Faculty of Medicine', 'Faculty of Architecture',
                                               'Faculty of Mathematics',
                                               'Faculty of Physics'],
                 'Imperial College London': ['Faculty of Engineering', 'Faculty of Medicine', 'Faculty of Mathematics',
                                             'Faculty of Chemistry', 'Faculty of Physics'],
                 'University of Edinburgh': ['Faculty of Law', 'Faculty of Arts', 'Faculty of Medicine',
                                             'Faculty of Veterinary Medicine', 'Faculty of Education',
                                             'Faculty of Science'],
                 'Heriot-Watt University': ['Faculty of Engineering', 'Faculty of Social Sciences', 'Faculty of Arts',
                                            'Faculty of Business', 'Faculty of Computer Engineering and Software'],
                 'University of Birmingham': ['Faculty of Arts', 'Faculty of Media',
                                              'Faculty of Business', 'Faculty of Law', 'Faculty of Social Sciences',
                                              'Faculty of Education', 'Faculty of Computer Engineering and Software',
                                              'Faculty of Engineering'],
                 'Aston University': ['Faculty of Business', 'Faculty of Social Sciences', 'Faculty of Engineering',
                                      'Faculty of Physics', 'Faculty of Life Science'],
                 'University of Manchester': ['Faculty of Biology', 'Faculty of Medicine', 'Faculty of Health',
                                              'Faculty of Science', 'Faculty of Engineering', 'Faculty of Humanities'],
                 'University of Salford': ['Faculty of Science', 'Faculty of Engineering', 'Faculty of Arts',
                                           'Faculty of Health', 'Faculty of Business'],
                 "Queen's University Belfast": ['Faculty of Arts', 'Faculty of Humanities', 'Faculty of Social Science',
                                                'Faculty of Engineering', 'Faculty of Physics', 'Faculty of Medicine']}

    programs = {'University College London': ['Magistracy', 'Undergraduate'],
                'Imperial College London': ['Magistracy', 'Undergraduate'],
                'University of Edinburgh': ['Magistracy', 'Undergraduate'],
                'Heriot-Watt University': ['Foundation', 'Undergraduate', 'MBA'],
                'University of Birmingham': ['Magistracy', 'Undergraduate'],
                'Aston University': ['Magistracy', 'Undergraduate'],
                'University of Manchester': ['Magistracy', 'Undergraduate'],
                'University of Salford': ['Magistracy', 'Undergraduate'],
                "Queen's University Belfast": ['Magistracy', 'Undergraduate', 'MBA']}
    links = {'University College London': 'https://www.ucl.ac.uk/',
             'Imperial College London': 'https://www.imperial.ac.uk/',
             'University of Edinburgh': 'https://www.ed.ac.uk/',
             'Heriot-Watt University': 'https://www.hw.ac.uk/',
             'University of Birmingham': 'https://www.birmingham.ac.uk/index.aspx',
             'Aston University': 'https://www.aston.ac.uk/',
             'University of Manchester': 'https://www.manchester.ac.uk/',
             'University of Salford': 'https://www.salford.ac.uk/international',
             "Queen's University Belfast": 'https://www.qub.ac.uk/'}

    images = {'University College London': 'university_college_london',
              'Imperial College London': 'imperial_college_london',
              'University of Edinburgh': 'university_of_edinburgh',
              'Heriot-Watt University': 'heriot_watt_university',
              'University of Birmingham': 'university_of_birmingham',
              'Aston University': 'aston_university',
              'University of Manchester': 'university_of_manchester',
              'University of Salford': 'university_of_salford',
              "Queen's University Belfast": 'queens_university_belfast'}
    # общага
    hostel = {'University College London': 'Yes',
              'Imperial College London': 'Yes',
              'University of Edinburgh': 'Yes',
              'Heriot-Watt University': 'Yes',
              'University of Birmingham': 'Yes',
              'Aston University': 'No',
              'University of Manchester': 'No',
              'University of Salford': 'No',
              "Queen's University Belfast": 'Yes'}
    # стипендия
    scolarship = {'University College London': 'Yes',
                  'Imperial College London': 'Yes',
                  'University of Edinburgh': 'Yes',
                  'Heriot-Watt University': 'Yes',
                  'University of Birmingham': 'Yes',
                  'Aston University': 'Yes',
                  'University of Manchester': 'Yes',
                  'University of Salford': 'Yes',
                  "Queen's University Belfast": 'Yes'
                  }
    # требования к поступлению
    requirements = {
        'University College London': 'High School Diploma + Recognition of 1 year university rejection recognized by UCL with a GPA of at least 4.5/5.0. If there is a discrepancy, the samples are taken for the preparatory year. '
                                     'The level of English proficiency depends on the program. ',
        'Imperial College London': 'Education at the university in English; all students for whom it is not native must confirm a good level of English',
        'University of Edinburgh': 'Applicants must have an excellent level of English, having passed the TOEFL iBT exam with at least 90 points or IELTS at least 6.5',
        'Heriot-Watt University': 'certificate of successful completion of the Foundation (Heriot-Watt University Degree Entry Program) with grades not lower than “B”; IELTS 6.0, not less than 5.5 for each part.',
        'University of Birmingham': '12 years of education or Foundation Certificate. '
                                    'Certificate of complete secondary education '
                                    'IELTS (Academic): minimum 6.0 (not lower than 5.5 in each part) '
                                    'Motivation letter',
        'Aston University': 'Education at the university in English; all students for whom it is not native must confirm a good level of English',
        'University of Manchester': 'high school diploma with a high GPA. '
                                    'score sheet. '
                                    'IELTS - 5.5-6.0',
        'University of Salford': 'certificate of successful completion of the Foundation (Heriot-Watt University Degree Entry Program) with grades not lower than “B”; IELTS 6.0, not less than 5.5 for each part.',
        "Queen's University Belfast": 'high school diploma with a high GPA. '
                                      'score sheet. '
                                      'IELTS - 5.5-6.0'}

    costs = {'University College London': 11000,
             'Imperial College London': 10000,
             'University of Edinburgh': 9000,
             'Heriot-Watt University': 9500,
             'University of Birmingham': 9600,
             'Aston University': 8900,
             'University of Manchester': 9700,
             'University of Salford': 9500,
             "Queen's University Belfast": 9400}

    sights = {'sight_name1': ["", '_sight'],
              'sight_name2': ["", '_sight'],
              'sight_name3': ["", '_sight']}
    beaches = {'beach_name1': ["", '_beach'],
               "beach_name2": ["", '_beach'],
               'beach_name3': ["", '_beach']}
    mountains = {'mountain_name1': ["", '_mountain'],
                 'mountain_name2': ["", '_mountain'],
                 'mountain_name3': ['', '_mountain'],
                 'mountain_name4': ['', '_mountain']}
    skiResorts = {'ski_resort_name1': ["", '_resort'],
                  'ski_resort_name2': ["", '_resort'],
                  'ski_resort_name3': ["", '_resort']}
    lakes = {'lake_name1': ["", '_lake'],
             'lake_name2': ["", '_lake'],
             'lake_name3': ['', '_lake']}
    rivers = {'river_name1': ["dicsr", '_river'],
              'river_name2': ["discr", '_river'],
              'river_name3': ["discr", '_river']}

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
    averageNumberOfFoggyDaysPerYear = 56  # days
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
    friendlyToForeigners = 1

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
                  citizenshipGlobalRank, friendlyToForeigners,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,
                  # education
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers
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
    cities = {'Helsinki': [True, True, "The Gulf of Finland"], 'Turku': [True, True, "Baltic Sea"], 'Tampere': [True, True, None],
              'Oulu': [True, True, "Baltic Gulf"], 'Rovaniemi': [True, True, None]}

    # education
    universities = {'Helsinki': ['University of Helsinki', 'Hanken School of Economics'],
                    'Turku': ['University of Turku', 'Abo Akademi University'],
                    'Tampere': ['University of Tampere'],
                    'Oulu': ['University of Oulu', 'Oulu University of Applied Sciences'],
                    'Rovaniemi': ['University of Lapland', 'Lapland University of Applied Sciences']}
    faculties = {'University of Helsinki': ['Faculty of Agriculture', 'Faculty of Arts', 'Faculty of Biology',
                                            'Faculty of Education', 'Faculty of Law', 'Faculty of Medicine',
                                            'Faculty of Science', 'Faculty of Theology',
                                            'Faculty of Veterinary Medicine'],
                 'Hanken School of Economics': ['Faculty of Business'],
                 'University of Turku': ['Faculty of Education', 'Faculty of Humanities', 'Faculty of Law',
                                         'Faculty of Medicine', 'Faculty of Science', 'Faculty of Technology'],
                 'Abo Akademi University': ['Faculty of Arts', 'Faculty of Psychology', 'Faculty of Theology',
                                            'Faculty of Education', 'Faculty of Science', 'Faculty of Engineering',
                                            'Faculty of Social Sciences', 'Faculty of Business'],
                 'University of Tampere': ['Faculty of Architecture', 'Faculty of Education', 'Faculty of Engineering',
                                           'Faculty of Science', 'Faculty of Computer Engineering and Software',
                                           'Faculty of Business', 'Faculty of Medicine'],
                 'University of Oulu': ['Faculty of Biochemistry', ' Faculty of Medicine', ' Faculty of Science',
                                        'Faculty of Humanities', 'Faculty of Electrical Engineering'],
                 'Oulu University of Applied Sciences': ['Faculty of Biochemistry', 'Faculty of Education',
                                                         'Faculty of Medicine',
                                                         'Faculty of Science', 'Faculty of Technology',
                                                         'Faculty of Business'],
                 'University of Lapland': ['Faculty of Arts', 'Faculty of Education',
                                           'Faculty of Law', 'Faculty of Social Sciences'],
                 'Lapland University of Applied Sciences': ['Faculty of Social Sciences', 'Faculty of Technology',
                                                            'Faculty of Engineering',
                                                            'Faculty of Computer Engineering and Software']}

    programs = {'University of Helsinki': ['Magistracy', 'Undergraduate'],
                'Hanken School of Economics': ['Magistracy', 'Undergraduate'],
                'University of Turku': ['Magistracy', 'Undergraduate'],
                'Abo Akademi University': ['Foundation', 'Undergraduate', 'MBA'],
                'University of Tampere': ['Magistracy', 'Undergraduate'],
                'University of Oulu': ['Magistracy', 'Undergraduate'],
                'Oulu University of Applied Sciences': ['Magistracy', 'Undergraduate'],
                'University of Lapland': ['Magistracy', 'Undergraduate'],
                'Lapland University of Applied Sciences': ['Magistracy', 'Undergraduate', 'MBA']}
    links = {'University of Helsinki': 'https://www.helsinki.fi/en',
             'Hanken School of Economics': 'https://www.hanken.fi/en',
             'University of Turku': 'https://www.utu.fi/en',
             'Abo Akademi University': 'https://www.abo.fi/en/',
             'University of Tampere': 'https://www.tuni.fi/en',
             'University of Oulu': 'https://www.oulu.fi',
             'Oulu University of Applied Sciences': 'https://www.oamk.fi',
             'University of Lapland': 'https://www.ulapland.fi',
             'Lapland University of Applied Sciences': 'https://www.lapinamk.fi'}

    images = {'University of Helsinki': 'university_of_helsinki',
              'Hanken School of Economics': 'hanken_school_of_economics',
              'University of Turku': 'university_of_turku',
              'Abo Akademi University': 'abo_akademi_university',
              'University of Tampere': 'university_of_tampere',
              'University of Oulu': 'university_of_oulu',
              'Oulu University of Applied Sciences': 'oulu_university_of_applied_sciences',
              'University of Lapland': 'university_of_lapland',
              'Lapland University of Applied Sciences': 'lapland_university_of_applied_sciences'}
    # общага
    hostel = {'University of Helsinki': 'Yes',
              'Hanken School of Economics': 'Yes',
              'University of Turku': 'Yes',
              'Abo Akademi University': 'Yes',
              'University of Tampere': 'Yes',
              'University of Oulu': 'No',
              'Oulu University of Applied Sciences': 'No',
              'University of Lapland': 'No',
              'Lapland University of Applied Sciences': 'Yes'}
    # стипендия
    scolarship = {'University of Helsinki': 'Yes',
                  'Hanken School of Economics': 'Yes',
                  'University of Turku': 'Yes',
                  'Abo Akademi University': 'Yes',
                  'University of Tampere': 'Yes',
                  'University of Oulu': 'Yes',
                  'Oulu University of Applied Sciences': 'Yes',
                  'University of Lapland': 'Yes',
                  'Lapland University of Applied Sciences': 'Yes'
                  }
    # требования к поступлению
    requirements = {
        'University of Helsinki': 'To enter the University of Helsinki, you must submit a document confirming your education (diploma or certificate). '
                                  'Along with the application for admission, it is necessary to send a motivation letter, resume and letters of recommendation from the previous place of study.',
        'Hanken School of Economics': 'the applicant must provide information about previous academic performance and passed exams',
        'University of Turku': 'For admission to the bachelors degree, you must provide a school leaving certificate and pass an exam in Finnish',
        'Abo Akademi University': 'the applicant must provide information about previous academic performance and passed exams',
        'University of Tampere': 'the applicant must provide information about previous academic performance and passed exams',
        'University of Oulu': 'To enter the University of Oulu, a Russian applicant must provide the original diploma and transcript or school certificate.',
        'Oulu University of Applied Sciences': 'Fill out an online application. Provide educational documents. Pass the entrance exams. Write a resume and a motivation letter (masters degree).',
        'University of Lapland': 'the applicant must provide information about previous academic performance and passed exams',
        'Lapland University of Applied Sciences': 'the applicant must provide information about previous academic performance and passed exams'
    }

    costs = {'University of Helsinki': 1500,
             'Hanken School of Economics': 1100,
             'University of Turku': 1500,
             'Abo Akademi University': 10000,
             'University of Tampere': 3000,
             'University of Oulu': 1100,
             'Oulu University of Applied Sciences': 1000,
             'University of Lapland': 1000,
             'Lapland University of Applied Sciences': 1000
             }

    sights = {'sight_name1': ["", '_sight'],
              'sight_name2': ["", '_sight'],
              'sight_name3': ["", '_sight']}
    beaches = {'beach_name1': ["", '_beach'],
               "beach_name2": ["", '_beach'],
               'beach_name3': ["", '_beach']}
    mountains = {'mountain_name1': ["", '_mountain'],
                 'mountain_name2': ["", '_mountain'],
                 'mountain_name3': ['', '_mountain'],
                 'mountain_name4': ['', '_mountain']}
    skiResorts = {'ski_resort_name1': ["", '_resort'],
                  'ski_resort_name2': ["", '_resort'],
                  'ski_resort_name3': ["", '_resort']}
    lakes = {'lake_name1': ["", '_lake'],
             'lake_name2': ["", '_lake'],
             'lake_name3': ['', '_lake']}
    rivers = {'river_name1': ["dicsr", '_river'],
              'river_name2': ["discr", '_river'],
              'river_name3': ["discr", '_river']}

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
    friendlyToForeigners = 0

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
                  citizenshipGlobalRank, friendlyToForeigners,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,
                  # education
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers
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
    cities = {'Oslo': [True, True, None], 'Drammen': [True, True, None], 'Bergen': [True, True, "Northern ocean"],
              'Trondheim': [True, True, "Trondheimsfjorden"], 'Stavanger': [True, True, "Northern ocean"]}

    # education
    universities = {'Oslo': ['University of Oslo', 'Oslo Metropolitan University'],
                    'Bergen': ['University of Bergen', 'Norwegian School of Economics'],
                    'Trondheim': ['Norwegian University of Science and Technology'],
                    'Stavanger': ['University of Stavanger']}
    faculties = {'University of Oslo': ['Faculty of Health', 'Faculty of Education', 'Faculty of Social Sciences',
                                        'Faculty of Technology', 'Faculty of Arts'],
                 'Oslo Metropolitan University': ['Faculty of Health', 'Faculty of Education',
                                                  'Faculty of Social Sciences',
                                                  'Faculty of Technology', 'Faculty of Arts'],
                 'University of Bergen': ['Faculty of Arts',
                                          'Faculty of Humanities', 'Faculty of Law', 'Faculty of Natural Sciences',
                                          'Faculty of Medicine', 'Faculty of Social Sciences'],
                 'Norwegian School of Economics': ['Faculty of Business',
                                                   'Faculty of Social Science'],
                 'Norwegian University of Science and Technology': ['Faculty of Architecture', 'Faculty of Arts',
                                                                    'Faculty of Humanities',
                                                                    'Faculty of Computer Engineering and Software',
                                                                    'Faculty of Engineering',
                                                                    'Faculty of Medicine'],
                 'University of Stavanger': ['Faculty of Arts', 'Faculty of Education', 'Faculty of Science',
                                             'Faculty of Technology', 'Faculty of Health']}

    programs = {'University of Oslo': ['Magistracy', 'Undergraduate', 'MBA'],
                'Oslo Metropolitan University': ['Magistracy', 'Undergraduate'],
                'University of Bergen': ['Foundation', 'Undergraduate', 'MBA'],
                'Norwegian School of Economics': ['Magistracy', 'Undergraduate'],
                'Norwegian University of Science and Technology': ['Magistracy', 'Undergraduate'],
                'University of Stavanger': ['Magistracy', 'Undergraduate']}
    links = {'University of Oslo': 'https://www.uio.no/english/',
             'Oslo Metropolitan University': 'https://www.oslomet.no/en/',
             'University of Bergen': 'https://www.uib.no/en',
             'Norwegian School of Economics': 'https://www.nhh.no/en/',
             'Norwegian University of Science and Technology': 'https://www.ntnu.edu/',
             'University of Stavanger': 'https://www.uis.no/en'}

    images = {'University of Oslo': 'university_of_oslo',
              'Oslo Metropolitan University': 'oslo_metropolitan_university',
              'University of Bergen': 'university_of_bergen',
              'Norwegian School of Economics': 'norwegian_school_of_economics',
              'Norwegian University of Science and Technology': 'norwegian_university_of_science_and_technology',
              'University of Stavanger': 'university_of_stavanger'}
    # общага
    hostel = {'University of Oslo': 'Yes',
              'Oslo Metropolitan University': 'Yes',
              'University of Bergen': 'Yes',
              'Norwegian School of Economics': 'No',
              'Norwegian University of Science and Technology': 'Yes',
              'University of Stavanger': 'No'}
    # стипендия
    scolarship = {'University of Oslo': 'Yes',
                  'Oslo Metropolitan University': 'Yes',
                  'University of Bergen': 'Yes',
                  'Norwegian School of Economics': 'No',
                  'Norwegian University of Science and Technology': 'Yes',
                  'University of Stavanger': 'Yes'
                  }
    # требования к поступлению
    requirements = {'University of Oslo': 'exams in Norwegian. the minimum results should be as follows: '
                                          'PTE Academic - 62;'
                                          'TOEFL - 90;'
                                          'IELTS - 6.5.',
                    'Oslo Metropolitan University': 'Confirm knowledge of Norwegian, you need to pass all parts of the Bergentest at the B2 + level or the language test at the university at the C + mark',
                    'University of Bergen': 'a high level of previous academic achievement and a language proficiency certificate are required',
                    'Norwegian School of Economics': 'The admission committee makes admission to the university based on the applicants performance and the results of the exams passed',
                    'Norwegian University of Science and Technology': 'provide a certificate or diploma of previously received education. Documents must be officially translated into English, Norwegian or another Scandinavian language.',
                    'University of Stavanger': 'higher specialized education, resume, letter of intent, TOEFL 80, IELTS 6.0.'
                    }

    costs = {'University of Oslo': 73,
             'Oslo Metropolitan University': 9000,
             'University of Bergen': 700,
             'Norwegian School of Economics': 800,
             'Norwegian University of Science and Technology': 500,
             'University of Stavanger': 100}

    sights = {'sight_name1': ["", '_sight'],
              'sight_name2': ["", '_sight'],
              'sight_name3': ["", '_sight']}
    beaches = {'beach_name1': ["", '_beach'],
               "beach_name2": ["", '_beach'],
               'beach_name3': ["", '_beach']}
    mountains = {'mountain_name1': ["", '_mountain'],
                 'mountain_name2': ["", '_mountain'],
                 'mountain_name3': ['', '_mountain'],
                 'mountain_name4': ['', '_mountain']}
    skiResorts = {'ski_resort_name1': ["", '_resort'],
                  'ski_resort_name2': ["", '_resort'],
                  'ski_resort_name3': ["", '_resort']}
    lakes = {'lake_name1': ["", '_lake'],
             'lake_name2': ["", '_lake'],
             'lake_name3': ['', '_lake']}
    rivers = {'river_name1': ["dicsr", '_river'],
              'river_name2': ["discr", '_river'],
              'river_name3': ["discr", '_river']}

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
    friendlyToForeigners = 0

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
                  citizenshipGlobalRank, friendlyToForeigners,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,
                  # education
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers
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
    cities = {'Stockholm': [True, True, "Baltic Sea"], 'Orebro': [True, True, None], 'Linkoping': [True, True, None],
              'Jonkoping': [True, True, "Vättern"], 'Goteborg': [True, True, "Kattegat"]}

    # education
    universities = {'Stockholm': ['Karolinska Institute', 'Stockholm University'],
                    'Orebro': ['Orebro University'],
                    'Linkoping': ['Linkoping University'],
                    'Jonkoping': ['Jonkoping University'],
                    'Goteborg': ['University of Gothenburg', 'Chalmers University of Technology']}
    faculties = {'Karolinska Institute': ['Faculty of Dentistry', 'Faculty of Medicine', 'Faculty of Anatomy',
                                          'Faculty of Biology', 'Faculty of Psychology'],
                 'Stockholm University': ['Faculty of Humanities', 'Faculty of Law', 'Faculty of Social Sciences',
                                          'Faculty of Science'],
                 'Orebro University': ['Faculty of Business', 'Faculty of Science', 'Faculty of Engineering',
                                       'Faculty of Humanities', 'Faculty of Social Sciences', 'Faculty of Medicine',
                                       'Faculty of Health'],
                 'Linkoping University': ['Faculty of Arts', 'Faculty of Science', 'Faculty of Education',
                                          'Faculty of Medicine', 'Faculty of Health', 'Faculty of Science',
                                          'Faculty of Engineering'],
                 'Jonkoping University': ['Faculty of Computer Engineering and Software', 'Faculty of Engineering',
                                          'Faculty of Mathematics',
                                          'Faculty of Physics', 'Faculty of Chemistry'],
                 'University of Gothenburg': ['Faculty of Computer Engineering and Software', 'Faculty of Humanities',
                                              'Faculty of Education',
                                              'Faculty of Arts', 'Faculty of Science', 'Faculty of Social Sciences'],
                 'Chalmers University of Technology': ['Faculty of Architecture',
                                                       'Faculty of Computer Engineering and Software',
                                                       'Faculty of Social Sciences',
                                                       'Faculty of Engineering']}
    programs = {'Karolinska Institute': ['Magistracy', 'Undergraduate'],
                'Stockholm University': ['Magistracy', 'Undergraduate', 'MBA'],
                'Orebro University': ['Magistracy', 'Undergraduate'],
                'Linkoping University': ['Foundation', 'Undergraduate', 'MBA'],
                'Jonkoping University': ['Magistracy', 'Undergraduate'],
                'University of Gothenburg': ['Magistracy', 'Undergraduate', 'MBA'],
                'Chalmers University of Technology': ['Magistracy', 'Undergraduate']}
    links = {'Karolinska Institute': 'https://ki.se/en',
             'Stockholm University': 'https://www.su.se/cmlink/stockholm-university',
             'Orebro University': 'https://www.oru.se/english/',
             'Linkoping University': 'https://liu.se/en',
             'Jonkoping University': 'https://ju.se/en',
             'University of Gothenburg': 'https://www.gu.se/en',
             'Chalmers University of Technology': 'https://www.chalmers.se/en/Pages/default.aspx'}

    images = {'Karolinska Institute': 'karolinska_institute',
              'Stockholm University': 'stockholm_university',
              'Orebro University': 'orebro_university',
              'Linkoping University': 'linkoping_university',
              'Jonkoping University': 'jonkoping_university',
              'University of Gothenburg': 'university_of_gothenburg',
              'Chalmers University of Technology': 'chalmers_university_of_technology'}
    # общага
    hostel = {'Karolinska Institute': 'Yes',
              'Stockholm University': 'Yes',
              'Orebro University': 'Yes',
              'Linkoping University': 'Yes',
              'Jonkoping University': 'Yes',
              'University of Gothenburg': 'No',
              'Chalmers University of Technology': 'No'}
    # стипендия
    scolarship = {'Karolinska Institute': 'Yes',
                  'Stockholm University': 'Yes',
                  'Orebro University': 'Yes',
                  'Linkoping University': 'Yes',
                  'Jonkoping University': 'Yes',
                  'University of Gothenburg': 'Yes',
                  'Chalmers University of Technology': 'Yes'
                  }
    # требования к поступлению
    requirements = {'Karolinska Institute': 'English proficiency at least 7.0 on the IELTS scale and an average score close to the maximum',
                    'Stockholm University': 'English proficiency at least 7.0 on the IELTS scale and an average score close to the maximum',
                    'Orebro University': 'It is noteworthy that the main factor in terms of recruiting students for a special admissions committee is considered to be the academic performance of each applicant.',
                    'Linkoping University': 'Certificate of general secondary education with grades and a certified translation Confirmation of the study of mathematics Motivation letter IELTS or TOEFL certificate (IELTS not lower than 6.5).',
                    'Jonkoping University': 'Certificate of general secondary education with grades and a certified translation Confirmation of the study of mathematics Motivation letter IELTS or TOEFL certificate (IELTS not lower than 6.5).',
                    'University of Gothenburg': 'application for participation in the scholarship program; copy of the passport; summary; motivation letter (no more than 500 words); the title page of an application for one of the masters programs that was submitted on the site.',
                    'Chalmers University of Technology': 'High School Diploma Swedish as a Second Language 3 Certificate English 6 Certificate.'}

    costs = {'Karolinska Institute': 1000,
             'Stockholm University': 1000,
             'Orebro University': 1000,
             'Linkoping University': 1000,
             'Jonkoping University': 1000,
             'University of Gothenburg': 1000,
             'Chalmers University of Technology': 1000}

    sights = {'sight_name1': ["", '_sight'],
              'sight_name2': ["", '_sight'],
              'sight_name3': ["", '_sight']}
    beaches = {'beach_name1': ["", '_beach'],
               "beach_name2": ["", '_beach'],
               'beach_name3': ["", '_beach']}
    mountains = {'mountain_name1': ["", '_mountain'],
                 'mountain_name2': ["", '_mountain'],
                 'mountain_name3': ['', '_mountain'],
                 'mountain_name4': ['', '_mountain']}
    skiResorts = {'ski_resort_name1': ["", '_resort'],
                  'ski_resort_name2': ["", '_resort'],
                  'ski_resort_name3': ["", '_resort']}
    lakes = {'lake_name1': ["", '_lake'],
             'lake_name2': ["", '_lake'],
             'lake_name3': ['', '_lake']}
    rivers = {'river_name1': ["dicsr", '_river'],
              'river_name2': ["discr", '_river'],
              'river_name3': ["discr", '_river']}
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
    friendlyToForeigners = 1

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
                  citizenshipGlobalRank, friendlyToForeigners,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,
                  # education
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers
                  )
    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()

    #############################   SWEDEN   #############################

    cc.createBorders()
    cc.close()
