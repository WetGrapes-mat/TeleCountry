from neo4j import GraphDatabase


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
                   # crime thing
                   levelOfCrime, crimeIncreasingInThePast3Years, worriesHomeBrokenAndThingsStolen,
                   worriesBeingMuggedOrRobbed,
                   worriesCarStolen, worriesThingsFromCarStolen,
                   worriesAttacked, worriesBeingInsulted,
                   worriesAttackBecauseOfYourSkinColorEtc, problemPeopleUsingOrDealingDrugs,
                   problemPropertyCrimes, problemViolentCrimes,
                   problemCorruptionAndBribery,
                   safetyWalkingAloneDuringNight, safetyWalkingAloneDuringDay,
                   # healthcare
                   numberOfDoctorsPer100kPopulation, levelOfModernityOfMedicalEquipment,
                   levelOfEducationOfMedicalStaff, responsivenessLevel,
                   levelOfCompetenceOfMedicalStaff, levelOfLocationOfMedicalInstitutions,
                   costOfMedicine, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                   # climat
                   airQualityLevel, drinkingWaterQualityLevel, garbageCollectionLevel,
                   streetCleanlinessLevel, levelOfLightAndNoisePollution, waterPollution,
                   satisfactionWithGarbageDisposal, comfortableTimeInTheCity, qualityOfParksAndGreenSpaces,
                   juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                   averageDurationOfWinter, averageRainfallPerMonth, averageNumberOfFoggyDaysPerYear,
                   averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,
                   # security
                   situationInTheCountry, freedomOfSpeech,
                   assessmentOfFamilyLife, attitudeTowardsLGBT,
                   # population
                   populationCount, procentOfMalesAndFemales, populationDensityPerSquareKilometer,
                   speedOfLife, workPlaces, nightLifeEntertainment,
                   # citizenship
                   visa_free_entry, citizenshipGlobalRank, friendlyToForeigners,
                   # communication
                   communicationOnEnglish,
                   # transport
                   averageTravelTimeToWork, developmentLevelOfPublicTransport,
                   # internet
                   speedOfInternetMbps, freeWifi,
                   # economic situation
                   averageSalaryAfterTaxes,
                   # Price of life per month
                   familyPriceOfLife, personPriceOfLife,
                   # Cafe and restaurant prices
                   priceOfFoodInAnInexpensiveRestaurant,
                   priceOfFoodInAMidRangeRestaurant,
                   priceOfFastFood, priceOfCoffee,
                   # Supermarket prices
                   priceOfMilk1Litre, priceOfBreadHalfOf1kg, priceOfRice1kg,
                   priceOfEggs12pcs, priceOfCheese1kg, priceOfChicken1kg,
                   priceOfBeef1kg, priceOfApples1kg, priceOfBanana1kg,
                   priceOfOrange1kg, priceOfTomato1kg, priceOfPotatoes1kg,
                   priceOfOnion1kg, priceOfLettuceHead, priceOfWaterOneAndAHalfLitre,
                   # transport prices
                   monthlyTravelByPublicTransport, taxiPricePer1km, gas1Litre,
                   # Utility prices
                   basicUtilitiesPrice, theInternetPrice,
                   # Prices for entertainment and recreation
                   fitnessClubPrice, movieTicketPrice,
                   # child care costs
                   privateKindergartenPrice, schoolPrice,
                   # Prices for clothes/shoes
                   aPairOfJeansPrice, dressPrice,
                   sneakersPrice, shoesPrice
                   ):
        with self.driver.session() as session:
            base = session.execute_write(self._createBase, countryName,
                                         citiesDict, languageName,
                                         # currency
                                         currencyName, currencyEqualsToDollar,
                                         # military
                                         milPolBlock, amountOfPeopleInArmy,
                                         # crime thing
                                         levelOfCrime, crimeIncreasingInThePast3Years, worriesHomeBrokenAndThingsStolen,
                                         worriesBeingMuggedOrRobbed,
                                         worriesCarStolen, worriesThingsFromCarStolen,
                                         worriesAttacked, worriesBeingInsulted,
                                         worriesAttackBecauseOfYourSkinColorEtc, problemPeopleUsingOrDealingDrugs,
                                         problemPropertyCrimes, problemViolentCrimes,
                                         problemCorruptionAndBribery,
                                         safetyWalkingAloneDuringNight, safetyWalkingAloneDuringDay,
                                         # healthcare
                                         numberOfDoctorsPer100kPopulation, levelOfModernityOfMedicalEquipment,
                                         levelOfEducationOfMedicalStaff, responsivenessLevel,
                                         levelOfCompetenceOfMedicalStaff, levelOfLocationOfMedicalInstitutions,
                                         costOfMedicine, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                                         # climat
                                         airQualityLevel, drinkingWaterQualityLevel, garbageCollectionLevel,
                                         streetCleanlinessLevel, levelOfLightAndNoisePollution, waterPollution,
                                         satisfactionWithGarbageDisposal, comfortableTimeInTheCity,
                                         qualityOfParksAndGreenSpaces,
                                         juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                                         averageDurationOfWinter, averageRainfallPerMonth,
                                         averageNumberOfFoggyDaysPerYear,
                                         averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,
                                         # security
                                         situationInTheCountry, freedomOfSpeech,
                                         assessmentOfFamilyLife, attitudeTowardsLGBT,
                                         # population
                                         populationCount, procentOfMalesAndFemales, populationDensityPerSquareKilometer,
                                         speedOfLife, workPlaces, nightLifeEntertainment,
                                         # citizenship
                                         visa_free_entry, citizenshipGlobalRank, friendlyToForeigners,
                                         # communication
                                         communicationOnEnglish,
                                         # transport
                                         averageTravelTimeToWork, developmentLevelOfPublicTransport,
                                         # internet
                                         speedOfInternetMbps, freeWifi,
                                         # economic situation
                                         averageSalaryAfterTaxes,
                                         # Price of life per month
                                         familyPriceOfLife, personPriceOfLife,
                                         # Cafe and restaurant prices
                                         priceOfFoodInAnInexpensiveRestaurant,
                                         priceOfFoodInAMidRangeRestaurant,
                                         priceOfFastFood, priceOfCoffee,
                                         # Supermarket prices
                                         priceOfMilk1Litre, priceOfBreadHalfOf1kg, priceOfRice1kg,
                                         priceOfEggs12pcs, priceOfCheese1kg, priceOfChicken1kg,
                                         priceOfBeef1kg, priceOfApples1kg, priceOfBanana1kg,
                                         priceOfOrange1kg, priceOfTomato1kg, priceOfPotatoes1kg,
                                         priceOfOnion1kg, priceOfLettuceHead, priceOfWaterOneAndAHalfLitre,
                                         # transport prices
                                         monthlyTravelByPublicTransport, taxiPricePer1km, gas1Litre,
                                         # Utility prices
                                         basicUtilitiesPrice, theInternetPrice,
                                         # Prices for entertainment and recreation
                                         fitnessClubPrice, movieTicketPrice,
                                         # child care costs
                                         privateKindergartenPrice, schoolPrice,
                                         # Prices for clothes/shoes
                                         aPairOfJeansPrice, dressPrice,
                                         sneakersPrice, shoesPrice
                                         )
            return base

    @staticmethod
    def _createBase(tx, countryName,
                    citiesDict, languageName,

                    # currency
                    currencyName, currencyEqualsToDollar,

                    # military
                    milPolBlock, amountOfPeopleInArmy,

                    # crime thing
                    levelOfCrime, crimeIncreasingInThePast3Years, worriesHomeBrokenAndThingsStolen, worriesBeingMuggedOrRobbed,
                    worriesCarStolen, worriesThingsFromCarStolen,
                    worriesAttacked, worriesBeingInsulted,
                    worriesAttackBecauseOfYourSkinColorEtc, problemPeopleUsingOrDealingDrugs,
                    problemPropertyCrimes, problemViolentCrimes,
                    problemCorruptionAndBribery,
                    safetyWalkingAloneDuringNight, safetyWalkingAloneDuringDay,

                    # healthcare
                    numberOfDoctorsPer100kPopulation, levelOfModernityOfMedicalEquipment,
                    levelOfEducationOfMedicalStaff, responsivenessLevel,
                    levelOfCompetenceOfMedicalStaff, levelOfLocationOfMedicalInstitutions,
                    costOfMedicine, menAverageLifeExpectancy, womenAverageLifeExpectancy,

                    # climat
                    airQualityLevel, drinkingWaterQualityLevel, garbageCollectionLevel,
                    streetCleanlinessLevel, levelOfLightAndNoisePollution, waterPollution,
                    satisfactionWithGarbageDisposal, comfortableTimeInTheCity, qualityOfParksAndGreenSpaces,
                    juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                    averageDurationOfWinter, averageRainfallPerMonth, averageNumberOfFoggyDaysPerYear,
                    averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,

                    # security
                    situationInTheCountry, freedomOfSpeech,
                    assessmentOfFamilyLife, attitudeTowardsLGBT,

                    #population
                    populationCount, procentOfMalesAndFemales, populationDensityPerSquareKilometer,
                    speedOfLife, workPlaces, nightLifeEntertainment,

                    # citizenship
                    visa_free_entry, citizenshipGlobalRank, friendlyToForeigners,

                    # communication
                    communicationOnEnglish,

                    # transport
                    averageTravelTimeToWork, developmentLevelOfPublicTransport,

                    # internet
                    speedOfInternetMbps, freeWifi,

                    # economic situation
                    averageSalaryAfterTaxes,
                    # Price of life per month
                    familyPriceOfLife, personPriceOfLife,
                    # Cafe and restaurant prices
                    priceOfFoodInAnInexpensiveRestaurant,
                    priceOfFoodInAMidRangeRestaurant,
                    priceOfFastFood, priceOfCoffee,
                    # Supermarket prices
                    priceOfMilk1Litre, priceOfBreadHalfOf1kg, priceOfRice1kg,
                    priceOfEggs12pcs, priceOfCheese1kg, priceOfChicken1kg,
                    priceOfBeef1kg, priceOfApples1kg, priceOfBanana1kg,
                    priceOfOrange1kg, priceOfTomato1kg, priceOfPotatoes1kg,
                    priceOfOnion1kg, priceOfLettuceHead, priceOfWaterOneAndAHalfLitre,
                    # transport prices
                    monthlyTravelByPublicTransport, taxiPricePer1km, gas1Litre,
                    # Utility prices
                    basicUtilitiesPrice, theInternetPrice,
                    # Prices for entertainment and recreation
                    fitnessClubPrice, movieTicketPrice,
                    # child care costs
                    privateKindergartenPrice, schoolPrice,
                    # Prices for clothes/shoes
                    aPairOfJeansPrice, dressPrice,
                    sneakersPrice, shoesPrice
                    ):
        # country
        resultStr = 'create (country:Country {name:"%s"})' % (str(countryName))
        # cities
        index = 1
        for city in citiesDict:
            resultStr += 'create (city%s:City {name:"%s", isBig:"%s"})' % (str(index), city, str(citiesDict[city]))
            resultStr += 'create (country)-[:has_city]->(city%s)' % (str(index))
            index += 1
        # language
        resultStr += 'create (language:Language {name:"%s"})' % (str(languageName))
        resultStr += 'create (country)-[:official_language]->(language)'
        # currency
        resultStr += 'create (currency:Currency {name:"%s", oneDollarEquals:%f})' % (str(currencyName), currencyEqualsToDollar)
        resultStr += 'create (country)-[:currency]->(currency)'
        # military political block
        resultStr += 'create (militaryPoliticalBlock:MilitaryPoliticalBlock {name:"%s"})' % (str(milPolBlock))
        resultStr += 'create (country)-[:belongs_to_military_political_block]->(militaryPoliticalBlock)'
        # military Power
        resultStr += 'create (militaryPower:MilitaryPower {amountOfPeople:"%d"})' % amountOfPeopleInArmy
        resultStr += 'create (country)-[:military_power]->(militaryPower)'
        # crime thing
        resultStr += 'create (crimeThing:CrimeThing {levelOfCrime:"%d",' \
                     '                               crimeIncreasingInThePast3Years:"%d",' \
                     '                               worriesHomeBrokenAndThingsStolen:"%d",' \
                     '                               worriesBeingMuggedOrRobbed:"%d",' \
                     '                               worriesCarStolen:"%d",' \
                     '                               worriesThingsFromCarStolen:"%d",' \
                     '                               worriesAttacked:"%d",' \
                     '                               worriesBeingInsulted:"%d",' \
                     '                               worriesAttackBecauseOfYourSkinColorEtc:"%d",' \
                     '                               problemPeopleUsingOrDealingDrugs:"%d",' \
                     '                               problemPropertyCrimes:"%d",' \
                     '                               problemViolentCrimes:"%d",' \
                     '                               problemCorruptionAndBribery:"%d",' \
                     '                               safetyWalkingAloneDuringNight:"%d",' \
                     '                               safetyWalkingAloneDuringDay:"%d"})' % (levelOfCrime, crimeIncreasingInThePast3Years, worriesHomeBrokenAndThingsStolen, worriesBeingMuggedOrRobbed,
                                                                                            worriesCarStolen, worriesThingsFromCarStolen,
                                                                                            worriesAttacked, worriesBeingInsulted,
                                                                                            worriesAttackBecauseOfYourSkinColorEtc, problemPeopleUsingOrDealingDrugs,
                                                                                            problemPropertyCrimes, problemViolentCrimes,
                                                                                            problemCorruptionAndBribery,
                                                                                            safetyWalkingAloneDuringNight, safetyWalkingAloneDuringDay)
        resultStr += 'create (country)-[:crime_thing]->(crimeThing)'
        # healthcare
        resultStr += 'create (healthcare:Healthcare {numberOfDoctorsPer100kPopulation:"%d",' \
                     '                    levelOfModernityOfMedicalEquipment:"%d",' \
                     '                    levelOfEducationOfMedicalStaff:"%d",' \
                     '                    responsivenessLevel:"%d",' \
                     '                    levelOfCompetenceOfMedicalStaff:"%d",' \
                     '                    levelOfLocationOfMedicalInstitutions:"%d",' \
                     '                    costOfMedicine:"%d",' \
                     '                    menAverageLifeExpectancy:"%d",' \
                     '                    womenAverageLifeExpectancy:"%d"})' % (numberOfDoctorsPer100kPopulation, levelOfModernityOfMedicalEquipment,
                                                                                levelOfEducationOfMedicalStaff, responsivenessLevel,
                                                                                levelOfCompetenceOfMedicalStaff, levelOfLocationOfMedicalInstitutions,
                                                                                costOfMedicine, menAverageLifeExpectancy, womenAverageLifeExpectancy)
        resultStr += 'create (country)-[:healthcare]->(healthcare)'
        # climat
        resultStr += 'create (climat:Climat {airQualityLevel:"%d",' \
                     '                    drinkingWaterQualityLevel:"%d",' \
                     '                    garbageCollectionLevel:"%d",' \
                     '                    streetCleanlinessLevel:"%d",' \
                     '                    levelOfLightAndNoisePollution:"%d",' \
                     '                    waterPollution:"%d",' \
                     '                    satisfactionWithGarbageDisposal:"%d",' \
                     '                    comfortableTimeInTheCity:"%d",' \
                     '                    qualityOfParksAndGreenSpaces:"%d",' \
                     '                    juneAverageTemperature:"%f °C" ,' \
                     '                    decemberAverageTemperature:"%f °C" ,' \
                     '                    averageHumidity:"%f" ,' \
                     '                    averageDurationOfWinter:"%f month" ,' \
                     '                    averageRainfallPerMonth:"%d",' \
                     '                    averageNumberOfFoggyDaysPerYear:"%d",' \
                     '                    averageNumberOfRainyDaysPerYear:"%d",' \
                     '                    averageNumberOfClearDays:"%d"})' % (airQualityLevel, drinkingWaterQualityLevel, garbageCollectionLevel,
                                                                              streetCleanlinessLevel, levelOfLightAndNoisePollution, waterPollution,
                                                                              satisfactionWithGarbageDisposal, comfortableTimeInTheCity, qualityOfParksAndGreenSpaces,
                                                                              juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                                                                              averageDurationOfWinter, averageRainfallPerMonth, averageNumberOfFoggyDaysPerYear,
                                                                              averageNumberOfRainyDaysPerYear, averageNumberOfClearDays)
        resultStr += 'create (country)-[:climat]->(climat)'

        # MMD is individual func

        # security
        resultStr += 'create (security:Security {situationInTheCountry:"%d",' \
                     '                    freedomOfSpeech:"%d",' \
                     '                    assessmentOfFamilyLife:"%d",' \
                     '                    attitudeTowardsLGBT:"%d"})' % (situationInTheCountry, freedomOfSpeech,
                                                                         assessmentOfFamilyLife, attitudeTowardsLGBT)
        resultStr += 'create (country)-[:security]->(security)'

        # population
        resultStr += 'create (population:Population {count:"%d",' \
                     '                               procentOfMalesAndFemales:"%d",' \
                     '                               populationDensityPerSquareKilometer:"%d",' \
                     '                               speedOfLife:"%d",' \
                     '                               workPlaces:"%d",' \
                     '                               nightLifeEntertainment:"%d"})' % (populationCount, procentOfMalesAndFemales, populationDensityPerSquareKilometer,
                                                                                       speedOfLife, workPlaces, nightLifeEntertainment)
        resultStr += 'create (country)-[:climat]->(climat)'

        # citizenship
        resultStr += 'create (citizenship:Citizenship {globalRank:"%d",' \
                     '                                 friendlyToForeigners:"%d"})' % (citizenshipGlobalRank, friendlyToForeigners)

        resultStr += 'create (country)-[:citizenship]->(citizenship)'
        if visa_free_entry:
            resultStr += 'create (citizenship)-[:visa_free_entry]->(country)'
        else:
            resultStr += 'create (citizenship)-[:visa_entry]->(country)'

        # communication
        resultStr += 'create (communication:Communication {communicationOnEnglish:"%d"})' % (communicationOnEnglish)

        resultStr += 'create (country)-[:communication]->(communication)'

        # transport
        resultStr += 'create (transport:Transport {averageTravelTimeToWork:"%d",' \
                     '                             developmentLevelOfPublicTransport:"%d"})' % (averageTravelTimeToWork, developmentLevelOfPublicTransport)

        resultStr += 'create (country)-[:transport]->(transport)'

        # internet
        resultStr += 'create (internet:Internet {speedOfInternetMbps:"%d",' \
                     '                           freeWifi:"%d"})' % (speedOfInternetMbps, freeWifi)

        resultStr += 'create (country)-[:internet]->(internet)'

        # economic situation
        resultStr += 'create (economicSituation:EconomicSituation {averageSalaryAfterTaxes:"%d"})' % (averageSalaryAfterTaxes)
        resultStr += 'create (country)-[:economicSituation]->(economicSituation)'
        # Price of life per month
        resultStr += 'create (priceOfLifePerMonth:PriceOfLifePerMonth {family:"%d", person:"%d"})' % (familyPriceOfLife, personPriceOfLife)
        resultStr += 'create (economicSituation)-[:price_of_life_per_month]->(priceOfLifePerMonth)'
        # Cafe and restaurant prices
        resultStr += 'create (cafeAndRestaurantPrices:CafeAndRestaurantPrices {priceOfFoodInAnInexpensiveRestaurant:"%d",' \
                     '                                                         priceOfFoodInAMidRangeRestaurant:"%d",' \
                     '                                                         priceOfFastFood:"%d",' \
                     '                                                         priceOfCoffee:"%d"})' % (priceOfFoodInAnInexpensiveRestaurant,
                                                                                                        priceOfFoodInAMidRangeRestaurant,
                                                                                                        priceOfFastFood, priceOfCoffee)
        resultStr += 'create (economicSituation)-[:cafe_and_restaurant_prices]->(cafeAndRestaurantPrices)'
        # Supermarket prices
        resultStr += 'create (supermarketPrices:SupermarketPrices {priceOfMilk1Litre:"%d",' \
                     '                                             priceOfBreadHalfOf1kg:"%d",' \
                     '                                             priceOfRice1kg:"%d",' \
                     '                                             priceOfEggs12pcs:"%d",' \
                     '                                             priceOfCheese1kg:"%d",' \
                     '                                             priceOfChicken1kg:"%d",' \
                     '                                             priceOfBeef1kg:"%d",' \
                     '                                             priceOfApples1kg:"%d",' \
                     '                                             priceOfBanana1kg:"%d",' \
                     '                                             priceOfOrange1kg:"%d",' \
                     '                                             priceOfTomato1kg:"%d",' \
                     '                                             priceOfPotatoes1kg:"%d",' \
                     '                                             priceOfOnion1kg:"%d",' \
                     '                                             priceOfLettuceHead:"%d",' \
                     '                                             priceOfWaterOneAndAHalfLitre:"%d",})' % (priceOfMilk1Litre, priceOfBreadHalfOf1kg, priceOfRice1kg,
                                                                                                            priceOfEggs12pcs, priceOfCheese1kg, priceOfChicken1kg,
                                                                                                            priceOfBeef1kg, priceOfApples1kg, priceOfBanana1kg,
                                                                                                            priceOfOrange1kg, priceOfTomato1kg, priceOfPotatoes1kg,
                                                                                                            priceOfOnion1kg, priceOfLettuceHead, priceOfWaterOneAndAHalfLitre)
        resultStr += 'create (economicSituation)-[:supermarket_prices]->(supermarketPrices)'
        # transport prices
        resultStr += 'create (transportPrices:TransportPrices {monthlyTravelByPublicTransport:"%d",' \
                     '                                         taxiPricePer1km:"%d",' \
                     '                                         gas1Litre:"%d"})' % (monthlyTravelByPublicTransport, taxiPricePer1km, gas1Litre)
        resultStr += 'create (economicSituation)-[:transport_prices]->(transportPrices)'
        # Utility prices
        resultStr += 'create (utilityPrices:UtilityPrices {basicUtilities:"%d",' \
                     '                                     theInternet:"%d"})' % (basicUtilitiesPrice, theInternetPrice)
        resultStr += 'create (economicSituation)-[:utility_prices]->(utilityPrices)'
        # Prices for entertainment and recreation
        resultStr += 'create (pricesForEntertainmentAndRecreation:PricesForEntertainmentAndRecreation {fitnessClub:"%d",' \
                     '                                                                                 movieTicket:"%d"})' % (fitnessClubPrice,
                                                                                                                              movieTicketPrice)
        resultStr += 'create (economicSituation)-[:prices_for_entertainment_and_recreation]->(pricesForEntertainmentAndRecreation)'
        # child care costs
        resultStr += 'create (childCareCosts:ChildCareCosts {privateKindergarten:"%d",' \
                     '                                       school:"%d"})' % (privateKindergartenPrice, schoolPrice)
        resultStr += 'create (economicSituation)-[:child_care_costs]->(childCareCosts)'
        # Prices for clothes/shoes
        resultStr += 'create (pricesForClothesAndShoes:PricesForClothesAndShoes {aPairOfJeans:"%d",' \
                     '                                                           dress:"%d",' \
                     '                                                           sneakers:"%d",' \
                     '                                                           shoes:"%d"})' % (aPairOfJeansPrice, dressPrice,
                                                                                                  sneakersPrice, shoesPrice)
        resultStr += 'create (economicSituation)-[:prices_for_clothes_and_shoes]->(pricesForClothesAndShoes)'

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
        resultStr += 'match (country)->[:climat]->(climat)'
        resultStr += 'create (manMadeDisaster:ManMadeDisaster {name:"%s", typeOfMMD:"%s", aomuntOfDeadPeople:"%d",' \
                     '                                         aomuntOfInjuredPeople:"%d", territoryOfPollution:"%d km^2"})' % (nameOfDisaster, typeOfMMD, aomuntOfDeadPeople,
                                                                                                                                aomuntOfInjuredPeople, territoryOfPollution)

        resultStr += 'create (climat)-[:man_made_disaster]->(manMadeDisaster)'

        result = tx.run(resultStr)




    def createEducation(self, countryName, citiesDict, rankingOfNationalEducationSystem):
        with self.driver.session() as session:
            education = session.execute_write(self._createEducation, countryName, citiesDict,
                                              rankingOfNationalEducationSystem)
            return education

    @staticmethod
    def _createEducation(tx, countryName, cities, rankingOfNationalEducationSystem):
        index = 1
        request = '''match (country:Country {name:"%s"})
         create (education:Education {rankingOfNationalEducationSystem:%d})
         create (country)-[:education]->(education)''' % (countryName, rankingOfNationalEducationSystem)
        for city in universities:
            for university in universities[city]:
                request += '''match (city%s:City {name:"%s"})
                              create (univ%s:University {name:})
                              create (country)-[:education]->(education)''' % (str(index), city, str(index))
                index += 1
        result = tx.run(request)


if __name__ == "__main__":
    cc = CountryCreator()

    # Country
    countryName = "Беларусь"
    officialLanguage = "Русский"

    # cities    name   isBig
    cities = {'Минск': True, 'Брест': True, 'Витебск': True, 'Гродно': True, 'Гомель': True}

    # education
    universities = {'Минск': ['Белорусский государственный университет информатики и радиоэлектроники',
                              'Белорусский государственный университет'],
                    'Брест': ['Брестский государственный технический университет',
                              'Брестский государственный университет имени А.С. Пушкина'],
                    'Витебск': ['Витебский государственный университет имени П.М. Машерова',
                                'Витебский государственный технологический университет'],
                    'Гродно': ['Гродненский государственный медицинский университет',
                               'Гродненский государственный университет имени Янки Купалы'],
                    'Гомель': ['Гомельский государственный медицинский университет',
                               'Гомельский государственный технический университет имени П.О.Сухого']}
    bsuirFaculties = {
        'Факультет компьютерного проектирования': ['Информационные системы и технологии (в обеспечении промышленной безопасности)',
                                                   'Медицинская электроника',
                                                   'Программируемые мобильные системы',
                                                   'Электронные системы безопасности'],
        'Факультет информационных технологий и управления': ['Автоматизированные системы обработки информации',
                                                             'Информационные технологии и управление в технических системах',
                                                             'Искусственный интеллект', 'Промышленная электроника',
                                                             'Информационные системы и технологии (в игровой индустрии)'],
        'Факультет компьютерных систем и сетей': ['Вычислительные машины, системы и сети',
                                                  'Информатика и технологии программирования',
                                                  'Программное обеспечение информационных технологий',
                                                  'Электронные вычислительные средства'],
        'Инженерно-экономический факультет': ['Информационные системы и технологии (в логистике)', 'Электронный маркетинг',
                                              'Информационные системы и технологии (в экономике)', 'Экономика электронного бизнеса', ]}
    bsuirPrograms = ['Балаклавриат', 'Магистратура', 'Аспирантура']
    bsuirCost = ''
    bsuFaculties = {
        'Факультет международных отношений': ['Международные отношения', 'Международное право', 'Менеджмент', 'Мировая экономика'],
        'Биологический факультет': ['Биология', 'Микробиология', 'Биохимия', 'Биоэкология'],
        'Факультет прикладной математики и информатики': ['Информатика', 'Прикладная информатика', 'Компьютерная безопасность',
                                                          'Экономическая кибернетика'],
        'Экономический факультет': ['Экономическая теория', 'Экономика', 'Экономическая информатика', 'Финансы и кредит']}
    bsuPrograms = bsuirPrograms
    brstuFaculties = {
        'Строительный факультет': ['Промышленное и гражданское строительство', 'Сельскохозяйственное строительство',
                                   'Городское строительство', 'Архитектура'],
        'Факультет электронно-информационных систем': ['Вычислительные машины, системы и сети', 'Автоматизированные системы обработки информации',
                                                       'Искусственный интеллект', 'Программируемые мобильные системы'],
        'Факультет инженерных систем и экологии': ['Мелиорация и водное хозяйство', 'Теплогазоснабжение, вентиляция и охрана воздушного бассейна',
                                                   'Природоохранная деятельность', 'Экология'],
        'Экономический факультет': ['Маркетинг', 'Бухгалтерский учет, анализ и аудит', 'Финансы и кредит', 'Логистика']}
    brstuPrograms = ['Докторантура', 'Аспирантура']
    brsupushkina = {
        'Социально-педагогический факультет': ['Дошкольное образование', 'Социальная работа', 'Логопедия', 'Социальная педагогика']}
    brsupushkinaPrograms = ['Магистратура']
    visumasherov = {
        'Факультет химико-биологических и географических наук': ['Биология', 'География', 'Теория и методика обучения и воспитания',
                                                                 'Биохимия'],
        'Юридический факультет': ['Судебно-прокурорско-следственная деятельность', 'Хозяйственное право', 'Международное право',
                                  'Юриспруденция'],
        'Факультет математики и информационных технологий': ['Информационные системы и технологии в здравоохранении', 'Прикладная информатика',
                                                             'Программное обеспечение информационных технологий', 'Прикладная математика'],
        'Педагогический факультет': ['Музыкальное искусство, ритмика и хореография', 'Начальное образование', 'Дошкольное образование',
                                     'Олигофренопедагогика']}
    visumasherovPrograms = ['Магистратура', 'Аспирантура']
    vistu = {
        'Факультет информационных технологий и робототехники': ['Информационные системы и технологии (в проектировании и производстве)',
                                                                'Компьютерная мехатроника', 'Технология машиностроения',
                                                                'Автоматизация технологических процессов и производств'],
        'Факультет экономики и бизнес-управления': ['Бухгалтерский учет, анализ и аудит', 'Коммерческая деятельность',
                                                    'Маркетинг', 'Финансы и кредит'],
        'Факультет производственных технологий': ['Метрология, стандартизация и сертификация', 'Товароведение и экспертиза товаров',
                                                  'Производство одежды, обуви и кожгалантерейных изделий',
                                                  'Производство текстильных материалов'],
        'Факультет дизайна': ['Дизайн виртуальной среды', 'Дизайн коммуникативный', 'Дизайн костюма и тканей', 'Дизайн предметно-пространственной среды']}
    vistuPrograms = ['Магистратура', 'Аспирантура']
    grsmu = {
        'Лечебный факультет': ['Врач-дерматовенеролог', 'Врач-диетолог', 'Врач-инфекционист', 'Врач-кардиолог'],
        'Медико-диагностический факультет': ['Медико-диагностическое дело', 'Сестринское дело'],
        'Педиатрический факультет': ['Педиатр'],
        'Факультет повышения квалификации и переподготовки': ['Ультразвуковая диагностика', 'Функциональная диагностика',
                                                              'Организация здравоохранения', 'Общая врачебная практика']}
    grsmuPrograms = ['Докторантура', 'Аспирантура']
    grsu = {
        'Факультет экономики и управления': ['Мировая экономика ', 'Финансы и кредит', 'Электронный маркетинг', 'Бухгалтерский учет, анализ и аудит'],
        'Физико-технический факультет': ['Компьютерная физика', 'Информационно-измерительная техника', 'Промышленные роботы и робототехнические комплексы',
                                         'Физика'],
        'Инженерно-строительный факультет': ['Теплогазоснабжение, вентиляция и охрана воздушного бассейна', 'Промышленное и гражданское строительство'],
        'Факультет математики и информатики': ['Искусственный интеллект', 'Компьютерная безопасность', 'Прикладная математика', 'Математика']}
    grsuPrograms = ['Магистратура', 'Аспирантура']
    gomsmu = {
        'Лечебный факультет': ['Врач-дерматовенеролог', 'Врач-диетолог', 'Врач-инфекционист', 'Врач-кардиолог'],
        'Медико-диагностический факультет': ['Медико-диагностическое дело', 'Медико-профилактическое дело', 'Врач-гигиенист', 'Врач-бактериолог'],
        'Педиатрический факультет': ['Педиатр'],
        'Факультет повышения квалификации и переподготовки': ['Ультразвуковая диагностика', 'Функциональная диагностика',
                                                              'Организация здравоохранения', 'Общая врачебная практика']}
    gomsmuPrograms = ['Докторантура', 'Аспирантура']
    gomstu = {
        'Энергетический факультет': ['Электроэнергетические системы и сети', 'Электроснабжение', 'Промышленная теплоэнергетика',
                                     'Техническая эксплуатация энергооборудования организаций'],
        'Механико-технологический факультет': ['Конструирование и производство изделий из композиционных материалов',
                                               'Производство изделий на основе трёхмерных технологий',
                                               'Проектирование и производство сельскохозяйственной техники',
                                               'Металлургическое производство и материалообработка'],
        'Факультет автоматизированных и информационных систем': ['Промышленная электроника','Информатика и технологии программирования',
                                                                 'Информационные системы и технологии (в игровой индустрии)',
                                                                 'Автоматизированные электроприводы'],
        'Машиностроительный факультет': ['Технология машиностроения', 'Гидропневмосистемы мобильных и технологических машин',
                                         'Разработка и эксплуатация нефтяных и газовых месторождений',
                                         'Автоматизация технологических процессов и производств']}
    gomstuPrograms = ['Докторантура', 'Аспирантура']

    # currency
    currencyName = 'BYN'
    currencyEqualsToDollar = 2.56

    # military
    milPolBlock = "ОДКБ"
    amountOfPeopleInArmy = 47950

    # crime thing
    levelOfCrime = 1  # [-2, 2]
    crimeIncreasingInThePast3Years = 2  # [-2, 2]
    worriesHomeBrokenAndThingsStolen = 0  # [-2, 2]
    worriesBeingMuggedOrRobbed = 0  # [-2, 2]
    worriesCarStolen = -1  # [-2, 2]
    worriesThingsFromCarStolen = 0  # [-2, 2]
    worriesAttacked = 1  # [-2, 2]
    worriesBeingInsulted = 1  # [-2, 2]
    worriesAttackBecauseOfYourSkinColorEtc = 0  # [-2, 2]
    problemPeopleUsingOrDealingDrugs = -1  # [-2, 2]
    problemPropertyCrimes = 0  # [-2, 2]
    problemViolentCrimes = 0  # [-2, 2]
    problemCorruptionAndBribery = 2  # [-2, 2]
    safetyWalkingAloneDuringNight = 0  # [-2, 2]
    safetyWalkingAloneDuringDay = -1  # [-2, 2]

    # healthcare
    numberOfDoctorsPer100kPopulation = 407
    levelOfModernityOfMedicalEquipment = 0  # [-2, 2]
    levelOfEducationOfMedicalStaff = 0  # [-2, 2]
    responsivenessLevel = -1  # [-2, 2]
    levelOfCompetenceOfMedicalStaff = 0  # [-2, 2]
    levelOfLocationOfMedicalInstitutions = 0  # [-2, 2]
    costOfMedicine = 0  # [-2, 2]
    menAverageLifeExpectancy = 61
    womenAverageLifeExpectancy = 69

    # climat
    airQualityLevel = 0  # [-2, 2]
    drinkingWaterQualityLevel = 1  # [-2, 2]
    garbageCollectionLevel = 1  # [-2, 2]
    streetCleanlinessLevel = 1  # [-2, 2]
    levelOfLightAndNoisePollution = 1  # [-2, 2]
    waterPollution = 0  # [-2, 2]
    satisfactionWithGarbageDisposal = 1  # [-2, 2]
    comfortableTimeInTheCity = 1  # [-2, 2]
    qualityOfParksAndGreenSpaces = 1  # [-2, 2]
    juneAverageTemperature = 19.9
    decemberAverageTemperature = -3.5
    averageHumidity = 67.5
    averageDurationOfWinter = 3.9
    averageRainfallPerMonth = 650
    averageNumberOfFoggyDaysPerYear = 180
    averageNumberOfRainyDaysPerYear = 48
    averageNumberOfClearDays = 96

    # Man-made disasters
    nameMMD = 'Авария на ЧАЭС'
    typeOfMMD = 'Авария на АЭС'
    aomuntOfDeadPeople = 37500
    aomuntOfInjuredPeople = 5000000
    territoryOfPollution = 145000
    # manMadeDisaster = {'name': 'Авария на ЧАЭС', 'typeOfMMD': 'Авария на АЭС', 'aomuntOfDeadPeople': 37500,
    #                    'aomuntOfInjuredPeople': 5000000, 'territoryOfPollution': 145000}


    # security
    situationInTheCountry = 0  # нет источника от Матвея [1, 5]
    freedomOfSpeech = 0  # нет источника от Матвея [1, 5]
    assessmentOfFamilyLife = 0  # нет источника от Матвея [1, 5]
    attitudeTowardsLGBT = 0  # нет источника от Матвея [1, 5]

    # population
    populationCount = 9399000
    procentOfMalesAndFemales = (53.8, 46.2)  # пара процентов, первое число - процент мужчин, второе - женщин
    populationDensityPerSquareKilometer = 45.5
    speedOfLife = 0  # нет источника от Матвея [1, 5]
    workPlaces = 0  # нет источника от Матвея [1, 5]
    nightLifeEntertainment = 0  # нет источника от Матвея [1, 5]

    # citizenship
    visa_free_entry = True
    citizenshipGlobalRank = 0  # источники!!! [1, 5]
    friendlyToForeigners = 0  # source!!! [1, 5]

    # communication
    communicationOnEnglish = 0  # источник [1, 5]

    # transport
    averageTravelTimeToWork = 50  # в чём измерять?
    developmentLevelOfPublicTransport = 0  # [1, 5]

    # internet
    speedOfInternetMbps = 55  # Мегабиты в секунду
    freeWifi = 0  # источник [1, 5]

    # economic situation
    averageSalaryAfterTaxes = 0  # $
    # Price of life per month
    familyPriceOfLife = 0  # $
    personPriceOfLife = 0  # $
    # Cafe and restaurant prices
    priceOfFoodInAnInexpensiveRestaurant = 0  # $
    priceOfFoodInAMidRangeRestaurant = 0  # $
    priceOfFastFood = 0  # $
    priceOfCoffee = 0  # $
    # Supermarket prices
    priceOfMilk1Litre = 0  # $
    priceOfBreadHalfOf1kg = 0  # $
    priceOfRice1kg = 0  # $
    priceOfEggs12pcs = 0  # $
    priceOfCheese1kg = 0  # $
    priceOfChicken1kg = 0  # $
    priceOfBeef1kg = 0  # $
    priceOfApples1kg = 0  # $
    priceOfBanana1kg = 0  # $
    priceOfOrange1kg = 0  # $
    priceOfTomato1kg = 0  # $
    priceOfPotatoes1kg = 0  # $
    priceOfOnion1kg = 0  # $
    priceOfLettuceHead = 0  # $
    priceOfWaterOneAndAHalfLitre = 0  # $
    # transport prices
    monthlyTravelByPublicTransport = 0  # $
    taxiPricePer1km = 0  # $
    gas1Litre = 0  # $
    # Utility prices
    basicUtilitiesPrice = 0  # $
    theInternetPrice = 0  # $
    # Prices for entertainment and recreation
    fitnessClubPrice = 0  # $
    movieTicketPrice = 0  # $
    # child care costs
    privateKindergartenPrice = 0  # $
    schoolPrice = 0  # $
    # Prices for clothes/shoes
    aPairOfJeansPrice = 0  # $
    dressPrice = 0  # $
    sneakersPrice = 0  # $
    shoesPrice = 0  # $

    cc.createBase(countryName, cities, officialLanguage,
                  # currency
                  currencyName, currencyEqualsToDollar,
                  # military
                  milPolBlock, amountOfPeopleInArmy,
                  # crime thing
                  levelOfCrime, crimeIncreasingInThePast3Years, worriesHomeBrokenAndThingsStolen,
                  worriesBeingMuggedOrRobbed,
                  worriesCarStolen, worriesThingsFromCarStolen,
                  worriesAttacked, worriesBeingInsulted,
                  worriesAttackBecauseOfYourSkinColorEtc, problemPeopleUsingOrDealingDrugs,
                  problemPropertyCrimes, problemViolentCrimes,
                  problemCorruptionAndBribery,
                  safetyWalkingAloneDuringNight, safetyWalkingAloneDuringDay,
                  # healthcare
                  numberOfDoctorsPer100kPopulation, levelOfModernityOfMedicalEquipment,
                  levelOfEducationOfMedicalStaff, responsivenessLevel,
                  levelOfCompetenceOfMedicalStaff, levelOfLocationOfMedicalInstitutions,
                  costOfMedicine, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                  # climat
                  airQualityLevel, drinkingWaterQualityLevel, garbageCollectionLevel,
                  streetCleanlinessLevel, levelOfLightAndNoisePollution, waterPollution,
                  satisfactionWithGarbageDisposal, comfortableTimeInTheCity, qualityOfParksAndGreenSpaces,
                  juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                  averageDurationOfWinter, averageRainfallPerMonth, averageNumberOfFoggyDaysPerYear,
                  averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,
                  # security
                  situationInTheCountry, freedomOfSpeech,
                  assessmentOfFamilyLife, attitudeTowardsLGBT,
                  # population
                  populationCount, procentOfMalesAndFemales, populationDensityPerSquareKilometer,
                  speedOfLife, workPlaces, nightLifeEntertainment,
                  # citizenship
                  visa_free_entry, citizenshipGlobalRank, friendlyToForeigners,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,

                  # economic situation
                  averageSalaryAfterTaxes,
                  # Price of life per month
                  familyPriceOfLife, personPriceOfLife,
                  # Cafe and restaurant prices
                  priceOfFoodInAnInexpensiveRestaurant,
                  priceOfFoodInAMidRangeRestaurant,
                  priceOfFastFood, priceOfCoffee,
                  # Supermarket prices
                  priceOfMilk1Litre, priceOfBreadHalfOf1kg, priceOfRice1kg,
                  priceOfEggs12pcs, priceOfCheese1kg, priceOfChicken1kg,
                  priceOfBeef1kg, priceOfApples1kg, priceOfBanana1kg,
                  priceOfOrange1kg, priceOfTomato1kg, priceOfPotatoes1kg,
                  priceOfOnion1kg, priceOfLettuceHead, priceOfWaterOneAndAHalfLitre,
                  # transport prices
                  monthlyTravelByPublicTransport, taxiPricePer1km, gas1Litre,
                  # Utility prices
                  basicUtilitiesPrice, theInternetPrice,
                  # Prices for entertainment and recreation
                  fitnessClubPrice, movieTicketPrice,
                  # child care costs
                  privateKindergartenPrice, schoolPrice,
                  # Prices for clothes/shoes
                  aPairOfJeansPrice, dressPrice,
                  sneakersPrice, shoesPrice
                  )
    cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
                             aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createEducation("Беларусь", cities, 5)
    cc.close()
