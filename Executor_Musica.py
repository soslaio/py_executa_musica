#copiar e colar o arquivo de música no Python. Clica com botão direito em cima do nome do projeto e seleciona paste.
from playsound import playsound
nome_da_musica = input('Digite o nome da música: ')
playsound(nome_da_musica)
print('Tocando Musica.mp3')
