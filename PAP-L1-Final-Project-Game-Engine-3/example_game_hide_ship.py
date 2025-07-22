from game_funcs import *
import game_engine
import random

# Create scene
GAME_HEIGHT = 900
GAME_WIDTH = 1600
set_game_size(GAME_WIDTH, GAME_HEIGHT)
background_color("black")
add_background('background.jpg', horizontal_align = "center", vertical_align="bottom")#, crop_size = (2314, 1302))

instructions = print_text('''HIDE SHIP GAME WASD or arrows to move.''', 20)
instructions2 = print_text('''Hide your ship behind the bouncing platforms.''', 20)

place_element(instructions, GAME_WIDTH-300, 30)
place_element(instructions2, GAME_WIDTH-300, 60)

#function definitions

def alien_victory():
    clear()
    print_heading('Direct hit! You lost', 48)
    play_audio("player-explosion.mp3")

def alien_bomb_platform():
    global alien_score
    alien_score += 1
    update_text(a_score_text, 'Aliens: ' + str(alien_score))
    if alien_score > 500:
        scoreboard()

def safe_haven_points():
    play_audio("player-haven-score.mp3")
    global player_score
    player_score += 1
    update_text(p_score_text, 'PLayer: ' + str(player_score))
    if player_score > 500:
        scoreboard()

def scoreboard():
    clear()
    if player_score > 500:
        print_heading("You win!", 80) 
        play_audio("win.mp3") 
    else:
        print_heading('Aliens win', 80)
        play_audio("lose.mp3")         


# Add and position player's ship with WASD control
player_ship = add_image('my_ship.png', 100)
place_element(player_ship, 1000, 280)
bind_to_screen(player_ship)

wasd_move(player_ship, speed = 350)
arrows_move(player_ship, speed = 350)   

# Add safe haven platforms
p_1 = add_image("platform-1.png", 150) 
place_element(p_1, 50, 400)
# bounce(p_1, 40) 

p_2 = add_image("platform-2.png",150) 
place_element(p_2, 400, 500)
# bounce(p_2, 50) 

p_3 = add_image("platform-3.png", 150) 
place_element(p_3, 800, 400)
# bounce(p_3, 60) 

p_4 = add_image("platform-4.png", 150) 
place_element(p_4, 1200, 300)
# bounce(p_4, 50) 

# list of platforms
platforms = [p_1,p_2,p_3,p_4]
# Add and animate aliens
aliens = []
def add_alien(i):
    image = add_image('alien.png', 100)
    aliens.append(image) 
    # random_x = random.randint(50,1300)
    random_x_start = random.randint(0, int(GAME_WIDTH/2))
    random_x_end = random.randint(int(GAME_WIDTH/2), GAME_WIDTH)
    # place_element(image, random_x, -100)
    animate_y(image, -100, 800, "infinite", True, 200, True);  
    animate_x(image, random_x_start, random_x_end, "infinite", True, 400, True); 
    detect_collision(image, player_ship, alien_victory)
    set_solid(image)
    
    # If an alien hits your ship, you lose
    # If an alien hits a platform, aliens get 1 point    
    for platform in platforms:
        detect_collision(platform, image, alien_bomb_platform)
set_interval(add_alien, 0.5, range(5))

print("hello there")
# Initialize, print, and position scores  
player_score = 0
alien_score = 0
p_score_text = print_text('PLayer: ' + str(player_score), 18)
a_score_text = print_text('Aliens: ' + str(alien_score), 18)
place_element(p_score_text, 20, 20)
place_element(a_score_text, 20, 60)

# When you hide behind a platform, you get points
for platform in platforms:
    detect_collision(platform, player_ship, safe_haven_points)

# WARNING: For advanced students/game requirements
# Called once per frame (there are 60 frames per second)
# DO NOT CHANGE FUNCTION NAME
def update():
    pass

#DO NOT EDIT BELOW 
game_engine.start(update)