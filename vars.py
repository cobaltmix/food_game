import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Evolution Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Player attributes
player_size = 20
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
player_speed = 5

# Food attributes
food_size = 10
food_list = []
food_eaten = 0
max_food_items = 10

# Obstacle attributes
obstacle_size = 50
obstacle_list = []
max_obstacles = 8

# Game loop variables
clock = pygame.time.Clock()
game_over = False