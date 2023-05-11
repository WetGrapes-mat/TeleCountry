from flask import Flask, request, jsonify
from flask_cors import CORS
from controller.controller import contrl, question
from controller.context_data import migration_list, country_data

from neo4j_country_db import cost_living_db, country_education_db, country_migration_db, country_resorts_db, \
    country_tourism_db, \
    country_ski_resorts_db, most_dangerous_places_db, standart_living_db

import pyaudio
import wave
import time


app = Flask(__name__)
CORS(app)

FLAG_VOICE = True



@app.route('/chat', methods=['POST'])
def chat():
    message = request.json
    if contrl.analize(message['answer'], migration_list):
        return jsonify({"result":question[len(contrl.ALL_ANSWER)]})
    state = contrl.preparation_data(message['question'], message['answer'])
    if state and len(contrl.ALL_ANSWER) != 8:
        return jsonify({'result':question[len(contrl.ALL_ANSWER)]})
    if len(contrl.ALL_ANSWER) == 8:
        result = contrl.control_migration()
        return jsonify({'result': result})
    if contrl.analize(message['answer'], country_data.keys()):
        result  = contrl.control_country_data(message['answer'])
        return jsonify({"result":result})
    if not state:
        return jsonify({"result": "Я не могу помочь с этим вопросом"})

@app.route('/voice', methods=['POST'])
def voice_chat():
    file = request.files['file']
    file.save('server/temp.wav')
    text = contrl.voice_to_test('server/temp.wav')
    if contrl.analize(text, migration_list):
        return jsonify({"result":question[len(contrl.ALL_ANSWER)]})
    if contrl.analize(text, country_data.keys()):
        result = contrl.control_country_data(text)
        return jsonify({"result": result})
    state = contrl.preparation_data(question[len(contrl.ALL_ANSWER)], text)
    if state and len(contrl.ALL_ANSWER) != 8:
        return jsonify({'result':question[len(contrl.ALL_ANSWER)]})
    if len(contrl.ALL_ANSWER) == 8:
        result = contrl.control_migration()
        return jsonify({'result': result})

    if not state:
        return jsonify({"result": "Я не могу помочь с этим вопросом"})

@app.route('/start_voice', methods=['GET'])
def start_voice():
    global FLAG_VOICE
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    WAVE_OUTPUT_FILENAME = "server/output.wav"

    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    frames = []
    print("Recording...")
    while FLAG_VOICE:
        data = stream.read(CHUNK)
        frames.append(data)
    print("Finished recording.")
    stream.stop_stream()
    stream.close()
    audio.terminate()
    wave_file = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wave_file.setnchannels(CHANNELS)
    wave_file.setsampwidth(audio.get_sample_size(FORMAT))
    wave_file.setframerate(RATE)
    wave_file.writeframes(b''.join(frames))
    wave_file.close()
    text = contrl.voice_to_test(WAVE_OUTPUT_FILENAME )
    print(text)
    return jsonify({"voice":text})

@app.route('/stop_voice', methods=['GET'])
def stop_voice():
    global FLAG_VOICE
    FLAG_VOICE = False
    time.sleep(1)
    FLAG_VOICE = True
    return jsonify({"voice":"Finished recording"})

@app.route('/cost_living', methods=['POST'])
def cost_living():
    input_data = request.json
    result = contrl.control_cost_living(input_data)
    return jsonify(result)


@app.route('/most_dangerous_places', methods=['GET'])
def most_dangerous_places():
    result = contrl.control_most_dangerous_places()
    return jsonify(result)


@app.route('/standard_of_living', methods=['GET'])
def standard_of_living():
    result = contrl.control_standard_of_living()
    return jsonify(result)


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