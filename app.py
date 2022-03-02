import os
import uuid

from flask import Flask, send_file, request
import texture_monkey
import texture_snake

app = Flask(__name__)


@app.route('/texture/<model>', methods=['POST'])
def texture_model(model):
    build_folder = 'build_' + str(uuid.uuid4())
    if 'screenshot' in request.files:
        os.mkdir(build_folder)
        request.files['screenshot'].save(os.path.join(build_folder, 'screenshot.jpg'))
        if model == 'monkey':
            return texture_monkey.color_monkey(build_folder)
        if model == 'snake':
            return texture_snake.color_snake(build_folder)
        # if model == 'rhinoceros':
            # return texture_rhinoceros.color_rhinoceros(build_folder)

    return ''


@app.route('/get/model/<build>/<model>', methods=['GET'])
def get_build(build, model):
    return send_file(build + '/' + model, download_name=model)


@app.route('/test', methods=['GET'])
def test():
    return "hello word"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000)
