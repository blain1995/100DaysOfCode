# ----------------- Billboard 100 time machine playlist -----------------
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

client_id = os.environ.get("SPOTIFY_CLIENT_ID")
client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")

# --------------- Scrape Billboard 100 for date of choice ---------------
date_of_interest = input("Which year do you want to travel to? Please respond in the following format YYYY-MM-DD: ")
response = requests.get(url=f"https://billboard.com/charts/hot-100/{date_of_interest}")
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, "html.parser")

song_titles = [song.text for song in soup.find_all(name="span", class_="chart-element__information__song")]
print(song_titles)
# ------------------------ Make Spotify playlist ------------------------

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
print(user_id)

year = date_of_interest.split("-")[0]
queries = [f"track: {song} year: {year}" for song in song_titles]
song_uri = []

for song in queries:
    result = sp.search(q=song, type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uri.append(uri)
    except IndexError:
        print(f"{song} is not available on Spotify.")

print(song_uri)

playlist = sp.user_playlist_create(user=user_id, name=f"{year} Billboard top 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uri)