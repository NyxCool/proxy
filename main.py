from flask import Flask, request
import requests

app = Flask('app')


@app.route('/')
def hello_world():
    return "Fui pingado"


@app.route('/send', methods={"POST"})
def send_webhook():
    content = request.get_json()
    response = requests.post(url=content["url"], json=content["json"])
    print("post")
    return response.content


print("started")
app.run(host='0.0.0.0', port=8080)
