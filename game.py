import pgzrun
import random as rnd
import math

# Global Variables
is_game_over = False
is_game_started = False
is_music_on = True
sounds_on = True

class MainCharacter(Actor):
    def __init__(self, image, pos, **kwargs):
        super().__init__(image, pos, **kwargs)

        self.direction = 'right'

        self.idle_animations_right = ['skeleton_idle_0', 'skeleton_idle_1', 'skeleton_idle_2', 'skeleton_idle_3', 'skeleton_idle_4', 'skeleton_idle_5', 
                                'skeleton_idle_6', 'skeleton_idle_7', 'skeleton_idle_8', 'skeleton_idle_9', 'skeleton_idle_10', 'skeleton_idle_11', 
                                'skeleton_idle_12', 'skeleton_idle_13', 'skeleton_idle_14', 'skeleton_idle_15','skeleton_idle_16', 'skeleton_idle_17']
        
        self.running_animations_right = ['skeleton_running_0', 'skeleton_running_1', 'skeleton_running_2', 'skeleton_running_3', 'skeleton_running_4', 
                                'skeleton_running_5', 'skeleton_running_6', 'skeleton_running_7', 'skeleton_running_8', 'skeleton_running_9', 
                                'skeleton_running_10', 'skeleton_running_11']
        
        self.slash_animations_right = ['skeleton_slash_0', 'skeleton_slash_1', 'skeleton_slash_2', 'skeleton_slash_3', 'skeleton_slash_4', 
                                'skeleton_slash_5', 'skeleton_slash_6', 'skeleton_slash_7', 'skeleton_slash_8', 'skeleton_slash_9', 
                                'skeleton_slash_10', 'skeleton_slash_11']
        
        self.slide_animations_right = ['skeleton_sliding_0', 'skeleton_sliding_1', 'skeleton_sliding_2', 'skeleton_sliding_3', 'skeleton_sliding_4', 
                                'skeleton_sliding_5']
    
        self.idle_animations_left = ['skeleton_idle_0_left', 'skeleton_idle_1_left', 'skeleton_idle_2_left', 'skeleton_idle_3_left', 'skeleton_idle_4_left',
                                'skeleton_idle_5_left', 'skeleton_idle_6_left', 'skeleton_idle_7_left', 'skeleton_idle_8_left', 'skeleton_idle_9_left', 
                                'skeleton_idle_10_left', 'skeleton_idle_11_left', 'skeleton_idle_12_left', 'skeleton_idle_13_left', 'skeleton_idle_14_left', 
                                'skeleton_idle_15_left','skeleton_idle_16_left', 'skeleton_idle_17_left']
    
        self.running_animations_left = ['skeleton_running_0_left', 'skeleton_running_1_left', 'skeleton_running_2_left', 'skeleton_running_3_left', 
                                    'skeleton_running_4_left', 'skeleton_running_5_left', 'skeleton_running_6_left', 'skeleton_running_7_left', 
                                    'skeleton_running_8_left', 'skeleton_running_9_left', 'skeleton_running_10_left', 'skeleton_running_11_left']
        
        self.slash_animations_left = ['skeleton_slash_0_left', 'skeleton_slash_1_left', 'skeleton_slash_2_left', 'skeleton_slash_3_left', 'skeleton_slash_4_left', 
                                'skeleton_slash_5_left', 'skeleton_slash_6_left', 'skeleton_slash_7_left', 'skeleton_slash_8_left', 'skeleton_slash_9_left', 
                                'skeleton_slash_10_left', 'skeleton_slash_11_left']
        
        self.slide_animations_left = ['skeleton_sliding_0_left', 'skeleton_sliding_1_left', 'skeleton_sliding_2_left', 'skeleton_sliding_3_left', 
                                      'skeleton_sliding_4_left', 'skeleton_sliding_5_left']
        
        self.idle_animation = 0
        self.running_animation = 0
        self.slash_animation = 0
        self.slide_animation = 0
        
        if self.direction == 'right':
            self.image = self.idle_animations_right[self.idle_animation]
        elif self.direction == 'left':
            self.image = self.idle_animations_left[self.idle_animation]
        
        self.velocity = 0
        self.gravity = 0.5
        
        self.lives = 0
        self.score = 0

    def idle(self, animation_speed):
        
        self.idle_animation += animation_speed
        
        if self.idle_animation >= len(self.idle_animations_right):
            self.idle_animation = 0
        
        if self.direction == 'right':
            self.image = self.idle_animations_right[int(self.idle_animation)]
        elif self.direction == 'left':
            self.image = self.idle_animations_left[int(self.idle_animation)]
        
    def slash(self, animation_speed):
        global is_game_started, is_game_over, sounds_on
    
        if self.slash_animation == 0 and not self.colliderect(fly):
            if is_game_started and not is_game_over and sounds_on:
                sounds.sword_swing.play()
        
        self.slash_animation += animation_speed
        
        if self.slash_animation >= len(self.slash_animations_right):
            self.slash_animation = 0
        
        if self.direction == 'right':
            self.image = self.slash_animations_right[int(self.slash_animation)]
        elif self.direction == 'left':
            self.image = self.slash_animations_left[int(self.slash_animation)]

    def slide(self, animation_speed):
                
        self.slide_animation += animation_speed
        
        if self.slide_animation >= len(self.slide_animations_right):
            self.slide_animation = 0
        
        if self.direction == 'right':
            self.image = self.slide_animations_right[int(self.slide_animation)]
            self.x += 5
        elif self.direction == 'left':
            self.image = self.slide_animations_left[int(self.slide_animation)]
            self.x -= 5

    def running(self, animation_speed):
        
        self.running_animation += animation_speed
        
        if self.running_animation >= len(self.running_animations_right):
            self.running_animation = 0
        
        if self.direction == 'right':
            self.image = self.running_animations_right[int(self.running_animation)]
            self.x += 5
        elif self.direction == 'left':
            self.image = self.running_animations_left[int(self.running_animation)]
            self.x -= 5
        
    def update(self):
        
        if keyboard.right:
            self.direction = 'right'
        elif keyboard.left:
            self.direction = 'left'
        
        if keyboard.up and self.y == 500:
            self.velocity = -15
        elif keyboard.down and self.x < 950 and self.x > 50:
            self.slide(0.5)
        elif keyboard.right and self.x != 950:
            self.running(0.5)
        elif keyboard.left and self.x != 50:
            self.running(0.5)
        elif keyboard.space:
            self.slash(0.8)
        else:
            self.idle(0.35)
            self.run_animation = 0
            self.slash_animation = 0
            
        self.y += self.velocity
        self.velocity += self.gravity
        
        if self.y > 500:
            self.velocity = 0
            self.y = 500
    
WIDTH = 1000
HEIGHT = 600

# Main Chracter
skeleton = MainCharacter('skeleton_idle_0', (WIDTH/2, 500))

# Fly Monster
fly = Actor('fly_monster_0')
fly.pos = (100, 450)

fly_running = 0

fly_animations = ['fly_monster_0', 'fly_monster_1', 'fly_monster_2', 'fly_monster_3', 'fly_monster_4', 'fly_monster_5', 
                  'fly_monster_6', 'fly_monster_7', 'fly_monster_8', 'fly_monster_9', 'fly_monster_10', 'fly_monster_11', 
                  'fly_monster_12', 'fly_monster_13', 'fly_monster_14', 'fly_monster_15','fly_monster_16', 'fly_monster_17']

# Ground Monster
ground = Actor('ground_monster_0')
ground.pos = (900, 500)

ground_running = 0

ground_animations = ['ground_monster_0', 'ground_monster_1', 'ground_monster_2', 'ground_monster_3', 'ground_monster_4', 'ground_monster_5', 
                    'ground_monster_6', 'ground_monster_7', 'ground_monster_8', 'ground_monster_9', 'ground_monster_10', 'ground_monster_11', 
                    'ground_monster_12', 'ground_monster_13', 'ground_monster_14', 'ground_monster_15','ground_monster_16', 'ground_monster_17']

# Floating Coins
gold_coin = Actor('gold')
gold_coin.pos = (100,0)

# Score indicator - Static Coin
static_coin = Actor('static_gold')
static_coin.pos = (900,50)

# Live indicator - Hearts
live1 = Actor('lives')
live1.pos = (50, 50)

live2 = Actor('lives')
live2.pos = (100, 50) 

live3 = Actor('lives')
live3.pos = (150, 50)

# Background Image
background = Actor('bg')
background.pos = (WIDTH/2, HEIGHT/2)

# Start Menu Button
start_button = Actor('play')
start_button.pos = (WIDTH/2, 350)

# Exit Menu Button
exit_button = Actor('exit')
exit_button.pos = (WIDTH/2, 450)

# Sound Menu Button
sound_button = Actor('sound')
sound_button.pos = (WIDTH/2 - 50, 250)

# No Sound Menu Button
no_sound_button = Actor('no_sound')
no_sound_button.pos = (WIDTH/2 + 50, 250)

# Restart Menu Button
restart_button = Actor('restart')
restart_button.pos = (WIDTH/2, 350)

if is_music_on:
    music.play('game_music')
else:
    music.stop()

def update():
    global is_game_started, is_game_over, fly_running, ground_running, sounds_on

    if is_game_started and not is_game_over:
        skeleton.update()

        fly_running += 0.5

        if fly_running >= len(fly_animations):
            fly_running = 0

        fly.image = fly_animations[int(fly_running)]

        ground_running += 0.5

        if ground_running >= len(ground_animations):
            ground_running = 0

        ground.image = ground_animations[int(ground_running)]

        fly.x += 4
        if fly.x >= 1050:
            fly.x = rnd.randint(-1000, 100)
            fly.y = 450

        ground.x -= 4
        if ground.x < -50:
            ground.x = rnd.randint(900, 2000)
            ground.y = 500
        
        gold_coin.y += rnd.randint(3,6)
        if gold_coin.y > 650:
            gold_coin.y = 0
            gold_coin.x = rnd.randint(100, 900)        

        # Collisions with fly
        if not keyboard.space or not keyboard.up:
            if not keyboard.down and abs(skeleton.x - fly.x) <= 10:
                if is_game_started and not is_game_over:
                    # Monster Hit
                    skeleton.lives -= 1
                    if skeleton.lives == 2:
                        live3.x = 2000 #off the screen
                    elif skeleton.lives == 1:
                        live2.x = 2000 #off the screen
                    elif skeleton.lives == 0:
                        live1.x = 2000 #off the screen
                        is_game_over = True
                        
                        if sounds_on:
                            sounds.game_over.play()
                    
                    if sounds_on:
                        sounds.hit.play()
                    fly.x = rnd.randint(-1000, 100)
                    fly.y = 450
        
        if keyboard.space and abs(skeleton.x - fly.x) <= 100:
            if is_game_started and not is_game_over:
                # Sword Hit
                skeleton.score += 1
                if sounds_on:
                    sounds.sword_cut.play()
                fly.x = rnd.randint(-1000, 100)
                fly.y = 450
        
        # Collision with ground
        if not keyboard.space or not keyboard.down:
            if not keyboard.up and abs(skeleton.x - ground.x) <= 10:
                if is_game_started and not is_game_over:  
                    # Monster Hit
                    skeleton.lives -= 1
                    if skeleton.lives == 2:
                        live3.x = 2000 #off the screen
                    elif skeleton.lives == 1:
                        live2.x = 2000 #off the screen
                    elif skeleton.lives == 0:
                        live1.x = 2000 #off the screen
                        is_game_over = True
                        
                        if sounds_on:
                            sounds.game_over.play()

                    if sounds_on:
                        sounds.hit.play()
                    ground.x = rnd.randint(900, 2000)
                    ground.y = 500
        
        if keyboard.space and abs(skeleton.x - ground.x) <= 100:
            
            if is_game_started and not is_game_over:
                # Sword Hit
                skeleton.score += 1
                if sounds_on:
                    sounds.sword_cut.play()
                ground.x = rnd.randint(900, 2000)
                ground.y = 500
        
        # Collect Coins    
        if abs(skeleton.x - gold_coin.x) <= 50 and (abs(skeleton.y - gold_coin.y) <= 25):
            if is_game_started and not is_game_over:
                if sounds_on:
                    sounds.collect.play()
                skeleton.score += 1
                gold_coin.y = 0
                gold_coin.x = rnd.randint(100, 900)

# Get mouse click events and bind them to menu buttons            
def on_mouse_down(pos):
    global is_game_started, is_game_over, sounds_on, is_music_on
    
    if abs(pos[0] - start_button.pos[0]) <= 50 and abs(pos[1] - start_button.pos[1]) <= 50:
        is_game_started = True
        is_game_over = False
        skeleton.lives = 3
        skeleton.score = 0

    if abs(pos[0] - restart_button.pos[0]) <= 50 and abs(pos[1] - restart_button.pos[1]) <= 50:
        is_game_started = True
        is_game_over = False
        
        skeleton.lives = 3
        skeleton.score = 0
        
        live1.pos = (50, 50)
        live2.pos = (100, 50) 
        live3.pos = (150, 50)
        
        skeleton.pos  = (WIDTH/2, 500)
        fly.pos = (100, 450)
        ground.pos = (900, 500)
        
    if abs(pos[0] - sound_button.pos[0]) <= 50 and abs(pos[1] - sound_button.pos[1]) <= 50:
        
        if not is_music_on:
            is_music_on = True
            music.play('game_music')
        
        if not sounds_on:
            sounds_on = True

    if abs(pos[0] - no_sound_button.pos[0]) <= 50 and abs(pos[1] - no_sound_button.pos[1]) <= 50:
        is_music_on = False
        music.stop()

        if sounds_on:
            sounds_on = False
        
    if abs(pos[0] - exit_button.pos[0]) <= 50 and abs(pos[1] - exit_button.pos[1]) <= 50:
        quit()

def draw():
    global is_game_over, sounds_on, is_game_started
    
    background.draw()
    
    if not is_game_started and not is_game_over:

        screen.draw.text('Monster Smash', (240,90), color=('black'), fontname='pacifico', fontsize=75)
        start_button.draw()
        sound_button.draw()
        no_sound_button.draw()
        exit_button.draw()

    elif is_game_started and not is_game_over:
        
        skeleton.draw()

        fly.draw()
        ground.draw()
        
        gold_coin.draw()
        static_coin.draw()

        live1.draw()
        live2.draw()
        live3.draw()
        
        screen.draw.text('x ' +  str(skeleton.score), (920,43), color=('black'))

    else:
        
        screen.draw.text('GAME OVER', (250,25), color=('black'), fontname='pacifico', fontsize=75)
        screen.draw.text('Score: ' + str(skeleton.score), (400,125), color=('black'), fontname='pacifico', fontsize=50)
        sound_button.draw()
        no_sound_button.draw()
        restart_button.draw()
        exit_button.draw()

pgzrun.go()