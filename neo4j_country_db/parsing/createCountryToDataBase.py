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

    def createBase(self, countryName, citiesDict, officialLanguage,
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
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers, friendlyToForeigners
                   ):
        with self.driver.session() as session:
            base = session.execute_write(self._createBase, countryName, citiesDict, officialLanguage,
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
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers, friendlyToForeigners
                                         )
            return base

    @staticmethod
    def _createBase(tx, countryName, citiesDict, officialLanguage,
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
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers, friendlyToForeigners
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
                resultStr += '\nmerge (water%d:Water {name:"%s"})' % (index, str(citiesDict[city][2]))
                resultStr += '\nmerge (water%d)-[:washes]->(city%d)' % (index, index)
                resultStr += '\nmerge (water%d)-[:washes]->(country)' % (index)
            index += 1
        # education
        resultStr += '\ncreate (education:Education {rankingOfNationalEducationSystem:%d})' % rankingOfNationalEducationSystem
        resultStr += '\ncreate (country)-[:education]->(education)\n'

        index = 1
        if sights:
            for sight in sights.keys():
                resultStr += '\ncreate (sight%d:Sight {name:"%s", description:"%s", image:"%s"})' % (
                    index, sight, sights[sight][0], sights[sight][1])
                resultStr += '\ncreate (country)-[:sight]->(sight%d)' % (index)
                index += 1

        index = 1
        if beaches:
            for beach in beaches.keys():
                resultStr += '\ncreate (beach%d:Beach {name:"%s", description:"%s", image:"%s"})' % (
                index, beach, beaches[beach][0], beaches[beach][1])
                resultStr += '\ncreate (country)-[:beach]->(beach%d)' % (index)
                index += 1

        index = 1
        if mountains:
            for mountain in mountains.keys():
                resultStr += '\ncreate (mountain%d:Mountain {name:"%s", description:"%s", image:"%s"})' % (
                    index, mountain, mountains[mountain][0], mountains[mountain][1])
                resultStr += '\ncreate (country)-[:mountain]->(mountain%d)' % (index)
                index += 1

        index = 1
        if lakes:
            for lake in lakes.keys():
                resultStr += '\ncreate (lake%d:Lake {name:"%s", description:"%s", image:"%s"})' % (
                    index, lake, lakes[lake][0], lakes[lake][1])
                resultStr += '\ncreate (country)-[:lake]->(lake%d)' % (index)
                index += 1

        index = 1
        if rivers:
            for river in rivers.keys():
                resultStr += '\ncreate (river%d:River {name:"%s", description:"%s", image:"%s"})' % (
                    index, river, rivers[river][0], rivers[river][1])
                resultStr += '\ncreate (country)-[:river]->(river%d)' % (index)
                index += 1

        index = 1
        if skiResorts:
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
        resultStr += '\ncreate (language:Language {name:"%s"})' % (str(officialLanguage))
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
        print('+', countryName)
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
                                                "Reconstruction work was carried out in an organized manner, but they dragged on until 1922.",
                                                'https://cdn.britannica.com/29/179429-050-EDBCAE49/Parliament-Buildings-Ottawa.jpg'],
              'Oratory of St. Joseph': ["Among those sights that you must visit in Canada is the Oratory of St. Joseph. Construction work began in 1904. "
                                        "The initiative of the project belongs to André Bessette. "
                                        "The original version of the oratorio was a small chapel that nestled comfortably on the slopes of Mont Royal next to Notre Dame College. "
                                        "The church quickly became popular, the number of parishioners increased every year. "
                                        "Therefore, already in 1917, a church for 1000 people was built here."
                                        "The church keeps the memory of many miracles performed by Brother Andre Bessette. "
                                        "It is significant that Pope John Paul II recognized the miracles that are attributed to brother Andrew. "
                                        "The recognition took place in 1982, and already in 2010 the canonization of brother Andrei took place. "
                                        "He was canonized by Pope Benedict XVII.", 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/18/2c/de/a9/photo0jpg.jpg?w=1200&h=1200&s=1'],
              'Niagara Falls': ["Niagara Falls is included in the list of natural attractions in Canada. "
                                "In addition, it is considered one of the wonders of the world. "
                                "The waterfall is located on the border of Canada and America. "
                                "With a terrifying roar, tons of water flows powerfully rush every second. "
                                "The waterfall is located in a dense cloud of spray, since the water pressure here is quite strong. "
                                'This is fully true, since a giant water stream falls from a 50-meter height. '
                                'Millions of travelers come here to see this unique natural phenomenon with their own eyes.',
                                'https://cdn.britannica.com/30/94430-050-D0FC51CD/Niagara-Falls.jpg']}
    beaches = {'Wasaga Beach': ["The longest freshwater beach in the world, attracting tourists with its 12 km of sandy coastline. "
                                "The warm, shallow waters of the beach are ideal for swimming, while the soft white sand is ideal for picnicking, "
                                "relaxing and watching the beautiful sunset. This urban beach, which is somewhat reminiscent of the famous beaches in Florida: "
                                "Daytona Beach and Fort Lauderdale.",
                                'https://a.travel-assets.com/findyours-php/viewfinder/images/res70/83000/83440-Wasaga-Beach-Provincial-Park.jpg'],
               "Brady’s Beach": ["Bradis Beach is located in a very secluded area on the Pacific Ocean. The only way to get here is by ferry, plane or timber barge. "
                                 "Yes, the path is not easy, but the rest here is worth such a voyage. Try to be there during the Music by The Sea festival. "
                                 "By August, the water here warms up to temperatures suitable for a refreshing swim. "
                                 "The advantages of this beach are that it is surrounded by the Pacific Rim National Park, the ocean, and the territory of the Indians. "
                                 "Excellent diving. Proximity to Barkley Sound islands inhabited by sea lions and bald eagles.",
                                 "https://i.pinimg.com/originals/7a/a9/8e/7aa98ea42f317f0d87f38eac822fe7ab.jpg"],
               'Ingonish Beach': ["Ingonish Beach is the only beach in the Cape Breton Highlands National Park, with a unique opportunity to swim in both fresh and sea water. "
                                  "This sandy beach is washed away in winter and washed back by waves every spring, and a natural barrier separates the lake from the waters of the Atlantic Ocean. "
                                  "In addition to swimming, here you will be offered to go on a boat trip to go fishing and, of course, watch the whales in their habitat.",
                                  'https://i0.wp.com/anotherwalkinthepark.com/wp-content/uploads/2015/01/briarisland_capebreton_canon-1503.jpg?ssl=1']}
    mountains = {'Robson': ['The highest point of the Rocky Mountains; it is also the highest point of the Canadian Rockies. '
                           'The mountain is located within the Robson Provincial Park in British Columbia.',
                            'https://s9.travelask.ru/system/images/files/001/326/820/wysiwyg_jpg/x1l4g1t1xa911.jpg?1560886998'],
                 'Temple': ['Mountain in Banff National Park in the Canadian Rockies, the 7th highest peak in Alberta. '
                            'The Temple is located in the Bow River Valley between Paradise Creek and Moraine Creek and is the highest point in the Lake Louise region.',
                            'https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Mount_Temple.jpg/640px-Mount_Temple.jpg'],
                 'Snow House': ['A mountain on the continental divide of the Columbia Icefield on the border of Banff and Jasper National Parks. '
                                'Located in the Canadian Rockies on the border of British Columbia and Alberta. The height of the peak is 3456 m.',
                                'https://img2.goodfon.com/wallpaper/nbig/8/55/winter-landscape-snow-zima-3936.jpg'],
                 'Assiniboine': ['Pyramidal mountain located on the American Continental Divide on the border of the Canadian provinces of Alberta and British Columbia. '
                                 'The height is 3618 m above sea level.',
                                 'https://offtracktravel.ca/wp-content/uploads/2020/03/viewpoint-mount-assiniboine-sunburst-bc-1000x750.jpg']}
    skiResorts = {'Whistler Blackcomb': ['At the heart of Whistler and Blackcomb is the charming village of Whistler. '
                                         "You don't even have to ski to enjoy your trip to Whistler, but if you do, you'll find "
                                         'seemingly limitless terrain that can accommodate any level of skier, from first timers to extreme skiers. '
                                         "You'll find beautiful wide-open bowls at Mount Whistler and incredible groomed runs on both mountains. "
                                         "On Blackcomb, the Horstmann Glacier offers year-round skiing.",
                                         'https://skibookings.com/wp-content/uploads/201712_wb_paulmorrison_village_064.jpg'],
                  'Lake Louise': ["Lake Louise, in the heart of the Rocky Mountains and less than an hour from the city of Banff, is one of Canada's most famous resorts. "
                                  "From the slopes, majestic scenery stretches over the Luke Valley and the surrounding mountains and beyond to the palatial Fairmont Chateau Lake Louise. "
                                  "This is a mountain for all skiers, from extreme skiers to families coming here to learn about the sport. "
                                  "In a resort with 4,200 acres of rocky terrain, the resort offers a combination of wide-open bowls, steepness, flumes and plenty of groomed trails."
                                  "The Lake Louise Ski Resort doesn't have an onsite location, but it does have fantastic daytime facilities at the base, as well as restaurants serving delicious food, "
                                  "as well as other restaurants in the mountains. Skiers can take a dip in the nearby village of Lake Louise or the town of Banff.",
                                  'https://skitheworld.com/wp-content/uploads/2018/12/LAke-louise-ski-village.jpg'],
                  'Revelstoke': ["Located in the interior of British Columbia, about 2.5 hours from the city of Kelowna, Revelstoke is a bit harder to get to some resorts, but well worth it. "
                                 "The mountain sees a large number of powder days; few crowds; and offers great terrain, from open bowls to tree trails and starter areas. "
                                 "Add to that the affordable accommodation options in Revelstoke; ski slopes, ski slopes on the mountain; and fabulous mountain scenery and it's hard to beat this resort. "
                                 "This is not the place for a glamorous five-star experience or shopping experience. It is a mountain of skiers and a great place for families.",
                                 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0e/34/81/6a/the-sutton-place-hotel.jpg?w=700&h=-1&s=1']}
    lakes = {'Louise': ["A natural wonder of Banff National Park. Lies surrounded by the Rocky Mountains and the bright greenery of the forest, at an altitude of 1646 meters. "
                        "The unusual emerald color of the water is due to the presence of rock particles brought into the lake by glaciers. The area of the lake is 0.8 km2. "
                        "On the shore there is a 5-star hotel, a number of campsites and tourist centers, nearby is the famous ski resort. "
                        "Hiking and cycling routes are organized around the reservoir. Canoe excursions are available.",
                        'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/01/25/ce/47/moraine-lake.jpg?w=700&h=-1&s=1'],
             'Moraine': ["One of the most beautiful and photographed lakes in the world. Business card of Canada. "
                         "Its stunning landscapes can be found in many magazines and catalogs, on Canadian currency, Windows screensaver, etc. "
                         "It lies in the Valley of the Ten Peaks of the famous Banff Park, at an altitude of 1885 meters. "
                         "Origin - glacial. The area is 0.5 km2. Routes have been laid out for tourists, it is better to move along them with an experienced guide. "
                         "A hotel was built on the shore, there is a boat rental.", 'https://media-cdn.tripadvisor.com/media/photo-s/10/23/d3/72/moraine-lake.jpg'],
             'Superior': ['The largest in terms of area in the composition of the Great Five and among the fresh lakes of the world. '
                          'Located in Canada and the USA. It occupies an area of 82.7 thousand km2. The shores are indented, there are large bays, islands. '
                          'There are many parks on the lake, a marine reserve has been created. The water is cold, even in summer it does not exceed 4 ° C, in winter it does not freeze due to frequent storms. '
                          'The lake is rich in fish. Navigable. The major port is Thunder Bay. The southern part of the reservoir is known as the graveyard of ships.',
                          'https://webmandry.com/wp-content/uploads/2019/07/Samye-bolshie-ozera-kakoe-samoe-bolshoe-ozero-v-mire-2-Verhnee.jpg']}
    rivers = {'Yukon': ["One of the largest rivers of the North American continent originates in Lake Marsh. "
                        "Most of the Yukon is located in the United States, but the source is located in the Canadian province of the same name. "
                        'A tributary of the Yukon, the Klondike, is famous for the gold rush of the 20th century. '
                        'Almost the entire river is located in the subarctic climate zone, but in the Canadian part of the Yukon it is much warmer than in the north.'
                        'The total length of the river is 3190 km.',
                        'https://www.worldatlas.com/r/w768/upload/5f/53/53/shutterstock-7670922581.jpg'],
              'Colombia': ["The source of the river is Lake Columbia in the Rocky Mountains. "
                           "Due to its fast current and large elevation difference, Colombia is actively used to generate electricity. "
                           "In total, there are 14 hydroelectric power stations on it. The river is a spawning ground for many species of salmon. "
                           "Dams and hydroelectric power stations prevent the advancement of both adults and fry, but all power plants have fish passages, "
                           "and fry are in some cases transported to the ocean by the US Army. "
                           "The total length of the river is 2000 km.",
                           'https://www.americanrivers.org/wp-content/uploads/2016/03/Columbia-River-Credit-Alan-Majchrowicz-header.jpg'],
              'Churchill': ["Thanks to an artificial canal built in the 20th century, most of the water from the Churchill River goes to Saskatchewan to increase hydroelectric power generation. "
                            "The river originates in the central part of the province of Saskatchewan and carries its waters east to Hudson Bay. "
                            "The rich flora and fauna of the river basin was the reason for its nomination for inclusion in the List of Protected Rivers of Canada.",
                            'https://media.socastsrm.com/wordpress/wp-content/blogs.dir/900/files/2022/05/churchill-falls-1969-heritage-nl.jpg']}
    universities = {'Ottawa': ['Carleton University', 'University of Ottawa'],
                    'Toronto': ['York University', 'University of Toronto'],
                    'Montreal': ['Montreal University', 'Polytechnique Montreal'],
                    'Quebec': ['Laval University', 'TELUQ University'],
                    'Vancouver': ['University of British Columbia', 'University Canada West']}
    faculties = {'Carleton University': ['Faculty of Arts', 'Faculty of Computer Engineering and Software', 'Faculty of Education',
                                         'Faculty of Law', 'Faculty of Science', 'Faculty of Social Sciences'],
                 'University of Ottawa': ['Faculty of Arts', 'Faculty of Engineering', 'Faculty of Education',
                                          'Faculty of Science', 'Faculty of Medicine', 'Faculty of Law', 'Faculty of Social Sciences'],
                 'York University': ['Faculty of Education', 'Faculty of Arts', 'Faculty of Medicine', 'Faculty of Science'],
                 'University of Toronto': ['Faculty of Arts', 'Faculty of Science', 'Faculty of Medicine'],
                 'Montreal University': ['Faculty of Arts', 'Faculty of Science', 'Faculty of Law', 'Faculty of Medicine',
                                         'Faculty of Education'],
                 'Polytechnique Montreal': ['Faculty of Computer Engineering and Software', 'Faculty of Science', 'Faculty of Medicine'],
                 'Laval University': ['Faculty of Arts', 'Faculty of Law', 'Faculty of Education', 'Faculty of Forestry', 'Faculty of Medicine'],
                 'TELUQ University': ['Faculty of Arts', 'Faculty of Science', 'Faculty of Medicine'],
                 'University of British Columbia': ['Faculty of Business', 'Faculty of Forestry', 'Faculty of Education',
                                                    'Faculty of Science', 'Faculty of Medicine', 'Faculty of Law'],
                 'University Canada West': ['Faculty of Arts', 'Faculty of Computer Engineering and Software', 'Faculty of Education',
                                            'Faculty of Law', 'Faculty of Science', 'Faculty of Social Sciences']}
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
    friendlyToForeigners = 1

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
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers, friendlyToForeigners
                  )
    #############################   CANADA   #############################
    #############################   United Arab Emirates   #############################

    # Country
    countryName = "United Arab Emirates"
    officialLanguage = "Arabic"

    # cities    name   isBig  washesBy
    cities = {'Abu Dhabi': [True, True, 'Persian Gulf'], 'Dubai': [True, True, 'Persian Gulf'],
              'Sharjah': [True, True, 'Persian Gulf'],
              'Al Ain': [True, False, None], 'Ajman': [True, True, 'Persian Gulf'],
              'Fujairah': [False, True, 'Gulf of Oman']}

    # education
    universities = {'Dubai': ['Murdoch University Dubai'],
                    'Abu Dhabi': ['Abu Dhabi University', 'Khalifa University'],
                    'Sharjah': ['American University of Sharjah']}
    faculties = {'Abu Dhabi University': ['Faculty of Arts', 'Faculty of Business', 'Faculty of Engineering',
                                          'Faculty of Medicine', 'Faculty of Law'],
                 'Khalifa University': ['Faculty of Arts', 'Faculty of Engineering', 'Faculty of Medicine'],
                 'Murdoch University Dubai': ['Faculty of Computer Engineering and Software', 'Faculty of Business',
                                              'Faculty of Psychology'],
                 'American University of Sharjah': ['Faculty of Arts', 'Faculty of Computer Engineering and Software',
                                                    'Faculty of Engineering',
                                                    'Faculty of Medicine', 'Faculty of Science']}
    programs = {'Abu Dhabi University': ['Magistracy', 'Undergraduate'],
                'Khalifa University': ['Magistracy', 'Undergraduate'],
                'Murdoch University Dubai': ['Magistracy', 'Undergraduate'],
                'American University of Sharjah': ['Magistracy', 'Undergraduate']}
    links = {'Abu Dhabi University': 'https://www.adu.ac.ae',
             'Khalifa University': 'https://www.ku.ac.ae',
             'Murdoch University Dubai': 'https://www.murdochuniversitydubai.com',
             'American University of Sharjah': 'https://www.aus.edu'}
    images = {'Abu Dhabi University': 'https://assets.wam.ae/uploads/2020/06/2314327737839258810.jpg',
              'Khalifa University': 'https://www.ku.ac.ae/wp-content/uploads/2020/09/Khalifa-University-Campus-at-Night-1.jpg',
              'Murdoch University Dubai': 'https://smapse.ru/storage/2020/03/murdoch-university-dubai-smapse14.jpg',
              'American University of Sharjah': 'https://i.dawn.com/primary/2022/06/62971f912ce9d.png'}
    hostel = {'Abu Dhabi University': 'Yes',
              'Khalifa University': 'Yes',
              'Murdoch University Dubai': 'Yes',
              'American University of Sharjah': 'Yes'}
    scolarship = {'Abu Dhabi University': 'Yes',
                  'Khalifa University': 'Yes',
                  'Murdoch University Dubai': 'Yes',
                  'American University of Sharjah': 'Yes'}
    requirements = {
        'Abu Dhabi University': 'During the application process, the admissions committee will evaluate academic performance from the school or college. '
                                'To be admitted to the University of Abu Dhabi, you must also pass exams for the chosen faculty. '
                                'In the process of learning, students learn the program of one course in two semesters, on the basis of which the academic year is formed.',
        'Khalifa University': 'For admission, it is required to provide the admission committee with a document on basic education, on the basis of the average score of which a decision will be made on further passing the examination. '
                              'Each faculty appoints its own set of examinations. The success of passing these tests serves as a guarantee of enrollment in Khalifa University.',
        'Murdoch University Dubai': 'Certificate of general secondary education. '
                                    'TOEFL certificate confirming the required level of a foreign language (min. 550/CAT 213 or 4.0 TWE or Internet Based 79-80/w24). '
                                    'Two letters of recommendation from high school teachers. '
                                    'In addition, you need to pay: Registration , Margin, Package of visa documents, Medical insurance.',
        'American University of Sharjah': 'An official high school diploma certified by the appropriate authorities: an American high school diploma - a minimum of B or 80% of the final grade (12th grade)'
                                          ' or the average of the best two years in 10th, 11th and 12th grades; British high school diploma - 5 subjects IGCSE / GCSE (level O) and two subjects GCE (level AS / A);'
                                          ' IB diploma in six subjects (excluding Islamic education) - a minimum of 24 points; German Abitur - minimum score of 7 in the last year. '
                                          'Official progress reports for the last three years of high school, certified by the relevant authorities. '
                                          'Color scan of the passport. '
                                          'English proficiency test results: IELTS Academic - 6.5, TOEFL iBT - 80, TOEFL iTP - 550, Cambridge English - 176, EmSAT Achieve-English - 1550.'}
    costs = {'Abu Dhabi University': 11000,
             'Khalifa University': 7000,
             'Murdoch University Dubai': 42200,
             'American University of Sharjah': 22200}
    sights = {'Burj Khalifa': ["What is the first thing that comes to mind when talking about the sights of the UAE? Of course, the grandiose Burj Khalifa. "
                               "According to the project, this building was originally planned to be the tallest in the world, "
                               "its height was kept secret until the end so that it could be adjusted if the building was designed higher. "
                               "The height of this truly huge skyscraper is 828 m (163 floors), which is 196 m higher than the Shanghai Tower, which is 632 m high."
                               "Inside this huge building, in addition to the hotel, there are apartments, a huge number of shopping centers and offices. "
                               "The highest observation deck is located at an altitude of 472 m. The air inside the Dubai Tower, in addition to cooling, is additionally flavored. "
                               "Not far from the skyscraper are the highest singing fountains in the world, which are an unusually beautiful sight.",
                               'https://luxeadventuretraveler.com/wp-content/uploads/2012/12/Luxe-Adventure-Traveler-Dubai-Burj-Khalifa-6.jpg'],
              'Palm Islands': ["The Palm Islands can rightly be considered the eighth wonder of the world. "
                               "Of all that has been built by man, only this artificial archipelago and the Great Wall of China are visible from space. "
                               "This place is a business center, today it is the center of tourism of the entire Persian Gulf."
                               "The archipelago is made up of three attractions of the UAE - islands that look like date palms. "
                               "This plant is especially revered in Islam. "
                               "The largest of the artificial islands is Palm Deira, the Palm Jebel Ali and Jumeirah are slightly more modest in size. "
                               "Following the terminology, it would be more correct to call the Palms peninsulas, since they are connected to the coastline by their trunks. "
                               "The crown of each island is a crescent - a symbol of the Islamic religion. "
                               "The islands are protected from the water by barrier reefs, on which quotes from the poems of Sheikh Dubai are carved.",
                               'https://cdn.hswstatic.com/gif/dubai-palm-island-1.jpg'],
              'Singing Fountains': ["Singing fountains in Dubai are a symbol of wealth and prosperity of the country. "
                                    "The complex is located in the center of the pool area of 12 hectares. "
                                    "The pool is decorated with mosaics and is located next to the Burj Khalifa, the tallest skyscraper. "
                                    "The pond is illuminated by a huge number of spotlights. The height of the jet during the performance reaches 150 meters. "
                                    "Such power is provided by water cannons, which make a sound similar to a shot."
                                    " Guns, pumps and music are controlled by a program that was developed specifically when creating the fountain. "
                                    "Powerful acoustic systems are located around the entire pool. "
                                    "They accompany the water dance with various songs in Arabic and English. "
                                    "In total, about 20 compositions are performed per day without repetitions. "
                                    "Only at the very beginning of the performance a song in honor of the capital sounds.",
                                    'https://www.taritravel.com/upload/medialibrary/21b/21bb5ac705f6abad5813f7991efdb091.jpg']}
    beaches = {'Cornish': ["Corniche Beach is located in the largest emirate and, at the same time, in the city of the same name, which is the capital of the UAE - in Abu Dhabi. "
                           "Corniche Beach is called one of the symbols of Abu Dhabi - the infrastructure is well developed here, the surroundings are clean, there is a constant flow of tourists. "
                           "There are no high waves here due to the nearby islands of Al Lulu and Al Marin. "
                           "The promenade, about 5 km long, has everything you need to enjoy your vacation by the sea: "
                           "here you can rent beach equipment, have fun on the rides, try international cuisine in coastal restaurants and cafes. "
                           "Along the beach there are hotels that meet high standards and skyscrapers, which gives the beach a certain charm. "
                           "There are three zones on the beach. There are paid and free. "
                           "The beach and the sea are the same there, but there is still a difference: "
                           "in paid areas you can rent sun loungers and towels, and there are also more local cafes and restaurants, beautiful small gardens with palm trees and flowers. "
                           "The third zone is a special area for families - Family Beach Section. You have to pay to enter there, but this family corner is worth it.",
                           'https://media.cntraveller.com/photos/611be91fa86777b29fbc4f00/16:9/w_2580,c_limit/beach-at-porthcurno-saint-levan-cornwall-conde-nast-traveller-18aug16-alamy.jpg'],
               "Saadiyat": ["Saadiyat Beach is located on the artificial island of the same name, 5 kilometers from the UAE capital Abu Dhabi. "
                            "The beach area has a length of 9 km. There is white soft sand, nice waves."
                            " The beach has a calm atmosphere and allows you to relax from the bustle of the city. "
                            "The beach itself can be divided into a public beach, party and a beach from hotels. "
                            "We note right away that the hotels on this beach are mostly luxury. "
                            "All areas on Saadiyat Beach are paid: the cheapest vacation is on the public beach, the most expensive is the beach of the Hyatt Hotel. "
                            "Saadiyat has a huge selection of entertainment: water rides, yachts, surfing. "
                            "For those who relax in the club or hotel zone, there is an opportunity to visit swimming pools, spas, fitness centers, elite restaurants and bars.",
                            'https://fs.tonkosti.ru/0g/91/0g91mdjb4lzww8s0gkggwgoo0.jpg'],
               'Jumeirah': ["Jumeirah Beach is the largest and most visited beach in Dubai, which includes several smaller beaches. "
                            "It is named after the area that bears the same name and stretches for 20 km. "
                            "The beaches succeed each other in a chain: first private, then public. "
                            "The prices here are very different: you can relax on the free Jumeirah Open Beach, and on the beach at the Jumeirah Beach Hotel. "
                            "The peculiarity of the beach is the view of the 7-star Burj Arab hotel. "
                            "Everyone who stays at Jumeirah Beach does not miss the opportunity to take a picture against the backdrop of the sail hotel. "
                            "By the way, because of the hotel, excursions from other Dubai beaches are organized to Jumeirah Beach. "
                            "We will tell you about the most popular and best areas of this huge beach.",
                            'https://www.timeoutdubai.com/cloud/timeoutdubai/2022/03/15/Dubais-best-beaches.jpg']}
    mountains = {'Jebel Hafeet': ["The mountain located mainly in the vicinity of Al Ain, which is located in the Emirate of Abu Dhabi in the UAE. "
                                  "Part of the mountain is surrounded by the border with Oman, and the peak is located entirely within the United Arab Emirates.",
                                  'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1b/b4/6a/9e/abu-dhabi-is-one-of-the.jpg?w=1200&h=-1&s=1'],
                 'Jabal Yibir': ["This is one of the best; if not the best mountain drive in UAE. "
                                 "Very steep climb and narrow hairpins. Dangerous but Adventurous. "
                                 "Won’t recommend to drive along with family though. Once you reached top of the mountain you are blessed with astonishing sceneries. "
                                 "Every angle will give you a perfect picture even for amateurs. "
                                 "You can see Dubai skyline along with setting sun and the marvelous Burj Khalifa at one view point.",
                                 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0e/dd/d1/2f/stopover-area.jpg?w=1200&h=-1&s=1'],
                 'Jabal Bil Ays': ['The mountain in the northwestern Hajar Range in the Musandam province of Oman, and also in Ras Al Khaimah, United Arab Emirates. '
                                    'The summit has a height of 1934 m.',
                                   'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/View_from_Jebel_Jais_-_panoramio.jpg/1200px-View_from_Jebel_Jais_-_panoramio.jpg']}
    skiResorts = {'Ski Dubai': ["An amusement park and the first indoor ski resort in the Middle East and one of the largest in the world with an area of about 22.5 thousand m², "
                                "covered with artificial snow all year round. Capacity - 1.5 thousand visitors. Located in the Mall of the Emirates.",
                                'https://static.toiimg.com/photo/40367677.cms']}
    lakes = {}
    rivers = {}
    # currency
    currencyName = 'DH'
    currencyEqualsToDollar = 3.67

    # military
    milPolBlock = "None"
    amountOfPeopleInArmy = 63000

    # healthcare
    numberOfDoctorsPer100kPopulation = 326
    menAverageLifeExpectancy = 78
    womenAverageLifeExpectancy = 80.7

    # climat
    juneAverageTemperature = 31.5
    decemberAverageTemperature = 20.5
    averageHumidity = 55
    averageDurationOfWinter = 0
    averageRainfallPerMonth = 7.4
    averageNumberOfFoggyDaysPerYear = 11
    averageNumberOfRainyDaysPerYear = 13
    averageNumberOfClearDays = 287

    # security
    situationInTheCountry = 3  # [1, 3] 1-bad, 3-good
    freedomOfSpeech = 1  # [1, 3]
    assessmentOfFamilyLife = 2  # [1, 3]
    attitudeTowardsLGBT = 1  # [1, 3]

    # population
    populationCount = 9991000
    procentOfMales = 69.5
    procentOfFemales = 30.5
    populationDensityPerSquareKilometer = 122.1
    speedOfLife = 3  # [1, 3]
    workPlaces = 3  # [1, 3]
    nightLifeEntertainment = 3  # [1, 3]

    # citizenship
    citizenshipGlobalRank = 15
    friendlyToForeigners = 2

    # communication
    communicationOnEnglish = 3  # [1, 3]

    # transport
    averageTravelTimeToWork = 36
    developmentLevelOfPublicTransport = 3  # [1, 3]

    # internet
    speedOfInternetMbps = 10.2  # Мегабиты в секунду
    freeWifi = 3  # [1, 3]

    # education
    rankingOfNationalEducationSystem = 46

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
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers, friendlyToForeigners
                  )

    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()
    #############################   United Arab Emirates   #############################
    #############################   USA   #############################

    # Country
    countryName = "United States of America"
    officialLanguage = "English"

    # cities    name   isBig  washesBy
    cities = {
        'New York': [True, True, 'Atlantic ocean'],
              'Los Angeles': [True, True, 'Pacific ocean'], 'Chicago': [True, True, None], 'Houston': [True, False, 'Gulf of Mexico'],
              'Miami': [False, True, 'Atlantic ocean'], 'Hawaii': [False, True, 'Pacific ocean'], 'Cambridge': [False, False, 'Atlantic ocean'],
              'Palo Alto': [False, False, None]}

    # education
    universities = {'Cambridge': ['Harvard University'],
                    'Palo Alto': ['Stanford University'],
                    'Chicago': ['University of Chicago'],
                    'New York': ['New York University']}
    faculties = {'Harvard University': ['Faculty of Arts', 'Faculty of Science', 'Faculty of Engineering', 'Faculty of Business', 'Faculty of Social Sciences'],
                 'Stanford University': ['Faculty of Business', 'Faculty of Engineering', 'Faculty of Computer Engineering and Software',
                                         'Faculty of Science', 'Faculty of Social Sciences',  'Faculty of Medicine', 'Faculty of Law'],
                 'University of Chicago': ['Faculty of Law', 'Faculty of Social Sciences', 'Faculty of Medicine', 'Faculty of Business'],
                 'New York University': ['Faculty of Arts', 'Faculty of Social Sciences',  'Faculty of Medicine', 'Faculty of Law']}
    programs = {'Stanford University': ['Magistracy', 'Undergraduate'],
                'New York University': ['Magistracy', 'Undergraduate', 'MBA'],
                'Harvard University': ['Magistracy', 'Undergraduate'],
                'University of Chicago': ['Magistracy', 'Undergraduate']}
    links = {'Harvard University': 'https://www.harvard.edu',
             'University of Chicago': 'https://www.uchicago.edu',
             'New York University': 'https://as.nyu.edu',
             'Stanford University': 'https://www.stanford.edu'}
    images = {'University of Chicago': 'https://www.pennclub.org/images/dynamic/getImage.gif?ID=100002765',
              'Harvard University': 'https://www.harvard.edu/wp-content/uploads/2021/02/091520_Stock_KS_025-1200x630.jpeg',
              'New York University': 'https://www.usnews.com/dims4/USNEWS/72c90e6/17177859217/resize/800x540%3E/quality/85/?url=https%3A%2F%2Fmedia.beam.usnews.com%2F9d%2Fd819230374ef6531890bb7eee1dac0%2FNYU_WSP_Header.jpg',
              'Stanford University': 'https://www.studylab.ru/upload/Institutions/image/big/28bdde35702ffcfbdcc4f9138a29be10.jpg'}
    # общага
    hostel = {'University of Chicago': 'Yes',
              'Harvard University': 'Yes',
              'New York University': 'Yes',
              'Stanford University': 'Yes'}
    # стипендия
    scolarship = {'University of Chicago': 'Yes',
                  'Harvard University': 'Yes',
                  'New York University': 'Yes',
                  'Stanford University': 'Yes'}
    # требования к поступлению
    requirements = {'University of Chicago': 'IELTS (7.0) or TOEFL (from 104), Application for admission, '
                                             'Officially certified and translated educational documents, Registration fee, '
                                             'Letters of recommendation from teachers, Financial documents, SAT and ACT exam results.',
                    'Harvard University': 'Passing the SAT or ACT exam. The choice is given to the applicant. '
                                          'The SAT is a standard exam that all applicants to higher education institutions in the United States take. '
                                          'Consists of 3 parts: mathematics, writing, text analysis. To know how to get into Harvard, you need to know how to take the American Admissions Exam.'
                                          'Apply. You can do this online, the cost of the application is $ 75. '
                                          'The certificate of school education needs to be translated. '
                                          'Passing TOEFL with a minimum of 90 points. '
                                          'The presence of 2 recommendations from teachers. Foreign applicants need a translation. '
                                          'The presence of a report from the school. Intermediate and annual required.',
                    'New York University': 'In this educational institution, education is given in 230 areas. '
                                           'This process is carried out on the basis of 14 14 colleges, schools and institutes. '
                                           'An applicant must leave an application for admission to NYU on the commonapp.org website, '
                                           'while making sure to pay a fee of $ 70, which, no matter the result, will not be returned. '
                                           'Foreigners need to add a certificate guaranteeing their ability to pay. '
                                           'If a student needs a scholarship, the relevant document should be submitted to the selection committee.',
                    'Stanford University': "Stanford University was founded by former California Governor Leland Stanford in 1891. "
                                           "More than 17,000 students study at Stanford, most of them undergraduates and graduate students."
                                           "The main campus was designed by architect and designer Frederick Law Olmstead, who also designed Central Park and Prospect Park in New York. "
                                           "Now the campus is one of the largest in the United States - there are even 24 bus routes on its territory."
                                           "Currently, 17 Nobel laureates, 4 Pulitzer Prize winners, 288 members of the American Academy of Arts and Sciences and 109 members of the National Academy of Engineering work and teach at the university. "
                                           "The university invests heavily in the development of research activities, and also motivates students to create start-ups, some of which are funded by the university and its trustees."
                                           "The 31st US President Herbert Hoover, the founders of high-tech companies: Sergey Brin (Google), "
                                           "William Hewlett and David Packard (Hewlett-Packard), Reed Hastings (Netflix), "
                                           "Mike Krieger (Instagram) studied at Stanford University at different times; and actress Sigourney Weaver."}
    costs = {'University of Chicago': 48759,
             'Harvard University': 28000,
             'New York University': 39000,
             'Stanford University': 54315}

    sights = {'The Statue of Liberty': ["For the first time in America, people tend to see all the sights of the United States. "
                                        "One of the most famous symbols of the country in the world - the Statue of Liberty - is located on a small island in the port of New York. "
                                        "The majestic sculpture of a woman with a torch in her hand, stretched into the sky, has become the personification of America's freedom. "
                                        "The crown on her head has seven rays, which means seven continents and seven oceans (according to Western geographical tradition). "
                                        "In her other hand she holds a slab engraved with the date of the Declaration of Independence. "
                                        "The monument was made by French masters by order of the US government and sent to the island in parts. "
                                        "Here, the Americans have already assembled it on a built plinth. "
                                        "The Statue of Liberty is not only a symbol, but also a functioning lighthouse in New York Harbor. "
                                        "The height of the statue from the beginning of the pedestal to the top of the torch is 93 meters. "
                                        "The figure is made of copper plates mounted on a steel frame.",
                                        'https://www.history.com/.image/ar_16:9%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTY1MTc1MTk3ODI0MDAxNjA5/topic-statue-of-liberty-gettyimages-960610006-promo.jpg'],
              'Central park': ["The sights of the United States are of great interest to tourists. New York's Central Park occupies a special place among them. "
                               "It is an oasis of calm in the bustling business flow of Manhattan. The green zone is 4 km long and 800 meters wide. "
                               "The opening of the park took place in 1859. Tens of thousands of workers ennobled the territory for another 20 years. "
                               "About 5 million trees were planted, and the land was brought from ecologically clean areas. "
                               "Now the park has a whole recreation infrastructure. "
                               "These are various playgrounds, attractions, skating rinks and just lawns for a picnic.",
                               'http://askandgo.ru/images/poi/2990.jpg'],
              'White House': ["US attractions are represented by a very extensive list. "
                              "But the most important of them in terms of the history of executive power is, of course, the White House. "
                              "It is a symbol of America's democracy. The residence of the rulers of the country is named after the color of the building itself. "
                              "This is one of the main attractions in the United States, and every year about one and a half million tourists"
                              " flock to the capital to see the grandeur and beauty of the world-famous building. "
                              "The President's House is also a museum of both history and art history. "
                              "The interior of the building contains old canvases, antique furniture and household items. "
                              "Of particular interest among tourists is the gallery of paintings, which depict all the presidents of the country and their wives. "
                              "Tours are free, but you need to sign up six months in advance. "
                              "Despite the accessibility, there are employees of the US Secret Service in the building itself and along its perimeter.",
                              'https://www.rd.com/wp-content/uploads/2017/12/this-is-why-the-white-house-is-white-119809810-Orhan-Cam-ft.jpg'],
              'Hollywood and Avenue of Stars': ["When asked by a tourist what to see in the USA, the answer comes with lightning speed - of course, Hollywood. "
                                                "Everyone wants to visit the Dream Factory and see with their own eyes the places where legends live and are created. "
                                                "Most of the film studios are located on the West Side. "
                                                "In Hollywood, location shooting and film editing are carried out. "
                                                "It also hosts the Oscars, America's highest award in the film industry. Since 2005, "
                                                "Hollywood has been recognized as an independent territorial unit. "
                                                "You can not pass by the famous landmark of the United States - Star Avenue. "
                                                "It is the symbol of California and the most visited place in America. "
                                                "The Alley is located in the courtyard of the Grauman Theater and is a complex of concrete slabs with copper stars. "
                                                "It is on these stars that the names of celebrities are imprinted. There are about 2600 such plates. "
                                                "The first star appeared back in 1958.",
                                                'https://thumbs.dreamstime.com/b/famous-hollywood-boulevard-avenue-stars-los-angelos-california-usa-september-147460759.jpg']}
    beaches = {'Siesta Beach': ["The beach located in the Gulf of Mexico on the coast of Florida. "
                                "Siesta Beach has received numerous awards, including being named America's Best Beach in 2011. "
                                " are lifeguards, showers and toilets, snack bars, souvenir shops, picnic tables, gazebos, sun loungers, equipped playgrounds, "
                                "tennis courts and a large parking lot for cars (it is better to arrive early on weekends so that there are no problems with free places). "
                                "The beach stretches along the coast for several kilometers, so there is always free space on it. "
                                "On the beach there is a shower with fresh water, as well as toilets and changing rooms. "
                                "The width of the beach reaches 100 meters, a smooth entrance to the sea, "
                                "the absence of big waves and a gentle shore make the beach a great place to relax with children.",
                                'https://www.siestakeyluxuryrentalproperties.com/wp-content/uploads/2020/07/shutterstock_319854593.jpg'],
               "Poipu Beach Park": ["Popular with visitors and locals alike, this crescent-shaped beach offers crystal-clear waters and occasional Hawaiian monk seal appearances. "
                                    "(If you do spot a monk seal, please be mindful by staying at least 100 feet away and no flash photography as they are currently on the endangered species list.)"
                                    " With lifeguards, picnic facilities, showers and a natural wading pool for young swimmers, it’s also a great destination for a family beach day. "
                                    "There’s a bodyboarding site directly in front of the park for older children and novice adults, a surfing site for experienced surfers and a good reef for snorkeling. "
                                    "From December through April, you can sometimes spot humpback whales in the distance.",
                                    'https://poipubeach.org/wp-content/uploads/2014/05/poipu-beach-aerial.jpg'],
               'Moonstone Beach': ["Famous for its dramatic coastline and breathtaking views, the Moonstone Beach Boardwalk is where your Cambria seaside escape begins. "
                                   "Whether you want to sink your toes into the sand, catch glimpses of marine life swimming by, explore living tide pools, "
                                   "or head out to sea for surfing, boating, and other aquatic adventures, you will find there is something for everyone to enjoy on Moonstone Beach. "
                                   "Take a relaxing one-mile stroll along the Moonstone Beach Boardwalk. "
                                   "Enjoy playful sea otters, watch whales and dolphins in season, "
                                   "and spy the wildlife on-shore while taking in the stunning ocean views.",
                                   'https://www.hikespeak.com/img/Central-Coast/SLO/Cambria/Moonstone_Beach_Boardwalk_IMG_9185.jpg']}
    mountains = {'Appalachians': ["Mountain system in the east of the country, running through Massachusetts, New York, Ohio, Virginia, "
                                  "Kentucky, Georgia, Alabama and numerous other states. Coal and other minerals are mined here. "
                                  "The average height of the mountains in the system is no more than a kilometer above sea level. "
                                  "The highest eastern point in the United States is Mount Mitchell in North Carolina. "
                                  "It rises more than 2 thousand meters.",
                                  'https://peakvisor.com/img/news/Appalachian-Mountains.jpg'],
                 'Pacific mountains': ["These are mountain ranges off the coast of the United States. "
                                     "The system begins in the north, where Mount Olympus rises 2.4 thousand meters in Washington. "
                                     "The western slopes of these mountains descend into the ocean. "
                                     "Then the Cascade Mountains rise to the south, forming a volcanic chain in California and Oregon. "
                                     "The last major eruption here was in the 80s. "
                                     "20th century The maximum height of the ridge in this area is 1,200 m.",
                                       'https://i.pinimg.com/736x/ef/be/93/efbe932a83360e8fc3854b8ddc30b891--mountain-range-south-island.jpg'],
                 'Rocky Mountains': ['In the Cordillera system, the ridge stretches for 4.5 thousand km. '
                                    'In the south, the mountains begin in New Mexico, gradually rising and widening towards Utah. '
                                    'Most of the major Rocky Mountains are located in Colorado. '
                                    'Here, the highest point of the region is Mount Elbert with a height of 4.5 thousand meters above the sea. '
                                    'Toward the northwest, the mountains decrease and narrow. '
                                    'The Rocky Mountains are rich in minerals, so gold, silver, copper, and lead are mined there. '
                                    'A national park has also been formed on the territory, protecting the thermal springs and geysers of the ridges. '
                                    'The Rocky Mountains separate the Pacific and Atlantic oceans.',
                                     'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Moraine_Lake_17092005.jpg/1200px-Moraine_Lake_17092005.jpg']}
    skiResorts = {'Aspen': ["Aspen is one of the largest resorts in the United States. "
                            "It has a reputation as a prestigious and expensive resort. "
                            "This is partly true, but Aspen is accessible to those on a tight budget, and snow is almost always guaranteed here. "
                            "Aspen combines four isolated ski areas - Aspen Mountain (Aspen Mountain), Aspen Highlands (Aspen Highlands), Buttermilk (Buttermilk) and Snowmass (Snowmass). "
                            "All together they offer 200 km of slopes for all tastes, both for beginners and experienced skiers, with a developed lift system. "
                            "The highest peaks in the area are Maroon Bells (4247m) and Pyramid Peak (4205m). "
                            "Aspen is a Victorian-style resort town nestled in the picturesque Roaring Fork Valley, with a plethora of restaurants, "
                            "shops and plenty of activities besides skiing.",
                            'https://ski.ru/kohana/upload/user_images/3_1359622357.jpg'],
                  'Heavenly': ["Heavenly Resort is located on the Nevada/California border. "
                               "At the foot of the mountain lies the largest mountain lake in the Americas, Lake Tahoe. "
                               "Here you will have a unique opportunity to combine a ski holiday with a visit to the casino. "
                               " Resort combines the beauty of nature, great skiing on the wooded slopes and unparalleled nightlife. "
                               "Located on the border of Nevada, Heavenly has gaming centers and casinos where you can spend time in the evening. "
                               "There is a wide choice of bars, restaurants, night clubs and discos for young people.",
                               'https://travelask.ru/uploads/hint_place/000/070/715/image/129ebb8e0c8f5e6800fa5305b55af7d7.jpg'],
                  'Keystone': ["Keystone is one of the largest ski resorts in Colorado where you can ski all day long with family and friends. "
                               "You can go down on an inflatable ring from the Adventure Point hill, go ice skating on the picturesque Keystone Lake"
                               " and visit the snow fortress at the top of Mount Dercum. The whole family will love it, and it's all in one place. "
                               "After descending the slopes, you can go snowshoeing, cross-country skiing or ice skating, or simply relax in the spa.",
                               'http://triplook.me/media/resorts/photo/5/e/u27.jpg']}
    lakes = {'Okeechobee': ["Okeechobee is a freshwater lake in Florida. It occupies the Glades, Okeechobee, Martin, Palm Beach, and Hendry counties. "
                            "By area, it is the largest lake in the southern United States and the second largest freshwater lake in area, located entirely in the country. "
                            "Several small rivers flow into the lake, the largest being the Kissimmee. "
                            "Several small channels of the Everglades biosystem flow from Okeechobee, to which the lake belongs. "
                            "Also on the lake there are several small islands, the largest of which is Creamer, inhabited. "
                            "The city of Cluiston is located on the south coast.",
                            'https://i0.wp.com/courrierdesameriques.com/wp-content/uploads/2018/03/Clewiston-Lake-Okeechobee-Floride-0555.jpg?resize=708%2C531&ssl=1'],
             'Ontario': ["Ontario is a lake in the United States and Canada, the lowest and smallest in area in the Great Lakes system. "
                         "It is the fifth largest lake in the United States by area. "
                         "The name of the lake comes from the language of the Huron Indian tribe and means Lake of shining waters. "
                         "Later, the province of Ontario became known as the same. On old maps you can see different names of the lake. On the map from 1662-1663. "
                         "The lake was called Ondiara.",
                         'https://touristam.com/wp-content/uploads/2020/12/ozero-ontario-1.jpg'],
             'Michigan': ['Michigan is a freshwater lake in the United States, one of the North American Great Lakes. '
                          'The only one of the Great Lakes that is entirely within the United States, the largest of those located entirely in the United States. '
                          'Located south of Lake Superior, connected to Lake Huron by the Strait of Mackinac, with the Mississippi River system - the Chicago-Lockport Canal. '
                          'From the point of view of hydrography, Michigan and Huron form a single system, but geographically they are considered to be separate lakes.',
                          'https://fanfacts.ru/picture/fakty-ozero-michigan-960x540.jpg']}
    rivers = {'Missouri': ["It flows through 10 states. This is the longest river in the USA. "
                           "Its source is in the Rocky Mountains at an altitude of 2750 meters above sea level. "
                           "More than 10 Indian tribes lived on its banks. "
                           "The Missouri became an important transportation route for westward settlers in the 19th century. "
                           "Many dams and dams began to be built on it. Beavers, raccoons, muskrats and otters live near the river. "
                           "The extraction of their fur attracted colonizers and indigenous people. "
                           "The length of the river is 3767 km.",
                           'https://pibig.info/uploads/posts/2021-05/thumbs/1622059734_4-pibig_info-p-missuri-reka-priroda-krasivo-foto-5.jpg'],
              'Mississippi': ["The river is one of the largest in the world. Flows in a southerly direction. "
                              "The source takes in the state of Minnesota, and ends in the Gulf of Mexico. "
                              "The course of the Mississippi is very winding. For several states, the river is a natural border. "
                              "The river is fed by rain and melt water. The river often causes floods. "
                              "The largest occurred in 1927, it was called the great flood.",
                              'https://s9.travelask.ru/system/images/files/001/457/202/wysiwyg_jpg/mississippi-river.jpg?1613421527'],
              'Yukon': ["Yukon translates as Big River. This name was given to her by the Gwich'in tribe. "
                        "It flows through Alaska and Canada, then flows into the Bering Sea. "
                        " the Gold Rush, thousands of prospectors came to the Yukon River and its tributary, the Klondike. "
                        "The famous writer Jack London was also on this river. The climate on the banks of the river is harsh, "
                        "in winter the temperature drops to minus fifty degrees, and in summer it rarely reaches plus twelve. "
                        "The length of the river is 3190 km.",
                        'https://about-planet.ru/images/severnaya_amerika/priroda/yukon/yukon2.jpg']}
    # currency
    currencyName = 'USD'
    currencyEqualsToDollar = 1

    # military
    milPolBlock = "NATO"
    amountOfPeopleInArmy = 1395350

    # healthcare
    numberOfDoctorsPer100kPopulation = 294
    menAverageLifeExpectancy = 73.2
    womenAverageLifeExpectancy = 79.1

    # climat
    juneAverageTemperature = 25
    decemberAverageTemperature = 9
    averageHumidity = 63
    averageDurationOfWinter = 3.5
    averageRainfallPerMonth = 27.6
    averageNumberOfFoggyDaysPerYear = 42
    averageNumberOfRainyDaysPerYear = 108
    averageNumberOfClearDays = 189

    # security
    situationInTheCountry = 2  # [1, 3] 1-bad, 3-good
    freedomOfSpeech = 3  # [1, 3]
    assessmentOfFamilyLife = 3  # [1, 3]
    attitudeTowardsLGBT = 3  # [1, 3]

    # population
    populationCount = 331900000
    procentOfMales = 49.4
    procentOfFemales = 50.6
    populationDensityPerSquareKilometer = 34.8
    speedOfLife = 3  # [1, 3]
    workPlaces = 3  # [1, 3]
    nightLifeEntertainment = 3  # [1, 3]

    # citizenship
    citizenshipGlobalRank = 3
    friendlyToForeigners = 3

    # communication
    communicationOnEnglish = 3  # [1, 3]

    # transport
    averageTravelTimeToWork = 32.91
    developmentLevelOfPublicTransport = 3  # [1, 3]

    # internet
    speedOfInternetMbps = 31  # Мегабиты в секунду
    freeWifi = 3  # [1, 3]

    # education
    rankingOfNationalEducationSystem = 1

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
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers, friendlyToForeigners
                  )

    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()
    #############################   USA   #############################

    #############################   Italy   #############################

    # Country
    countryName = "Italy"
    officialLanguage = "Italian"

    # cities    name   isBig  washesBy
    cities = {
        'Rome': [True, False, None], 'Milan': [True, False, None], 'Naples': [True, True, 'Tyrrhenian Sea'],
        'Turin': [True, False, None], 'Palermo': [True, True, 'Tyrrhenian Sea'], 'Venice': [False, True, 'Adriatic Sea'],
        'Sicily': [False, True, 'Mediterranean Sea'], 'Rimini': [False, True, 'Adriatic Sea'], 'Bologna': [False, False, None]}

    # education
    universities = {'Milan': ['Politecnico di Milano', 'University of Milan'],
                    'Rome': ['Sapienza University'],
                    'Turin': ['Politecnico di Torino']}
    faculties = {
        'Politecnico di Milano': ['Faculty of Arts', 'Faculty of Medicine', 'Faculty of Engineering',
                                  'Faculty of Computer Engineering and Software', 'Faculty of Science'],
        'University of Milan': ['Faculty of Medicine', 'Faculty of Law', 'Faculty of Science', 'Faculty of Social Sciences',
                                'Faculty of Computer Engineering and Software'],
        'Sapienza University': ['Faculty of Business', 'Faculty of Arts', 'Faculty of Law', 'Faculty of Engineering', 'Faculty of Medicine',
                                'Faculty of Social Sciences', 'Faculty of Architecture', 'Faculty of Science'],
        'Politecnico di Torino': ['Faculty of Engineering', 'Faculty of Computer Engineering and Software', 'Faculty of Medicine', 'Faculty of Arts']}
    programs = {
        'Politecnico di Milano': ['Magistracy', 'Undergraduate'],
        'University of Milan': ['Magistracy', 'Undergraduate'],
        'Sapienza University': ['Magistracy', 'Undergraduate'],
        'Politecnico di Torino': ['Magistracy', 'Undergraduate']}
    links = {'Politecnico di Milano': 'https://www.polimi.it',
             'University of Milan': 'https://misom.unimi.it',
             'Sapienza University': 'https://www.uniroma1.it',
             'Politecnico di Torino': 'https://www.polito.it'}
    images = {'Politecnico di Milano': 'https://italyadaegitim.com/wp-content/uploads/2020/11/politecnico-di-milano.jpg',
             'University of Milan': 'https://diginlaw.files.wordpress.com/2021/04/02.-faculty-photo.jpg?w=1200',
             'Sapienza University': 'https://smapse.ru/storage/2018/09/sapienza-universita-roma.jpg',
             'Politecnico di Torino': 'https://fartakapply.com/wp-content/uploads/2020/09/6-POLITO.jpg'}
    # общага
    hostel = {'Politecnico di Milano': 'Yes',
             'University of Milan': 'Yes',
             'Sapienza University': 'No',
             'Politecnico di Torino': 'No'}
    # стипендия
    scolarship = {'Politecnico di Milano': 'Yes',
                  'University of Milan': 'Yes',
                  'Sapienza University': 'Yes',
                  'Politecnico di Torino': 'Yes'}
    # требования к поступлению
    requirements = {'Politecnico di Milano': 'For admission, applicants must provide: '
                                             'Certified translation of the certificate of secondary education, '
                                             'TOEFL iBT 80 (minimum)/Academic IELTS 6.0 (minimum), '
                                             'Entrance exam results, Registration fee payment certificate = $160.',
                    'University of Milan': 'The requirements for admission to the University of Milan are standard, as in many other universities in Europe: '
                                           'previous grades and entrance exams, certificate / diploma + for enrolling in some specialties, '
                                           'you may need a motivation letter and recommendations.',
                    'Sapienza University': '12 years completed education. '
                                           'All documents must be translated, apostilled and legalized with a Dichiarazione di valore in loco consular certificate. '
                                           'For studying in Italian: level B2 and above. '
                                           'For study in English: certificate IELTS, TOEFL, Cambridge B2, TOEIC (exact requirements depend on the program). '
                                           'If the applicant does not have a certificate at the time of application, he can take the Italian exam at the university '
                                           '(usually held in September, but the exact dates need to be clarified). '
                                           'Applicants for medical courses take the IMAT test, for closed and open access programs, a TOLC type exam may be required.',
                    'Politecnico di Torino': 'To enter the university, citizens of other states need to study at least one '
                                             'year at any university so that their documents meet the requirements of the admission committee.'}
    costs = {'Politecnico di Milano': 3900,
             'University of Milan': 2500,
             'Sapienza University': 2280,
             'Politecnico di Torino': 3600}

    sights = {'Pantheon': ["A real achievement of the building technologies of antiquity, "
                           "a magnificent temple, which became a model of ancient architecture and gave rise to many imitators. "
                           "The Pantheon, fortunately, is perfectly preserved, so everyone can visit it. "
                           "This is best done at noon, when a real pillar of light breaks through the hole in the roof.", 'https://top10.travel/wp-content/uploads/2014/10/panteon.jpg'],
              'Coliseum': ["This is a visiting card of Rome, a building that is familiar even to those who have never left their hometown. "
                           "Today, the Colosseum, of course, bears the marks of time and needs to be reconstructed. "
                           "And still, a visit to this historical monument is included in the mandatory program of "
                           "all tourists and leaves an indelible impression.", 'https://top10.travel/wp-content/uploads/2014/10/kolizey.jpg'],
              'San Gimignano': ["City in Tuscany, near Florence. "
                                "San Gimignano is known for the fact that it managed to preserve its medieval appearance and from afar it "
                                "seems that horse-drawn carts still move along its streets, and knights with swords walk sedately. "
                                "Be sure to see the 14 ancient towers and the local history museum.", 'https://top10.travel/wp-content/uploads/2014/10/san-gimignano.jpg']}
    beaches = {'Red bay': ["Looking for a quiet beach to get away from everyone and have some peace and quiet? "
                           "Head to Favignana, a tiny island off the coast of Sicily. "
                           "Only a few thousand people live here and there are four dozen hotels on the entire island. "
                           "Getting here is not easy - only by ferry from Sicily, but that's why there are few people here. "
                           "The only thing that can overshadow your vacation is your phone, so don't forget to turn it off on the ship.",
                           'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/13/a7/bf/3a/red-beach.jpg?w=1200&h=-1&s=1'],
               "Marina Picola": ["The island of Capri has been an elite resort for a very long time: Caesar Augustus had a “cottage” here. "
                                 "And since the days of the Roman Empire, for some reason (or perhaps just following the fashion), celebrities have flocked here. "
                                 "Russian celebrities are no exception, almost every outstanding person in our recent history has visited Capri: "
                                 "from Tchaikovsky and Bunin to Gorky and Lenin. "
                                 "The beach at Marina Picola Bay is overshadowed by Capri's other famous beaches and attractions, such as the famous Blue Grotto. "
                                 "But this is for the best, because today Capri is still an elite resort, and finding a secluded place here is not so easy.",
                                 'https://tournavigator.pro/%D1%84%D0%BE%D1%82%D0%BE/other_1022_1003_1657754408.jpg'],
               'Rabbit beach': ["Rabbit Beach has been repeatedly recognized as the best beach in the world. "
                                "No wonder, because this is one of those places where you want to stay forever. "
                                "The beach is located in a protected area, and it is not easy to get to it. "
                                "First you need to come to the island of Lampedusa, which in itself is not a trivial task. "
                                "Then you need to go by bus or car, and then walk for 20 minutes. "
                                "And these 20 minutes, perhaps, will leave you even more impressions than the beach itself: "
                                "the views from the mountain path are simply amazing.",
                                'https://ostrova24.ru/wp-content/uploads/2017/05/ostrov-Lampeduza-v-Italii.jpg']}
    mountains = {'Mont Blanc': ["Mont Blanc is a peak in the massif of the same name, rising above Lake Leman in the Alps. "
                                "This is the highest point of the Alps, reaching a height of 4810 m above sea level. "
                                "The highest mountain in the European Union and Europe, excluding the Caucasus Mountains as part of Europe. "
                                "Located on the border of Italy and France.",
                                'https://funart.pro/uploads/posts/2019-11/1573381953_monblan-gora-francija-3.jpg'],
                 'Marmolada': ["Marmolada is a mountain in northeastern Italy, the highest mountain in the Dolomites. "
                               "This is part of the ridge that stretches from west to east. "
                               "In the west, the mountain breaks into steep cliffs, forming a stone wall several kilometers long. "
                               "To the north is the relatively gentle Marmolada Glacier.",
                               'https://st2.depositphotos.com/1355276/5612/i/950/depositphotos_56122677-stock-photo-marmolada-ski-resort-in-italy.jpg'],
                 'Dolomites': ['The Dolomites are a mountain range in the Eastern Alps, part of the system of the Southern Limestone Alps. '
                               'The massif is located in the northeastern part of Italy in the provinces of Belluno, Bolzano, Pordenone, Trento and Udine. '
                               'The massif is bounded by river valleys: Isarco, Pusteria, Piave, Brenta and Adige.',
                               'https://otdyhateli.com/wp-content/uploads/2017/03/The-Dolomites-1050x700.jpg']}
    skiResorts = {'Breuil-Cervinia': ["The Breuil-Cervinia ski resort is located in the Valle d'Aosta region, at the foot of the Matterhorn rocky ridge (2050 above sea level). "
                                      "It is considered one of the best in the north of the country. "
                                      "From here, via a single ski area, you can reach the Swiss side of the Matterhorn on the slopes of Zermatt. "
                                      "The entire winter season, even not at a very high altitude, there will be plenty of snow here, and this is almost 6 months a year. "
                                      "In total, Cervinia covers more than 100 km of ski slopes of varying difficulty. "
                                      "In summer, the cross-country ski run turns into a golf course. "
                                      "Also in the summer, hiking is very developed and climbing to the top of the Matterhorn is popular.",
                                      'https://planetofhotels.com/guide/sites/default/files/styles/paragraph__live_banner__lb_image__1880bp/public/live_banner/Cervinia-1.jpg'],
                  'Val Gardena': ["Val Gardena is one of the best ski resorts in Italy, divided into the three municipalities of Ortisei, Santa Cristina in Val Gardena and Selva di Val Gardena (Trentino-Alto Adige region). "
                                  "Val Gardena is located in the heart of the Dolomites and offers some challenging pistes surrounded by beautiful pine forests. "
                                  "The valley is very popular among tourists, partly because of the fact that the stages of the Ski World Cup take place here. "
                                  "In total, there are 175 km of ski slopes, 115 km of cross-country trails and 83 ski lifts.",
                                  'https://www.dolomiticlass.it/storage/localities/67/conversions/Selva_Gardena_inverno-tablet.jpg'],
                  "Cortina d'Ampezzo": ["Cortina d'Ampezzo is located in the Veneto region, and is called the Pearl of the Dolomites, for the presence of slopes for every taste. "
                                        "In total, they make up 115 km of ski slopes with different levels of difficulty. "
                                        "Cortina d'Ampezzo is considered one of the most equipped ski resorts in Italy and is the ideal place for a family holiday. "
                                        "One of the strengths of this resort is the presence of numerous hotels and inns that can satisfy the needs of even the most demanding tourists. "
                                        "The main attraction of Cortina d'Ampezzo is, of course, the historic center of the city, where the main sports, antique and souvenir shops are located.",
                                        'https://live.staticflickr.com/65535/49089210372_6f075ba8d5_o.jpg']}
    lakes = {'Lago Maggiore': ["On the border of Lombardy, Piedmont and Switzerland, Lake Maggiore is located, an endless expanse of water that reflects the surrounding landscapes: "
                               "fragrant pine groves, centuries-old forests and majestic mountains. "
                               "In the middle of the emerald green vegetation and the blinding blue of the sky, numerous castles, "
                               "palaces and Italian gardens rise, related to the two noble families that influenced the history of this place - the Visconti and the Borromeo. "
                               "You can start your journey through these picturesque beauties from Stresa on the Piedmontese coast, "
                               "opposite the Borromean Islands, real open-air museums: Bella Island with the Borromeo Palace, "
                               "Madre Island with its stunning vegetation and the Fishermen's Island, on which, as the name suggests, there is a characteristic settlement. "
                               "Verbania is another lively Piedmont town with a number of beautiful villas such as Villa Giulia, San Remigio and Taranto, "
                               "where you can see 20,000 species of plants.",
                               'https://www.travelbook.de/data/uploads/2022/04/gettyimages-642500890.jpg'],
             'Lago di Bracciano': ["Lake Bracciano, also called Lake Sabatino, is of volcanic origin, only one river flows into it - Arrone, "
                                   "originating on the southeast coast and carrying its waters to the Tyrrhenian Sea. "
                                   "The coast of Italy's lake is conducive to long walks. "
                                   "There are various establishments along the way. "
                                   "Including restaurants whose cuisine specializes in dishes with lake fish. "
                                   "The beach is wide with a large sandy area.",
                                   'https://www.lazionascosto.it/wp-content/uploads/2019/05/lago-di-bracciano.jpg'],
             'Lago di Garda': ['Lake Garda, or Benaco, is the largest lake in Italy. '
                               'In the south it is surrounded by moraine hills formed by the last glacier, and in the north by higher mountain '
                               'ranges that help maintain a mild Mediterranean climate. '
                               'The radiance of nature, the mildness of the climate, the rich vegetation (mainly olive trees, palms, cypresses, lemons, oleanders and oranges)'
                               ' and the majestic scenery, together with cultural and historical values, make Lake Garda the most attractive among Italian lakes.',
                               'https://www.valeggio.com/wp-content/uploads/2021/03/lago-di-garda-lanfredi-valeggio-5.jpg']}
    rivers = {'Po': ["In Italy, the Po River is the longest, most abundant and has the largest basin. "
                     "Along it there are several cities of interest for their historical monuments, and its mouth itself is a landmark.",
                     'https://planetofhotels.com/guide/sites/default/files/styles/paragraph__text_with_image___twi_image/public/2020-05/po-river-1.jpg']}
    # currency
    currencyName = 'ITL'
    currencyEqualsToDollar = 1835.88

    # military
    milPolBlock = "NATO"
    amountOfPeopleInArmy = 161550

    # healthcare
    numberOfDoctorsPer100kPopulation = 395
    menAverageLifeExpectancy = 78.8
    womenAverageLifeExpectancy = 84.1

    # climat
    juneAverageTemperature = 27
    decemberAverageTemperature = 12
    averageHumidity = 69
    averageDurationOfWinter = 1.5
    averageRainfallPerMonth = 78.8
    averageNumberOfFoggyDaysPerYear = 42
    averageNumberOfRainyDaysPerYear = 80
    averageNumberOfClearDays = 117

    # security
    situationInTheCountry = 2  # [1, 3] 1-bad, 3-good
    freedomOfSpeech = 3  # [1, 3]
    assessmentOfFamilyLife = 2  # [1, 3]
    attitudeTowardsLGBT = 1  # [1, 3]

    # population
    populationCount = 59070000
    procentOfMales = 49
    procentOfFemales = 51
    populationDensityPerSquareKilometer = 33.6
    speedOfLife = 2  # [1, 3]
    workPlaces = 2  # [1, 3]
    nightLifeEntertainment = 3  # [1, 3]

    # citizenship
    citizenshipGlobalRank = 2
    friendlyToForeigners = 3

    # communication
    communicationOnEnglish = 1  # [1, 3]

    # transport
    averageTravelTimeToWork = 33.56
    developmentLevelOfPublicTransport = 2  # [1, 3]

    # internet
    speedOfInternetMbps = 13  # Мегабиты в секунду
    freeWifi = 1  # [1, 3]

    # education
    rankingOfNationalEducationSystem = 14

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
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers, friendlyToForeigners
                  )

    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()
    #############################   Italy   #############################

    #############################   Spain   #############################

    # Country
    countryName = "Spain"
    officialLanguage = "Spanish"

    # cities    name   isBig  washesBy
    cities = {
        'Madrid': [True, False, None], 'Barcelona': [True, True, 'Balearic sea'], 'Valencia': [True, True, 'Balearic sea'],
        'Seville': [True, False, None], 'Zaragoza': [True, False, None], 'Ibiza': [True, True, 'Balearic sea'],
        'Majorca': [True, True, 'Balearic sea'], 'San Sebastian': [False, True, 'Atlantic ocean']}

    # education
    universities = {'Barcelona': ['University of Barcelona', 'EU Business School'],
                    'Madrid': ['Saint Louis University'],
                    'Seville': ['University of Seville']}
    faculties = {
        'University of Barcelona': ['Faculty of Medicine', 'Faculty of Law', 'Faculty of Science', 'Faculty of Business', 'Faculty of Social Sciences'],
        'EU Business School': ['Faculty of Business', 'Faculty of Arts', 'Faculty of Social Sciences', 'Faculty of Education'],
        'Saint Louis University': ['Faculty of Arts', 'Faculty of Social Sciences', 'Faculty of Medicine', 'Faculty of Education'],
        'University of Seville': ['Faculty of Business', 'Faculty of Social Sciences', 'Faculty of Law', 'Faculty of Computer Engineering and Software']}
    programs = {
        'University of Barcelona': ['Magistracy', 'Undergraduate', 'Doctoral'],
        'EU Business School': ['Magistracy', 'Undergraduate', 'MBA', 'Foundation'],
        'Saint Louis University': ['Magistracy', 'Undergraduate'],
        'University of Seville': ['Magistracy', 'Undergraduate']}
    links = {'University of Barcelona': 'https://www.ub.edu',
             'EU Business School': 'https://www.euruni.edu',
             'Saint Louis University': 'https://www.uhsp.edu',
             'University of Seville': 'https://ics-seville.org'}
    images = {
        'University of Barcelona': 'https://www.usnews.com/object/image/00000152-46f4-d86f-a7f6-cfff51660000/160115-universityofbarcelona-submitted.jpg?update-time=1452889458023&size=responsiveFlow970',
        'EU Business School': 'https://www.studylab.ru/upload/Institutions/image/big/cc262389c39ef03abce744a2f1991757.jpg',
        'Saint Louis University': 'https://nogoonjade.mn/wp-content/uploads/2019/02/Saint-Louis-University.jpg',
        'University of Seville': 'https://ics-seville.org/wp-content/uploads/2017/01/notas-de-corte-universidad-de-sevilla-2016.jpg'}
    # общага
    hostel = {'University of Barcelona': 'Yes',
              'EU Business School': 'Yes',
              'Saint Louis University': 'Yes',
              'University of Seville': 'Yes'}
    # стипендия
    scolarship = {'University of Barcelona': 'Yes',
                  'EU Business School': 'Yes',
                  'Saint Louis University': 'Yes',
                  'University of Seville': 'Yes'}
    # требования к поступлению
    requirements = {'University of Barcelona': 'There are no restrictions on the basis of religious views, as well as on the basis of gender for admission to the university. '
                                               'Enrollment is made on the basis of the provided data on the academic achievements of the applicant.'
                                               ' One of the conditions put forward by the university is knowledge of the Spanish language, which is assessed by a special test. '
                                               'The list of documents required for admission is posted on the university website. '
                                               'For foreign applicants - all documents included in the application package must have a notarized translation into Spanish. '
                                               'Usually about 80% of applicants are enrolled, but depending on the prestige of the faculty, this figure may vary. '
                                               'The cost of studying at the University of Barcelona is relatively low. '
                                               "Obtaining a bachelor's degree will cost USD 1,000 per year, and an annual master's degree will cost USD 3,000. "
                                               "There is also a scholarship program based on the competition.",
                    'EU Business School': 'Age: 17+, Duration: 6-7 semesters (3 - 3.5 years), ECTS: 240, '
                                          'Beginning of studies: August, October, February and June, '
                                          'Language requirements: TOEFL iBT 80+, IELTS Academic 6.0+, CAE B2 (169+), '
                                          'Academic requirements: completed secondary or secondary special education with good academic performance',
                    'Saint Louis University': '1. Age: from 17 years old; '
                                              '2. High school diploma (good and excellent grades and high GPA);'
                                              '3. Proficiency in English: IELTS 6.5/TOEFL 80/Pearson Versant 69 or equivalent (certificate is valid for two years after the exam date); '
                                              '4. Portfolio; '
                                              '5. GPA-3.0; '
                                              '6. High performance and knowledge in core disciplines.',
                    'University of Seville': 'The admission procedure provides for the provision of a document confirming academic performance at the previous place of study. '
                                             'Then comes the exam. According to the general results, enrollment takes place. '
                                             'Everything related to admission, deadlines for submitting documents and the cost of individual programs is described on the official '
                                             'website of the University of Seville.'}
    costs = {'University of Barcelona': 3000,
             'EU Business School': 4900,
             'Saint Louis University': 10880,
             'University of Seville': 1000}

    sights = {'National Prado Museum': ["The museum is located on the Boulevard of Arts - a popular tourist route. "
                                        "Its most valuable collection includes more than 8.5 thousand paintings and about 700 sculptures. "
                                        "Art connoisseurs from different eras will find something to see in Spain, in particular, in the Prado Museum. "
                                        "It welcomes visitors with paintings by the great Spanish masters, including paintings by Goya and Velasquez. "
                                        "The Italian art school is represented here by the works of Tintoretto, Botticelli, Titian, Raphael, Veronese, Fra Angelico, Mantegna. "
                                        "And within the framework of Flemish painting, the museum exhibits paintings by Vander Weyden, Pieter Brueghel the Elder, Hieronymus Bosch, Jacob Jordaens, Peter Paul Rubens.",
                                        'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2017/04/Spain-1-The-Prado-Museum-e1491982394705.jpg'],
              'Sagrada Familia': ["The place of this attraction in Spain is included in the lists of UNESCO sites. "
                                  "Sagrada Familia or Sagrada Familia, as it is also called, gives tourists different feelings. "
                                  "The first associations evoke an old church building, but the unusual structure suggests that it was created by an alien mind. "
                                  "The creator of the project of the original temple is Antoni Gaudí. Don't know what to see in Spain that will be remembered forever? "
                                  "Visit the Sagrada Familia. As conceived by Gaudi, the temple was destined for the role of the Bible, embodied in architecture. "
                                  "The magnificent facades were supposed to symbolize the main stages of the life of Christ: the Birth, the Torments of Christ, the Resurrection. "
                                  "The amazing acoustics in the temple is due to the perfect bell system, and the columns, approaching the vaults, form a fantastic likeness of intertwining tree branches.",
                                  'https://media.decorateme.com/images/aa/48/d5/vitaia-forma-bashen-gaudi-obiasniaetsia-tem-chto.webp'],
              'Ordesa y Monte Perdido National Park': ["The famous sights of Spain are also in its most remote corners. "
                                                       "One of the first national parks - Ordesa y Monte Perdido Reserve - is still considered the most beautiful in the country. "
                                                       "The main attraction of the park is the Ordesa Canyon. "
                                                       "It impresses with huge rocks hanging from both sides of the mountain path. "
                                                       "The river of the same name runs along the bottom of the canyon. "
                                                       "Its waters are replenished by streams flowing down the slopes. "
                                                       "The lower part of the park is represented by a dense forest, where you can meet many representatives of the forest fauna. "
                                                       "There are many waterfalls that cascade one after another. "
                                                       "Among them, the most powerful, perhaps, is the Cola de Caballo waterfall, from which the Ordesa River begins. "
                                                       "Cows graze on the spacious meadows of the park, dense poplar and beech forests are located at the foot of the mountains.",
                                                       'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2017/04/Spain-9-Ordesa-y-Monte-Perdido-National-Park-e1491984613524.jpg']}
    beaches = {'Rodas, Sie Islands': ["Rodas Beach (Playa de Rodas) topped the ranking of the best beaches in the world in 2007, according to the British newspaper The Guardian. "
                                      "And this is no coincidence. "
                                      "The Cies archipelago is made up of three large islands - Monteagudo, Faro, San Martino. Since 2002 they have been part of the National Park of the Atlantic Islands of Galicia. "
                                      "Protected by the state. Here are the most beautiful beaches in Spain. "
                                      "It is no coincidence that they are called paradises - there is impeccable white sand and huge areas of untouched nature. "
                                      "Add to this the abundance of rare birds in the vicinity and dolphins in the ocean waters.",
                                      'https://planetofhotels.com/guide/sites/default/files/styles/paragraph__text_with_image___twi_image/public/2020-08/Praia-de-Rodas-beach.jpg'],
               "Burriana": ["Burriana (Playa Burriana) is one of the best beaches in Spain. "
                            "It is located in the city of Nerja (province of Malaga) along the Paseo Marítimo Antonio Mercero promenade. "
                            "The coastline is 800 meters long and 40 meters wide. "
                            "Playa Burriana is marked with the Blue Flag, famous for its clean sand, luxurious palm trees and many entertainments. "
                            "There are playgrounds, clubs, bars and restaurants.",
                            'https://planetofhotels.com/guide/sites/default/files/styles/paragraph__text_with_image___twi_image/public/2020-08/Playa-Burriana-at-Nerja.jpg'],
               'Playa de Palma, Mallorca': ["It is difficult to find a person who has not heard about this resort on the Mediterranean coast. "
                                            "Its beauty is painted by artists and sung by poets. "
                                            "Playa de Palma beach has been awarded the Blue Flag and proudly bears this award, delighting with white sand and developed infrastructure. "
                                            "It is perfect for a family vacation, as the entrance to the sea is quite gentle here, and the bottom is sandy and soft, like a velvet cover. "
                                            "On the beach there are playgrounds for playing volleyball, basketball, rental of bicycles and equipment for water activities, it is possible to rent sun loungers. "
                                            "Within walking distance there are at least a dozen bars with refreshing drinks.",
                                            'https://planetofhotels.com/guide/sites/default/files/styles/paragraph__text_with_image___twi_image/public/2020-06/palma-de-mallorca-4.jpg']}
    mountains = {'Mulasen': ["Mulasen is a mountain in southern Spain, the highest peak of the Iberian Peninsula. "
                             "It is located in the Sierra Nevada, one of the spurs of the Cordillera Penibetica. "
                             "On the northern slope of the mountain lies a small avalanche glacier, from which the river Khenil originates.",
                             'https://i.pinimg.com/736x/29/82/0e/29820ee0e5527c20b6d4d20b3c0b3c6f--natural-park-sierra-nevada.jpg'],
                 'Aneto': ["Aneto Peak is the highest mountain in the Pyrenees, located in the province of Huesca, Spain. "
                           "The third highest mountain in Spain. "
                           "The mountain is also known by the French name Pic de Neto, but this name is rarely used, since the mountain is entirely in Spanish territory.",
                           'https://peakfinder.ru/image/original/304_pik_aneto.jpg'],
                 'Veleta': ['Veleta is a mountain peak in southern Spain, in the province of Granada in Andalusia. '
                            'It is part of the Sierra Nevada mountain range. One of the highest points in the entire Iberian Peninsula.',
                            'https://ic.pics.livejournal.com/vpervye1/34433614/1067216/1067216_original.jpg']}
    skiResorts = {'Sierra Nevada': ["Sierra Nevada is the most popular resort in Spain, the highest geographical location. "
                                    "It is located in the southwest, near Granada. The elite of society comes here: actors, famous people, politicians. "
                                    "87 kilometers of slopes of different levels are equipped here, there are cross-country flat trails. "
                                    "More than 400 cannons provide ideal coverage of the slopes. "
                                    "Fashionable hotels, ski schools, all kinds of après-ski establishments are open for guests.",
                                    'https://espanarusa.com/files/autoupload/3/21/70/3ealic0o48095.jpg'],
                  'Baqueira-Beret': ["Baqueira Beret is the largest resort in the Pyrenees on the eastern side of the Aran Valley (Catalonia). "
                                     "Here, among the magnificent landscapes, very reminiscent of the Alpine landscapes, the snow remains for a long time - until March. "
                                     "110 km of diverse routes have been laid; stable snow cover is provided by 500 guns. "
                                     "The resort is considered universal, democratic: skiers of all levels and ages come here. "
                                     "The skiing season is from December to April.",
                                     'https://i.f1g.fr/media/figaro/orig/2018/01/17/XVM346ad012-fac7-11e7-9962-196e3970bf6d.jpg'],
                  'Port del Comte': ["Port del Comte is a relatively new resort, it has existed since the 70s. "
                                     "XX century, located in the Eastern Pyrenees. "
                                     "The length of its tracks is approximately 40 km; Ten lifts have been installed. "
                                     "The local slopes have a low, simple relief; the local ski school employs dozens of instructors. "
                                     "Ski season from late November to late March",
                                     'https://upload.wikimedia.org/wikipedia/commons/b/b6/Port_del_Comte-Estivella.JPG']}
    lakes = {'Lago de Sanabria': ["Lake Sanabria in Zamora is one of the largest in Spain and Europe. "
                                  "Its width is 1.5 kilometers, length - 3 kilometers, and depth - about 50 meters. "
                                  "Since there are many different types of water activities on the lake, you can meet hundreds of people enjoying water recreation here.",
                                  'https://upload.wikimedia.org/wikipedia/commons/8/80/Lago_de_Sanabria%2C_provincia_de_Zamora%2C_Espa%C3%B1a.jpg'],
             'Lagos de Covadonga': ["Lagos de Covadonga are three glacial lakes in the Picos de Europa National Park in Spain. "
                                    "Enol, La Ercina and El Brisial lakes have water only in the warm months of the year after the ice has melted. "
                                    "This area is one of the most visited places of natural beauty in Spain, especially during the summer.",
                                    'https://www.65ymas.com/uploads/s1/14/25/49/santuario-lagos-covadonga-asturias-2.jpeg'],
             'Lago de Sant Maurici': ['This stunning lake in Spain is located in the Pyrenees on the Catalan side. '
                                      'It is located in Espot in Lleida at an altitude of 1,910 meters. '
                                      'The lake is part of the Aiguestortes Natural Park, which is the only one in the Catalonia region. '
                                      'Lake Maurici is 1,100 meters long and 200 meters wide.',
                                      'https://1.bp.blogspot.com/-A55cdO4aPRQ/XoIqhXZ2VSI/AAAAAAAALCw/8E0xeUVUs6AOOq9f-w58onJX9KVJlLrfgCLcBGAsYHQ/s1600/estany-gerber-aiguestortes-2.jpg']}
    rivers = {'Mundo': ["Located in the province of Albacete, next to the city of Riopar, it is the source of the world river, "
                        "in particular in the Natural Park of Calares del Mundo y de la Sima, to which many people go to admire the beautiful waterfall and cave. "
                        "The area known as Los Chorros, where the Mundo river originates, where springs and beautiful waterfalls are located, "
                        "is accessible by a route of about 6.5 kilometers, which takes no more than two hours. "
                        "The mountainous region surrounding the area offers visitors waterfalls between caves and tunnels. "
                        "Along the trail you can hear how the riverbed descends abundantly parallel to the trail, "
                        "leaving behind many lakes with crystal clear water, where trout lives.",
                        'https://upload.wikimedia.org/wikipedia/commons/7/78/Nacimiento_del_R%C3%ADo_Mundo.jpg'],
              'Tagus': ["The longest river in Spain originates in the Universal Mountains, west of the province of Teruel on the border with Cuenca, "
                        "and flows off the coast of Portugal in the Atlantic Ocean. "
                        "A monument with the symbols of the provinces of Teruel (bull with a star), Guadalajara (knight) and Cuenca (bowl) marks the beginning of its canal, "
                        "which can be reached by car, and from this point you can start the route on foot. "
                        "It passes through a pine forest until it reaches Casas de Fuente Garcia. "
                        "The first stream of water from the Tagus falls there. "
                        "It is located near the beautiful town of Albarracín, the ideal place to end your holiday in Teruel.",
                        'https://terra-z.com/wp-content/uploads/2014/03/523.jpg']}
    # currency
    currencyName = 'EUR'
    currencyEqualsToDollar = 0.95

    # military
    milPolBlock = "NATO"
    amountOfPeopleInArmy = 122850

    # healthcare
    numberOfDoctorsPer100kPopulation = 382
    menAverageLifeExpectancy = 78.2
    womenAverageLifeExpectancy = 84.4

    # climat
    juneAverageTemperature = 25
    decemberAverageTemperature = 14
    averageHumidity = 71
    averageDurationOfWinter = 3.5
    averageRainfallPerMonth = 54
    averageNumberOfFoggyDaysPerYear = 26
    averageNumberOfRainyDaysPerYear = 63
    averageNumberOfClearDays = 97

    # security
    situationInTheCountry = 3  # [1, 3] 1-bad, 3-good
    freedomOfSpeech = 3  # [1, 3]
    assessmentOfFamilyLife = 2  # [1, 3]
    attitudeTowardsLGBT = 3  # [1, 3]

    # population
    populationCount = 47330000
    procentOfMales = 49.4
    procentOfFemales = 50.6
    populationDensityPerSquareKilometer = 92.1
    speedOfLife = 3  # [1, 3]
    workPlaces = 3  # [1, 3]
    nightLifeEntertainment = 3  # [1, 3]

    # citizenship
    citizenshipGlobalRank = 2
    friendlyToForeigners = 2

    # communication
    communicationOnEnglish = 2  # [1, 3]

    # transport
    averageTravelTimeToWork = 29.06
    developmentLevelOfPublicTransport = 3  # [1, 3]

    # internet
    speedOfInternetMbps = 21  # Мегабиты в секунду
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
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers, friendlyToForeigners
                  )

    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()
    #############################   Spain   #############################

    #############################   Portugal   #############################

    # Country
    countryName = "Portugal"
    officialLanguage = "Portuguese"

    # cities    name   isBig  washesBy
    cities = {
        'Lisbon': [True, True, 'Atlantic ocean'],
        'Portu': [True, True, 'Atlantic ocean'],
        'Amadora': [True, True, 'Atlantic ocean'],
        'Braga': [True, False, None],
        'Setubal': [True, True, 'Atlantic ocean'],
        'Faro': [True, True, 'Atlantic ocean']}

    # education
    universities = {'Lisbon': ['Polytechnic Institute', 'University of Lisbon'],
                    'Portu': ['Universidade do Porto'],
                    'Faro': ['Universidade do Algarve']}
    faculties = {
        'Polytechnic Institute': ['Faculty of Education', 'Faculty of Engineering', 'Faculty of Medicine', 'Faculty of Business'],
        'University of Lisbon': ['Faculty of Architecture', 'Faculty of Arts', 'Faculty of Law', 'Faculty of Science',
                                 'Faculty of Education', 'Faculty of Medicine'],
        'Universidade do Porto': ['Faculty of Architecture', 'Faculty of Arts', 'Faculty of Law', 'Faculty of Business',
                                  'Faculty of Engineering', 'Faculty of Medicine'],
        'Universidade do Algarve': ['Faculty of Business', 'Faculty of Medicine', 'Faculty of Law', 'Faculty of Engineering']}
    programs = {
        'Polytechnic Institute': ['Magistracy', 'Undergraduate'],
        'University of Lisbon': ['Magistracy', 'Undergraduate', 'Doctoral'],
        'Universidade do Porto': ['Magistracy', 'Undergraduate', 'Doctoral'],
        'Universidade do Algarve': ['Magistracy', 'Undergraduate']}
    links = {'Polytechnic Institute': 'https://www.ipl.pt',
             'University of Lisbon': 'https://www.ulisboa.pt',
             'Universidade do Porto': 'https://www.up.pt/',
             'Universidade do Algarve': 'https://www.ualg.pt/'}
    images = {
        'Polytechnic Institute': 'https://smapse.com/storage/2019/08/z1-21.jpg',
        'University of Lisbon': 'https://smapse.com/storage/2020/12/universidade-de-lisboa-smapse7.jpg',
        'Universidade do Porto': 'https://www.estudarfora.org.br/wp-content/uploads/2020/04/unipo.jpg',
        'Universidade do Algarve': 'https://www.clbrief.com/wp-content/uploads/2020/11/algarve-uni-2-1000x642.jpg'}
    # общага
    hostel = {'Polytechnic Institute': 'Yes',
              'University of Lisbon': 'Yes',
              'Universidade do Porto': 'Yes',
              'Universidade do Algarve': 'Yes'}
    # стипендия
    scolarship = {'Polytechnic Institute': 'Yes',
                  'University of Lisbon': 'Yes',
                  'Universidade do Porto': 'Yes',
                  'Universidade do Algarve': 'Yes'}
    # требования к поступлению
    requirements = {
        'Polytechnic Institute': 'A certain number of students can enter the university every year. '
                                 'A special selection committee makes its decision on the recruitment of first-year students, based on data on past academic performance. '
                                 'The results of the entrance exams are also taken into account. By and large, not only residents of Portugal, but also the entire globe, apply for places in the university.',
        'University of Lisbon': 'The deadline for submitting documents is from June 20 to July 20.',
        'Universidade do Porto': 'High school diploma (12 years), certificates of additional programs (International Foundation), documents confirming the completion of 1-2 courses. '
                                 'Proficiency in Portuguese - B2 according to CEFRL. '
                                 'Compliance with the prerequisites (physical, functional or professional conditions) established for the study cycle they intend to take.',
        'Universidade do Algarve': 'Enrollment to study at the university is based on the previously provided results of the exams passed. '
                                   'Each academic year is traditionally divided into semesters.'}
    costs = {'Polytechnic Institute': 3200,
             'University of Lisbon': 1900,
             'Universidade do Porto': 3500,
             'Universidade do Algarve': 3460}

    sights = {'Obidos Castle': ["A true favorite among the medieval castles of Portugal can be considered the castle of Obidos, located on a hill, "
                                "offering a wonderful view of the surroundings of the city of the same name: vineyards, windmills, bright terracotta roofs of the surrounding houses. "
                                "The castle itself attracts many tourists with its battlements, preserved from the Middle Ages to the present day in surprisingly good condition. "
                                "In the form in which we see the castle now, it was built in the 13th century, and before that, in the era of the Roman Empire, "
                                "there were public baths and a square, which played the role of the center of the political life of the settlement. "
                                "After the fall of the Roman Empire, with the coming to power of the Visigoths, a fortress was built on this site, around which a settlement was formed - the future city of Obidos. "
                                "In the 8th century, the fortress passed into the possession of the Muslims, and only in the 13th century did the Portuguese king Afonso recapture this building. "
                                "Today, this landmark of Portugal has retained its appearance, which is why it attracts many tourists - you can walk around the castle grounds, "
                                "study its architecture - arched passages, medieval bas-reliefs, as well as view magnificent views of the surroundings from a height.",
                                'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0d/6e/7b/06/castelo-de-obidos.jpg?w=1200&h=-1&s=1'],
              'Pena Palace': ["Sintra is a suburb of the Portuguese capital, the most important in terms of attractions in Portugal. "
                              "Not far from Sintra, in the mountains, there is an unusual castle-palace of Pena. "
                              "Its uniqueness lies in the fact that initially an empty monastery was taken as its basis, which was erected here back in the distant 12th century in honor of the Mother of God. "
                              "Over time, the temple fell into disrepair. "
                              "The inconspicuous and abandoned chapel, lost in the mountains, was remembered only in the 16th century, when King Manuel I, "
                              "being very religious, turned his gaze to this temple and to the rather vast empty lands around it. "
                              "From that moment, the reconstruction of the sanctuary began - it was rebuilt from stone and stood for about 2 more centuries, "
                              "until a powerful earthquake known throughout Europe happened, which turned the monastery into ruins. "
                              "And only in 1838, King Fernando II buys the land along with the ruins of the temple and the picturesque adjacent territories on the mountain. "
                              "He orders to rebuild a palace on these lands, which later became the summer residence of the royal family. "
                              "Romantic Fernando made a significant contribution to the design of the castle and its surrounding areas. "
                              "As a result, a beautiful and majestic building has grown on these lands with an exotic exterior, representing a mixture of several styles, "
                              "bright facades and an amazing park, with its winding paths, cozy gazebos and rich colors of outlandish plants.",
                              'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2017/06/Portugal-3-The-Pena-Palace-e1497061654426.jpg'],
              'Alto Douro': ["The Alto Douro region has long been known for producing wine of exceptional taste and quality for over 2,000 years. "
                             "Local climatic conditions have such weather features that allow you to collect generous harvests of grapes of various varieties. "
                             "The area is distinguished by a rather steep soil relief, from different sides it is protected from winds and moisture by the mountains of Montemuro and Maran, "
                             "which creates a dry and hot climate here, which is most favorable for the ripening of grapes and for obtaining fragrant fortified wines. "
                             "The wine produced here takes first place in international competitions, and this once again confirms the quality of local products. "
                             "Traveling through the wine attractions of Portugal, in one of the local farms you can have a tasting of drinks, buy delicious wine or port wine. "
                             "If you wish, you can take part in the harvest and the subsequent wine festival, feel the taste of life in this beautiful and fertile land.",
                             'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2017/06/Portugal-5-Alto-Douro-e1497062089463.jpg']}
    beaches = {'Praia da Marina beach': ["The beach is distinguished not only by its exquisite beauty, "
                                         "but also by the steepness of the coastline, therefore, to get to the water, you have to go down a long and steep staircase, but it's worth it. "
                                         "Below you will see the coast from a new angle - many islands-rocks, which have bizarre shapes due to prolonged exposure to water and wind, "
                                         "in an ensemble with the sea create an amazingly beautiful landscape. "
                                         "On the beach, you can not only swim or soak up the sun - outdoor enthusiasts can explore the local bays, caves and grottoes. "
                                         "Despite the wild scenery, the beach itself is landscaped - there is parking, a restaurant, rental of swimming equipment, lifeguards work. "
                                         "There is also the opportunity to snorkel and explore the rich underwater world - it may not be as rich as in the Red Sea, but all kinds of shrimp, "
                                         "colorful fish and starfish are present here in abundance.",
                                         'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2017/06/Portugal-11-Praia-da-Marinha-e1497064402881.jpg'],
               "Praia de Sao Rafael": ["San Rafael is beautiful, like all the beaches in the south of Portugal. "
                                       "It is surrounded by several limestone cliffs with unique water caves. "
                                       "Here, the purest water and soft sand, however, during low tide and strong surf, "
                                       "it is very difficult to enter the water - immediately behind the sandy strip, the bottom is lined with stones. "
                                       "You need to go down the stairs to the beach, although the descent is not big. "
                                       "The infrastructure of de Sao Rafael is quite well developed: there are many public showers, there are shops, there is an excellent restaurant serving fresh seafood. "
                                       "There is a large free car park nearby. But there are no places to rent sunbeds.",
                                       'https://kuku.travel/wp-content/uploads/2018/04/%D0%9F%D0%BB%D1%8F%D0%B6-Praia-de-Sao-Rafael.jpg'],
               'Praia da Coelha': ["5 km east of Albufeira there is a small Coelha beach with a sand strip of 70-80 m long, completely protected from the winds by high cliffs. "
                                   "Like many beaches around Albufeira, it has been awarded the Blue Flag. "
                                   "Clean and gentle entry into the water makes this beach attractive for a relaxing holiday with kids, and many adults will enjoy snorkeling among the coastal cliffs. "
                                   "In summer, the water warms up to an average of + 20-23 ºC.",
                                   'https://kuku.travel/wp-content/uploads/2018/04/%D0%A4%D0%BE%D1%82%D0%BE-%D0%BF%D0%BB%D1%8F%D0%B6%D0%B0-Praia-da-Coelha.jpg']}
    mountains = {'Pico': ["Pico is a dormant active stratovolcano located on the Mid-Atlantic Ridge and is the highest point of the ridge, Pico Island and Portugal.",
                          'https://upload.wikimedia.org/wikipedia/commons/f/fd/Picocanal.jpg'],
                 'Pico do Arieiro': ["Pico do Arieiro is the third highest mountain on the island of Madeira, "
                                     "the main island of the archipelago of the same name in the Atlantic Ocean, after Pico Ruivo and Pico das Torres. "
                                     "It is a good vantage point for viewing the surrounding landscapes, "
                                     "as well as one of the options for the starting point of the PR1 Vereda do Areeiro hiking route.",
                                     'https://upload.tury.club/data/41f045bafea2d2b40352c725132f5394/9A3PBhFx/GwcyrlD8.jpg'],
                 'Pico Ruivo': ['Pico Ruivo is the highest mountain in Madeira, the main island of the Madeira archipelago in the Atlantic Ocean. '
                                'The height of the mountain is 1862 meters. It is also the third highest peak in Portugal.',
                                'https://fs.tonkosti.ru/9g/z6/9gz6f3rpujoksckogkgks4wsc.jpg']}
    skiResorts = {}
    lakes = {'Lagoa do Fogo': ["This lake is situated on Sao Miguel island, Azores. It is the second largest lake on the island. In 1974 it was declared a natural reserve. "
                               "It covers an area of 13.6 km², located at an altitude of 947 m above sea level, "
                               "located on the cauldron of an extinct volcano, which formed about 15,000 years ago",
                               'https://s9.travelask.ru/uploads/hint_place/000/115/653/image/aa2b00ee315d4f6aed788503f3c9c91f.jpg'],
             'Pateira de Fermentelos': ["This is the largest natural lake in the entire Iberian Peninsula, which is known as a habitat for a variety of flora and fauna. "
                                        "It is fed by two rivers, the Settima and the Agueda, which converge at the lake. "
                                        "Pateira de Fermentelos offers its guests excellent fishing, canoeing, boating and sailing. "
                                        "In the nearest city, Aveiro, tourists will find many options for accommodation.",
                                        'https://womanadvice.ru/sites/default/files/49/2018-03-03_1703/pateyra_de_fermentelos.jpg'],
             'Lake Obidos': ['In this unique location, located in the Obidos and Caldas da Reina regions of Portugal, the lake is bordered by a sea lagoon. '
                             'As well as relaxing on stunning beaches, you can enjoy shellfishing, boating, sailing, windsurfing and canoeing. '
                             'In the nearby town of Obidos, tourists will find several small guesthouses and hotels, authentic Portuguese cuisine and an impressive medieval fortress.',
                             'https://womanadvice.ru/sites/default/files/49/2018-03-03_1703/ozero_obidush.jpg']}
    rivers = {'Minho': ["Length - 340 km, basin area - 22.5 thousand km². "
                        "The sources of Minho are in the Cantabrian Mountains in the Meira region of the province of Lugo, then the river flows through the hilly terrain of the autonomous community of Galicia. "
                        "After the confluence of the main tributary, the Sil River, the valley becomes wider. "
                        "The last 80 km before it flows into the Atlantic Ocean, Minho is the border between Spain and Portugal.",
                        'https://img.freepik.com/premium-photo/panoramic-view-of-cerveira-and-the-river-minho-on-the-border-between-portugal-and-spain_462054-914.jpg'],
              'Tacho': ["Tajo flows in Spain through the autonomous communities of Aragon, Castile-La Mancha, Madrid and Extremadura, "
                        "then a small section of the river runs along the border of Spain and Portugal. "
                        "A river flows through the territory of Portugal under the name Tagus. "
                        "To the southeast of Lisbon, the river is crossed by the Vasco da Gama Bridge, 17.2 km long. "
                        "The river flows into the bay of Mar da Paglia, which is sometimes considered its estuary. "
                        "The double name of the river, as a rule, is reflected on geographical maps. "
                        "On the territory of Spain, the river is called Tajo, and in Portugal the name changes to Tejo: "
                        "there is an analogy for the change of names in the Western Dvina in the territories of Russia and Belarus, "
                        "which in the territory of Latvia changes its name to the Daugava, as well as the Neman in Belarus, "
                        "which is in the territory of Lithuania called Nemunas.",
                        'https://thumbs.dreamstime.com/b/%D1%80%D0%B5%D0%BA%D0%B0-%D1%82%D0%B0%D1%85%D0%BE-35824273.jpg']}
    # currency
    currencyName = 'EUR'
    currencyEqualsToDollar = 0.95

    # military
    milPolBlock = "NATO"
    amountOfPeopleInArmy = 27250

    # healthcare
    numberOfDoctorsPer100kPopulation = 443
    menAverageLifeExpectancy = 75.3
    womenAverageLifeExpectancy = 82

    # climat
    juneAverageTemperature = 22
    decemberAverageTemperature = 16
    averageHumidity = 71
    averageDurationOfWinter = 3
    averageRainfallPerMonth = 68
    averageNumberOfFoggyDaysPerYear = 26
    averageNumberOfRainyDaysPerYear = 112
    averageNumberOfClearDays = 184

    # security
    situationInTheCountry = 3  # [1, 3] 1-bad, 3-good
    freedomOfSpeech = 3  # [1, 3]
    assessmentOfFamilyLife = 2  # [1, 3]
    attitudeTowardsLGBT = 3  # [1, 3]

    # population
    populationCount = 47330000
    procentOfMales = 49.4
    procentOfFemales = 50.6
    populationDensityPerSquareKilometer = 92.1
    speedOfLife = 3  # [1, 3]
    workPlaces = 3  # [1, 3]
    nightLifeEntertainment = 3  # [1, 3]

    # citizenship
    citizenshipGlobalRank = 3
    friendlyToForeigners = 1

    # communication
    communicationOnEnglish = 3  # [1, 3]

    # transport
    averageTravelTimeToWork = 29.56
    developmentLevelOfPublicTransport = 3  # [1, 3]

    # internet
    speedOfInternetMbps = 28  # Мегабиты в секунду
    freeWifi = 2  # [1, 3]

    # education
    rankingOfNationalEducationSystem = 25

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
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers, friendlyToForeigners
                  )

    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()
    #############################   Portugal   #############################
    cc.createBorders()
    cc.close()
