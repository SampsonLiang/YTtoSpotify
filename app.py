from flask import Flask, render_template, request
import youtube
import spotify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods = ['POST'])
def convert_playlist():
    youtube_api_key = request.form.get('youtube_api_key')
    spotify_client_id = request.form.get('spotify_client_id')
    spotify_client_secret = request.form.get('spotify_client_secret')
    youtube_playlist_url = request.form.get('youtube_playlist_url')

    try:
        yt = youtube.build_youtube(youtube_api_key)
        tracks = youtube.get_playlist_items(yt, youtube_playlist_url)
        
    except Exception:
        failure_message ='Something went wrong...Youtube URL or API key is invalid.'
        return render_template('index.html', message = failure_message, success = False)
    
    try:
        sp = spotify.build_spotify(spotify_client_id, spotify_client_secret)
        uris = spotify.get_spotify_track_uris(sp, tracks)
        playlist_id = spotify.create_playlist(sp)

    except Exception:
        failure_message = 'Something went wrong...Spotify Client ID or Secret is invalid.'
        return render_template('index.html', message = failure_message, success = False)
    
    try:
        spotify.add_tracks(sp, playlist_id, uris)

    except Exception:
        failure_message = 'Something went wrong...Spotify API quota limit may be reached.'
        return render_template('index.html', message = failure_message, success = False)  

    success_message = 'Conversion successful! Please find your new playlist in Spotify under the name "YtToSpotify Playlist"'
    return render_template('index.html', message = success_message, success = True)

if __name__ == '__main__':
    app.run(debug=True)