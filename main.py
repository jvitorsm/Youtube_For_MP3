import os.path
from pytube import YouTube

yt = YouTube('Youtube link')

videos = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

audio = yt.streams.filter(only_audio=True).first()
download_file = videos.download()
base, ext = os.path.splitext(download_file)
new_file = base + '.mp4'
os.rename(videos,new_file)
print('...')
# caso queira baixar video, coloque em comentario as linhas 8 a 12