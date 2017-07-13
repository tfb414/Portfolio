import pygame
from PIL import Image
import time
import random



def main():
    width = 512
    height = 480
    color = (97, 159, 182)
    wall_color = (255,255,0)
    number_of_blocks = 1
    score_count = 0

    pygame.init()
    myfont = pygame.font.SysFont("monospace", 30)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()



    class Block(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.xloc = width
            self.yloc = random.randint(10, height)
            self.speed = random.randint(1, 10)
            self.rect = pygame.Rect(self.xloc, self.yloc, 30, 30)

        def make_and_move(self):
            self.rect = pygame.Rect(self.xloc, self.yloc, 30, 30)
            pygame.draw.rect(screen, wall_color, pygame.Rect(self.rect))
            self.xloc -= self.speed
            if self.is_too_far():
                self.reset()
        def is_too_far(self):
            return self.xloc < -30

        def reset(self):
            self.xloc = width
            self.yloc = random.randint(10, height)
            self.speed = random.randint(1, 5)
                    
    class Create_blocks(object):
        def __init__(self):
            self.blocks_array = []
            
        def spawn(self, number_of_blocks):
            for i in range(number_of_blocks):
                self.blocks_array.append(Block())
                
            
    
    class Hero(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.height = 60
            self.width = 60
            self.xloc = 100
            self.yloc = 100
            self.rect = pygame.Rect(self.xloc, self.yloc,self.width, self.height)
            pygame.draw.rect(screen, color, pygame.Rect(self.rect))
        
        def move(self):
            self.rect = pygame.Rect(self.xloc, self.yloc,self.width, self.height)
            pygame.draw.rect(screen, color, pygame.Rect(self.rect))
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP] and self.yloc >= 0: self.yloc -= 5
            if pressed[pygame.K_DOWN] and self.yloc <= (height - self.height): self.yloc += 5
            if pressed[pygame.K_LEFT] and self.xloc >= 0: self.xloc -= 5
            if pressed[pygame.K_RIGHT] and self.xloc <= (width - self.width): self.xloc += 5
    
    def collision_detection(number_of_blocks, all_blocks):
        block_locations = []
        collision = False
        for i in range(number_of_blocks):
            block_locations.append(all_blocks.blocks_array[i].rect)
            if(block_locations[i].colliderect(hero.rect)):
                collision = True
        return collision

    def block_mover(number_of_blocks, all_blocks):
        for block in all_blocks.blocks_array:
            block.make_and_move()
        
    def has_collided(collision):
        if collision == True:
            color = (255, 100, 0)
        if collision == False:
            color = (97, 159, 182)
        return color

    def show_score(score_count):
        score_count = str(int(score_count) + 1)
        score = myfont.render(score_count, 1, (255,0,0))
        screen.blit(score, (200, 15))
        return score_count

    def difficulty(score_count, all_blocks, number_of_blocks):
        if (int(score_count) % 100 == 0):
            all_blocks.spawn(1)
            number_of_blocks = number_of_blocks + 1
        return number_of_blocks

    
    all_blocks = Create_blocks()
    all_blocks.spawn(number_of_blocks)
    hero = Hero()
    stop_game = False
    
    
    while not stop_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_game = True

        screen.fill((50,50,50))

        hero.move()
        number_of_blocks = difficulty(score_count, all_blocks, number_of_blocks)
        collision = collision_detection(number_of_blocks, all_blocks)
        # print collision
        # color = has_collided(collision)
        stop_game = collision
        block_mover(number_of_blocks, all_blocks)
        score_count = show_score(score_count)

        # difficulty(score_count)
        
        
        
        
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()


# function for moving, color, and collision detection
# Collision detection not working for any but the first block