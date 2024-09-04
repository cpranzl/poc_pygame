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
meteor_surface = pygame.image.load("images/meteorbrown_big3.png")
meteor_rect = meteor_surface.get_rect(center=(screen_width // 4, screen_height // 4))
meteor_speed = pygame.Vector2(3, 3)
meteor_angle = 0
meteor_angular_speed = 2

player_surface = pygame.image.load("images/alien.gif")
player_rect = player_surface.get_rect(center=(screen_width // 2, screen_height // 2))
player_speed = 300
player_angle = 0
player_angular_speed = 1

while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # rotate meteor
    rotated_meteor_surface = pygame.transform.rotate(meteor_surface, meteor_angle)
    rotated_meteor_rect = rotated_meteor_surface.get_rect(center=meteor_rect.center)
    
    meteor_angle += meteor_angular_speed
    if meteor_angle >= 360:
        meteor_angle = 0

    # move meteor
    meteor_rect.x += meteor_speed[0]
    meteor_rect.y += meteor_speed[1]

    if meteor_rect.left < 0 or meteor_rect.right > screen_width:
        meteor_speed[0] = -meteor_speed[0]
    if meteor_rect.top < 0 or meteor_rect.bottom > screen_height:
        meteor_speed[1] = -meteor_speed[1]

    # render meteor
    screen.blit(rotated_meteor_surface, rotated_meteor_rect)

    # rotate player
    rotated_player_surface = pygame.transform.rotate(player_surface, player_angle)
    rotated_player_rect = rotated_player_surface.get_rect(center=player_rect.center)

    player_angle += player_angular_speed
    if player_angle >= 360:
        player_angle = 0

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

    # render player
    screen.blit(rotated_player_surface, rotated_player_rect)

    # text
    meteor_pos_text = font.render(" X: {:04d};  Y: {:04d}".format(int(meteor_rect.x), int(meteor_rect.y)), True, (255, 255, 255))
    meteor_pos_text_rect = meteor_pos_text.get_rect(topleft=(20, 20))
    
    meteor_speed_text = font.render("vX: {:04d}; vY: {:04d}".format(int(meteor_speed[0]), int(meteor_speed[1])), True, (255, 255, 255))
    meteor_speed_text_rect = meteor_speed_text.get_rect(topleft=(20, 40))
    
    player_pos_text = font.render(" X: {:04d};  Y: {:04d}".format(int(player_rect.x), int(player_rect.y)), True, (255, 255, 255))
    player_pos_text_rect = player_pos_text.get_rect(topleft=(200, 20))
    

    # render text
    screen.blit(meteor_pos_text, meteor_pos_text_rect)
    screen.blit(meteor_speed_text, meteor_speed_text_rect)
    screen.blit(player_pos_text, player_pos_text_rect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()