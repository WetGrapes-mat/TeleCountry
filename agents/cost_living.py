from neo4j_country_db.cost_living import cost_living_db


class CostLiving:
    def __init__(self):
        super().__init__()
        self.prices = []

    def get_information(self):
        self.prices = cost_living_db.findAllPrices()
        for price in self.prices:
            print(price)
        cost_living_db.close()


if __name__ == "__main__":
    cl = CostLiving()
    cl.get_information()

