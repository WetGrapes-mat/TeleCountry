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
                   costOfMedicine, menAverageLifeExpectancy, womenAverageLifeExpectancy
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
                                         costOfMedicine, menAverageLifeExpectancy, womenAverageLifeExpectancy
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
                    costOfMedicine, menAverageLifeExpectancy, womenAverageLifeExpectancy
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

        result = tx.run(resultStr)



if __name__ == "__main__":
    cc = CountryCreator()
    # Country
    countryName = "Беларусь"
    officialLanguage = "Русский"
    # cities    name   isBig
    cities = {'Минск': True, 'Брест': True, 'Витебск': True, 'Гродно': True, 'Орша': False}
    # currency
    currencyName = 'BYN'
    currencyEqualsToDollar = 2.56
    # military
    milPolBlock = "ОДКБ"
    amountOfPeopleInArmy = 47950
    # crime thing
    levelOfCrime = 1
    crimeIncreasingInThePast3Years = 2
    worriesHomeBrokenAndThingsStolen = 0
    worriesBeingMuggedOrRobbed = 0
    worriesCarStolen = -1
    worriesThingsFromCarStolen = 0
    worriesAttacked = 1
    worriesBeingInsulted = 1
    worriesAttackBecauseOfYourSkinColorEtc = 0
    problemPeopleUsingOrDealingDrugs = -1
    problemPropertyCrimes = 0
    problemViolentCrimes = 0
    problemCorruptionAndBribery = 2
    safetyWalkingAloneDuringNight = 0
    safetyWalkingAloneDuringDay = -1
    # healthcare
    numberOfDoctorsPer100kPopulation = 407
    levelOfModernityOfMedicalEquipment = 0
    levelOfEducationOfMedicalStaff = 0
    responsivenessLevel = -1
    levelOfCompetenceOfMedicalStaff = 0
    levelOfLocationOfMedicalInstitutions = 0
    costOfMedicine = 0
    menAverageLifeExpectancy = 61
    womenAverageLifeExpectancy = 69

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
                  costOfMedicine, menAverageLifeExpectancy, womenAverageLifeExpectancy
                  )
    cc.close()
