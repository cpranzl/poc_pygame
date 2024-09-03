# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()

screen_size = screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode(screen_size)

clock = pygame.time.Clock()

font = pygame.font.Font(None, 24)

running = True
dt = 0

# game setup
player = pygame.image.load("images/alien.gif")
player_speed = 300
player_rect = player.get_rect()
player_angular_speed = 1

meteor = pygame.image.load("images/meteorbrown_big3.png")
meteor_speed = pygame.Vector2(3, 3)
meteor_rect = meteor.get_rect()
meteor_angular_speed = 3

while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # render text
    meteor_pos_text = font.render(" X: {:04d};  Y: {:04d}".format(int(meteor_rect.x), int(meteor_rect.y)), True, (255, 255, 255))
    meteor_pos_text_rect = meteor_pos_text.get_rect(topleft=(20, 20))
    screen.blit(meteor_pos_text, meteor_pos_text_rect)

    meteor_speed_text = font.render("vX: {:04d}; vY: {:04d}".format(int(meteor_speed[0]), int(meteor_speed[1])), True, (255, 255, 255))
    meteor_speed_text_rect = meteor_speed_text.get_rect(topleft=(20, 40))
    screen.blit(meteor_speed_text, meteor_speed_text_rect)

    player_pos_text = font.render(" X: {:04d};  Y: {:04d}".format(int(player_rect.x), int(player_rect.y)), True, (255, 255, 255))
    player_pos_text_rect = player_pos_text.get_rect(topleft=(200, 20))
    screen.blit(player_pos_text, player_pos_text_rect)

    # render meteor
    screen.blit(meteor, meteor_rect)
    
    # move meteor
    meteor_rect = meteor_rect.move(meteor_speed)
    if meteor_rect.left < 0 or meteor_rect.right > screen_width:
        meteor_speed[0] = -meteor_speed[0]
    if meteor_rect.top < 0 or meteor_rect.bottom > screen_height:
        meteor_speed[1] = -meteor_speed[1]

    # render player
    screen.blit(player, player_rect)

    # move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_rect.y -= player_speed * dt
        if player_rect.top < 0:
            player_rect.top = 0
    if keys[pygame.K_a]:
        player_rect.x -= player_speed * dt
        if player_rect.left < 0:
            player_rect.left = 0
    if keys[pygame.K_s]:
        player_rect.y += player_speed * dt
        if player_rect.bottom > screen_height:
            player_rect.bottom = screen_height
    if keys[pygame.K_d]:
        player_rect.x += player_speed * dt
        if player_rect.right > screen_width:
            player_rect.right = screen_width

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()