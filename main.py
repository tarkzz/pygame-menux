import pygame
from menux import *
import random

# ---------- SOME COLORS -------------
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 122, 80)
RED = (255, 0, 0)


m = menux("MY MENU", 50, 50, YELLOW, 20, ("1. Start", "2. Credits", "3. EXIT"))


pygame.init()
sw, sh = 500, 500
s = pygame.display.set_mode((sw, sh))
clock = pygame.time.Clock()

# generate random number between 1-rr
def rnd(rr):
    return random.randint(1, rr)

# just an animation for menu background
def anim1():
    for x in range(10):
        s.set_at((rnd(sw), rnd(sh)), WHITE)

# just an animation for gameplay
def anim2():
    for x in range(10):
        s.set_at((rnd(sw), rnd(sh)), WHITE)
        pygame.draw.circle(s, WHITE, (rnd(sw), rnd(sh)), rnd(50))


def exitgame():
    pygame.quit()
    quit()


key = 0
running = True
inplay = False


while running:
    m.inmenu = True

    while m.inmenu:
        s.fill(BLACK)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                m.inmenu = False

            if e.type == pygame.KEYDOWN:
                key = e.key

        m.update(key, s)

        key = 0  # reset key for not repeated press
        anim1()  # the animation of background, while in menu

        pygame.display.flip()
        clock.tick(11)


    print("we exit menu")
    print(m.selected)

    if running == False:
        exitgame()

    if m.selected == 1:   # MENU : Start Game selected
        print("game start")
        inplay = True

        while inplay:
            s.fill(BLACK)

            anim2()

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False
                    inplay = False

                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        inplay = False

            TextGraph("Press any key for return !", sw/3, sh/3, "Times New Roman", 18, (200, 200, 0), False, s)

            pygame.display.update()
            clock.tick(11)

    elif m.selected == 2:  # MENU:  Credits selected.
        s.fill(BLACK)
        TextGraph("by Serkan (tarkzz) @ 2022", 25, 100, "Times New Roman", 25, (100, 200, 0), False, s)
        pygame.display.update()
        keypressed = False
        while not(keypressed):
            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN:
                    keypressed = True

    elif m.selected == 3:  # MENU:  Exit selected.
        running = False

exitgame()
