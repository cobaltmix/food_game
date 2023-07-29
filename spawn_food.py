from vars import *
from evolution_step import *


def spawn_food():
    exclusion_radius = 50  # Adjust the radius as needed
    max_attempts = 100

    attempts = 0
    while attempts < max_attempts:
        food_pos = [
            random.randint(0, SCREEN_WIDTH - food_size),
            random.randint(0, SCREEN_HEIGHT - food_size),
        ]

        # Check for collisions with obstacles within the exclusion radius
        collides_with_obstacle = False
        for obstacle in obstacle_list:
            distance = euclidean_distance(food_pos, obstacle)
            if distance < exclusion_radius:
                collides_with_obstacle = True
                break

        if not collides_with_obstacle:
            food_list.append(food_pos)
            break

        attempts += 1
