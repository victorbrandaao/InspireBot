from flask import Flask, jsonify
import random
from apscheduler.schedulers.background import BackgroundScheduler
from atproto import Client
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Inicializa o cliente Bluesky
client = Client(base_url='https://bsky.social')
client.login(app.config['BLUESKY_USERNAME'], app.config['BLUESKY_PASSWORD'])


# Carrega as frases motivacionais
def load_quotes():
    try:
        with open('quotes.txt', 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []


quotes = load_quotes()


@app.route('/')
def daily_motivation():
    if quotes:
        return random.choice(quotes).strip()
    else:
        return "No quotes available."


@app.route('/add_quote', methods=['POST'])
def add_quote():
    # Implementar a lógica para adicionar uma nova frase
    pass


# Função para verificar menções no Bluesky
def check_mentions():
    mentions = client.get('https://bsky.social/api/mentions')  # URL fictícia; ajuste conforme a API real

    if mentions:
        for mention in mentions:
            if '@InspireBot' in mention['text']:
                handle_command(mention['text'], mention['user'])


# Função para responder a comandos como #quote
def handle_command(text, user):
    if '#quote' in text:
        respond_to_mention(user, daily_motivation())


def respond_to_mention(user, message):
    reply = f"@{user} {message}"
    # Faz o post utilizando o SDK do Bluesky
    post = client.send_post(reply)
    print(f"Post enviado: {post.uri}")


# Scheduler para verificar menções a cada minuto
scheduler = BackgroundScheduler()


def scheduled_task():
    check_mentions()


scheduler.add_job(scheduled_task, 'interval', minutes=1)
scheduler.start()

if __name__ == '__main__':
    app.run(debug=True)
