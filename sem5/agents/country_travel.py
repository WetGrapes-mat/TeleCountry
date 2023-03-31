from neo4j import GraphDatabase


class Requester:

    def __init__(self):
        self.driver = GraphDatabase.driver("bolt://localhost:7999", auth=("neo4j", "admin"))

    def close(self):
        self.driver.close()

    def request_city_names(self, country_name):  # входная функция, просто передаёт элементы в приватный метод
        with self.driver.session() as session:
            request = session.execute_write(self._request_city_names, country_name)
            return request

    # по факту в кавычках пишется запрос на языке cypher
    @staticmethod
    def _request_city_names(tx, country_name):  # приватный метод который дерает запрос в neo4j
        result_str = 'match (country:Country {name:"%s"}) \n' % country_name  # ищем страну с заданным названием
        result_str += 'match (country)-[:has_city]->(city:City) \n'  # ищем узлы со связями has_city
        result_str += 'return city.name \n'  # возвращаем названия найденных городов
        result = tx.run(result_str)  # запускаем написанный запрос
        return [cityName["city.name"] for cityName in result]  # возвращаем массив названий городов

    # запросы можно строить и в одном result_str
    # result_str = """
    # запрос
    # запрос
    # запрос
    # """


if __name__ == "__main__":
    rqst = Requester()  # создаём запросник

    city_names = rqst.request_city_names("Poland")  # делаем запрос на названия городов в заданной стране
    print(city_names)

    rqst.close()  # закрываем запросник
