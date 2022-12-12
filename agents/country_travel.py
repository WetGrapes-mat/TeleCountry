from math import sqrt

from neo4j_country_db.country_travel import country_resorts_db as rdb, country_ski_resorts_db as srdb, country_tourism_db as ctdb


class CountryResortsAgent:
    result = dict()

    @staticmethod
    def check_resort(choice):
        beach = rdb.find_resort(choice)
        return beach

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



class CountrySkiResortsAgent:
    result = dict()

    @staticmethod
    def check_ski_resort(choice):
        ski = srdb.find_ski_resort(choice)
        return ski

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


class CountryTourismAgent:
    result = dict()

    @staticmethod
    def check_sight(choice):
        sight = ctdb.find_ski_resort(choice)
        return sight

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


resorts_agent = CountryResortsAgent()
ski_resorts_agent = CountrySkiResortsAgent()
tourism_agent = CountryTourismAgent()
