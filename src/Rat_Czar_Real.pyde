# Rat Czar Ripley Killen


# game states
END_SCREEN = 2
START_SCREEN = 0
GAME_PLAYING = 1

# Starting game state
current_state = START_SCREEN

# make points and clicks
points = 0
click_counter = 0




def setup():
    size(400, 400)
    background(400);
    global rat
    rat = loadImage("RatCzar.png")  # Load rat
    global hammer
    hammer = loadImage("Hammer2.png")

def draw():
    global current_state
   # print(curent_state)
    if current_state == START_SCREEN:
        draw_start_screen()
    elif current_state == GAME_PLAYING:
        draw_game()
    elif current_state == END_SCREEN:
        draw_end_screen()

def draw_start_screen():
    background(255)
    textAlign(CENTER, CENTER)
    fill(155,0,0)
    textSize(20)
    text("Welcome To Rat Czar! Click Anywhere to Begin ", width/2, height/2)
    

def draw_game():
    
    background(255)
    
  
    fill(0)
    textSize(20)
    text("Points: " + str(points), 350, 20)
    text("Clicks: " + str(click_counter), 350, 50)
    image(rat, width/2 - rat.width/2, height/2 - rat.height/2)
    image(hammer, mouseX-40, mouseY-30)
    
def draw_end_screen():
    background(0,400,0)
    fill(255)
    textSize(25)
    text("Congratulations!", width/2, height/1.5 -100)
    textSize(20)
    text("You have killed all the rats in New York City!" , width/2, height/2 +40)
    textSize(15)
    textColor(30)
    text("You have replaced Kathleen Cordati as the RAT CZAR!" , width/2, height/2 +80)
    
def update_points():
    global points, current_state, END_SCREEN
    points += 100  # Start points
    if points > 999:
        current_state = END_SCREEN
        
def mouseClicked():
    global current_state, click_counter

    if current_state == START_SCREEN:
        current_state = GAME_PLAYING
    elif current_state == GAME_PLAYING:
        # Check iif rat clicked
        if (mouseX > width/2 - rat.width and mouseX < width/2 + rat.width and
                mouseY > height/2 - rat.height and mouseY < height/2 + rat.height):
            click_counter += 1  # Click counter
            update_points()
    elif current_state == END_SCREEN:
        draw_end_screen
