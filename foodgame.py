from vars import *
from avoid_obstacles import *
from evolution_step import *
from spawn_obstacles import *
from spawn_food import *



# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # AI movement
    evolution_step()
    
    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        move_player(-player_speed, 0)
    if keys[pygame.K_RIGHT]:
        move_player(player_speed, 0)
    if keys[pygame.K_UP]:
        move_player(0, -player_speed)
    if keys[pygame.K_DOWN]:
        move_player(0, player_speed)

    # Spawn food and obstacles randomly
    if random.randint(0, 100) < 3:
        spawn_food()

    if random.randint(0, 100) < 1:
        spawn_obstacle()

    # Check for collisions with food
    for food in food_list:
        if check_collision(player_pos, food, player_size, food_size):
            food_list.remove(food)
            food_eaten += 1

    # Check for collisions with obstacles
    for obstacle in obstacle_list:
        if check_collision(player_pos, obstacle, player_size, obstacle_size):
            game_over = True

    # Clear the screen
    screen.fill(WHITE)

    # Draw the player
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

    # Draw food
    for food in food_list:
        pygame.draw.rect(screen, GREEN, (food[0], food[1], food_size, food_size))

    # Draw obstacles
    for obstacle in obstacle_list:
        pygame.draw.rect(screen, BLACK, (obstacle[0], obstacle[1], obstacle_size, obstacle_size))

    # Display food eaten count
    font = pygame.font.Font(None, 30)
    text = font.render("Food Eaten: " + str(food_eaten), True, BLACK)
    screen.blit(text, (10, 10))

    # Update the screen
    pygame.display.flip()

    # Control the frame rate
    clock.tick(160)

# End of the game
pygame.quit()
sys.exit()