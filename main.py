import time
import requests
import json
from login import Loging

def auto_message_response(token):
    try:
        print("Messages")
        threads_url = CONFIG['enviorment'] + "/messaging/threads/"
        headers = {'Authorization': 'Bearer ' + token, 'Accept': "application/vnd.allegro.public.v1+json"}
        threads = requests.get(threads_url, headers=headers, verify=True).json()
        for thread in threads['threads']:
            messages_url = CONFIG['enviorment'] + "/messaging/threads/" + thread['id'] + "/messages"
            message = requests.get(messages_url, headers=headers, verify=True).json()
            if message['messages'][0]['author']['login'] != CONFIG['mylogin']:
                response = {
                    "text": "Dzień dobry, \nDziękujemy za wiadomość. Odpowiemy na nią w możliwie najkrótszym czasie.\nPozdrawiamy,\nBikiniPL"
                }

                print(requests.post(messages_url, headers=headers, verify=True, data=json.dumps(response)).json())

    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


def auto_dispute_response(token):
    try:
        print("Disputes")
        disputes_url = CONFIG['enviorment'] + "/sale/disputes"
        headers = {'Authorization': 'Bearer ' + token, 'Accept': "application/vnd.allegro.public.v1+json"}
        disputes = requests.get(disputes_url, headers=headers, verify=True).json()
        for dispute in disputes['disputes']:
            dispute_messages_url = CONFIG['enviorment'] + "/sale/disputes/" + dispute['id'] + "/messages"
            dispute_messages = requests.get(dispute_messages_url, headers=headers, verify=True).json()
            role = dispute_messages['messages'][0]['author']['role']
            if role != "SELLER" and role != "ADMIN" and role != "SYSTEM":
                print(dispute_messages['messages'][0]['author']['login'])
                response = {
                    "text": "Dzień dobry, \nDziękujemy za wiadomość. Odpowiemy na nią w możliwie najkrótszym czasie.\nPozdrawiamy,\nBikiniPL",
                    "type": "REGULAR"
                }
                print(requests.post(dispute_messages_url, headers=headers, verify=True, data=json.dumps(response)).json())

    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)


def initialize(enviorment):
    try:
        with open('config.json') as f:
            data = json.load(f)
            global CONFIG
            CONFIG = data[enviorment]
    except FileNotFoundError:
        print("File not found")
        exit(-1)


def main():
    enviorment = "allegro"
    initialize(enviorment)
    x = Loging(enviorment)

    while True:
        x.get_new_token_pair()
        auto_message_response(x.access_token)
        auto_dispute_response(x.access_token)
        time.sleep(60 * 60)



if __name__ == "__main__":
    main()
