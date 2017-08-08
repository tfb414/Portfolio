import pygame
from PIL import Image
import time
import random

def main():
    class Game_world(object):
        def __init__(self):
            self.width = 512
            self.height = 480
            self.screen = pygame.display.set_mode((self.width, self.height))
            self.score_font = pygame.font.Font("/Users/timbrady/Documents/Development/Code-practice/DigitalCrafts/Week2/day3/fonts/LuckiestGuy.ttf", 15)
            self.title_font_size = 1
            
            self.game_setup = pygame.display.set_caption('BlockyBlocks')
            self.clock = pygame.time.Clock()
            self.color = (77,137,7)
            self.wall_color = (40,37,41)
            self.number_of_blocks = 1
            self.score_count = 1
            self.quit = False
            self.block_speed = random.randint(5, 9)
            self.menu_selection = 0
            self.press_button = 0
            

        def block_mover(self, number_of_blocks, array_of_blocks):
            for block in array_of_blocks.blocks_array:
                block.make_and_move()

        def collision_detection(self, number_of_blocks, array_of_blocks):
            block_locations = []
            collision = False
            for i in range(number_of_blocks):
                block_locations.append(array_of_blocks.blocks_array[i].rect)
                if(block_locations[i].colliderect(self.hero.rect)):
                    collision = True
            return collision
        # def has_collided(self, collision):
        #     if collision == True:
        #         game_world.color = (255, 100, 0)
        #     if collision == False:
        #         game_world.color = (97, 159, 182)
        #     return game_world.color
        def show_score(self, score_count):
            score_count = str(score_count + 1)
            score = game_world.title_font.render(score_count, 1, (255,0,0))
            score_rect = score.get_rect(center=(game_world.width/2, 40))
            game_world.screen.blit(score, score_rect)
            
            return int(score_count)

        def menu_score(self, score_count):
            score_count = score_count + 1
            return score_count

        def menu_blocks(self, score_count, array_of_blocks, number_of_blocks):
            # score_count = str(int(score_count) + 1)
            if (score_count % 20 == 0 and number_of_blocks < 20):
                array_of_blocks.spawn(1)
                number_of_blocks = number_of_blocks + 1
            return number_of_blocks
            # return score_count

        def difficulty(self, score_count, array_of_blocks, number_of_blocks):
            if (score_count % 100 == 0):
                array_of_blocks.spawn(1)
                number_of_blocks = number_of_blocks + 1
            return number_of_blocks
        
        def title_text(self, score_count):
            score_count = score_count * 3
            if score_count < 70:
                self.title_font_size = score_count
            self.title_font = pygame.font.Font("/Users/timbrady/Documents/Development/Code-practice/DigitalCrafts/Week2/day3/fonts/LuckiestGuy.ttf", self.title_font_size)
            menu = self.title_font.render("Blocky Blocks", 1, (255,0,0))
            menu_rect = menu.get_rect(center=(self.width/2, 100))
            self.screen.blit(menu,menu_rect)

        def menu_items(self, score_count):
            score_count = score_count * 3
            if (score_count > 80):
                self.menu_item_font_size = score_count - 80
                if(score_count > 125):
                    self.menu_item_font_size = 45
                self.menu_item_font = pygame.font.Font("/Users/timbrady/Documents/Development/Code-practice/DigitalCrafts/Week2/day3/fonts/LuckiestGuy.ttf", self.menu_item_font_size)
                start_game = self.menu_item_font.render("Start Game", 1, (255,0,0))
                start_game_rect = start_game.get_rect(center=(self.width/2, 200))
                high_scores = self.menu_item_font.render("High Scores", 1, (255,0,0))
                high_scores_rect = high_scores.get_rect(center=(self.width/2, 250))
                quit_game = self.menu_item_font.render("Quit", 1, (255,0,0))
                quit_game_rect = quit_game.get_rect(center=(self.width/2, 300))
                self.screen.blit(quit_game,quit_game_rect)
                self.screen.blit(start_game,start_game_rect)
                self.screen.blit(high_scores,high_scores_rect)
            
        # have a value and when they go up and down it adds or subtracts form the value. Those values are tied to whichever thing
      
            return self.menu_selection
            
        def button_debounce(self, selection):
            pressed = pygame.key.get_pressed()
            
            if (pressed[pygame.K_UP] or pressed[pygame.K_w]) and self.selection >= 1 and self.press_button > 11: 
                selection -= 1
                self.press_button = 0
            if (pressed[pygame.K_DOWN] or pressed[pygame.K_s]) and self.selection <= 1 and self.press_button > 11: 
                selection += 1
                self.press_button = 0
            elif self.press_button < 12: self.press_button += 1
            print self.press_button
            return selection

        def use_menu(self, menu_selection, score_count):
            self.location = {
                0: 200,
                1: 250,
                2: 300
            }
            score_count = score_count * 3
            self.selection = menu_selection
            if (score_count > 80):
                self.menu_item_font_size = score_count - 80
                if(score_count > 125):
                    self.menu_item_font_size = 45
             
                self.menu_item_font = pygame.font.Font("/Users/timbrady/Documents/Development/Code-practice/DigitalCrafts/Week2/day3/fonts/LuckiestGuy.ttf", self.menu_item_font_size)
                self.selection = self.button_debounce(self.selection)
                arrow = self.menu_item_font.render(">", 1, (255,0,0))
                arrow_rect = arrow.get_rect(center=(100, self.location[self.selection]))
                self.screen.blit(arrow,arrow_rect)
            
            return self.selection



        def full_menu(self, score_count):
            # score_count = score_count * 3
            self.title_text(score_count)
            self.menu_items(score_count)
            self.menu_selection = self.use_menu(self.menu_selection, score_count)



        def run_menu(self):
            self.number_of_blocks = 1
            array_of_blocks = Create_blocks()
            array_of_blocks.spawn(self.number_of_blocks)
            while not self.quit:
                for event in pygame.event.get():
                    if event.type == pygame.quit:
                        self.quit = True
                    pressed = pygame.key.get_pressed()
                    if pressed[pygame.K_RETURN] and self.selection == 0: 
                        self.game_loop()
                    
                    if pressed[pygame.K_RETURN] and self.selection == 2: 
                        self.quit = True
                    
                
                self.screen.fill((50,50,50))
                self.number_of_blocks = self.menu_blocks(self.score_count, array_of_blocks, self.number_of_blocks)
                self.score_count = self.menu_score(self.score_count)
                self.block_mover(self.number_of_blocks, array_of_blocks)
                
                
                # self.title_text(self.score_count)
                self.full_menu(self.score_count)
                pygame.display.update()
                self.clock.tick(60)
            
        def game_loop(self):
            self.hero = Hero()
            self.block_speed = 7
            self.score_count = 0
            self.number_of_blocks = 1
            array_of_blocks = Create_blocks()
            array_of_blocks.spawn(self.number_of_blocks)
            while not self.quit:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.quit = True
                self.screen.fill((50,50,50))
                self.hero.move()
                self.block_mover(self.number_of_blocks, array_of_blocks)
                self.number_of_blocks = self.difficulty(self.score_count, array_of_blocks, self.number_of_blocks)
                self.score_count = self.show_score(self.score_count)
                
                collision = self.collision_detection(self.number_of_blocks, array_of_blocks)
                
                # self.quit = collision
                if collision:
                    self.score_count = 0
                    self.run_menu()
                pygame.display.update()
                self.clock.tick(60)
        
    pygame.init()
    game_world = Game_world()
    

    class Block(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.xloc = game_world.width
            self.yloc = random.randint(10, game_world.height)
            # self.speed = random.randint(1, 10)
            self.speed = game_world.block_speed
            self.rect = pygame.Rect(self.xloc, self.yloc, 30, 30)

        def make_and_move(self):
            self.rect = pygame.Rect(self.xloc, self.yloc, 30, 30)
            pygame.draw.rect(game_world.screen, game_world.wall_color, pygame.Rect(self.rect))
            self.xloc -= self.speed
            if self.is_too_far():
                self.reset()
        def is_too_far(self):
            return self.xloc < -30

        def reset(self):
            self.xloc = game_world.width
            self.yloc = random.randint(10, game_world.height)
            # self.speed = random.randint(1, 5)
            self.speed = 7
                    
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
            pygame.draw.rect(game_world.screen, game_world.color, pygame.Rect(self.rect))
        
        def move(self):
            self.rect = pygame.Rect(self.xloc, self.yloc,self.width, self.height)
            pygame.draw.rect(game_world.screen, game_world.color, pygame.Rect(self.rect))
            pressed = pygame.key.get_pressed()
            if (pressed[pygame.K_DOWN] or pressed[pygame.K_w]) and self.yloc >= 0: self.yloc -= 5
            if (pressed[pygame.K_DOWN] or pressed[pygame.K_s]) and self.yloc <= (game_world.height - self.height): self.yloc += 5
            if (pressed[pygame.K_DOWN] or pressed[pygame.K_a]) and self.xloc >= 0: self.xloc -= 5
            if (pressed[pygame.K_DOWN] or pressed[pygame.K_d]) and self.xloc <= (game_world.width - self.width): self.xloc += 5
    
   
    game_world.run_menu()
    # game_world.game_loop()
    pygame.quit()

if __name__ == '__main__':
    main()
# ^ move everything into a game_world class then have the while loop and my setup inside of that then you need to change the above code
# game world methods should operate on things that they recieve game would pass in difficulty level, or number of blocks etc. 
# game world is it's own thing, it's in init I have self.array_of_blocks it'll be initialized there and you can make changes without haveing to pass down the paramaters

# function for moving, color, and collision detection
# Collision detection not working for any but the first block


# you need to use super classes instead of just game_world. for example like game_world.hero instead of super 