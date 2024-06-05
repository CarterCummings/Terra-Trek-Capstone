import pygame
SWIDTH = 1536
SHEIGHT = 864
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

class Player(object):

    def __init__(self):
        self.player = pygame.rect.Rect((300,400,50,50))
        self.color = "white"

    def move(self, x_speed, y_speed):
        self.player.move_ip((x_speed,y_speed))
        if self.player.x < 0:
            self.player.x = 0
        if self.player.y < 0:
            self.player.y = 0
        if self.player.x > SWIDTH-50:
            self.player.x = SWIDTH-50
        if self.player.y > SHEIGHT-50:
            self.player.y = SHEIGHT-50            

    def change_color(self, color):
        self.color = color

    def draw(self, game_screen):
        pygame.draw.rect(game_screen, self.color, self.player)


class Player2(object):

    def __init__(self):
        self.player = pygame.rect.Rect((300,400,50,50))
        self.color = "green"

    def move(self, x_speed, y_speed):
        self.player.move_ip((x_speed,y_speed))
        if self.player.x < 0:
            self.player.x = 0
        if self.player.y < 0:
            self.player.y = 0
        if self.player.x > SWIDTH-50:
            self.player.x = SWIDTH-50
        if self.player.y > SHEIGHT-50:
            self.player.y = SHEIGHT-50            

    def change_color(self, color):
        self.color = color

    def draw(self, game_screen):
        pygame.draw.rect(game_screen, self.color, self.player)

pygame.init()

player = Player()
player2 = Player2()

pygame.display.set_icon(pygame.image.load('TerraTrekLogo.png'))
pygame.display.set_caption("Controller Demo") 

screen = pygame.display.set_mode([SWIDTH,SHEIGHT])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.JOYBUTTONDOWN:
            if pygame.joystick.Joystick(0).get_button(0):
                player.change_color("blue")
            elif pygame.joystick.Joystick(0).get_button(1):
                player.change_color("red")
            elif pygame.joystick.Joystick(0).get_button(2):
                player.change_color("yellow")
                pygame.joystick.Joystick(0).rumble(0,0.7,500)
            elif pygame.joystick.Joystick(0).get_button(3):
                player.change_color("white")
            else:
                print(event)
    


    if pygame.joystick.Joystick(0).get_axis(0) > .1 or pygame.joystick.Joystick(0).get_axis(0) < -.1 or pygame.joystick.Joystick(0).get_axis(1) > .1 or pygame.joystick.Joystick(0).get_axis(1) < -.1:
        x_speed = round(pygame.joystick.Joystick(0).get_axis(0))
        y_speed = round(pygame.joystick.Joystick(0).get_axis(1))
        
        player.move(x_speed,y_speed)

    if pygame.joystick.Joystick(0).get_axis(2) > .1 or pygame.joystick.Joystick(0).get_axis(2) < -.1 or pygame.joystick.Joystick(0).get_axis(3) > .1 or pygame.joystick.Joystick(0).get_axis(3) < -.1:
        x_speed = round(pygame.joystick.Joystick(0).get_axis(2))
        y_speed = round(pygame.joystick.Joystick(0).get_axis(3))
        
        player2.move(x_speed,y_speed)

    screen.fill((0,0,0))
    player.draw(screen)
    player2.draw(screen)
    pygame.display.update()

pygame.quit()