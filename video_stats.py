import json
import requests

API_KEY = "AIzaSyALCGXqkFL3NciCBkGFhuzG7spkWQzBNj8"
CHANNEL_HANDLE = "Mrbeast"


def get_playlist_id():
    try:

        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"

        response = requests.get(url)

        print (response)

        data = response.json()

        channel_items = data["items"][0]

        channel_playlistId = channel_items["contentDetails"]["relatedPlaylists"]["uploads"]
        print (channel_playlistId)
    except requests.exceptions.RequestException as e:
        raise e



if __name__ == "__main__":
    get_playlist_id()