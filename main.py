from random import randint
import pygame
import solver


def drawActual(screen, pos):
    w = 60
    h= 60
    for row in range(3):
        for column in range(3):
            pygame.draw.rect(screen, ((randint(0, 2000)*row)%255,(randint(0, 2000)*column)%255,0), pygame.Rect(pos[0]+w*row, pos[1]+h*column, 60, 60))



backgroundColor = (234, 212, 252)

screen = pygame.display.set_mode((600, 600)) # w, h

pygame.display.set_caption('8 Puzzle Solver')
screen.fill(backgroundColor)


running = True

# pygame.draw.rect(screen, (255,0,0), pygame.Rect(30, 30, 60, 60))

drawActual(screen, (5, 50))

pygame.display.flip()


while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print('LEFT')
                running = False
            if event.key in [pygame.K_UP, pygame.K_w]:
                print('UP')
            if event.key in [pygame.K_DOWN, pygame.K_s]:
                print('DOWN')
            if event.key in [pygame.K_LEFT, pygame.K_a]:
                print('LEFT')
            if event.key in [pygame.K_RIGHT, pygame.K_d]:
                print('RIGHT')