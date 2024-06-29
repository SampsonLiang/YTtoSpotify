from googleapiclient.discovery import build

def build_youtube(api_key):
    '''
    Build and return the YouTube client necessary for extracting playlist items using 
    the given YouTube API Key.
    '''
    youtube = build('youtube', 'v3', developerKey = api_key)
    return youtube

def get_playlist_items(youtube, url):
    '''
    Get the titles of all videos in a playlist and return them as a list.
    '''
    playlistId = url[38:]
    max_results = 50
    request = youtube.playlistItems().list(part = 'snippet', playlistId = playlistId, maxResults = max_results)
    result = request.execute()

    tracks = []
    finished = False
    while not finished:
        for item in result['items']:
            if not item['snippet']['title'] == 'Private video':
                tracks.append(item['snippet']['title'])

        # Add all additional pages of videos since the limit is 50 videos a page per API call
        if 'nextPageToken' in result and max_results >= 50:
            request = youtube.playlistItems().list(part = 'snippet', playlistId = playlistId, maxResults = 50, pageToken = result['nextPageToken'])
            result = request.execute()
        else:
            finished = True

    return tracks