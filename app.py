from flask import Flask, jsonify
import random
import requests
from apscheduler.schedulers.background import BackgroundScheduler
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Carrega as frases motivacionais
def load_quotes():
    with open('quotes.txt', 'r') as file:
        return file.readlines()

quotes = load_quotes()

@app.route('/')
def daily_motivation():
    if quotes:  # Verifica se a lista de frases não está vazia
        return random.choice(quotes).strip()
    else:
        return "No quotes available."


@app.route('/add_quote', methods=['POST'])
def add_quote():
    # Implementar a lógica para adicionar uma nova frase
    pass

# Função para verificar menções no Bluesky
def check_mentions():
    response = requests.get('https://bsky.social/api/mentions', auth=(app.config['victorbrandaao'], app.config['Brandao0510@']))
    if response.status_code == 200:
        mentions = response.json()
        for mention in mentions:
            if '@InspireBot' in mention['text']:
                handle_command(mention['text'], mention['user'])

# Função para responder a comandos como #quote
def handle_command(text, user):
    if '#quote' in text:
        respond_to_mention(user, daily_motivation())

def respond_to_mention(user, message):
    reply = f"@{user} {message}"
    requests.post('https://bsky.social/api/post', json={"message": reply}, auth=(app.config['BLUESKY_USERNAME'], app.config['BLUESKY_PASSWORD']))

# Scheduler para verificar menções a cada minuto
scheduler = BackgroundScheduler()

def scheduled_task():
    check_mentions()

scheduler.add_job(scheduled_task, 'interval', minutes=1)
scheduler.start()

if __name__ == '__main__':
    app.run(debug=True)
