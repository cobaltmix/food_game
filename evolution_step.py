from avoid_obstacles import *

def check_collision(pos1, pos2, size1, size2):
    return pos1[0] < pos2[0] + size2 and pos1[0] + size1 > pos2[0] and pos1[1] < pos2[1] + size2 and pos1[1] + size1 > pos2[1]

def move_player(x, y):
    # Calculate the next position of the player
    next_x = player_pos[0] + x
    next_y = player_pos[1] + y

    # Check for collisions with obstacles at the next position
    collides_with_obstacle = False
    for obstacle in obstacle_list:
        if check_collision((next_x, next_y), obstacle, player_size, obstacle_size):
            collides_with_obstacle = True
            break

    # If no collision with obstacles at the next position, update the player's position
    if not collides_with_obstacle:
        player_pos[0] = next_x
        player_pos[1] = next_y

def evolution_step():
    if food_list:
        nearest_food = min(food_list, key=lambda food: euclidean_distance(player_pos, food))
        direction_x = 0
        direction_y = 0

        if player_pos[0] < nearest_food[0]:
            direction_x = player_speed
        elif player_pos[0] > nearest_food[0]:
            direction_x = -player_speed

        if player_pos[1] < nearest_food[1]:
            direction_y = player_speed
        elif player_pos[1] > nearest_food[1]:
            direction_y = -player_speed

        # Avoid obstacles
        direction_x, direction_y = avoid_obstacles(direction_x, direction_y)

        move_player(direction_x, direction_y)