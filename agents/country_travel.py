from math import sqrt

from neo4j_country_db.country_travel import country_travel_db as rdb


class CountryResortsAgent:
    result = dict()

    @staticmethod
    def check_resort(choice):
        beach = rdb.find_resort(choice)
        return beach

    @staticmethod
    def check_ski_resort(choice):
        ski = rdb.find_ski_resort(choice)
        return ski

    @staticmethod
    def check_sight(choice):
        sight = rdb.find_sight(choice)
        return sight

    def find1(self, answer):
        try:
            a = self.check_resort(answer['country'])
            links = list()
            srt_q = ''
            for i in a:
                links.append(i['photo'])
                srt_q += i['country']
                srt_q += '\n'
                srt_q += i['resortName']
                srt_q += '\n'
                srt_q += i['description']
                srt_q += '\n\n'
            return links, srt_q
        except:
            return ['https://www.meme-arsenal.com/memes/eab8e51231e8f8de8fc9de70913056c4.jpg'], "не удалось найти"


    def find2(self, answer):
        try:
            a = self.check_ski_resort(answer['country'])
            links = list()
            srt_q = ''
            for i in a:
                links.append(i['photo'])
                srt_q += i['country']
                srt_q += '\n'
                srt_q += i['skiResortName']
                srt_q += '\n'
                srt_q += i['description']
                srt_q += '\n\n'
            return links, srt_q
        except:
            return ['https://www.meme-arsenal.com/memes/eab8e51231e8f8de8fc9de70913056c4.jpg'], "не удалось найти"


    def find3(self, answer):
        try:
            a = self.check_sight(answer['country'])
            print(a)
            links = list()
            srt_q = ''
            for i in a:
                links.append(i['photo'])
                srt_q += i['country']
                srt_q += '\n'
                srt_q += i['sightName']
                srt_q += '\n'
                srt_q += i['description']
                srt_q += '\n\n'
            return links, srt_q
        except:
            return ['https://www.meme-arsenal.com/memes/eab8e51231e8f8de8fc9de70913056c4.jpg'], "не удалось найти"


resorts_agent = CountryResortsAgent()

if __name__ == "__main__":
    print(resorts_agent.find3("Canada"))


