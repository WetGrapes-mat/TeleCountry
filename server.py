from flask import Flask, request, jsonify
from flask_cors import CORS
from controller.controller import contrl, question
from neo4j_country_db import cost_living_db, country_education_db, country_migration_db, country_resorts_db, \
    country_tourism_db, \
    country_ski_resorts_db, most_dangerous_places_db, standart_living_db

app = Flask(__name__)
CORS(app)


@app.route('/chat', methods=['POST'])
def chat():
    message = request.json
    if contrl.analize(message['answer']):
        return jsonify(question)
    contrl.preparation_data(message['question'], message['answer'])
    if len(contrl.ALL_ANSWER) == 8:
        result = contrl.control_migration()
        return jsonify({'result': result})

@app.route('/cost_living', methods=['POST'])
def cost_living():
    input_data = request.json
    result = contrl.control_cost_living(input_data)
    return jsonify({'result': result})


@app.route('/most_dangerous_places', methods=['GET'])
def most_dangerous_places():
    result = contrl.control_most_dangerous_places()
    return jsonify({'result': result})


@app.route('/standard_of_living', methods=['GET'])
def standard_of_living():
    result = contrl.control_standard_of_living()
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run()
    cost_living_db.close()
    country_education_db.close()
    country_migration_db.close()
    country_resorts_db.close()
    country_ski_resorts_db.close()
    country_tourism_db.close()
    most_dangerous_places_db.close()
    standart_living_db.close()