import pygame
pygame.init()
run= True
TITLE= "Recycling Game"
WIDTH=800
HEIGHT=800
background= pygame.image.load("plantbackground.png")
bin= pygame.image.load("bin.png")
pencil=pygame.image.load("pencil.png")
bag= pygame.image.load("bag.png")
item1= pygame.image.load("item1.png")
box=pygame.image.load("box.png")
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)








while run: 
    screen.blit(background, (0,0))


    pygame.display.update()




