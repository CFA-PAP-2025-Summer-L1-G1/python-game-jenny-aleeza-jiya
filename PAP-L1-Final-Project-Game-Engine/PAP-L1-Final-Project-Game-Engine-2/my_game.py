from game_funcs import *
import game_engine as ge

start_game = False

# Flappy Fish Game
set_game_size(1600, 900)

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
        kelp = add_image("kelp.png", 350)
        kelp_height = ground - (kelp.y + kelp.image.get_height())
        set_solid(kelp)
        set_collider(kelp, width = 92, height = kelp.image.get_height())
        place_element(kelp, 700, kelp_height)
        animate_x(kelp, 2000, -200, 1, False, 450)
   
        kelp2 = add_image("kelp2.png", 350)
        set_solid(kelp2)
        set_collider(kelp2, width = 92, height = kelp2.image.get_height())
        place_element(kelp2, 700, kelp2.y)
        animate_x(kelp2, 2000, -200, 1, False, 450)
    else:
        print("hello")
         
set_interval(kelp_obstacles, 2.0, range(0, 10000))

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
