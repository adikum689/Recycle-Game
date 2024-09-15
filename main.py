import pygame, random
pygame.init()
run= True
TITLE= "Recycling Game"
WIDTH=800
HEIGHT=800
background= pygame.image.load("plantbackground.png")
bin= pygame.transform.scale(pygame.image.load("bin.png"), (50,60))
pencil=pygame.transform.scale(pygame.image.load("pencil.png"), (30, 20))
nr= pygame.transform.scale(pygame.image.load("bag.png"), (40, 30))
item1= pygame.transform.scale(pygame.image.load("item1.png"), (30,40))
r =pygame.transform.scale(pygame.image.load("box.png"), (40, 50))
point= 0
start= pygame.time.get_ticks()
total= 0
timer= 10000
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
list=[pencil, item1, r]

class Bin(pygame.sprite.Sprite):
    def __init__(self,x,y,img):
        super().__init__()
        self.image=img
        self.rect=self.image.get_rect()
        self.rect.x= x
        self.rect.y= y

class Nr(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__()
        self.image=img
        self.rect=self.image.get_rect()
        self.rect.x =x
        self.rect.y=y

class R(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__()
        self.image= img
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y


Rgroup=pygame.sprite.Group()
Nrgroup= pygame.sprite.Group()
Bingroup=pygame.sprite.Group()

bin1= Bin(10, 10, bin)

Bingroup.add(bin1)

for n in range(20):
    nr1= Nr( random.randint(50, 750), random.randint(50,750), nr)
    Nrgroup.add(nr1)

for n in range(30):
    r1=R(random.randint(50,750), random.randint(50,750), list[random.randint(0,2)])
    Rgroup.add(r1)










while run: 
    screen.blit(background, (0,0))
    Rgroup.draw(screen)
    Nrgroup.draw(screen)
    Bingroup.draw(screen)
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        bin1.rect.y-=5
    if keys[pygame.K_DOWN]:
        bin1.rect.y+=5
    if keys[pygame.K_LEFT]:
        bin1.rect.x-=5
    if keys[pygame.K_RIGHT]:
        bin1.rect.x+=5 
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    if pygame.sprite.groupcollide(Bingroup, Rgroup, False, True): 
        point+=1
    if pygame.sprite.groupcollide(Bingroup, Nrgroup, False, True):
        point-=1
    font= pygame.font.SysFont("Arial", 30)
    message=font.render("Score"+str(point), True, "black")
    screen.blit(message, (400,50))
    total= pygame.time.get_ticks()-start 
    message=font.render("Time"+str(total), True, "black")
    screen.blit(message, (600,50))

    if total>timer:
        run=False

        
    pygame.display.update()
    




