import requests
from dotenv import load_dotenv
import os


load_dotenv()

test_key="3cEYpjA9oz9GiPac4AsH4n"

#returns and auth token valid for one hour
def get_token():
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": os.getenv("CLIENT_ID"), 
        "client_secret": os.getenv("CLIENT_SECRET") 
    }
    
    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        return response.json()['access_token'] 
    else:
        response.raise_for_status()

#returns a  playlist from playlist id
def get_playlist(playlist_id):
    token = get_token()
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def get_tracks(playlist_id):
    data = get_playlist(playlist_id)
    return data['tracks']

# playlist_data = get_playlist(test_key)
# print(playlist_data)

# print(get_token())

#print(get_tracks(test_key))