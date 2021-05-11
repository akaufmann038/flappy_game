import pygame
from pygame import joystick
from constants import *
from game import game

class view:
    def __init__(self, game_object, win):
        self.game_object = game_object
        self.win = win

    def draw_obstacles(self):
        '''
        Draws obstacles on the screen
        '''
        obstacles = self.game_object.get_obstacles()
        win.fill(BLACK)

        for obs in obstacles:
            top_len = obs.get_top_length()
            bottom_len = obs.get_bottom_length()
            x_loc = obs.get_x_loc()

            top_rect = pygame.Rect(x_loc, 0, OBSTACLE_WIDTH, top_len)
            bottom_rect = pygame.Rect(x_loc, WINDOW_HEIGHT - bottom_len, OBSTACLE_WIDTH, bottom_len)
            pygame.draw.rect(self.win, OBSTACLE_COLOR, top_rect)
            pygame.draw.rect(self.win, OBSTACLE_COLOR, bottom_rect)

    def create_obstacle(self, frames):
        '''
        Creates an obstacle in the game object to be displayed on the screen
        '''
        if frames % 1300 == 0:
            self.game_object.create_obstacles()

    def move_obstacles(self):
        self.game_object.move_obstacles()

    def draw(self):
        self.draw_obstacles()
        pygame.display.update()



pygame.init()
win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
win.fill(BLACK) # sets black background
pygame.display.set_caption('Bouncing Ball Game')
pygame.display.update() # updates display
clock = pygame.time.Clock() # creates game clock

# creates game and view objects
game = game()
view = view(game, win)


is_quit = False
frames = 0
while not is_quit:

    clock.tick(FPS)
    frames += FPS

    view.create_obstacle(frames)
    view.move_obstacles()
    view.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_quit = True

