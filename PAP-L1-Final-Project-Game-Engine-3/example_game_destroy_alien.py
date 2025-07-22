from game_funcs import *
import game_engine
import random

instructions = print_text('DESTROY ALIENT GAME Click on an alien ship to destroy it.', 20)

place_element(instructions, 800, 30)

#function definitions

def kill_alien(target):
    remove_el(target)
    global player_score
    player_score = player_score + 1
    update_text(p_score_text, 'Player: '+str(player_score))
    play_audio(player_score_sound)
    if player_score > 20:
        scoreboard()

def alien_bomb_platform():
    global alien_score
    alien_score = alien_score + 1
    update_text(a_score_text, 'Aliens: '+str(alien_score))
    # if alien touches platform for 120 frames (2 seconds) then they win
    if alien_score > 120:
        scoreboard()   

def scoreboard():
    clear()
    if player_score > 20:
        print_heading("You win", 100) 
        play_audio(win) 
    else:
        print_heading('Aliens win', 100)         
        play_audio(lose)

# Scene set up
background_color("black")
add_background('background.jpg')  

# Add sound effects
player_score_sound = "player-explosion.mp3"
alien_haven_score = "alien-haven-score.mp3"
win = "win.mp3"
lose = "lose.mp3"

# Add safe haven platforms
p_1 = add_image("platform-1.png", 200) 
place_element(p_1, 50, 400)

p_2 = add_image("platform-2.png", 200) 
place_element(p_2, 300, 450)

p_3 = add_image("platform-3.png", 200) 
place_element(p_3,600, 400)

p_4 = add_image("platform-4.png", 200) 
place_element(p_4, 900, 350)

# list of platforms
platforms = [p_1,p_2,p_3,p_4]

# Add and animate aliens
aliens = []
def add_alien(i):
    image = add_image('alien.png', 80)
    aliens.append(image)
    random_x = random.randint(50,1300)
    place_element(image, random_x, -100)
    animate_y(image, -100, 1200, "infinite", True, 90);  
    animate_x(image, random_x, 200, "infinite", True, 90); 
    # When you click on an alien you kill it and get 1 point
    # If an alien hits a platform, aliens get 1 point  
    click(image, kill_alien)
    for platform in platforms:
        detect_collision(platform, image, alien_bomb_platform)

set_interval(add_alien, 0.5, range(0, 26))

# Initialize, print, and position scores  
player_score = 0
alien_score = 0
p_score_text = print_text('Player: '+str(player_score), 24)
a_score_text = print_text('Aliens: '+str(alien_score), 24)
place_element(p_score_text, 20, 20)
place_element(a_score_text, 20, 60)


# WARNING: For advanced students/game requirements
# Called once per frame (there are 60 frames per second)
# DO NOT CHANGE FUNCTION NAME
def update():
    pass

#DO NOT EDIT BELOW 
game_engine.start(update)