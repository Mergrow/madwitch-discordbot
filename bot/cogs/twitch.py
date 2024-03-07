import requests
import os
from discord.ext import tasks
import asyncio
from cogs.variables import *

CLIENT_ID = os.environ.get("twitch_client")
CLIENT_SECRET = os.environ.get("twitch_secret")
STREAMER_NAME = ["mergrow_", "nani_naniii"]
CHECK_INTERVAL = "5"
CHANNEL_ID = "962651845308874762"
last_notification_times = {}




def get_access_token(client_id, client_secret):
    url = "https://id.twitch.tv/oauth2/token"
    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }
    response = requests.post(url, params=payload)
    data = response.json()
    return data['access_token']

access_token = get_access_token(CLIENT_ID, CLIENT_SECRET)
headers = {
    'Client-ID': CLIENT_ID,
    'Authorization': f'Bearer {access_token}'
}
@tasks.loop(seconds=int(CHECK_INTERVAL))
async def check_streamer_status():
    channel = client.get_channel(int(CHANNEL_ID))
    current_time = asyncio.get_event_loop().time()  # Pegue o horário atual do loop de eventos

    for streamer in STREAMER_NAME:
        # Se o streamer foi notificado recentemente (dentro da última hora), pule
        if streamer in last_notification_times and current_time - last_notification_times[streamer] < 3600:
            continue

        # Obtenha o ID do usuário com base no nome do usuário
        user_url = f'https://api.twitch.tv/helix/users?login={streamer}'
        user_response = requests.get(user_url, headers=headers)
        user_data = user_response.json()
        STREAMER_URL = f"https://twitch.tv/{streamer}"

        if not user_data['data']:
            print(f"Streamer {streamer} not found.")
            continue

        user_id = user_data['data'][0]['id']

        # Verifique o status da transmissão
        stream_url = f'https://api.twitch.tv/helix/streams?user_id={user_id}'
        stream_response = requests.get(stream_url, headers=headers)
        stream_data = stream_response.json()

        if stream_data['data']:
            print(STREAMER_URL)
            await channel.send((f"**{STREAMER_URL} ficou on, segue lá @everyone!**"), silent=True)
            
            # Atualize o horário da última notificação para o streamer
            last_notification_times[streamer] = current_time


