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

clock = pygame.time.Clock() #create clock object

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galatic Battle")

divider = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT) #rect is an object

player1_x = 100
player1_y = 200

player2_x = 800
player2_y = 200

#creating bullet class blueprint
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()

#creating player class blueprint
class Player(pygame.sprite.Sprite): #makes Player inherit from Pygame's Sprite class.
    def __init__(self, x, y, image_path, controls, side):
        super().__init__() #initialises the parent sprite class
        self.image = pygame.image.load(image_path) #loads players image from file
        self.rect = self.image.get_rect(topleft = (x,y)) #creates rectangle to position the image
        self.controls = controls
        self.side = side #stores side which player belongs to
        self.health = 10
        self.bullets = pygame.sprite.Group() #stores that players bullets in a group

    def move(self, pressed_keys):
        if pressed_keys[self.controls['left']]:
            self.rect.x -= PLAYER_SPEED
        if pressed_keys[self.controls['right']]:
            self.rect.x += PLAYER_SPEED
        if pressed_keys[self.controls['up']]:
            self.rect.y -= PLAYER_SPEED
        if pressed_keys[self.controls['down']]:
            self.rect.y += PLAYER_SPEED

        self.rect.top = max(0, self.rect.top)
        self.rect.bottom = min(HEIGHT, self.rect.bottom)
        if self.side == 'left':
            self.rect.left = max(0, self.rect.left)
            self.rect.right = min(divider.left, self.rect.right )
        else:
            self.rect.left = max(divider.right, self.rect.left)
            self.rect.right = min(WIDTH, self.rect.right)

player1 = Player(player1_x, player1_y, 'assets/left.png', {
    'left': pygame.K_a, 'right':pygame.K_d, 'up':pygame.K_w, 'down':pygame.K_s
}, 'left')
player2 = Player(player2_x, player2_y, 'assets/right.png', {
    'left':pygame.K_LEFT, 'right':pygame.K_RIGHT, 'up':pygame.K_UP, 'down':pygame.K_DOWN
}, 'right')

players = pygame.sprite.Group()
players.add(player1)
players.add(player2)

def draw():
    screen.fill('green')
    pygame.draw.rect(screen, 'black', divider)
    players.draw(screen)
    left_text = health_font.render(f"Health: {player1.health}", True, 'black')
    screen.blit(left_text, (50,30))
    right_text = health_font.render(f"Health: {player2.health}", True, 'black')
    screen.blit(right_text, (WIDTH - 180,30))
    pygame.display.update() #updating screen display (last instruction in loop) change


def main():
    global player1_x, player1_y, player2_x, player2_y#so variable can be used throughout code
    while True:
        draw()
        for event in pygame.event.get(): #check for event

            if event.type == pygame.QUIT:
                exit()

        #getting all the keys pressed
        keys = pygame.key.get_pressed()
        player1.move(keys)
        player2.move(keys)

    pygame.quit()

main()

#create 
