from agents.cost_living import cl
from agents.country_migration import cm
from agents.country_education import ce
from agents.most_dangerous_places import mdp
from agents.standard_of_living import st


class Controller:
    def control_migration(self, answer_user):
        return cm.calculate(answer_user)

    def control_cost_living(self, user_answers):
        cl.get_information()
        return cl.out(int(user_answers["child_preschool"]),
                      int(user_answers["child_school"]),
                      int(user_answers["members"]),
                      int(user_answers["smoking"]),
                      user_answers["transportation"],
                      user_answers["rent"],
                      user_answers["country"])

    def control_education(self, answer_user):
        return ce.find_result(answer_user)

    def control_most_dangerous_places(self, answer_user):
        mdp.get_all_information()
        return mdp.count(answer_user)

    def control_standard_of_living(self):
        return st.get_country_rating()


contrl = Controller()
