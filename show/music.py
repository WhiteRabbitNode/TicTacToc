import pygame


# play music from specified file path
def music(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(1)
