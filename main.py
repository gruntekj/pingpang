from pygame import *
font.init()
font1 = font.SysFont('Arial', 100)
window = display.set_mode((700, 500))
display.set_caption('ping pong')
background = transform.scale(image.load('background.png'), (700, 500))
clock = time.Clock()
run = True
class GameSprite(sprite.Sprite):
    def __init__(self, p_image, p_x, p_y, p_width, p_height, p_speed):
        super().__init__()
        self.image = transform.scale(image.load(p_image), (p_width, p_height))
        self.speed = p_speed
        self.rect = self.image.get_rect() 
        self.rect.x = p_x
        self.rect.y = p_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def __init__(self, p_image, p_x, p_y, p_width, p_height, p_speed, K_1, K_2):
        super().__init__(p_image, p_x, p_y, p_width, p_height, p_speed)
        self.key1 = K_1
        self.key2 = K_2
    def update(self):
        keys = key.get_pressed()
        if keys[self.key1] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[self.key2] and self.rect.y < 267:
            self.rect.y += self.speed
p_1 = Player('stick.png', 0, 250, 50, 170, 5, K_w, K_s)
p_2 = Player('stick.png', 650, 250, 50, 170, 5, K_UP, K_DOWN)
ball = GameSprite('ball.png', 350, 250, 50, 50, 10)
mx = 4
my = 4
while run == True:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(background, (0, 0))
    if ball.rect.colliderect(p_1.rect):
        mx *= -1
    if ball.rect.colliderect(p_2.rect):
        mx *= -1
    
    if ball.rect.y < 0:
        my *= -1
    elif ball.rect.y > 450:
        my *= -1
    if ball.rect.x < 40 or ball.rect.x > 670:
        run = False
        text_lose = font1.render('LOX', True, (255, 0, 0))
        window.blit(text_lose, (200, 150))
    
    ball.rect.x += mx
    ball.rect.y += my
    p_1.reset()
    p_1.update()
    p_2.reset()
    p_2.update()
    ball.reset()
    display.update()
    clock.tick(60)