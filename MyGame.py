#PONG Arcade Game
import pygame
import keyboard
from random import randint
import time

BLACK = (0, 0, 0)
SILVER = (192, 192, 192)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

screen_width = 800
screen_height = 500

player_height = 100
player_width = 20
ball_height = 20
ball_width = 20

p1_score = 0
p2_score = 0

entry = True

clock = pygame.time.Clock()

class Ball(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()

        self.image = pygame.Surface([ball_width, ball_height])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.velocity = [randint(6,7),randint(-7,7)]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-5,5)


class Player(pygame.sprite.Sprite):

    def __init__(self, x, color):

        super().__init__()

        self.image = pygame.Surface([player_width, player_height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = screen_height/2 - 40


pygame.init()

screen = pygame.display.set_mode([screen_width, screen_height])

pygame.display.set_caption('PONG (Created by: Sebastien Augsburger)')

font = pygame.font.Font('freesansbold.ttf', 32)

all_sprites_list = pygame.sprite.Group()


# function to reset player and player 2 positions after a score
def reset_players(player1):
    player1.rect.x = 20
    player1.rext.y = (screen_height / 2) - 40


def paused():


    """
    text = font.render('PLAY AGAIN or QUIT???', True, BLACK)

    textRect = text.get_rect()

    textRect.center = (screen_width / 2, 20)

    screen.fill(SILVER)

    screen.blit(text, textRect)
    """

    paused = True

    while paused:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if keyboard.is_pressed(' ') or keyboard.is_pressed('w') or keyboard.is_pressed('s') or keyboard.is_pressed('i') or keyboard.is_pressed('k'):
                    paused = False

        # gameDisplay.fill(white)

        pygame.display.update()
        clock.tick(15)


# main game loop function
def game_loop(scoreP1, scoreP2):
    # paused()
    count = 0
    p1_score = scoreP1
    p2_score = scoreP2
    player1 = Player(20, BLUE)
    player2 = Player(screen_width - 40, RED)
    ball = Ball(screen_width/2, screen_height/2)
    all_sprites_list.add(ball)
    all_sprites_list.add(player1)
    all_sprites_list.add(player2)

    pdl_snd = pygame.mixer.Sound('paddle-sound.ogg')
    wall_snd = pygame.mixer.Sound('boing_spring.wav')
    scr_snd = pygame.mixer.Sound('pacman_eatghost.wav')



    done = False
    while not done:

        # check for event
        for event in pygame.event.get():
            # check event type
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if keyboard.is_pressed('q'):
                    done = True
                if keyboard.is_pressed(' '):
                    pause = True
                    paused()
            # check event type
            if event.type == pygame.KEYDOWN:
                # check if selected key is up or down, if so adjust change in y (dy)
                if keyboard.is_pressed('w'):
                    player1.rect.y -= 30
                if keyboard.is_pressed('s'):
                    player1.rect.y += 30
                if keyboard.is_pressed('i'):
                    player2.rect.y -= 30
                if keyboard.is_pressed('k'):
                    player2.rect.y += 30

        all_sprites_list.update()

        # check player1 boundary conditions
        if player1.rect.y > screen_height - player_height:
            player1.rect.y = screen_height - player_height
        if player1.rect.y < 0:
            player1.rect.y = 0
        # check player2 boundary conditions
        if player2.rect.y > screen_height - player_height:
            player2.rect.y = screen_height - player_height
        if player2.rect.y < 0:
            player2.rect.y = 0
        # Check if the ball is bouncing against the floor or roof:
        if ball.rect.y > screen_height - ball_height:
            # wall_snd.play()
            ball.velocity[1] = -ball.velocity[1]


        if ball.rect.y < 0:
            # wall_snd.play()
            ball.velocity[1] = -ball.velocity[1]


        if pygame.sprite.collide_rect(ball, player1) or pygame.sprite.collide_rect(ball, player2):
            pdl_snd.play()
            ball.bounce()

        if ball.rect.x > screen_width - 40:

            ball.rect.x = screen_width / 2
            ball.rect.y = screen_height / 2
            p1_score += 1
            # scr_snd.play()
            ball.bounce()


        # game_loop(p1_score, p2_score)

        if ball.rect.x < 20:
            ball.rect.x = screen_width / 2
            ball.rect.y = screen_height / 2
            p2_score += 1
            # scr_snd.play()
            ball.bounce()


        # game_loop(p1_score, p2_score)



        text = font.render('Scoreboard  ' + str(p1_score) + ' : ' + str(p2_score), True, SILVER)

        textRect = text.get_rect()

        textRect.center = (screen_width / 2, 20)

        screen.fill(BLACK)

        screen.blit(text, textRect)

        all_sprites_list.draw(screen)

        pygame.display.flip()

        if p2_score > 4 or p1_score > 4:
            pygame.mixer.music.load('win_snd.mp3')
            pygame.mixer.music.play()
            time.sleep(7)
            done = True

        if count == 0:
            paused()
            count += 1

        clock.tick(60)

    pygame.quit()
    quit()


pygame.mixer.music.load('super-mario-bros.mp3')
pygame.mixer.music.play(-1)
game_loop(p1_score, p2_score)

