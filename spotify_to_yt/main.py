import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pytube import Search

scope = "user-libary-read"

while True:
    playlist_input = input("Playlist Link > ")

    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id="01a1893b6f08433da314c6324e048c42", 
                                                                         client_secret="a20ed7d7544f4b54ae5633c13c7429ed"))

    playlist = sp.playlist_tracks(playlist_input)

    song_names = [f"{item['track']['name']} by {item['track']['artists'][0]['name']} original" for item in playlist["items"]]
    search_results = []

    for song in song_names:
        print(f"Searching {song}...")
        search = Search(song)
        search_results.append(search.results[0].watch_url)
        print(f"Found {search.results[0].watch_url}.")

    link_endings = [link[-11:] for link in search_results]

    yt_list = f"\nPlaylist Link: http://www.youtube.com/watch_videos?video_ids={','.join(link for link in link_endings)}\n"

    print(yt_list)
