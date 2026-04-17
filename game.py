import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fictional Chainsaw Game")
running = True
fps_limit = 60
clock = pygame.time.Clock()
posx = 400.0
posy = 300.0
pygame.display.flip()

# Movement variables
vx = 0.0
vy = 0.0
accel = 0.2
friction = 0.99
max_speed = 20.0

while running:
    clock.tick(fps_limit)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        vx -= accel
    if keys[pygame.K_RIGHT]:
        vx += accel
    if keys[pygame.K_UP]:
        vy -= accel
    if keys[pygame.K_DOWN]:
        vy += accel
    if keys[pygame.K_SPACE]:
        screen.fill((0, 0, 0))
    if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        vx *= friction
    if not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
        vy *= friction

# Limit speed and update position
    vx = max(-max_speed, min(max_speed, vx))
    vy = max(-max_speed, min(max_speed, vy))
    posx += vx
    posy += vy

    posx = max(5, min(790, posx))
    posy = max(5, min(590, posy))

    pygame.draw.circle(screen, (150, 0, 0), (int(posx), int(posy)), 5)
    pygame.display.flip()
pygame.quit()
