import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255,255,0)
blue = (0,0,255)
green = (0,255,0)
background = (50,153,200)

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption('Summmer Snake game')


snake_size = 10
 
clock = pygame.time.Clock()
speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def Score(score):
    value = score_font.render("Score: " + str(score), True, black)
    screen.blit(value, [0, 0])

def my_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])
 
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width/5, screen_height/3])

def gameloop():
    over = False
    close = False

    x1 = screen_width/2
    y1 = screen_height/2
    
    x1_change = 0       
    y1_change = 0

    snake_list = []
    snake_length = 1
    

    x_food = round(random.randrange(0,screen_width-snake_size)/10) * 10
    y_food = round(random.randrange(0,screen_height-snake_size)/10) * 10
    

    while not over:

        while close == True:

            screen.fill(background)
            message("Game over!! N-Next game or C-Close",red)
            Score(snake_length-1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        over = True
                        close = False
                    if event.key == pygame.K_n:
                        gameloop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_size
                    x1_change = 0

        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(background)

        pygame.draw.rect(screen,green,[x_food,y_food,snake_size,snake_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                close = True    
        
        my_snake(snake_size,snake_list)
        Score(snake_length-1)

        pygame.display.update()

        if x1 == x_food and y1 == y_food:
            x_food = round(random.randrange(0,screen_width-snake_size)/10) * 10
            y_food = round(random.randrange(0,screen_height-snake_size)/10) * 10
            snake_length += 1

        clock.tick(speed)

    pygame.quit()
    quit()

gameloop()

 




pygame.quit()
quit()