from constants import *
import random

class game:
    def __init__(self):
        self.obstacles = [] # all obstacles present in the game
        self.agents = [] # all ai_objects present in the game

    def create_obstacles(self):
        '''
        Adds an obstacle object to self.obstacles
        '''
        # get top height
        top_height = random.randint(100, 200)
        
        # calculate bottom height
        bottom_height = WINDOW_HEIGHT - OBSTACLE_SPACE - top_height
        
        to_add = obstacle(top_height, bottom_height)
        self.obstacles.append(to_add)

    def get_obstacles(self):
        return self.obstacles

    def move_obstacles(self):
        for obs in self.obstacles:
            obs.move()


class obstacle:
    def __init__(self, top_length, bottom_length):
        self.top_length = top_length
        self.bottom_length = bottom_length
        self.x_loc = OBSTACLE_START_X_LOC

    def get_top_length(self):
        return self.top_length

    def get_bottom_length(self):
        return self.bottom_length
    
    def get_x_loc(self):
        return self.x_loc

    def move(self):
        self.x_loc -= OBSTACLE_X_CHANGE
