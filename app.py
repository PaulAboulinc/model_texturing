from flask import Flask, send_file
import texture_monkey

app = Flask(__name__)


@app.route('/get/texture/<model>', methods=['POST'])
def texture_model(model):
    if model == 'monkey':
        texture_monkey.color_monkey()
        return send_file("build/monkey.gltf", mimetype='application/octet-stream')

    return 0


@app.route('/test', methods=['GET'])
def test():
    return "hello word"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000)
