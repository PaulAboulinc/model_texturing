import os
import uuid

from flask import Flask, send_file, request
import texture_monkey

app = Flask(__name__)


@app.route('/texture/<model>', methods=['POST'])
def texture_model(model):
    build_folder = 'build_' + str(uuid.uuid4())
    if model == 'monkey' and 'screenshot' in request.files:
        os.mkdir(build_folder)
        request.files['screenshot'].save(os.path.join(build_folder, 'screenshot.jpg'))
        return texture_monkey.color_monkey(build_folder)

    return ''


@app.route('/get/model/<build>/<model>', methods=['GET'])
def get_build(build, model):
    return send_file(build + '/' + model, download_name=model)


@app.route('/test', methods=['GET'])
def test():
    return "hello word"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000)
