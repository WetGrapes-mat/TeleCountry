from flask import Flask, request, jsonify
from flask_cors import CORS
from controller.controller import contrl
from neo4j_country_db import cost_living_db, country_education_db, country_migration_db, country_resorts_db, \
    country_tourism_db, \
    country_ski_resorts_db, most_dangerous_places_db, standart_living_db

app = Flask(__name__)
CORS(app)


@app.route('/migration', methods=['POST'])
def migration():
    sentence = request.json['sentence']
    result = contrl.control_migration(sentence)
    return jsonify({'result': result})


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
    app.run()
    cost_living_db.close()
    country_education_db.close()
    country_migration_db.close()
    country_resorts_db.close()
    country_ski_resorts_db.close()
    country_tourism_db.close()
    most_dangerous_places_db.close()
    standart_living_db.close()
