from neo4j_country_db.requests import Request


class CostLiving(Request):
    def __init__(self):
        super().__init__()
        self.prices = []

    def get_information(self):
        request = Request()
        self.prices = request.findAllPrices()
        for price in self.prices:
            print(price)
        request.close()


cost_living_db = CostLiving()

if __name__ == "__main__":
    cost_living_db = CostLiving()
    cost_living_db.get_information()

