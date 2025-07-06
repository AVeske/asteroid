import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatatable, drawable)
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

    
    Asteroid.containers = (asteroids, updatatable, drawable)
    AsteroidField.containers = updatatable
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatatable, drawable)



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
            
        updatatable.update(dt)

        screen.fill(color="black")
        for obj in drawable:
            obj.draw(screen)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        
    
if __name__ == "__main__":
    main()