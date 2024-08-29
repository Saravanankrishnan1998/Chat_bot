from flask import Flask, render_template, request, jsonify
from chatbot import nltk_chatBot

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_input = request.args.get('msg')
    if not isinstance(user_input, str):
        user_input = str(user_input)
    response = nltk_chatBot(user_input)
    return jsonify(response)

if __name__ == "__main__":
    app.run()
    