import requests
from twilio.rest import Client
import time
from datetime import datetime
import json

# Charger la configuration depuis config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)

ACCOUNT_SID = config["account_sid"]
AUTH_TOKEN = config["auth_token"]
TWILIO_PHONE_NUMBER = config["twilio_phone_number"]
YOUR_PHONE_NUMBER = config["your_phone_number"]

# Configuration des requêtes
HEADERS = {
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Accept-Language": "fr-FR,fr;q=0.9",
    "Sec-Ch-Ua": "\"Not?A_Brand\";v=\"99\", \"Chromium\";v=\"130\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.70 Safari/537.36",
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://www.tradingcard6107.fr",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.tradingcard6107.fr/pokemon/",
    "Accept-Encoding": "gzip, deflate, br",
    "Priority": "u=1, i"
}

COOKIES = {
    "session": "ian8eierf6jsa2m0868k5pnknn",
    "allowToCommentBlog": "true",
    "crisp-client%2Fsession%2Fa32927ee-9498-4a89-a0d8-596d252776cf": "session_622be7f8-803c-4dcb-ae54-883710eebba7"
}

URL = "https://www.tradingcard6107.fr/panier.php?ajax"

# Produits à surveiller
PRODUCTS = [
    {"id": 485, "name": "Product 485"},
    {"id": 487, "name": "Product 487"}
]

def check_availability():
    for product in PRODUCTS:
        payload = f"id_prod={product['id']}&nb_prod=1"
        try:
            response = requests.post(URL, headers=HEADERS, cookies=COOKIES, data=payload)
            if response.status_code == 200:
                if "Désolé, nous n'avons plus ce produit en stock pour le moment" not in response.text:
                    print(f"{datetime.now().time()} : Le produit {product['name']} est disponible!")
                    send_sms(product['name'])
                else:
                    print(f"{datetime.now().time()} : Le produit {product['name']} n'est pas disponible.")
            else:
                print(f"{datetime.now().time()} : Erreur {response.status_code} pour {product['name']}.")
        except Exception as e:
            print(f"{datetime.now().time()} : Erreur lors de la requête pour {product['name']}: {e}")
        time.sleep(3)  # Pause pour éviter de surcharger le serveur

def send_sms(product_name):
    try:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(
            body=f"PRODUIT DISPONIBLE : {product_name}",
            from_=TWILIO_PHONE_NUMBER,
            to=YOUR_PHONE_NUMBER
        )
        print(f"{datetime.now().time()} : SMS envoyé pour {product_name}. SID: {message.sid}")
    except Exception as e:
        print(f"{datetime.now().time()} : Erreur lors de l'envoi du SMS pour {product_name}: {e}")

if __name__ == "__main__":
    while True:
        check_availability()