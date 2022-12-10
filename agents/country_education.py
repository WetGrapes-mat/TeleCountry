from neo4j_country_db.country_education import country_education_db as db


class CountryEducation:
    country_choice = dict()

    def program(self):
        program = []
        c = db.find_program()


agent = CountryEducation()
if __name__ == "__main__":
    pass
