from neo4j_country_db.country_education import country_education_db as db


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

    def find_result(self, answer):
        result = list(set(self.check_faculty(answer["faculties"])) & set(self.check_program(answer["programs"])) & \
                      set(self.check_hostel(answer["hostel"])) & set(self.check_cost(answer["cost"])))
        print(result)
        if len(result) == 0:
            return "Мы не смогли подобрать университет по вашим параметрам ;(\n"
        else:
            uni_rank = self.check_rank()
            sorted_values = dict(sorted(uni_rank.items(), key=lambda item: item[1]))
            print(sorted_values)
            sorted_result = []
            for key in sorted_values.keys():
                if key in result:
                    sorted_result.append(key)
                    result.remove(key)
            result = sorted_result
            print(sorted_result)

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
                txt += f"""<a href="{uni_info[0]['photo']}">&#8203;</a>\n"""
            return txt


agent = CountryEducationAgent()

if __name__ == "__main__":
    answer = {"faculties": "Faculty of Arts", "programs": "Magistracy", "hostel": "Yes", "cost": 50000}
    res = agent.find_result(answer)
    print(res)

    text = agent.check_rank()
    print(text)


