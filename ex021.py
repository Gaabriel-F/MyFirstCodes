import pygame

# Inicialize o pygame
pygame.init()

# Carregue o arquivo de som
pygame.mixer.music.load("/storage/emulated/0/snaptube/download/snapaudio/win_audio.mp3")

# Inicie a reprodução
pygame.mixer.music.play()

# Espere até que o som termine de tocar
while pygame.mixer.music.get_busy():
    pass

# Encerre o pygame
pygame.quit()
