import pygame
from constants import CONSTANT, CENTER, PORIADOK
from balls import Ball
from random import choice, randint
import utilit
import sys

pygame.init()

BLACK = (0, 0, 0)
W, H = 700, 700
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption('BEBPA')
pygame.display.set_icon(pygame.image.load('data/icon.ico'))

clock = pygame.time.Clock()
FPS = 60

balls_images = ['1.png', '2.png', '3.png']  # , '4.png', '5.png', '6.png', '7.png', '8.png'
balls_surf = [pygame.image.load('data/' + path).convert_alpha() for path in balls_images]
center_balls_images = ['1.png', '2.png', '3.png', 'plus.png']  # '4.png', '5.png', '6.png', '7.png', '8.png', 
center_balls_surf = [pygame.image.load('data/' + path).convert_alpha() for path in center_balls_images]
f = pygame.font.SysFont('Arial', 40)

ALL_BALLS = []
NOT_BALLS = [*CONSTANT]
SPISOK = {}
list_xy = []
SCORE = 0


def start_screen():
    k = 0
    fon = pygame.transform.scale(utilit.load_image('zastavka.png'), (W, H))
    sc.blit(fon, (0, 0))
    fon1 = pygame.transform.scale(utilit.load_image('zastavka1.png'), (W, H))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif (event.type == pygame.KEYDOWN or \
                  event.type == pygame.MOUSEBUTTONDOWN) and k == 0:
                sc.blit(fon1, (0, 0))
                k += 1
            elif (event.type == pygame.KEYDOWN or \
                  event.type == pygame.MOUSEBUTTONDOWN) and k != 0:
                return
        pygame.display.flip()
        clock.tick(FPS)


start_screen()


def finish_screen():
    k = 0
    fon = pygame.transform.scale(utilit.load_image('zastavka_f.png'), (W, H))
    sc.blit(fon, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
        pygame.display.flip()
        clock.tick(FPS)


def create_balls(group):
    indx = randint(0, len(balls_surf) - 1)
    while True:
        indx1 = randint(0, 19)
        xy = CONSTANT[indx1]
        if xy not in ALL_BALLS:
            ALL_BALLS.append(xy)
            NOT_BALLS.remove(xy)
            PORIADOK[xy] = balls_images[indx]
            x, y = xy
            return Ball(x, y, balls_surf[indx], group)
        elif len(ALL_BALLS) >= len(CONSTANT):
            break
        else:
            continue


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


def center_create_balls(group):
    global QW, RT
    indx = randint(0, len(center_balls_surf) - 1)
    x, y = CENTER
    ball = [center_balls_surf[indx], group]
    QW = center_balls_surf[indx]
    RT = center_balls_images[indx]
    return Ball(x, y, center_balls_surf[indx], group)


balls = pygame.sprite.Group()


def check_balls(dictt, coords=''):
    global key, SCORE
    xy = coords
    if xy != '':
        list_xy.append(xy)
    work_list = dictt
    val = list(work_list.values())
    key = list(work_list.keys())
    indx = [i for i in range(len(val)) if val[i] != '']
    val = [val[i] for i in indx]
    key = [key[i] for i in indx]
    if 'plus.png' in val:
        for i in list_xy:
            indx = key.index(i)
            if val[len(val) - 1 if (indx - 1) < 0 else indx - 1] == val[(indx + 1) % len(val)] and val[
                (indx + 1) % len(val)] != 'plus.png':
                for ball in balls:
                    xy1 = key[len(val) - 1 if (indx - 1) < 0 else indx - 1]
                    xy2 = key[(indx + 1) % len(val)]
                    if xy1 == ball.coords() or xy2 == ball.coords():
                        balls.remove(ball)
                        PORIADOK[key[len(val) - 1 if (indx - 1) < 0 else indx - 1]] = ''
                        PORIADOK[key[(indx + 1) % len(val)]] = ''
                list_xy.remove(i)
                if val[len(val) - 2 if (indx - 2) < 0 else indx - 2] == val[(indx + 2) % len(val)] and val[
                    (indx + 1) % len(val)] != 'plus.png':
                    for ball in balls:
                        xy1 = key[len(val) - 2 if (indx - 2) < 0 else indx - 2]
                        xy2 = key[(indx + 2) % len(val)]
                        if xy1 == ball.coords() or xy2 == ball.coords():
                            balls.remove(ball)
                            PORIADOK[key[len(val) - 2 if (indx - 2) < 0 else indx - 2]] = ''
                            PORIADOK[key[(indx + 2) % len(val)]] = ''
                    new_name = (str(int(str(val[(indx + 1) % len(val)])[:1]) + 2)) + '.png'
                    # SCORE += int(str(val[(indx + 1) % len(val)])[:1]) + 2
                    PORIADOK[key[indx]] = new_name
                    Ball(i[0], i[1], pygame.image.load('data/' + new_name).convert_alpha(), balls)
                    if val[len(val) - 3 if (indx - 3) < 0 else indx - 3] == val[(indx + 3) % len(val)] and val[
                        (indx + 1) % len(val)] != 'plus.png':
                        for ball in balls:
                            xy1 = key[len(val) - 3 if (indx - 3) < 0 else indx - 3]
                            xy2 = key[(indx + 3) % len(val)]
                            if xy1 == ball.coords() or xy2 == ball.coords():
                                balls.remove(ball)
                                PORIADOK[key[len(val) - 3 if (indx - 3) < 0 else indx - 3]] = ''
                                PORIADOK[key[(indx + 3) % len(val)]] = ''
                        new_name = (str(int(str(val[(indx + 1) % len(val)])[:1]) + 3)) + '.png'
                        # SCORE += int(str(val[(indx + 1) % len(val)])[:1]) + 3
                        PORIADOK[key[indx]] = new_name
                        Ball(i[0], i[1], pygame.image.load('data/' + new_name).convert_alpha(), balls)
                        if val[len(val) - 4 if (indx - 4) < 0 else indx - 4] == val[(indx + 4) % len(val)] and val[
                            (indx + 1) % len(val)] != 'plus.png':
                            for ball in balls:
                                xy1 = key[len(val) - 4 if (indx - 4) < 0 else indx - 4]
                                xy2 = key[(indx + 4) % len(val)]
                                if xy1 == ball.coords() or xy2 == ball.coords():
                                    balls.remove(ball)
                                    PORIADOK[key[len(val) - 4 if (indx - 4) < 0 else indx - 4]] = ''
                                    PORIADOK[key[(indx + 4) % len(val)]] = ''
                            new_name = (str(int(str(val[(indx + 1) % len(val)])[:1]) + 4)) + '.png'
                            # SCORE += int(str(val[(indx + 1) % len(val)])[:1]) + 4
                            PORIADOK[key[indx]] = new_name
                            Ball(i[0], i[1], pygame.image.load('data/' + new_name).convert_alpha(), balls)
                            if val[len(val) - 5 if (indx - 5) < 0 else indx - 5] == val[(indx + 5) % len(val)] and val[
                                (indx + 1) % len(val)] != 'plus.png':
                                for ball in balls:
                                    xy1 = key[len(val) - 5 if (indx - 5) < 0 else indx - 5]
                                    xy2 = key[(indx + 5) % len(val)]
                                    if xy1 == ball.coords() or xy2 == ball.coords():
                                        balls.remove(ball)
                                        PORIADOK[key[len(val) - 5 if (indx - 5) < 0 else indx - 5]] = ''
                                        PORIADOK[key[(indx + 5) % len(val)]] = ''
                                new_name = (str(int(str(val[(indx + 1) % len(val)])[:1]) + 5)) + '.png'
                                # SCORE += int(str(val[(indx + 1) % len(val)])[:1]) + 5
                                PORIADOK[key[indx]] = new_name
                                Ball(i[0], i[1], pygame.image.load('data/' + new_name).convert_alpha(), balls)
                                if val[len(val) - 6 if (indx - 6) < 0 else indx - 6] == val[(indx + 6) % len(val)] and \
                                        val[(indx + 1) % len(val)] != 'plus.png':
                                    for ball in balls:
                                        xy1 = key[len(val) - 6 if (indx - 6) < 0 else indx - 6]
                                        xy2 = key[(indx + 6) % len(val)]
                                        if xy1 == ball.coords() or xy2 == ball.coords():
                                            balls.remove(ball)
                                            PORIADOK[key[len(val) - 6 if (indx - 6) < 0 else indx - 6]] = ''
                                            PORIADOK[key[(indx + 6) % len(val)]] = ''
                                    new_name = (str(int(str(val[(indx + 1) % len(val)])[:1]) + 6)) + '.png'
                                    # SCORE += int(str(val[(indx + 1) % len(val)])[:1]) + 6
                                    PORIADOK[key[indx]] = new_name
                                    Ball(i[0], i[1], pygame.image.load('data/' + new_name).convert_alpha(), balls)
                                    if val[len(val) - 7 if (indx - 7) < 0 else indx - 7] == val[
                                        (indx + 7) % len(val)] and val[(indx + 1) % len(val)] != 'plus.png':
                                        for ball in balls:
                                            xy1 = key[len(val) - 7 if (indx - 7) < 0 else indx - 7]
                                            xy2 = key[(indx + 7) % len(val)]
                                            if xy1 == ball.coords() or xy2 == ball.coords():
                                                balls.remove(ball)
                                                PORIADOK[key[len(val) - 7 if (indx - 7) < 0 else indx - 7]] = ''
                                                PORIADOK[key[(indx + 7) % len(val)]] = ''
                                        new_name = (str(int(str(val[(indx + 1) % len(val)])[:1]) + 7)) + '.png'
                                        # SCORE += int(str(val[(indx + 1) % len(val)])[:1]) + 7
                                        PORIADOK[key[indx]] = new_name
                                        Ball(i[0], i[1], pygame.image.load('data/' + new_name).convert_alpha(), balls)
                                        if val[len(val) - 8 if (indx - 8) < 0 else indx - 8] == val[
                                            (indx + 8) % len(val)] and val[(indx + 1) % len(val)] != 'plus.png':
                                            for ball in balls:
                                                xy1 = key[len(val) - 8 if (indx - 8) < 0 else indx - 8]
                                                xy2 = key[(indx + 8) % len(val)]
                                                if xy1 == ball.coords() or xy2 == ball.coords():
                                                    balls.remove(ball)
                                                    PORIADOK[key[len(val) - 8 if (indx - 8) < 0 else indx - 8]] = ''
                                                    PORIADOK[key[(indx + 8) % len(val)]] = ''
                                            new_name = (str(int(str(val[(indx + 1) % len(val)])[:1]) + 8)) + '.png'
                                            # SCORE += int(str(val[(indx + 1) % len(val)])[:1]) + 8
                                            PORIADOK[key[indx]] = new_name
                                            Ball(i[0], i[1], pygame.image.load('data/' + new_name).convert_alpha(),
                                                 balls)
                                            if val[len(val) - 9 if (indx - 9) < 0 else indx - 9] == val[
                                                (indx + 9) % len(val)] and val[(indx + 1) % len(val)] != 'plus.png':
                                                for ball in balls:
                                                    xy1 = key[len(val) - 9 if (indx - 9) < 0 else indx - 9]
                                                    xy2 = key[(indx + 9) % len(val)]
                                                    if xy1 == ball.coords() or xy2 == ball.coords():
                                                        balls.remove(ball)
                                                        PORIADOK[key[len(val) - 9 if (indx - 9) < 0 else indx - 9]] = ''
                                                        PORIADOK[key[(indx + 9) % len(val)]] = ''
                                                new_name = (str(int(str(val[(indx + 1) % len(val)])[:1]) + 9)) + '.png'
                                                # SCORE += int(str(val[(indx + 1) % len(val)])[:1]) + 9
                                                PORIADOK[key[indx]] = new_name
                                                Ball(i[0], i[1], pygame.image.load('data/' + new_name).convert_alpha(),
                                                     balls)
                                            else:
                                                new_name = (str(int(str(val[(indx + 1) % len(val)])[:1]) + 8)) + '.png'
                                                SCORE += int(str(val[(indx + 1) % len(val)])[:1]) + 8
                                                PORIADOK[key[indx]] = new_name
                                                Ball(i[0], i[1], pygame.image.load('data/' + new_name).convert_alpha(),
                                                     balls)
                                        else:
                                            new_name = (str(int(str(val[(indx + 1) % len(val)])[:1]) + 7)) + '.png'
                                            SCORE += int(str(val[(indx + 1) % len(val)])[:1]) + 7
                                            PORIADOK[key[indx]] = new_name
                                            Ball(i[0], i[1], pygame.image.load('data/' + new_name).convert_alpha(),
                                                 balls)
                                    else:
                                        new_name = (str(int(str(val[(indx + 1) % len(val)])[:1]) + 6)) + '.png'
                                        SCORE += int(str(val[(indx + 1) % len(val)])[:1]) + 6
                                        PORIADOK[key[indx]] = new_name
                                        Ball(i[0], i[1], pygame.image.load('data/' + new_name).convert_alpha(), balls)
                                else:
                                    new_name = (str(int(str(val[(indx + 1) % len(val)])[:1]) + 5)) + '.png'
                                    SCORE += int(str(val[(indx + 1) % len(val)])[:1]) + 5
                                    PORIADOK[key[indx]] = new_name
                                    Ball(i[0], i[1], pygame.image.load('data/' + new_name).convert_alpha(), balls)
                            else:
                                new_name = (str(int(str(val[(indx + 1) % len(val)])[:1]) + 4)) + '.png'
                                SCORE += int(str(val[(indx + 1) % len(val)])[:1]) + 4
                                PORIADOK[key[indx]] = new_name
                                Ball(i[0], i[1], pygame.image.load('data/' + new_name).convert_alpha(), balls)
                        else:
                            new_name = (str(int(str(val[(indx + 1) % len(val)])[:1]) + 3)) + '.png'
                            SCORE += int(str(val[(indx + 1) % len(val)])[:1]) + 3
                            PORIADOK[key[indx]] = new_name
                            Ball(i[0], i[1], pygame.image.load('data/' + new_name).convert_alpha(), balls)
                    else:
                        new_name = (str(int(str(val[(indx + 1) % len(val)])[:1]) + 2)) + '.png'
                        SCORE += int(str(val[(indx + 1) % len(val)])[:1]) + 2
                        PORIADOK[key[indx]] = new_name
                        Ball(i[0], i[1], pygame.image.load('data/' + new_name).convert_alpha(), balls)
                else:
                    new_name = (str(int(str(val[(indx + 1) % len(val)])[:1]) + 1)) + '.png'
                    SCORE += int(str(val[(indx + 1) % len(val)])[:1]) + 1
                    PORIADOK[key[indx]] = new_name
                    Ball(i[0], i[1], pygame.image.load('data/' + new_name).convert_alpha(), balls)


def game_loop():
    global SCORE
    for i in range(5):
        create_balls(balls)
    center_create_balls(balls)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                val = list(PORIADOK.values())
                key = list(PORIADOK.keys())
                indx = [i for i in range(len(val)) if val[i] != '']
                val = [val[i] for i in indx]
                key = [key[i] for i in indx]
                NOT_BALLS = [*CONSTANT]
                for kay in key:
                    NOT_BALLS.remove(kay)
                for i in NOT_BALLS:
                    if (pygame.mouse.get_pos()[0] <= (i[0] + 20) and pygame.mouse.get_pos()[0] >= (i[0] - 20)) and \
                            (pygame.mouse.get_pos()[1] <= (i[1] + 20) and pygame.mouse.get_pos()[1] >= (i[1] - 20)):
                        if PORIADOK[i] == '':
                            Ball(i[0], i[1], QW, balls)
                            PORIADOK[i] = RT
                            if RT == 'plus.png':
                                check_balls(PORIADOK, i)
                            else:
                                check_balls(PORIADOK)
                            center_create_balls(balls)
                            check_balls(PORIADOK)
                if len(NOT_BALLS) <= 1:
                    finish_screen()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
                    NOT_BALLS = [*CONSTANT]
                    for i in PORIADOK.keys():
                        PORIADOK[i] = ''
                    balls.empty()
                    SCORE = 0
        sc.fill(BLACK)
        sc_text = f.render(str(SCORE), 10, (255, 255, 255))
        sc.blit(sc_text, (350, 20))

        for i in CONSTANT:
            pygame.draw.circle(sc, (255, 255, 255), (i), 19, 1)
        pygame.draw.circle(sc, (255, 255, 255), (CENTER), 19, 1)
        balls.draw(sc)
        pygame.display.update()
        clock.tick(FPS)
        balls.update()


while True:
    game_loop()
