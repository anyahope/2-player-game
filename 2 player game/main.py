import pygame

pygame.init() #starts all features

#constants
WIDTH = 1000
HEIGHT = 500
PLAYER_SPEED = 5
BULLET_SPEED = 9
MAX_BULLETS = 3
FPS = 60 #ensures game is smooth, refresh rate is same

health_font = pygame.font.SysFont('georgia', 20)
win_font = pygame.font.SysFont('timesnewroman', 50)

clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galatic Battle")

divider = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT) #rect is an object

#creating player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, controls, side):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft = (x,y))

        self.controls = controls
        self.side = side
        self.health = 10
        self.bullets = pygame.sprite.Group()

def draw():
    screen.fill('green')
    pygame.draw.rect(screen, 'black', divider)

    pygame.display.update() #updating screen display (last instruction in loop) change

def main():
    while True:
        draw()
        for event in pygame.event.get(): #check for event

            if event.type == pygame.QUIT:
                exit()

        
    pygame.quit()

main()