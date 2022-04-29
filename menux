import pygame


def TextGraph(txt, x, y, f, sz, c, focus, scr):

    if focus:
        c = (255-c[0], 255-c[1], 255-c[2])

    fnt = pygame.font.SysFont(f, sz)
    fnt_img = fnt.render(txt, True, c)
    fnt_rec = fnt_img.get_rect()
    fnt_rec.x = x-10
    fnt_rec.y = y
    fnt_rec.width = fnt_rec.width+30

    if focus:
        pygame.draw.rect(scr, (255, 0, 0), fnt_rec)

    scr.blit(fnt_img, (x, y))

class menux():
    def __init__(self, menutitle, mx, my, mcolor, msize, mitems):
        self.title = menutitle
        self.x, self.y = mx, my
        self.color = mcolor
        self.font = 'arial'
        self.size = msize
        self.items = mitems
        self.selected = 1    # when create first item is selected
        self.inmenu = False


    def drawmenu(self, scr):
        #menutitle is 1.5x bigger of menu size
        red = (255, 0, 0)
        coloroftitle = (255-self.color[0], 255-self.color[1], 255-self.color[2])
        TextGraph(self.title, self.x, self.y, self.font, int(self.size*1.5), coloroftitle, False, scr)

        for i in self.items:
            if self.selected != self.items.index(i)+1:
                TextGraph(i, self.x + self.size, self.y + int(self.size/2) + (self.size + 10) * (self.items.index(i) + 1), self.font,self.size, self.color, False, scr)
            else:
                TextGraph(i, self.x + self.size, self.y + int(self.size/2) + (self.size + 10) * (self.items.index(i) + 1), self.font, self.size, red, True, scr)

    def update(self, key, scr):

        if key == pygame.K_DOWN:
            self.selected += 1
        if key == pygame.K_UP:
            self.selected -= 1
        if key == pygame.K_RETURN:
            self.inmenu = False


        if self.selected > len(self.items):
            self.selected = 1
        if self.selected < 1:
            self.selected = len(self.items)

        print(self.selected)

        self.drawmenu(scr)
