from math import sqrt

from neo4j_country_db.country_education import country_education_db as db
from agents.standard_of_living import st
from keybords import cost_living



class CountryEducationAgent:
    university_choose = dict()

    @staticmethod
    def check_faculty(choice):
        uni = db.find_faculty(choice)
        return uni

    @staticmethod
    def check_program(choice):
        uni = db.find_program(choice)
        return uni

    @staticmethod
    def check_hostel(choice):
        uni = db.find_hostel(choice)
        return uni

    @staticmethod
    def check_cost(choice):
        uni = db.find_cost(choice)
        return uni

    @staticmethod
    def check_rank():
        ranks = db.find_rank()
        return ranks

    @staticmethod
    def check_uni_country():
        res = db.find_uni_country()
        return res

    @staticmethod
    def check_uni(choice):
        uni = db.find_university(choice)
        return uni

    def send_imgs(self, answer):
        result = list(set(self.check_faculty(answer["faculties"])) & set(self.check_program(answer["programs"])) & \
                      set(self.check_hostel(answer["hostel"])) & set(self.check_cost(answer["cost"])))
        imgs = []
        if len(result) != 0:
            # сортировка
            result = result[:3]
            for info in result:
                imgs.append(info['photos'])
        return imgs

    def price_living(self, params):
        cost_living.cl.get_information()
        answer = dict()
        answer['child_preschool'] = 0
        answer['child_school'] = 0
        answer['members'] = 1
        answer['smoking'] = int(params['smoking'])
        answer['transportation'] = params['transportation']
        answer["rent"] = params['rent']
        answer['country'] = 'Рейтинг стран'

        rez = cost_living.cl.count_cost_living(0, 0, 1,
                                               answer['smoking'], answer['transportation'], answer['rent'],
                                               answer['country'])
        return {z[0][:-1]: float(z[1][:-2]) for z in [i.split("--") for i in rez.split('\n')][:-1]}

    @staticmethod
    def change_value_to_score(d):
        min_value, max_value = min(d.values()), max(d.values())
        delta = (max_value - min_value) / 5
        intervals = [min_value, min_value + delta, min_value + 2 * delta, min_value + 3 * delta,
                     max_value - delta, max_value + 1]
        for key in d.keys():
            for i in range(len(intervals) - 1):
                if intervals[i] <= d[key] < intervals[i + 1]:
                    d[key] = len(intervals) - (i + 1)
        return d

    def multicriteria_choice(self, temp_rank, temp_price):
        coofficients = {"rank": 0.7 / 5, "price": 0.3 / 5}
        price = self.change_value_to_score(temp_price)
        rank = self.change_value_to_score(temp_rank)
        result = {}
        for key in rank.keys():
            a = coofficients['rank'] * pow((rank[key] - 5), 2)
            b = coofficients['price'] * pow((price[key] - 5), 2)
            c = sqrt(sum([a, b]))
            result[key] = c
        return result

    def connect_rank_and_uni(self, ranks, unis):
        result = {}
        for key in unis.keys():
            result[unis[key]] = ranks[key]
        return result

    def find_result(self, answer):
        price = self.price_living(answer)
        rank = self.check_rank()
        d = self.multicriteria_choice(rank, price)
        result = list(set(self.check_faculty(answer["faculties"])) & set(self.check_program(answer["programs"])) & \
                      set(self.check_hostel(answer["hostel"])) & set(self.check_cost(answer["cost"])))
        if len(result) == 0:
            txt = "Мы не смогли подобрать университет по вашим параметрам ;(\n"
            return txt
        else:
            uni_rank = self.check_uni_country()
            uni_rank = self.connect_rank_and_uni(d, uni_rank)
            print(uni_rank)
            sorted_values = dict(sorted(uni_rank.items(), key=lambda item: item[1]))
            print(sorted_values)
            sorted_result = []
            for key in sorted_values.keys():
                if key in result:
                    sorted_result.append(key)
                    result.remove(key)
            result = sorted_result
            print(result)
            photo = []
            result = result[:3]
            txt = "Мы подобрали следующие варианты:\n "
            for i in range(len(result)):
                uni_info = self.check_uni(result[i])
                faculties_ls = []
                programs_ls = []

                for info in uni_info:
                    if info['faculties'] not in faculties_ls:
                        faculties_ls.append(info['faculties'])
                    if info['programs'] not in programs_ls:
                        programs_ls.append(info['programs'])

                faculties = ", ".join(faculties_ls)
                programs = ", ".join(programs_ls)

                txt += "---------------------------------------------------------\n"
                txt += f"{i + 1}. University: {uni_info[0]['university']}\n" \
                       f"Location: {uni_info[0]['country']}, {uni_info[0]['city']}\n" \
                       f"Cost: {uni_info[0]['cost']}\n" \
                       f"Faculties: {faculties}\n" \
                       f"Programs: {programs}\n" \
                       f"Hostel: {uni_info[0]['hostel']}\n" \
                       f"Grant: {uni_info[0]['grant']}\n" \
                       f"Admission requirements: {uni_info[0]['requirements']}\n" \
                       f"Link: {uni_info[0]['link']}\n"
                photo.append(uni_info[0]['photo'])
            if len(photo) == 0:
                return ["https://www.meme-arsenal.com/memes/eab8e51231e8f8de8fc9de70913056c4.jpg"], \
                       "Мы не смогли подобрать университет по вашим параметрам ;(\n"
            else:
                return photo, txt



agent = CountryEducationAgent()

if __name__ == "__main__":
    answer = {"faculties": "Faculty of Arts", "programs": "Magistracy", "hostel": "Yes", "cost": 50000, 'smoking': 1,
              'rent':"своё жильё", 'transportation':'такси'}
    res = agent.find_result(answer)

    #print(res)

    # d = agent.price_living({"smoking": 0, "transportation": "такси", 'rent': 'своё жильё'})
    # print(d)
    #a = agent.change_value_to_score(agent.check_rank())
    '''b = agent.change_value_to_score(agent.price_living({"smoking": 0, "transportation": "такси",
                                                          'rent': 'своё жильё'}))'''
    '''print(a)
    print(b)'''

    #print(agent.multicriteria_choice(a, b))



