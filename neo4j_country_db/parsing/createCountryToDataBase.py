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
                   name, typeOfMMD, aomuntOfDeadPeople,
                   aomuntOfInjuredPeople, territoryOfPollution
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
                                         name, typeOfMMD, aomuntOfDeadPeople,
                                         aomuntOfInjuredPeople, territoryOfPollution
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
                    name, typeOfMMD, aomuntOfDeadPeople,
                    aomuntOfInjuredPeople, territoryOfPollution
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

        resultStr += 'create (manMadeDisaster:ManMadeDisaster {name:"%s", typeOfMMD:"%s", aomuntOfDeadPeople:"%d",' \
                     '                                         aomuntOfInjuredPeople:"%d", territoryOfPollution:"%d km^2"})' % (name, typeOfMMD, aomuntOfDeadPeople,
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
    # climat
    airQualityLevel = 0
    drinkingWaterQualityLevel = 1
    garbageCollectionLevel = 1
    streetCleanlinessLevel = 1
    levelOfLightAndNoisePollution = 1
    waterPollution = 0
    satisfactionWithGarbageDisposal = 1
    comfortableTimeInTheCity = 1
    qualityOfParksAndGreenSpaces = 1
    juneAverageTemperature = 19.9
    decemberAverageTemperature = -3.5
    averageHumidity = 67.5
    averageDurationOfWinter = 3.9
    averageRainfallPerMonth = 650
    averageNumberOfFoggyDaysPerYear = 180
    averageNumberOfRainyDaysPerYear = 48
    averageNumberOfClearDays = 96

    manMadeDisaster = {'name': 'Авария на ЧАЭС', 'typeOfMMD': 'Авария на АЭС', 'aomuntOfDeadPeople': 37500, 'aomuntOfInjuredPeople': 5000000,
                       'territoryOfPollution': 145000}
    name = 'Авария на ЧАЭС'
    typeOfMMD = 'Авария на АЭС'
    aomuntOfDeadPeople = 37500
    aomuntOfInjuredPeople = 5000000
    territoryOfPollution = 145000

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
                  name, typeOfMMD, aomuntOfDeadPeople,
                  aomuntOfInjuredPeople, territoryOfPollution
                  )
    # cc.createEducation("Беларусь", cities, 5)
    cc.close()
