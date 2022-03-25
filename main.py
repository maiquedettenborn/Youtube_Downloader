#importando o pacote YouTube do módulo pytube
from pytube import YouTube
import datetime 

#link do video do youtube
#video = YouTube('https://www.youtube.com/watch?v=LXb3EKWsInQ&t=148s&ab_channel=Jacob%2BKatieSchwarz') #video 4k
#video = YouTube('https://www.youtube.com/watch?v=SMRVFIrPevA&ab_channel=CalvinHarris') #video calvin harris
video = YouTube('https://www.youtube.com/watch?v=vX2vsvdq8nw&ab_channel=4KClipsAndTrailers')


#definições de variaveis
video_nome = video.title                #nome do video
video_image = video.thumbnail_url       #imagem do video
video_views = video.views               #números de views
video_tempo_segundos = video.length     #tempo de video em segundos
video_lista_streams = video.streams     #lista de possibilidades de download's

video_tempo_convertido = datetime.timedelta(seconds=video_tempo_segundos)   #converte otempo de video de segundos para (hh:mm:ss)

print()
print()
print('Nome do vídeo:',video_nome)
print('url da capa do vídeo:', video_image)
print('Número de visualizações do vídeo:', video_views)
print('Tempo de vídeo (hh:mm:ss):', video_tempo_convertido)
#print(video_tempo//60,':', video_tempo%60)
'''for c in range (0, len(video_lista_streams)):
    print(video_lista_streams[c])'''
print()