
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

#creating player class blueprint
class Player(pygame.sprite.Sprite): #makes Player inherit from Pygame's Sprite class.
    def __init__(self, x, y, image_path, control, side): #parameters
        super().__init__() #initialises the parent sprite class
        self.image = pygame.image.load(image_path) #loads players image from file
        #creating hitbox/collider around the image
        self.rect = self.image.get_rect(topleft = (x,y)) #creates rectangle to position the image, hitbox

        self.control = control
        self.side = side #stores side which player belongs to
        self.health = 10
        self.bullets = pygame.sprite.Group() #stores that players bullets in a group

    def move(self, pressed_keys):
        if pressed_keys[self.control['left']]:
            self.rect.x -= PLAYER_SPEED
        if pressed_keys[self.control['up']]:
            self.rect.y -= PLAYER_SPEED
        if pressed_keys[self.control['right']]:
            self.rect.x += PLAYER_SPEED
        if pressed_keys[self.control['down']]:
            self.rect.y +=  PLAYER_SPEED

        #top and bottom screen boundary
        self.rect.top = max(0, self.rect.top) #look for max value between 2 options
        self.rect.bottom = min(self.rect.bottom, HEIGHT)

        if self.side == 'left':
            self.rect.left = max(0, self.rect.left)
            self.rect.right = min(self.rect.right, divider.left)
        else:
            self.rect.left = max(divider.right, self.rect.left)
            self.rect.right = min(self.rect.right, WIDTH)
#creating player object
player1 = Player(player1_x, player1_y, 'assets/left.png',{'left':pygame.K_a, 'up':pygame.K_w, 'down':pygame.K_s, 'right':pygame.K_d}, 'left')
player2 = Player(player2_x, player2_y, 'assets/right.png',{'left':pygame.K_LEFT, 'up':pygame.K_UP, 'down':pygame.K_DOWN, 'right':pygame.K_RIGHT},'right')

#creating player group --> when instruction given to a group, it  automatically assigns all instructions to members in group, instead of giving it to to them one by one
players = pygame.sprite.Group() 
players.add(player1, player2)

#user define function to make sure all drawing displayed on screen is put tgt in one place
def draw():
    screen.fill('green')
    pygame.draw.rect(screen, 'black', divider)

    #displaying players
    players.draw(screen) #system function used by specific group wherever they are

    #styling health text, doesn't display the actual text on screen. Render applies font to text given
    p1_healthtext = health_font.render(f"Health: {player1.health}", True, 'black') #true smoothens edge points automatically
    p2_healthtext = health_font.render(f"Health: {player2.health}", True, 'black')

    #displaing text on screen
    screen.blit(p1_healthtext, (50, 30))
    screen.blit(p2_healthtext, (850, 30))


    pygame.display.update() #updating screen display (last instruction in loop) change

#user define function  
def main():
    while True:
        draw()

        #getting all the keys pressed
        keys = pygame.key.get_pressed() #function

        #calling move function
        player1.move(keys)
        player2.move(keys)


        for event in pygame.event.get(): #check for event

            if event.type == pygame.QUIT:
                exit()
        
             
    pygame.quit()

main()
