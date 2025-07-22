from game_funcs import *
import game_engine
import random

# Dino jump game
# If the dino jumps over all the asteroids, you win!

explode = "player-explosion.mp3"

instructions = print_text('''DINO JUMP GAME WASD or arrows to move. Space to jump.''', 20)

place_element(instructions, 20, 20)
   
def remove_thing(target):
    remove_el(target)

click(instructions, remove_thing)

def extinction():
    clear()
    print_heading('You lose!', 68)
    play_audio(explode)

def player_victory():
    clear()
    print_heading('You win!', 68)

# Create scene
background_color("black")
add_background('underwater.png', vertical_align="center", horizontal_align="center")
bg_music = play_music("underwater.mp3")

# Create the player
player_dino = add_image('flappyfish.png', 100)


set_collider(player_dino, width = 82, height = 40)
set_solid(player_dino)
place_element(player_dino, 250, 250)
jump(player_dino, 100, 1, False)
bind_to_screen(player_dino)

# wasd_move(player_dino, ['w', 's'], speed = 600)
# arrows_move(player_dino, ['up', 'down'], speed = 600)

platform = add_image("wall.png", 100)
rotate_image(platform, 90)
set_collider(platform, height = 20, offset_y = 15)
place_element(platform, 500, 450)
set_solid(platform)

wall = add_image('wall.png', 80)
place_element(wall, -80, 400)

# Add and animate asteroids
asteroids = []

def spawn_asteroid(i):
    image = add_image('asteroid.png', 120)
    asteroids.append(image)
    place_element(image, 1200, random.choice([550, 250, 400]))
    animate_x(image, 1200, -200, 2, False, 450)
    # If an asteroid hits the dino, you lose
    detect_collision(player_dino, image, extinction)
    # This will be the last asteroid
set_interval(spawn_asteroid, 2.5, range(0, 10))

# WARNING: For advanced students/game requirements
# Called once per frame (there are 60 frames per second)
# DO NOT CHANGE FUNCTION NAME
def update():
    if player_dino.start:
        ground = game_engine.screen_height
        dino_height = player_dino.y + player_dino.image.get_height()
        if dino_height >= game_engine.screen_height:
            print_heading("Game Over", 250)
            
#DO NOT EDIT BELOW 
game_engine.start(update)