from neo4j_country_db.requests import Request


class CountryEducation(Request):
    def __init__(self):
        super().__init__()

    def find_faculty(self):
        with self.driver.session() as session:
            faculty = session.execute_write(self._faculty)
            return faculty

    def find_program(self):
        with self.driver.session() as session:
            program = session.execute_write(self._program)
            return program

    def find_cost(self):
        with self.driver.session() as session:
            cost = session.execute_write(self._cost)
            return cost

    def find_min_cost(self):
        with self.driver.session() as session:
            min_cost = session.execute_write(self._min_cost)
            return min_cost

    def find_max_cost(self):
        with self.driver.session() as session:
            max_cost = session.execute_write(self._max_cost)
            return max_cost


    def find_hostel(self):
        with self.driver.session() as session:
            hostel = session.execute_write(self._hostel)
            return hostel

    def find_university(self):
        with self.driver.session() as session:
            uni = session.execute_write(self._university())
            return uni

    @staticmethod
    def _university(tx):
        result = tx.run("match (country:Country) -[:university]-> (uni:University)"
                        "-[:faculty]-> (f:Faculty), "
                        "(city:City)-[:university]->(uni)-[:program]->(program:Program) "
                        "return "
                        "country.name as country, "
                        "city.name as city, "
                        "f.name as faculty, "
                        "program.name as program, "
                        "uni.name as university, "
                        "uni.link as link, "
                        "uni.cost as cost, "
                        "uni.hostel as hostel, "
                        "uni.scolarship as grant, "
                        "uni.requirements as requirements, "
                        "uni.image as photo")
        return [{"country": info["country"],
                 "city": info["city"],
                 "university": info["university"],
                 "faculties": info["faculty"],
                 "programs": info["program"],
                 "link": info["link"],
                 "cost": info["cost"],
                 "hostel": info["hostel"],
                 "grant": info["grant"],
                 "requirements": info["requirements"],
                 "photo": info["photo"]} for info in result]

    @staticmethod
    def _faculty(tx):
        result = tx.run("match (country:Country) -[:university]->(uni:University)"
                        "-[:faculty]->(f:Faculty) "
                        "return "
                        "country.name as country, "
                        "university.name as university, "
                        "f.name as faculty")
        return [{"country": info["country"],
                 "university": info["university"],
                 "faculties": info["faculty"]} for info in result]

    @staticmethod
    def _program(tx):
        result = tx.run("match (country:Country) -[:university]->(uni:University)"
                        "-[:program]->(p:Program) "
                        "return "
                        "country.name as country, "
                        "university.name as university, "
                        "p.name as program")
        return [{"country": info["country"],
                 "university": info["university"],
                 "programs": info["program"]} for info in result]


    @staticmethod
    def _cost(tx):
        result = tx.run("match (country:Country) -[:university]->(uni:University) "
                        "return "
                        "country.name as country, "
                        "university.name as university, "
                        "university.cost as cost")
        return [{"country": info["country"],
                 "university": info["university"],
                 "cost": info["cost"]} for info in result]

    @staticmethod
    def _min_cost(tx):
        result = tx.run("match (uni:University) "
                        "return "
                        "MIN(university.cost) as cost")
        return result[0]["cost"]


    @staticmethod
    def _max_cost(tx):
        result = tx.run("match (uni:University) "
                        "return "
                        "MAX(university.cost) as cost")
        return result[0]["cost"]


    @staticmethod
    def _hostel(tx):
        result = tx.run("match (country:Country) -[:university]->(uni:University) "
                        "return "
                        "country.name as country, "
                        "university.name as university, "
                        "university.hostel as hostel")
        return [{"country": info["country"],
                 "university": info["university"],
                 "hostel": info["hostel"]} for info in result]


country_education_db = CountryEducation()

if __name__ == "__main__":
    pass
