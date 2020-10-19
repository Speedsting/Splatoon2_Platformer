import pygame
import random

pygame.init()

windowwidth = 400
windowheight = 400

white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)

class Player1:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 50
        self.height = 50
        self.vely = 0
        self.gravity = 1
        self.jumping = False
        self.jumppower = 20
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.coincount = 0

    def tick(self):
        if keys[pygame.K_LEFT]:
            self.x -= 5
        if keys[pygame.K_RIGHT]:
            self.x += 5
        if keys[pygame.K_UP] and self.jumping == False:
            self.vely = -self.jumppower
            self.jumping = True

        self.vely += self.gravity
        self.y += self.vely

        if self.x > windowwidth - self.width:
            self.x = windowwidth - self.width
        if self.x < 0:
            self.x = 0
        if self.y > windowheight - self.height:
            self.y = windowheight - self.height
            self.vely = 0
            self.jumping = False
        if self.y < 0:
            self.y = 0

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, white, player1.rect)

class Player2:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 50
        self.height = 50
        self.vely = 0
        self.gravity = 1
        self.jumping = False
        self.jumppower = 20
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.coincount = 0

    def tick(self):
        if keys[pygame.K_a]:
            self.x -= 5
        if keys[pygame.K_d]:
            self.x += 5
        if keys[pygame.K_w] and self.jumping == False:
            self.vely = -self.jumppower
            self.jumping = True

        self.vely += self.gravity
        self.y += self.vely

        if self.x > windowwidth - self.width:
            self.x = windowwidth - self.width
        if self.x < 0:
            self.x = 0
        if self.y > windowheight - self.height:
            self.y = windowheight - self.height
            self.vely = 0
            self.jumping = False
        if self.y < 0:
            self.y = 0

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, white, player2.rect)

class Pickup:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 50
        self.height = 50
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def tick(self):
        if self.rect.colliderect(player1.rect) == True:
            player1.coincount += 1
            print("P1 has $" + str(player1.coincount))
            overlapping = True

            while overlapping == True:
                self.x = random.randint(0, windowwidth - coin.width)
                self.y = random.randint(windowheight // 2 - self.height // 2, windowheight - coin.height)

                self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
                if self.rect.colliderect(player1.rect) == False:
                    overlapping = False

        if self.rect.colliderect(player2.rect) == True:
            player2.coincount += 1
            print("P2 has $" + str(player2.coincount))
            overlapping = True

            while overlapping == True:
                self.x = random.randint(0, windowwidth - coin.width)
                self.y = random.randint(windowheight // 2 - self.height // 2, windowheight - coin.height)

                self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
                if self.rect.colliderect(player2.rect) == False:
                    overlapping = False

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.ellipse(win, yellow, self.rect, 5)

# create window
win = pygame.display.set_mode((windowwidth, windowheight))
pygame.display.set_caption("Splatoon 2")


player1 = Player1()
player2 = Player2()
coin = Pickup()

run = True
while run:
    pygame.time.delay(25)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    win.fill(black)
    player1.tick()
    player2.tick()

    coin.tick()

    pygame.display.update()
print("end of game")