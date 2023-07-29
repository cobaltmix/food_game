from evolution_step import *


def spawn_obstacle():
    exclusion_radius = 100  # Adjust the radius as needed
    max_attempts = 100

    attempts = 0
    while attempts < max_attempts:
        obstacle_pos = [
            random.randint(0, SCREEN_WIDTH - obstacle_size),
            random.randint(0, SCREEN_HEIGHT - obstacle_size),
        ]

        # Check for collisions with food within the exclusion radius
        collides_with_food = False
        for food in food_list:
            distance = euclidean_distance(obstacle_pos, food)
            if distance < exclusion_radius:
                collides_with_food = True
                break

        if not collides_with_food:
            # Check for collisions with player
            if not check_collision(
                player_pos, obstacle_pos, player_size, obstacle_size
            ):
                # Check for collisions with other obstacles
                collides_with_obstacle = False
                for obstacle in obstacle_list:
                    if check_collision(
                        obstacle_pos, obstacle, obstacle_size, obstacle_size
                    ):
                        collides_with_obstacle = True
                        break

                if not collides_with_obstacle:
                    obstacle_list.append(obstacle_pos)
                    break

        attempts += 1
