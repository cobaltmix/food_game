from vars import *


def euclidean_distance(pos1, pos2):
    return ((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2) ** 0.5


def avoid_obstacles(direction_x, direction_y):
    avoid_radius = 100
    repulsion_strength = 1.5
    look_ahead_distance = 500

    steering_x, steering_y = 0, 0

    # Calculate the future position after the next movement
    future_pos_x = player_pos[0] + direction_x * look_ahead_distance
    future_pos_y = player_pos[1] + direction_y * look_ahead_distance

    for obstacle in obstacle_list:
        obstacle_x, obstacle_y = obstacle[0], obstacle[1]
        distance = euclidean_distance(
            (future_pos_x, future_pos_y), (obstacle_x, obstacle_y)
        )

        if distance < avoid_radius:
            repulsion_force_x = player_pos[0] - obstacle_x
            repulsion_force_y = player_pos[1] - obstacle_y

            # Scale the repulsion force based on the distance
            repulsion_force_x /= distance
            repulsion_force_y /= distance

            # Accumulate the repulsion forces
            steering_x += repulsion_force_x
            steering_y += repulsion_force_y

    # Avoid getting stuck between obstacles
    for obstacle in obstacle_list:
        obstacle_x, obstacle_y = obstacle[0], obstacle[1]
        distance_to_obstacle = euclidean_distance(player_pos, (obstacle_x, obstacle_y))

        if distance_to_obstacle < avoid_radius:
            direction_from_obstacle_x = player_pos[0] - obstacle_x
            direction_from_obstacle_y = player_pos[1] - obstacle_y

            # Scale the direction from obstacle based on the distance
            direction_from_obstacle_x /= distance_to_obstacle
            direction_from_obstacle_y /= distance_to_obstacle

            # If the player is moving towards the obstacle, change the direction to avoid it
            dot_product = (
                direction_x * direction_from_obstacle_x
                + direction_y * direction_from_obstacle_y
            )
            if dot_product > 0:
                steering_x += direction_from_obstacle_x * repulsion_strength
                steering_y += direction_from_obstacle_y * repulsion_strength

    # Calculate the resulting direction after obstacle avoidance
    direction_x += steering_x * repulsion_strength
    direction_y += steering_y * repulsion_strength

    # Normalize the resulting direction
    length = euclidean_distance((0, 0), (direction_x, direction_y))
    if length != 0:
        direction_x /= length
        direction_y /= length

    return direction_x, direction_y
