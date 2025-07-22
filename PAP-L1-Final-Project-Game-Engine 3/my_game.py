from game_funcs import *
import game_engine as ge
import random

# Flappy Fish Game
set_game_size(1600, 900)
start_game = False

instructions = print_text('''Press space to jump. Avoid the obstacles!''', 20)
place_element(instructions, 20, 20)

def remove_thing(target):
    remove_el(target)

click(instructions, remove_thing)

# Create scene
background_color("black")
add_background('underwater.png', vertical_align="center", horizontal_align="center")
bg_music = play_music("underwater.mp3")

# Create the player
flappy_fish = add_image('flappyfish.png', 130)
set_collider(flappy_fish, width = 92, height = 50)
set_solid(flappy_fish)
place_element(flappy_fish, 400, 350)
jump(flappy_fish, 100, 1, False)
bind_to_screen(flappy_fish)

ground = ge.screen_height

# Create obstacles
def kelp_obstacles(i):
    global start_game
    if start_game:
        def combo1():
            kelp_mid = add_image("kelpb(3.28).png", 350)
            kelp_mid_height = ground - (kelp_mid.y + kelp_mid.image.get_height())
            set_solid(kelp_mid)
            set_collider(kelp_mid, width = 92, height = kelp_mid.image.get_height())
            place_element(kelp_mid, 700, kelp_mid_height)
   
            kelp_mid2 = add_image("kelpt(3.28).png", 350)
            set_solid(kelp_mid2)
            set_collider(kelp_mid2, width = 92, height = kelp_mid2.image.get_height())
            place_element(kelp_mid2, 700, kelp_mid2.y)

            animate_x(kelp_mid, 2000, -200, 1, False, 450)
            animate_x(kelp_mid2, 2000, -200, 1, False, 450)

        def combo2():
            kelp_big = add_image("kelpb(3.90).png", 350)
            kelp_big_height = ground - (kelp_big.y + kelp_big.image.get_height())
            set_solid(kelp_big)
            set_collider(kelp_big, width = 92, height = kelp_big.image.get_height())
            place_element(kelp_big, 700, kelp_big_height)

            kelp_small2 = add_image("kelpt(1.90).png", 350)
            set_solid(kelp_small2)
            set_collider(kelp_small2, width = 92, height = kelp_small2.image.get_height())
            place_element(kelp_small2, 700, kelp_small2.y)

            animate_x(kelp_big, 2000, -200, 1, False, 450)
            animate_x(kelp_small2, 2000, -200, 1, False, 450)

        def combo3():
            kelp_big2 = add_image("kelpt(3.90).png", 350)
            set_solid(kelp_big2)
            set_collider(kelp_big2, width = 92, height = kelp_big2.image.get_height())
            place_element(kelp_big2, 700, kelp_big2.y)

            kelp_small = add_image("kelpb(1.90).png", 350)
            kelp_small_height = ground - (kelp_small.y + kelp_small.image.get_height())
            set_solid(kelp_small)
            set_collider(kelp_small, width = 92, height = kelp_small.image.get_height())
            place_element(kelp_small, 700, kelp_small_height)

            animate_x(kelp_big2, 2000, -200, 1, False, 450)
            animate_x(kelp_small, 2000, -200, 1, False, 450)

        random.choice([combo1, combo2, combo3])()

set_interval(kelp_obstacles, 2.5, range(0, 10000))

# WARNING: For advanced students/game requirements
# Called once per frame (there are 60 frames per second)
# DO NOT CHANGE FUNCTION NAME
def update():
    global ground
    global start_game
    fish_height = flappy_fish.y + flappy_fish.image.get_height()
    if fish_height >= ge.screen_height:
        print_heading("Game Over", 250)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        start_game = True
    
#DO NOT EDIT BELOW 
ge.start(update)
