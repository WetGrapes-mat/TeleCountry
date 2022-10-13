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
                      universityPhoto, hostelAvailability, universityProgramName,
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
                                         universityPhoto, hostelAvailability, universityProgramName,
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
                       universityPhoto, hostelAvailability, universityProgramName,
                       averageGraduatesSalary, graduatesWhoFoundJobsInShortTime,
                       facultyName, specialityName, passingScore, placesCount, subjectsForAdmission
                       ):
        result = tx.run("CREATE (country:Country {name:'$countryName'})"

                        "CREATE (language:Language {name:'$languageName'})"
                        "CREATE (country)-[:official_language]->(language) "
                        
                        "CREATE (city1:City {name:'$cityName1', isBig:$isBig1})"
                        "CREATE (city2:City {name:'$cityName2', isBig:$isBig2})"
                        "CREATE (city3:City {name:'$cityName3', isBig:$isBig3})"
                        "CREATE (city4:City {name:'$cityName4', isBig:$isBig4})"
                        "CREATE (city5:City {name:'$cityName5', isBig:$isBig5})"
                        
                        "CREATE (country)-[:capital]->(city1)"
                        "CREATE (country)-[:has_city]->(city1)"
                        "CREATE (country)-[:has_city]->(city2)"
                        "CREATE (country)-[:has_city]->(city3)"
                        "CREATE (country)-[:has_city]->(city4)"
                        "CREATE (country)-[:has_city]->(city5)"

                        "CREATE (currency:Currency {name:'$currencyName', oneDollarEquals:$oneDollarEquals})"
                        "CREATE (country)-[:currency]->(currency)"
                        
                        "CREATE (militaryPoliticalBlock:MilitaryPoliticalBlock {name:'$milPolBlock'})"
                        "CREATE (country)-[:belongs_to_military_political_block]->(militaryPoliticalBlock)"

                        "CREATE (militaryPower:MilitaryPower {amountOfPeople:$amountOfPeopleInArmy})"
                        "CREATE (country)-[:military_power]->(militaryPower)"

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
                        "CREATE (country)-[:crime_indexes]->(crimeThing)"

                        "CREATE (healthcare:Healthcare {numberOfDoctorsPer100kPopulation:$numberOfDoctorsPer100kPopulation,"
                        "                               levelOfModernityOfMedicalEquipment:$levelOfModernityOfMedicalEquipment,"
                        "                               levelOfEducationOfMedicalStaff:$levelOfEducationOfMedicalStaff,"
                        "                               responsivenessLevel:$responsivenessLevel,"
                        "                               levelOfCompetenceOfMedicalStaff:$levelOfCompetenceOfMedicalStaff,"
                        "                               levelOfLocationOfMedicalInstitutions:$levelOfLocationOfMedicalInstitutions,"
                        "                               costOfMedicine:$costOfMedicine,"
                        "                               menAverageLifeExpectancy:$menAverageLifeExpectancy,"
                        "                               womenAverageLifeExpectancy:$womenAverageLifeExpectancy})"
                        "CREATE (country)-[:helthcare]->(helthcare)"
# good

                        "CREATE (education:Education {rankingOfNationalEducationSystem:$rankingOfNationalEducationSystem})"
                        "CREATE (country)-[:education]->(education)"
                        
                        "CREATE (university:University {name:'$universityName', costOfEducation:$costOfEducation, "
                        "                               photo:'$universityPhoto', hostelAvailability:$hostelAvailability}) "
                        
                        "CREATE (uniProgram1:Program {name:'$universityProgramName1'})"
                        "CREATE (uniProgram2:Program {name:'$universityProgramName2'})"
                        "CREATE (uniProgram3:Program {name:'$universityProgramName3'})"
                        "CREATE (uniPerspectives:Perspectives {averageGraduatesSalary:$averageGraduatesSalary,"
                        "                                      graduatesWhoFoundJobsInShortTime:$graduatesWhoFoundJobsInShortTime}"
                        "CREATE (uf1:uniFaculty {name:'$facultyName1'})"
                        "CREATE (uf2:uniFaculty {name:'$facultyName2'})"
                        "CREATE (uf3:uniFaculty {name:'$facultyName3'})"
                        "CREATE (uf4:uniFaculty {name:'$facultyName4'})"
                        "CREATE (us11:uniSpeciality {name:'$specialityName11', passingScore:$passingScore11,"
                        "                       placesCount:$placesCount11, subjectsForAdmission:'$subjectsForAdmission11'})"
                        "CREATE (us12:uniSpeciality {name:'$specialityName12', passingScore:$passingScore12,"
                        "                       placesCount:$placesCount12, subjectsForAdmission:'$subjectsForAdmission12'})"
                        "CREATE (us21:uniSpeciality {name:'$specialityName21', passingScore:$passingScore21,"
                        "                       placesCount:$placesCount21, subjectsForAdmission:'$subjectsForAdmission21'})"
                        "CREATE (us22:uniSpeciality {name:'$specialityName22', passingScore:$passingScore22,"
                        "                       placesCount:$placesCount22, subjectsForAdmission:'$subjectsForAdmission22'})"
                        "CREATE (us31:uniSpeciality {name:'$specialityName31', passingScore:$passingScore31,"
                        "                       placesCount:$placesCount31, subjectsForAdmission:'$subjectsForAdmission31'})"
                        "CREATE (us32:uniSpeciality {name:'$specialityName32', passingScore:$passingScore32,"
                        "                       placesCount:$placesCount32, subjectsForAdmission:'$subjectsForAdmission32'})"
                        "CREATE (us41:uniSpeciality {name:'$specialityName41', passingScore:$passingScore41,"
                        "                       placesCount:$placesCount41, subjectsForAdmission:'$subjectsForAdmission41'})"
                        "CREATE (us42:uniSpeciality {name:'$specialityName42', passingScore:$passingScore42,"
                        "                       placesCount:$placesCount42, subjectsForAdmission:'$subjectsForAdmission42'})"


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
                        universityPhoto=universityPhoto, hostelAvailability=hostelAvailability,

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
                     True, True, True, True, False,
                     "BYN", 2.56,
                     "ОДКБ", 47950
                     )
    cc.close()
