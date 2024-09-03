# Example file showing a basic pygame zero "game loop"
import pgzrun

# pygame zero setup
screen_size = WIDTH, HEIGHT = 1280, 720

# game setup
player = Actor('alien')
player_speed = 5
player.pos = player_x, player_y = WIDTH / 2, HEIGHT / 2
player.angle = 0
player_angular_speed = 1

meteor = Actor('meteorbrown_big3')
meteor_speed = meteor.speed_x, meteor.speed_y = 3, 3
meteor.pos = meteor_x, meteor_y = WIDTH // 2, HEIGHT // 2
meteor.angle = 0
meteor_angular_speed = 3


def draw():
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # render text
    screen.draw.text(" X: {:04d};  Y: {:04d}".format(int(meteor.x), int(meteor.y)), (20, 20))
    screen.draw.text("vX: {:04d}; vY: {:04d}".format(int(meteor.speed_x), int(meteor.speed_y)), (20, 40))
    screen.draw.text(" X: {:04d};  Y: {:04d}".format(int(player.x), int(player.y)), (200, 20))

    # render meteor
    meteor.draw()

    # render player
    player.draw()

def update():
    # rotate meteor
    meteor.angle += meteor_angular_speed
    if meteor.angle >= 360:
        meteor.angle = 0
    
    # move meteor
    meteor.x += meteor.speed_x
    meteor.y += meteor.speed_y
    if meteor.left < 0 or meteor.right > WIDTH:
        meteor.speed_x = -meteor.speed_x
    if meteor.top < 0 or meteor.bottom > HEIGHT:
        meteor.speed_y = -meteor.speed_y

    # rotate player
    player.angle += player_angular_speed
    if player.angle >= 360:
        player.angle = 0
    
    # move player
    if keyboard.w:
        player.y -= player_speed
        if player.top < 0:
            player.top = 0
    if keyboard.a:
        player.x -= player_speed
        if player.left < 0:
            player.left = 0
    if keyboard.s:
        player.y += player_speed
        if player.bottom > HEIGHT:
            player.bottom = HEIGHT
    if keyboard.d:
        player.x += player_speed
        if player.right > WIDTH:
         player.right = WIDTH

pgzrun.go()