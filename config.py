import os
from atproto import Client

class Config:
    BLUESKY_USERNAME = os.getenv('victorbrandaao.bsky.social')
    BLUESKY_PASSWORD = os.getenv('Brandao0510@')

client = Client(base_url='https://bsky.social')
client.login(Config.BLUESKY_USERNAME, Config.BLUESKY_PASSWORD)
