import pygame
import random


bg = pygame.image.load("bg.png")
background = pygame.transform.scale(bg,(500,400))
bucket = pygame.image.load("bucket.png")
small_bucket = pygame.transform.scale(bucket,(100,50))
egg = pygame.image.load("egg.png")
small_egg = pygame.transform.scale(egg,(30,30))

#variables
blue = (19,203,240)
white = (255, 255, 255)
(width, height) = (500, 400)

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Egg Chatcher')
pygame.display.update()
clock = pygame.time.Clock()



egg_x = random.randint(10,450)
egg_y = 40
fps = 30
velocity_x = 0
velocity_y = 0
backet_x = 200
backet_y = 350
egg_velocity = 5
broken_egg = 0
score = 0

font = pygame.font.SysFont(None, 30)
# headscore = font.render(f"score is : {score}",True,(0,0,0))
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, [x,y])

exit_game = False


while not exit_game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:

                if score > 20:
                    velocity_x = -8
                    velocity_y = 0
                else:
                    velocity_x = -5
                    velocity_y = 0

            if event.key == pygame.K_RIGHT:
                if score > 20:
                    velocity_x = 8
                    velocity_y = 0
                else:
                    velocity_x = 5
                    velocity_y = 0


            if  egg_y<0 or egg_y>height:
                broken_egg = broken_egg+1
                pygame.mixer.init()
                pygame.mixer.music.load("crack1.mp3")
                pygame.mixer.music.play()
                egg_x = random.randint(10, 450)
                egg_y = 40
                egg_y = egg_y + egg_velocity


            if backet_x<0 or backet_x > 450:
                backet_x = 50

            if abs(backet_x-egg_x)<70 and abs(backet_y-egg_y)<70:
                score = score+1
                if score > 20:
                    egg_velocity = 10
                pygame.mixer.init()
                pygame.mixer.music.load("drop.mp3")
                pygame.mixer.music.play()
                egg_x = random.randint(10, 450)
                egg_y = 20


    backet_x = backet_x + velocity_x
    backet_y = backet_y + velocity_y
    egg_y = egg_y + egg_velocity



    screen.fill(white)
    screen.blit(background,(0,0))
    text_screen(f"Broken egg : {broken_egg}", (0, 0, 0), 180, 10)
    text_screen(f"High Score : {score}",(0,0,0),185,40)
    # screen.blit(headscore, (5, 5))
    screen.blit(small_bucket,(backet_x,backet_y))
    screen.blit(small_egg,(egg_x, egg_y))
    pygame.display.update()
    # pygame.draw.rect(screen, white, [backet_x,backet_y, 80, 10])
    # pygame.draw.egg(screen, white, [egg_x, egg_y,],10)
    # pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()