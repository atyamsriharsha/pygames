import pygame
import time
import random

pygame.init()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
display_width = 800
display_height  = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snake Game')
icon = pygame.image.load('apple.png')
pygame.display.set_icon(icon)
img = pygame.image.load('snakehead.png')
appleimg = pygame.image.load('apple.png')
starting_logo = pygame.image.load('starting_logo1.png')
rules_logo = pygame.image.load('rules.png')
game_over = pygame.image.load('gameover.png')
paused_logo = pygame.image.load('paused.png')
clock = pygame.time.Clock()
AppleThickness = 30
block_size = 20
FPS = 15
direction = "right"
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

def rules():
    ruled = True
    while ruled:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    ruled = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.fill(white)
        gameDisplay.blit(rules_logo,(300,100))
        message_to_screen("Welcome to Snake Game",green,-80,"medium")
        message_to_screen("1.The objective of the game is to eat red apples",black,-30)
        message_to_screen("2.The more apples you eat, the longer you get",black,10)
        message_to_screen("3.If you run into yourself, or the edges, you die!",black,50)
        message_to_screen("4.Press C to play, P to pause or Q to quit.",black,100)
        pygame.display.update()
        clock.tick(5)

def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.fill(white)
        gameDisplay.blit(paused_logo,(300,100))
        message_to_screen("Press C to continue or Q to quit.",black,25,"medium")
        pygame.display.update()
        clock.tick(5)
                    

def score(score):
    text = smallfont.render("Score: "+str(score), True, black)
    gameDisplay.blit(text, [0,0])

def applesgenerate():
    randAppleX = round(random.randrange(0, display_width-AppleThickness))
    randAppleY = round(random.randrange(0, display_height-AppleThickness))
    return randAppleX,randAppleY

def starting_game():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.fill(white)
        gameDisplay.blit(starting_logo,(300,100))
        message_to_screen("Press C to play, P to pause or Q to quit.",black,100,"medium")
        pygame.display.update()
        clock.tick(15)

def snake(block_size, snakelist):
    if direction == "right":
        head = pygame.transform.rotate(img, 270)
    if direction == "left":
        head = pygame.transform.rotate(img, 90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img, 180)
    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay,black, [XnY[0],XnY[1],block_size,block_size])

def font_view(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()
    
    
def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = font_view(msg,color, size)
    textRect.center = (display_width / 2), (display_height / 2)+y_displace
    gameDisplay.blit(textSurf, textRect)


def run_game():
    global direction
    direction = 'right'
    gameExit = False
    gameOver = False
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 10
    lead_y_change = 0
    snakeList = []
    snakeLength = 1
    randAppleX,randAppleY = applesgenerate()
    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(white)
            gameDisplay.blit(game_over,(300,100))
            message_to_screen("Press C to play again or Q to quit",black,50,size="medium")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        run_game()
        for event in pygame.event.get():
            pygame.mixer.music.load('game_running.mp3')
            pygame.mixer.music.play(-1)
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_p:
                    pause()
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True
        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(white)
        gameDisplay.blit(appleimg, (randAppleX, randAppleY))
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        if len(snakeList) > snakeLength:
            del snakeList[0]
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
        snake(block_size, snakeList)
        score(snakeLength-1)
        pygame.mixer.music.load('game_running.mp3')
        pygame.mixer.music.play(-1)
        pygame.display.update()
        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:
                pygame.mixer.music.load('game_running.mp3')
                pygame.mixer.music.play(-1)
                randAppleX,randAppleY = applesgenerate()
                snakeLength += 1
            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                pygame.mixer.music.load('game_running.mp3')
                pygame.mixer.music.play(-1)
                randAppleX,randAppleY = applesgenerate()
                snakeLength += 1
        clock.tick(FPS)
    pygame.quit()
    quit()
starting_game()
rules()
run_game()