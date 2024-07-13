import pygame
import logic

def start_game():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0
    board = logic.start_game()

    center_x, center_y = (screen.get_width() / 2, screen.get_height() / 2)
    screen.fill("black")


    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
        draw_board(screen, 1200, center_x, center_y)
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_w]:
        #     player_pos.y -= 300 * dt
        # if keys[pygame.K_s]:
        #     player_pos.y += 300 * dt
        # if keys[pygame.K_a]:
        #     player_pos.x -= 300 * dt
        # if keys[pygame.K_d]:
        #     player_pos.x += 300 * dt

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()

def draw_board(surface, size, pos_x, pos_y):
    x_increment = -200
    y_increment = -200
    for i in range(4):
        for j in range(4):
            draw_square(surface, size // 20, pos_x + x_increment, pos_y + y_increment)
            x_increment += 100
        x_increment = -200
        y_increment += 100
    
def draw_square(surface, size, pos_x, pos_y):
    pygame.draw.rect(surface, "white", (pos_x, pos_y, size, size), border_radius=5)
