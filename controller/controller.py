from agents.cost_living import cl
from agents.country_migration import cm
from agents.most_dangerous_places import mdp
from agents.standard_of_living import st
from agents.country_data import cd
import re

import nltk
import pymorphy2

from transformers import BertTokenizer, BertModel
import torch
import speech_recognition as sr


model_name = 'DeepPavlov/rubert-base-cased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)

r = sr.Recognizer()

question = {1:"Важно ли для вас наличие моря/океана?",
            2:"Вы предпочитаете быстрый темп жизни или размеренный темп?",
            3:"Какой климат вы бы предпочли:\n"
              "- холодный - средняя годовая температура меньше 10 градусов;\n"
              "- умеренный - средняя годовая температура от 10 до 20 градусов\n;"
              "- жаркий - средняя годовая температура более 20 градусов?",
            4:"Вы планируете переехать один или семьей?",
            5:"Вы планируете передвигаться на общественном транспорте или на своей машине?",
            6:"Где вы планируете снимать жилье: в центре или на окраине?",
            7:"Введите заработок, на который вы рассчитываете?"}


class Controller:
    ALL_ANSWER = {'lgbt':'False'}

    def control_migration(self):
        if len(self.ALL_ANSWER) == 8:
            rez = cm.calculate(self.ALL_ANSWER)
            self.ALL_ANSWER.clear()
            self.ALL_ANSWER =  {'lgbt':'False'}
            return rez
        else:
            print('ERROR')


    def control_cost_living(self, user_answers):
        self.__preparation_data_ccl(user_answers)
        print(user_answers)
        return cl.get_info_for_interface(user_answers)

    def __preparation_data_ccl(self, answer):
        if answer["transportation"] == "Taxi":
            answer["transportation"] = "такси"
        elif answer["transportation"] == "Own car":
            answer["transportation"] = "своя машина"
        elif answer["transportation"] == "Public transport":
            answer["transportation"] = "общественный транспорт"
        if answer["rent"] == "1-bed in city center":
            answer["rent"] = "1-к в центре"
        elif answer["rent"] == "3-bed in city center":
            answer["rent"] = "3-к в центре"
        elif answer["rent"] == "1-bed on the outskirts":
            answer["rent"] = "1-к на окраине"
        elif answer["rent"] == "3-bed on the outskirts":
            answer["rent"] = "3-к на окраине"
        elif answer["rent"] == "own house/flat":
            answer["rent"] = "своё жильё"


    def control_most_dangerous_places(self):
        return mdp.get_info_for_interface()

    def control_standard_of_living(self):
        return st.get_info_for_interface()

    def control_country_data(self, text):
        return cd.analize_country_name(text)

    def __get_sentence_embedding(self, sentence):
        inputs = tokenizer(sentence, return_tensors='pt', truncation=True, padding=True)
        with torch.no_grad():
            outputs = model(**inputs)
        embeddings = torch.mean(outputs.last_hidden_state, dim=1)
        return embeddings

    def analize(self, text, context):
        tokens_word = nltk.word_tokenize(text)
        for t in tokens_word:
            morph = pymorphy2.MorphAnalyzer()
            word = morph.parse(t)[0].normal_form
            if word in context:
                return True
        return False

    def preparation_data(self, question, answer):
        if question == 'Важно ли для вас наличие моря/океана?':
            self.ALL_ANSWER['water'] = self.__water_data(answer)
            return True
        elif question == 'Вы предпочитаете быстрый темп жизни или размеренный темп?':
            self.ALL_ANSWER['isBig'] = self.__is_big_data(answer)
            return True
        elif question == 'Какой климат вы бы предпочли:\n' \
                         '- холодный - средняя годовая температура меньше 10 градусов;\n' \
                         '- умеренный - средняя годовая температура от 10 до 20 градусов\n;' \
                         '- жаркий - средняя годовая температура более 20 градусов?':
            self.ALL_ANSWER['climat'] = self.__climate_data(answer)
            return True
        elif question == 'Вы планируете переехать один или семьей?':
            self.ALL_ANSWER['family'] = self.__family_data(answer)
            return True
        elif question == 'Вы планируете передвигаться на общественном транспорте или на своей машине?':
            self.ALL_ANSWER['transport'] = self.__transport_data(answer)
            return True
        elif question == 'Где вы планируете снимать жилье: в центре или на окраине?':
            self.ALL_ANSWER['flat'] = self.__flat_data(answer)
            return True
        elif question == 'Введите заработок, на который вы рассчитываете?':
            self.ALL_ANSWER['price'] = self.__price_data(answer, self.ALL_ANSWER['family'])
            return True
        return False

    def __water_data(self, text: str):
        sentence1 = 'Да мне важно наличие моря'
        sentence2 = 'Нет мне не важно наличие моря'
        embedding1 = self.__get_sentence_embedding(sentence1)
        embedding2 = self.__get_sentence_embedding(sentence2)
        embedding_text = self.__get_sentence_embedding(text)
        cosine_similarity_yes = torch.nn.functional.cosine_similarity(embedding1, embedding_text)
        cosine_similarity_no = torch.nn.functional.cosine_similarity(embedding2, embedding_text)

        if cosine_similarity_yes > cosine_similarity_no:
            return 'True'
        else:
            return 'False'


    def __is_big_data(self, text: str):
        sentence1 = 'Я бы хотел жить в городе с быстрым темпом жизни'
        sentence2 = 'Я бы хотел жить в городе с размеренным темпом жизни'
        embedding1 = self.__get_sentence_embedding(sentence1)
        embedding2 = self.__get_sentence_embedding(sentence2)
        embedding_text = self.__get_sentence_embedding(text)

        cosine_similarity_yes = torch.nn.functional.cosine_similarity(embedding1, embedding_text)
        cosine_similarity_no = torch.nn.functional.cosine_similarity(embedding2, embedding_text)

        if cosine_similarity_yes > cosine_similarity_no:
            return '1'
        else:
            return '2'

    def __climate_data(self, text: str):
        temp_int = None
        temp = text.split()
        for i in temp:
            try:
                temp_int = int(i)
            except:
                pass
        if type(temp_int) is int:
            if temp_int <= 10:
                return '1'
            elif 10 < temp_int <= 20:
                return '2'
            else:
                return '3'
        else:
            sentence1 = 'холодном климате'
            sentence2 = 'умеренном климате'
            sentence3 = 'жарком климате'
            # Получение эмбеддингов предложений
            embedding1 = self.__get_sentence_embedding(sentence1)
            embedding2 = self.__get_sentence_embedding(sentence2)
            embedding3 = self.__get_sentence_embedding(sentence3)
            embedding_text = self.__get_sentence_embedding(text)
            cosine_similarity = torch.nn.functional.cosine_similarity(embedding1, embedding_text)
            cosine_similarity1 = torch.nn.functional.cosine_similarity(embedding2, embedding_text)
            cosine_similarity2 = torch.nn.functional.cosine_similarity(embedding3, embedding_text)
            if cosine_similarity > cosine_similarity1 and cosine_similarity > cosine_similarity2:
                return '1'
            elif cosine_similarity1 > cosine_similarity and cosine_similarity1 > cosine_similarity2:
                return '2'
            else:
                return '3'

    def __family_data(self, text: str):
        sentence1 = 'Я перееду один'
        sentence2 = 'Мы переедем семьей'
        embedding1 = self.__get_sentence_embedding(sentence1)
        embedding2 = self.__get_sentence_embedding(sentence2)
        embedding_text = self.__get_sentence_embedding(text)
        cosine_similarity_one = torch.nn.functional.cosine_similarity(embedding1, embedding_text)
        cosine_similarity_family = torch.nn.functional.cosine_similarity(embedding2, embedding_text)

        if cosine_similarity_one > cosine_similarity_family:
            return '1'
        else:
            return '3'

    def __transport_data(self, text: str):
        sentence1 = 'своя машина'
        sentence2 = 'общественный транспорт'
        embedding1 = self.__get_sentence_embedding(sentence1)
        embedding2 = self.__get_sentence_embedding(sentence2)
        embedding_text = self.__get_sentence_embedding(text)
        cosine_similarity_car = torch.nn.functional.cosine_similarity(embedding1, embedding_text)
        cosine_similarity_transport = torch.nn.functional.cosine_similarity(embedding2, embedding_text)

        if cosine_similarity_car > cosine_similarity_transport:
            return 'своя машина'
        else:
            return 'общественный транспорт'

    def __flat_data(self, text: str):
        sentence1 = 'в центре'
        sentence2 = 'на периферии'
        embedding1 = self.__get_sentence_embedding(sentence1)
        embedding2 = self.__get_sentence_embedding(sentence2)
        embedding_text = self.__get_sentence_embedding(text)
        cosine_similarity_center = torch.nn.functional.cosine_similarity(embedding1, embedding_text)
        cosine_similarity_periphery = torch.nn.functional.cosine_similarity(embedding2, embedding_text)

        if cosine_similarity_center > cosine_similarity_periphery:
            return 'в центре'
        else:
            return 'на окраине'


    def voice_to_test(self, file):
        with sr.AudioFile(file) as source:
            audio_data = r.record(source)
            text = r.recognize_google(audio_data, language='ru-RU')
        return text

    def __price_data(self, text: str, family):
        string = re.sub(r'[a-zA-Zа-яА-Я$@#%^&*()+=_!~`/\\|]', '', text)
        lst = list(filter(lambda x: len(x) > 0, string.split("-")))
        try:
            temp_int = int(lst[0])
            if family == '1':
                if temp_int <= 1300:
                    return '1300'
                elif 1300 < temp_int <= 1800:
                    return '1300_1800'
                else:
                    return '1800'
            else:
                if temp_int <= 3600:
                    return '3600'
                elif 3600 < temp_int <= 5200:
                    return '3600_5200'
                else:
                    return '5200'
        except:
            if family == '1':
                return '1300_1800'
            else:
                return '3600_5200'



contrl = Controller()

