import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fictional Chainsaw Game")
running = True
fps_limit = 30
clock = pygame.time.Clock()
posx = 400
posy = 300
pygame.display.flip()
while running:
    clock.tick(fps_limit)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        posx -= 5
    if keys[pygame.K_RIGHT]:
        posx += 5
    if keys[pygame.K_UP]:
        posy -= 5
    if keys[pygame.K_DOWN]:
        posy += 5
    if keys[pygame.K_SPACE]:
        screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (150, 0, 0), (posx, posy), 5)
    pygame.display.flip()
pygame.quit()
