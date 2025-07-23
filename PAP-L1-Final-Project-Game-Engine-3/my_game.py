from game_funcs import *
import game_engine as ge
import random

# Flappy Fish Game Setup
set_game_size(1600, 900)
start_game = False
score = 0
score_text = None
kelp2_list = []
kelp_list = []

instructions = print_text('''Press space to jump. Avoid the obstacles!''', 20)
place_element(instructions, 20, 20)

def remove_thing(target):
    remove_el(target)

click(instructions, remove_thing)

# Background
background_color("black")
add_background('underwater.png', vertical_align="center", horizontal_align="center")
bg_music = play_music("underwater.mp3")

# Fish
flappy_fish = add_image('flappyfish.png', 130)
set_collider(flappy_fish, width=92, height=50)
set_solid(flappy_fish)
place_element(flappy_fish, 400, 350)
jump(flappy_fish, 100, 1, False)
bind_to_screen(flappy_fish)

ground = ge.screen_height

# --- Obstacle Combos ---
def kelp_obstacles(i):
    global start_game
    if start_game:
        def combo1():
            kelp_mid = add_image("kelpb(3.28).png", 350)
            kelp_mid_y = ge.screen_height - kelp_mid.image.get_height()
            set_solid(kelp_mid)
            set_collider(kelp_mid, width=92, height=kelp_mid.image.get_height())
            place_element(kelp_mid, 700, kelp_mid_y)
            kelp_list.append(kelp_mid)


            kelp_mid2 = add_image("kelpt(3.28).png", 350)
            set_solid(kelp_mid2)
            set_collider(kelp_mid2, width=92, height=kelp_mid2.image.get_height())
            place_element(kelp_mid2, 700, 0)

            animate_x(kelp_mid, 2000, -200, 1, False, 450)
            animate_x(kelp_mid2, 2000, -200, 1, False, 450)
            kelp_mid2.passed = False
            kelp2_list.append(kelp_mid2)
            kelp_list.append(kelp_mid2)

        def combo2():
            kelp_big = add_image("kelpb(3.90).png", 350)
            kelp_big_y = ge.screen_height - kelp_big.image.get_height()
            set_solid(kelp_big)
            set_collider(kelp_big, width=92, height=kelp_big.image.get_height())
            place_element(kelp_big, 700, kelp_big_y)
            kelp_list.append(kelp_big)

            kelp_small2 = add_image("kelpt(1.90).png", 350)
            set_solid(kelp_small2)
            set_collider(kelp_small2, width=92, height=kelp_small2.image.get_height())
            place_element(kelp_small2, 700, 0)

            animate_x(kelp_big, 2000, -200, 1, False, 450)
            animate_x(kelp_small2, 2000, -200, 1, False, 450)
            kelp_small2.passed = False
            kelp2_list.append(kelp_small2)
            kelp_list.append(kelp_small2)

        def combo3():
            kelp_big2 = add_image("kelpt(3.90).png", 350)
            set_solid(kelp_big2)
            set_collider(kelp_big2, width=92, height=kelp_big2.image.get_height())
            place_element(kelp_big2, 700, 0)
            kelp_list.append(kelp_big2)

            kelp_small = add_image("kelpb(1.90).png", 350)
            kelp_small_y = ge.screen_height - kelp_small.image.get_height()
            set_solid(kelp_small)
            set_collider(kelp_small, width=92, height=kelp_small.image.get_height())
            place_element(kelp_small, 700, kelp_small_y)

            animate_x(kelp_big2, 2000, -200, 1, False, 450)
            animate_x(kelp_small, 2000, -200, 1, False, 450)
            kelp_small.passed = False
            kelp2_list.append(kelp_small)
            kelp_list.append(kelp_small)

        random.choice([combo1, combo2, combo3])()

# --- Score Display ---
def update_score():
    global score_text
    if score_text:
        remove_el(score_text)
    score_text = print_text(f'Score = {score}', 20)
    place_element(score_text, 40, 40)

set_interval(kelp_obstacles, 2.5, range(0, 10000))

# --- Game Loop ---
def update():
    global ground
    global start_game
    global score
    flappy_fish.x = 400

    # Game Over if fish hits bottom
    fish_height = flappy_fish.y + flappy_fish.image.get_height()
    if fish_height >= ge.screen_height:
        print_heading("Game Over", 250)

    # Start game on space key
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        start_game = True

    for kelp in kelp2_list:
        if not kelp.passed and kelp.x < flappy_fish.x:
            kelp.passed = True
            score += 1
            update_score()

    for kelps in kelp_list:
        if flappy_fish.collide(kelps):
            print_heading("Game Over", 250)

# --- Start Game ---
ge.start(update)
