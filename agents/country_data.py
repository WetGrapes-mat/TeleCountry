import pymorphy2
import nltk
from controller.context_data import country_data



class CountryData:
    def __init__(self):
        self.data = country_data

    def analize_country_name(self, text):
        tokens_word = nltk.word_tokenize(text)
        for t in tokens_word:
            morph = pymorphy2.MorphAnalyzer()
            word = morph.parse(t)[0].normal_form.lower()
            if word in self.data.keys():
                result = self.get_data_for_interface(word)
                return result
            else:
                for key in self.data.keys():
                    if word in key.split():
                        result = self.get_data_for_interface(key)
                        return result
        return "Извините, я ничего не знаю про эту страну."

    def get_data_for_interface(self, country: str):
        return self.data[country]


cd = CountryData()


if __name__ == "__main__":
    agent = CountryData()
    print(agent.analize_country_name("расскажи о Польше"))
