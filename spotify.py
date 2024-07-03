import spotipy
from spotipy.oauth2 import SpotifyOAuth
from compare_strings import difference_score

def build_spotify(client_id, client_secret):
    '''
    Build and return the Spotify client necessary for creating a new playlist, searching, 
    and adding songs given the client ID and client secret.
    '''
    sp = spotipy.Spotify(
        auth_manager = SpotifyOAuth(
            client_id = client_id, 
            client_secret = client_secret, 
            scope = 'playlist-modify-public',
            redirect_uri = 'http://localhost:5000'
        )
    ) 
    return sp

def get_spotify_track_uris(sp, tracks):
    '''
    Take a list of song titles and search them on Spotify, before returning their corresponding
    URIs.
    '''
    print('Found tracks on Spotify:')
    uris = []
    for track in tracks:
        # Search for the first 2 albums and first 2 tracks that come up and get the uri of 
        # the song that best matches the search query.
        search = sp.search(q = track, limit = 2, type = 'album,track')
        
        found_tracks = {}
        if 'albums' in search:
            for item in search['albums']['items']:
                uri = item['uri']
                if 'album' not in uri:
                    name = item['name']
                    artist = item['artists'][0]['name']
                    uri = item['uri']
                    found_tracks[artist + " " + name] = uri

        for item in search['tracks']['items']:
            name = item['name']
            artist = item['artists'][0]['name']
            uri = item['uri']
            found_tracks[artist + " " + name] = uri

        best_track = ''
        lowest_score = float('inf')
        for found_track in found_tracks.keys():
            if lowest_score > difference_score(found_track, track):
                lowest_score = difference_score(found_track, track)
                best_track = found_track

        if best_track != '':
            print(best_track)
            best_uri = found_tracks[best_track]
            uris.append(best_uri)

    return uris

def create_playlist(sp):
    '''
    Create a new playlist in the user's account under the name YtToSpotify Playlist.
    '''
    user_id = sp.me()['id']
    playlist = sp.user_playlist_create(user = user_id, name = 'YtToSpotify Playlist', public = True)
    playlist_id = playlist['id']

    return playlist_id

def add_tracks(sp, playlist_id, uris):
    '''
    Add songs to a playlist based on a given playlist ID and a list of URIs.
    '''
    split_uris = []
    for i in range(0, len(uris), 100):
        split_uris.append(uris[i:i + 100])

    for split_uri in split_uris:
        sp.playlist_add_items(playlist_id, split_uri)
    print('Done')