# Description
Convert regular Youtube playlists containing songs into Spotify playlists.

This application works by taking a YouTube playlist URL and finding the same songs on Spotify before compiling them together into a new Spotify playlist. This requires that you sign into your Spotify account in order for the new playlist to be created under your account.

Since the application uses the YouTube data API and Spotify Web API, you will need an API key for YouTube and a client ID and client secret for Spotify. This is quick to set up and the instructions on how to do so can be found below.

# Set Up
### Requirements
Make sure you install the required libraries by running in the terminal: ```pip3 install -r requirements.txt```

### When running the application
In order to use the application, you will first need:
* A YouTube API Key
* A Spotify Client ID
* A Spotify Client Secret
* A YouTube Playlist URL
  
### How to Get YouTube API Key
1) Go to https://console.cloud.google.com/apis/credentials
2) Click on '+ Create Credientials' and select 'API key'.

https://developers.google.com/youtube/registering_an_application

### How to Get Spotify Client ID and Client Secret
1) Go to https://developer.spotify.com/dashboard
2) Click on 'Create App' and give the app any name and description you like.
3) Find your newly created app and open it.
4) The Spotify Client Id and Client Secret will be found under Settings > Basic Information.

https://developer.spotify.com/documentation/web-api/concepts/apps

# How to Run
1) Run the Flask app ```app.py```
2) Navigate in your browser to ```localhost:5000```
3) Sign in to Spotify when prompted
4) Enter the YouTube API key, Spotify Client ID, Spotify Client Secret, and YouTube playlist URL that you would like to convert.
5) Press 'Convert'
6) Wait for the application to finish. The songs discovered on Spotify will be displayed in the terminal.
7) When finished, find your newly created playlist in Spotify under the name 'YTToSpotify Playlist'.
