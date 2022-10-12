from neo4j import GraphDatabase


class CountryCreator:

    def __init__(self):
        self.driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "admin"))

    def close(self):
        self.driver.close()

    def createCountry(self, countryName, languageName,
                      # Cities
                      cityName1, cityName2, cityName3, cityName4, cityName5,
                      isBig1, isBig2, isBig3, isBig4, isBig5,
                      # Currency
                      currencyName, oneDollarEquals,
                      # Military
                      milPolBlock, amountOfPeopleInArmy,
                      # Crime thing
                      crimeIncreasingInThePast3Years, worriesBeingMuggedOrRobbed, worriesCarStolen,
                      worriesThingsFromCarStolen, worriesAttackBecauseOfYourSkinColorEtc,
                      safetyWalkingAloneDuringNight, safetyWalkingAloneDuringDay,
                      problemPeopleUsingOrDealingDrugs, problemPropertyCrimes,
                      worriesBeingInsulted, worriesAttacked, problemViolentCrimes, problemCorruptionAndBribery,
                      # Health care
                      numberOfDoctorsPer100kPopulation, levelOfModernityOfMedicalEquipment,
                      levelOfEducationOfMedicalStaff, responsivenessLevel,
                      levelOfCompetenceOfMedicalStaff, levelOfLocationOfMedicalInstitutions,
                      costOfMedicine, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                      # Education
                      rankingOfNationalEducationSystem, universityName, costOfEducation,
                      universityPhotos, hostelAvailability, universityProgramName,
                      averageGraduatesSalary, graduatesWhoFoundJobsInShortTime,
                      facultyName, specialityName, passingScore, placesCount, subjectsForAdmission
                      ):
        with self.driver.session() as session:
            city = session.execute_write(self._createCountry, countryName, languageName,
                                         # Cities
                                         cityName1, cityName2, cityName3, cityName4, cityName5,
                                         isBig1, isBig2, isBig3, isBig4, isBig5,
                                         # Currency
                                         currencyName, oneDollarEquals,
                                         # Military
                                         milPolBlock, amountOfPeopleInArmy,
                                         # Crime thing
                                         crimeIncreasingInThePast3Years, worriesBeingMuggedOrRobbed, worriesCarStolen,
                                         worriesThingsFromCarStolen, worriesAttackBecauseOfYourSkinColorEtc,
                                         safetyWalkingAloneDuringNight, safetyWalkingAloneDuringDay,
                                         problemPeopleUsingOrDealingDrugs, problemPropertyCrimes,
                                         worriesBeingInsulted, worriesAttacked, problemViolentCrimes,
                                         problemCorruptionAndBribery,
                                         # Health care
                                         numberOfDoctorsPer100kPopulation, levelOfModernityOfMedicalEquipment,
                                         levelOfEducationOfMedicalStaff, responsivenessLevel,
                                         levelOfCompetenceOfMedicalStaff, levelOfLocationOfMedicalInstitutions,
                                         costOfMedicine, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                                         # Education
                                         rankingOfNationalEducationSystem, universityName, costOfEducation,
                                         universityPhotos, hostelAvailability, universityProgramName,
                                         averageGraduatesSalary, graduatesWhoFoundJobsInShortTime,
                                         facultyName, specialityName, passingScore, placesCount, subjectsForAdmission
                                         )
            return city

    @staticmethod
    def _createCountry(tx, countryName, languageName,
                       # Cities
                       cityName1, cityName2, cityName3, cityName4, cityName5,
                       isBig1, isBig2, isBig3, isBig4, isBig5,
                       # Currency
                       currencyName, oneDollarEquals,
                       # Military
                       milPolBlock, amountOfPeopleInArmy,
                       # Crime thing
                       crimeIncreasingInThePast3Years, worriesBeingMuggedOrRobbed, worriesCarStolen,
                       worriesThingsFromCarStolen, worriesAttackBecauseOfYourSkinColorEtc,
                       safetyWalkingAloneDuringNight, safetyWalkingAloneDuringDay,
                       problemPeopleUsingOrDealingDrugs, problemPropertyCrimes,
                       worriesBeingInsulted, worriesAttacked, problemViolentCrimes, problemCorruptionAndBribery,
                       # Health care
                       numberOfDoctorsPer100kPopulation, levelOfModernityOfMedicalEquipment,
                       levelOfEducationOfMedicalStaff, responsivenessLevel,
                       levelOfCompetenceOfMedicalStaff, levelOfLocationOfMedicalInstitutions,
                       costOfMedicine, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                       # Education
                       rankingOfNationalEducationSystem, universityName, costOfEducation,
                       universityPhotos, hostelAvailability, universityProgramName,
                       averageGraduatesSalary, graduatesWhoFoundJobsInShortTime,
                       facultyName, specialityName, passingScore, placesCount, subjectsForAdmission
                       ):
        result = tx.run("CREATE (country:Country {name:$countryName}) "

                        "CREATE (language:Language {name:$languageName}) "
                        "SET country-[Official_language]->language "

                        "CREATE (city1.City {name:$cityName1, isBig:$isBig1}) "
                        "CREATE (city2.City {name:$cityName2, isBig:$isBig2}) "
                        "CREATE (city3.City {name:$cityName3, isBig:$isBig3}) "
                        "CREATE (city4.City {name:$cityName4, isBig:$isBig4}) "
                        "CREATE (city5.City {name:$cityName5, isBig:$isBig5}) "
                        "SET country-[Capital]->city1 "
                        "SET country-[Has_city]->city1 "
                        "SET country-[Has_city]->city2 "
                        "SET country-[Has_city]->city3 "
                        "SET country-[Has_city]->city4 "
                        "SET country-[Has_city]->city5 "

                        "CREATE (currency.Currency {name:$currencyName, oneDollarEquals:$oneDollarEquals}) "
                        "SET country-[Currency]->city "

                        "CREATE (militaryPoliticalBlock:MilitaryPoliticalBlock {name:$milPolBlock}) "
                        "SET country-[belongs_to_military_political_block]->militaryPoliticalBlock "

                        "CREATE (militaryPower:MilitaryPower {amountOfPeople:$amountOfPeopleInArmy}) "
                        "SET country-[Military_power]->militaryPower "

                        "CREATE (crimeThing:CrimeThing {levelOfCrime:$levelOfCrime,"
                        "                               crimeIncreasingInThePast3Years:$crimeIncreasingInThePast3Years,"
                        "                               worriesBeingMuggedOrRobbed:$worriesBeingMuggedOrRobbed,"
                        "                               worriesCarStolen:$worriesCarStolen,"
                        "                               worriesThingsFromCarStolen:$worriesThingsFromCarStolen,"
                        "                               worriesAttackBecauseOfYourSkinColorEtc:$worriesAttackBecauseOfYourSkinColorEtc,"
                        "                               safetyWalkingAloneDuringNight:$safetyWalkingAloneDuringNight,"
                        "                               safetyWalkingAloneDuringDay:$safetyWalkingAloneDuringDay,"
                        "                               problemPeopleUsingOrDealingDrugs:$problemPeopleUsingOrDealingDrugs,"
                        "                               problemPropertyCrimes:$problemPropertyCrimes,"
                        "                               worriesBeingInsulted:$worriesBeingInsulted,"
                        "                               worriesAttacked:$worriesAttacked,"
                        "                               problemViolentCrimes:$problemViolentCrimes,"
                        "                               problemCorruptionAndBribery:$problemCorruptionAndBribery}) "
                        "SET country-[Crime_indexes]->crimeThing "

                        "CREATE (healthcare:Healthcare {numberOfDoctorsPer100kPopulation:$numberOfDoctorsPer100kPopulation,"
                        "                               levelOfModernityOfMedicalEquipment:$levelOfModernityOfMedicalEquipment,"
                        "                               levelOfEducationOfMedicalStaff:$levelOfEducationOfMedicalStaff,"
                        "                               responsivenessLevel:$responsivenessLevel,"
                        "                               levelOfCompetenceOfMedicalStaff:$levelOfCompetenceOfMedicalStaff,"
                        "                               levelOfLocationOfMedicalInstitutions:$levelOfLocationOfMedicalInstitutions,"
                        "                               costOfMedicine:$costOfMedicine,"
                        "                               menAverageLifeExpectancy:$menAverageLifeExpectancy,"
                        "                               womenAverageLifeExpectancy:$womenAverageLifeExpectancy})"
                        "SET country-[Helthcare]->helthcare "


                        "CREATE (education.Education {rankingOfNationalEducationSystem:$rankingOfNationalEducationSystem}) "
                        "SET country-[Education]->education "
                        
                        "CREATE (university.University {name:$universityName, costOfEducation:$costOfEducation, "
                        "                               photos:$universityPhotos, hostelAvailability:$hostelAvailability}) "
                        
                        "CREATE (uniProgram.Program {name:$universityProgramName})"
                        "CREATE (uniPerspectives.Perspectives {averageGraduatesSalary:$averageGraduatesSalary,"
                        "                                      graduatesWhoFoundJobsInShortTime:$graduatesWhoFoundJobsInShortTime }"
                        "CREATE (uniFaculty {name:$facultyName})"
                        "CREATE (uniSpeciality {name:$specialityName, passingScore:$passingScore,"
                        "                       placesCount:$placesCount, subjectsForAdmission:$subjectsForAdmission })"
                        
                        "SET education-[University]->university "
                        "SET university-[Program]->uniProgram "
                        "SET university-[Perspectives]->uniPerspectives "
                        "SET university-[Faculty]->uniFaculty "
                        
                        '''
                        "SET city-[Education]->university " # ? >.< ?
                        '''

                        ,
                        countryName=countryName,
                        languageName=languageName,
                        # Cities
                        cityName1=cityName1, cityName2=cityName2, cityName3=cityName3, cityName4=cityName4,
                        cityName5=cityName5,
                        isBig1=isBig1, isBig2=isBig2, isBig3=isBig3, isBig4=isBig4, isBig5=isBig5,
                        # Currency
                        currencyName=currencyName, oneDollarEquals=oneDollarEquals,
                        # Military block
                        milPolBlock=milPolBlock, amountOfPeopleInArmy=amountOfPeopleInArmy,
                        # Crime thing
                        crimeIncreasingInThePast3Years=crimeIncreasingInThePast3Years,
                        worriesBeingMuggedOrRobbed=worriesBeingMuggedOrRobbed,
                        worriesCarStolen=worriesCarStolen,
                        worriesThingsFromCarStolen=worriesThingsFromCarStolen,
                        worriesAttackBecauseOfYourSkinColorEtc=worriesAttackBecauseOfYourSkinColorEtc,
                        safetyWalkingAloneDuringNight=safetyWalkingAloneDuringNight,
                        safetyWalkingAloneDuringDay=safetyWalkingAloneDuringDay,
                        problemPeopleUsingOrDealingDrugs=problemPeopleUsingOrDealingDrugs,
                        problemPropertyCrimes=problemPropertyCrimes,
                        worriesBeingInsulted=worriesBeingInsulted,
                        worriesAttacked=worriesAttacked,
                        problemViolentCrimes=problemViolentCrimes,
                        problemCorruptionAndBribery=problemCorruptionAndBribery,
                        # Healthcare
                        numberOfDoctorsPer100kPopulation=numberOfDoctorsPer100kPopulation,
                        levelOfModernityOfMedicalEquipment=levelOfModernityOfMedicalEquipment,
                        levelOfEducationOfMedicalStaff=levelOfEducationOfMedicalStaff,
                        responsivenessLevel=responsivenessLevel,
                        levelOfCompetenceOfMedicalStaff=levelOfCompetenceOfMedicalStaff,
                        levelOfLocationOfMedicalInstitutions=levelOfLocationOfMedicalInstitutions,
                        costOfMedicine=costOfMedicine,
                        menAverageLifeExpectancy=menAverageLifeExpectancy,
                        womenAverageLifeExpectancy=womenAverageLifeExpectancy,
                        # Education
                        rankingOfNationalEducationSystem=rankingOfNationalEducationSystem,

                        universityName=universityName, costOfEducation=costOfEducation,
                        universityPhotos=universityPhotos, hostelAvailability=hostelAvailability,

                        universityProgramName=universityProgramName,

                        averageGraduatesSalary=averageGraduatesSalary, graduatesWhoFoundJobsInShortTime=graduatesWhoFoundJobsInShortTime,

                        facultyName=facultyName,

                        specialityName=specialityName, passingScore=passingScore, placesCount=placesCount,
                        subjectsForAdmission=subjectsForAdmission


                        )
        return result.single()[0]


if __name__ == "__main__":
    cc = CountryCreator()
    cc.createCountry("Беларусь", "Русский",
                     "Минск", "Брест", "Витебск", "Гродно", "Орша",
                     "True", "True", "True", "True", "False",
                     "BYN", "2,56",
                     "ОДКБ", "47 950"
                     )
    cc.close()
