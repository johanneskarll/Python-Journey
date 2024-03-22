import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
load_dotenv()

clientid = os.getenv("SPOTIFYID")
clientsecret = os.getenv("SPOTIFYSECRET")
redirecturl="http://example.com"
spotifyapi = "https://api.spotify.com"


travelto = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ').split("-")
traveltoyear = travelto[0]
traveltomonth = travelto[1]
traveltodate = travelto[2]

# scraping
billboardlink = f"https://www.billboard.com/charts/hot-100/{traveltoyear}-{traveltomonth}-{traveltodate}/"
response = requests.get(billboardlink)
soup = BeautifulSoup(response.text, "html.parser")


songtitle = soup.select(selector="li ul li h3")
songlist = [song.get_text().strip() for song in songtitle]

# aunthentication + get uri
scope = "playlist-modify-private" 
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clientid,client_secret=clientsecret, scope=scope, redirect_uri=redirecturl, cache_path="token.txt"))
userid = sp.current_user()['id']

song_uris = []
for song in songlist:
    result = sp.search(q=f"track:{song} year:{traveltoyear}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# creating playlist + add tracks using uri
createplaylist = sp.user_playlist_create(user=userid,name=f"{traveltoyear}-{traveltomonth}-{traveltodate} Billboard 100", public=False)
playlistid = createplaylist['id']
sp.playlist_add_items(playlist_id=playlistid,items=song_uris)