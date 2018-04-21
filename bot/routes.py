from bot import app
from codechef import codechef_scraper
from os import environ
import json
import requests
from flask import request


@app.route("/newMessage", methods=['POST', 'GET'])
def new_message_handler():
    update_json = request.get_json()

    chat_id = update_json["message"]["chat"]["id"]
    codechef_contests = codechef_scraper()
    payload = {
        "chat_id": chat_id,
        "text": codechef_contests
    }

    resp = requests.post(environ.get("bot_base_url") + "/sendMessage", payload)
    return "Request received"


@app.route("/")
def hello():
    return "Working so far"
