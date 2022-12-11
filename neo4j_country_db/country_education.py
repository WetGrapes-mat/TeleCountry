from neo4j_country_db.requests import Request


class CountryEducation(Request):
    def __init__(self):
        super().__init__()

    def find_faculty(self, fac):
        with self.driver.session() as session:
            faculty = session.execute_write(self._faculty, fac)
            return faculty

    def find_program(self, progr):
        with self.driver.session() as session:
            program = session.execute_write(self._program, progr)
            return program

    def find_cost(self, c):
        with self.driver.session() as session:
            cost = session.execute_write(self._cost, c)
            return cost

    def find_min_cost(self):
        with self.driver.session() as session:
            min_cost = session.execute_write(self._min_cost)
            return min_cost

    def find_max_cost(self):
        with self.driver.session() as session:
            max_cost = session.execute_write(self._max_cost)
            return max_cost

    def find_hostel(self, host):
        with self.driver.session() as session:
            hostel = session.execute_write(self._hostel, host)
            return hostel

    def find_university(self, u):
        with self.driver.session() as session:
            uni = session.execute_write(self._university, u)
            return uni

    def find_rank(self):
        with self.driver.session() as session:
            ranks = session.execute_write(self._education_rank)
            return ranks

    @staticmethod
    def _university(tx, uni):
        result = tx.run("match (country:Country) -[:university]-> (uni:University)"
                        "-[:faculty]-> (f:Faculty), "
                        "(city:City)-[:university]->(uni)-[:program]->(program:Program) "
                        "where uni.name = $name "
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
                        "uni.image as photo", name=uni)
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
    def _faculty(tx, faculty):
        result = tx.run("match (uni:University)-[:faculty]->(f:Faculty {name: $faculty}) "
                        "return "
                        "uni.name as university", faculty=faculty)
        return [info["university"] for info in result]
    # [info["university"] for info in res if info["faculties"] == "Faculty of Psychology"]

    @staticmethod
    def _program(tx, program):
        result = tx.run("match (uni:University)-[:program]->(p:Program {name:$program}) "
                        "return "
                        "uni.name as university", program=program)
        return [info["university"] for info in result]


    @staticmethod
    def _cost(tx, cost):
        result = tx.run("match (country:Country) -[:university]->(uni:University) "
                        "where uni.cost <= $cost "
                        "return "
                        "uni.name as university", cost=cost)
        return [info["university"] for info in result]

    @staticmethod
    def _min_cost(tx):
        result = tx.run("match (uni:University) "
                        "return "
                        "MIN(uni.cost) as cost")
        return [{"cost": info["cost"]} for info in result][0]["cost"]


    @staticmethod
    def _max_cost(tx):
        result = tx.run("match (uni:University) "
                        "return "
                        "MAX(uni.cost) as cost")
        return [{"cost": info["cost"]} for info in result][0]["cost"]


    @staticmethod
    def _hostel(tx, host):
        result = tx.run("match (uni:University {hostel: $host}) "
                        "return "
                        "uni.name as university", host=host)
        return [info["university"] for info in result]

    @staticmethod
    def _education_rank(tx):
        result = tx.run("match (uni:University)<--(:Country)-->(ed:Education) "
                        "return "
                        "uni.name as university, "
                        "ed.rankingOfNationalEducationSystem as rank")
        return {info["university"]:info["rank"] for info in result}


country_education_db = CountryEducation()

if __name__ == "__main__":
    print(country_education_db.find_cost(12000))
    print(country_education_db.find_rank())
