import os
try:
  from pytube import YouTube
  from pytube import Playlist
except Exception as e:
  print('missing modules {}'.format(e))

print('Youtube playlist to mp3 files')

#url
url = input('Enter Playist URL: ')

#playlist
playlist = Playlist(url)
print(f'Playlist Name: {playlist.title}')

#download path (new folder for playlist)
path = os.path.dirname(os.path.abspath(__file__)) + '\\'+ playlist.title
print(f'Downloading at: {path}')

#download all videos from playlist
for video in playlist.videos:
  title=video.title
  print(f'Downloading: {title}')
  out_file = video.streams.filter(only_audio=True).first().download(output_path=path)

  #change from mp4 to mp3
  base, ext = os.path.splitext(out_file) 
  new_file = base + '.mp3'
  os.rename(out_file, new_file) 

print('Playlist Download Complete')
