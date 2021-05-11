import json

import flask
from flask import Flask, jsonify, request

import sentences_server

app = Flask(__name__)


def check_api_key(request):
    token = request.headers.get('Authorization')
    if token != 'B*TyX&y7bDd5xLXYNw5iaN6X7%QAiqTQ#9nvtgMX3X2risrD64ew!*Q9*ky3PRvrSWYE6euykHycNzQqmViKo%XfoyTCSrJTFSUK*ycP2P$!Psn55iJT4@b4tdxw*XA!':
        flask.abort(401)


def get_sentence(request):
    data = json.loads(request.data.decode('utf8').replace("'", '"'))
    data = str(data['sentence']).lower()
    return data


@app.route("/send", methods=['POST'])
def hello():
    check_api_key(request)
    data = get_sentence(request)
    print(data)

    # add support for multiples actions in one sentence (two actions here)
    if " et " in data:
        phrases = data.split(" et ")

        response = sentences_server.recogniseSentence(phrases[0]) + "et" + sentences_server.recogniseSentence(phrases[1])
        return jsonify(response)
    else:
        return jsonify(sentences_server.recogniseSentence(data))


if __name__ == '__main__':
    sentences_server.registerSentences()
    app.run()

