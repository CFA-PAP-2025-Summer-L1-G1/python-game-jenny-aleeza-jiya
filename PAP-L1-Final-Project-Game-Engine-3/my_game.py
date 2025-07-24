from game_funcs import *
import game_engine as ge
from random import choice

# Flappy Fish Game Setup
set_game_size(1600, 900)
ground = ge.screen_height
game_over = False 
start_game = False
score = 0
score_text = None
kelp2_list = []
kelp_list = []

# For removing instructions
instructions = print_text('''Press space to jump. Avoid the obstacles!''', 20)
place_element(instructions, 20, 20)
def remove_thing(target):
    remove_el(target)
click(instructions, remove_thing)

# Background
background_color("black")
add_background('underwater.png', vertical_align="center", horizontal_align="center")
bg_music = play_music("underwater.mp3")

# Player
flappy_fish = add_image('flappyfish.png', 130)
set_collider(flappy_fish, width=92, height=50)
set_solid(flappy_fish)
place_element(flappy_fish, 400, 350)
jump(flappy_fish, 130, 1, False)
bind_to_screen(flappy_fish)

# --- Obstacle Combos ---
def kelp_obstacles(i):
    global start_game, game_over
    if start_game and not game_over:
        def combo1(): # player must pass through middle opening
            kelp_mid = add_image("kelpb(3.28).png", 350)
            kelp_mid_y = ge.screen_height - kelp_mid.image.get_height()
            set_solid(kelp_mid)
            set_collider(kelp_mid, width=92, height=kelp_mid.image.get_height())
            place_element(kelp_mid, 700, kelp_mid_y)
            
            kelp_mid2 = add_image("kelpt(3.28).png", 350)
            set_solid(kelp_mid2)
            set_collider(kelp_mid2, width=92, height=kelp_mid2.image.get_height())
            place_element(kelp_mid2, 700, 0)

            kelp_list.append(kelp_mid2)
            kelp_list.append(kelp_mid)
            kelp2_list.append(kelp_mid2)
            kelp_mid2.passed = False

            return kelp_mid, kelp_mid2

        def combo2(): # player must pass through the top opening
            kelp_big = add_image("kelpb(3.90).png", 350)
            kelp_big_y = ge.screen_height - kelp_big.image.get_height()
            set_solid(kelp_big)
            set_collider(kelp_big, width=92, height=kelp_big.image.get_height())
            place_element(kelp_big, 700, kelp_big_y)

            kelp_small2 = add_image("kelpt(1.90).png", 350)
            set_solid(kelp_small2)
            set_collider(kelp_small2, width=92, height=kelp_small2.image.get_height())
            place_element(kelp_small2, 700, 0)

            kelp_list.append(kelp_small2)
            kelp_list.append(kelp_big)
            kelp2_list.append(kelp_small2)
            kelp_small2.passed = False

            return kelp_big, kelp_small2

        def combo3(): # player must pass through the bottom opening
            kelp_big2 = add_image("kelpt(3.90).png", 350)
            set_solid(kelp_big2)
            set_collider(kelp_big2, width=92, height=kelp_big2.image.get_height())
            place_element(kelp_big2, 700, 0)
          
            kelp_small = add_image("kelpb(1.90).png", 350)
            kelp_small_y = ge.screen_height - kelp_small.image.get_height()
            set_solid(kelp_small)
            set_collider(kelp_small, width=92, height=kelp_small.image.get_height())
            place_element(kelp_small, 700, kelp_small_y)
            
            kelp_list.append(kelp_small)
            kelp_list.append(kelp_big2)
            kelp2_list.append(kelp_small)
            kelp_small.passed = False

            return kelp_big2, kelp_small

        obstacle_1, obstacle_2 = choice([combo1, combo2, combo3])()
        animate_x(obstacle_1, 2000, -2000, 1, False, 450)
        animate_x(obstacle_2, 2000, -2000, 1, False, 450)

set_interval(kelp_obstacles, 2.5, range(0, 10000))

# --- Score Display ---
def update_score():
    global score_text
    if score_text in ge.elements:
        remove_el(score_text)
    score_text = print_text(f'Score = {score}', 20)
    place_element(score_text, 40, 40)

# --- Game Over ---
def gameover():
    global game_over
    if not game_over:
        game_over = True
        clear()
        print_heading(f"Game Over", 250)
        final_score_text = print_text(f"Final Score = {score}", 80)
        place_element(final_score_text, 593, 550)
        start_over_text = print_text ("Press the space bar to try again", 50)
        place_element(start_over_text, 530, 720)

# --- Restart ---
def restart_game():
    clear() 
    global score, kelp2_list, kelp_list, game_over, start_game, score_text

    kelp_list.clear()
    kelp2_list.clear()
    score = 0 
    game_over = False
    start_game = True

    if score_text in ge.elements:
        remove_el(score_text)
    update_score()

# --- Game Loop ---
def update():
    global ground, start_game, score, flappy_fish

    # Game Over if fish hits bottom
    fish_height = flappy_fish.y + flappy_fish.image.get_height()
    if fish_height >= ge.screen_height and not game_over:
        gameover()
 
    # Start game on space key or restart game on space key when game over
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if game_over:
            clear()
            restart_game()

            flappy_fish = add_image('flappyfish.png', 130)
            set_collider(flappy_fish, width=92, height=50)
            set_solid(flappy_fish)
            place_element(flappy_fish, 400, 350)
            jump(flappy_fish, 130, 1, False)
            bind_to_screen(flappy_fish)
        else:
            start_game = True

    for kelp in kelp2_list:
        if not kelp.passed and kelp.x < flappy_fish.x:
            kelp.passed = True
            score += 1
            update_score()

    for kelps in kelp_list:
        if flappy_fish.collide(kelps) and not game_over:
            gameover()
    # Restart game when space pressed 

# --- Start Game ---
ge.start(update)