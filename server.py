from flask import Flask, request, jsonify
from flask_cors import CORS
from controller.controller import contrl
from neo4j_country_db import cost_living_db, country_education_db, country_migration_db, country_resorts_db, \
    country_tourism_db, \
    country_ski_resorts_db, most_dangerous_places_db, standart_living_db

app = Flask(__name__)
CORS(app)
FLAG_MIGRATION = False

@app.route('/migration', methods=['POST'])
def migration():
    sentence = request.json['sentence']
    result = contrl.control_migration(sentence)
    return jsonify({'result': result})

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json
    #TODO какая то логика фильтрации миграции
    if FLAG_MIGRATION:
        contrl.preparation_data(message['question'], message['answer'])
        if len(contrl.ALL_ANSWER) == 8:
            result = contrl.control_migration()
            return jsonify({'result': result})

    # result = contrl.control_migration(sentence)
    # return jsonify({'result': result})


@app.route('/cost_living', methods=['POST'])
def cost_living():
    sentence = request.json['sentence']
    result = contrl.control_cost_living(sentence)
    return jsonify({'result': result})


@app.route('/education', methods=['POST'])
def education():
    sentence = request.json['sentence']
    result = contrl.control_education(sentence)
    return jsonify({'result': result})


@app.route('/most_dangerous_places', methods=['POST'])
def most_dangerous_places():
    sentence = request.json['sentence']
    result = contrl.control_most_dangerous_places(sentence)
    return jsonify({'result': result})


@app.route('/standard_of_living', methods=['POST'])
def standard_of_living():
    sentence = request.json['sentence']
    result = contrl.control_standard_of_living()
    return jsonify({'result': result})


if __name__ == '__main__':
    # contrl.preparation_data('Важно ли для вас наличие моря/океана?', 'Нет')
    # contrl.preparation_data('Вы предпочитаете быстрый темп жизни или размеренный темп?', 'Быстрый')
    # contrl.preparation_data('Какой климат вы бы предпочли:\n' \
    #                          '- холодный - средняя годовая температура меньше 10 градусов;\n' \
    #                          '- умеренный - средняя годовая температура от 10 до 20 градусов\n;' \
    #                          '- жаркий - средняя годовая температура более 20 градусов?', '20 градусов')
    # contrl.preparation_data('Вы планируете переехать один или семьей?', 'один')
    # contrl.preparation_data('Вы планируете передвигаться на общественном транспорте или на своей машине?', 'на автобусе')
    # contrl.preparation_data('Где вы планируете снимать жилье: в центре или на окраине?', 'в центре')
    # contrl.preparation_data('Введите заработок, на который вы рассчитываете?', '2454$')
    # print(contrl.control_migration())


    # app.run()
    # cost_living_db.close()
    # country_education_db.close()
    # country_migration_db.close()
    # country_resorts_db.close()
    # country_ski_resorts_db.close()
    # country_tourism_db.close()
    # most_dangerous_places_db.close()
    # standart_living_db.close()
    pass
