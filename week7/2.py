import pygame 
import os 

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Music')

music_folder = "playlist"
playlist = [os.path.join(music_folder, file) for file in os.listdir(music_folder) if file.endswith('.mp3')]

cur = 0
pygame.mixer.music.load(playlist[cur])

def play():
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def next():
    global cur 
    cur = (cur + 1) % len(playlist)
    pygame.mixer.music.load(playlist[cur])
    pygame.mixer.music.play()

def prev():
    global cur
    cur = (cur - 1) % len(playlist) 
    pygame.mixer.music.load(playlist[cur])
    pygame.mixer.music.play()

running = True
while running:
    screen.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play()
            elif event.key == pygame.K_s:
                stop()
            elif event.key == pygame.K_n:
                next()
            elif event.key == pygame.K_m:
                prev()
    pygame.display.update()
pygame.quit()