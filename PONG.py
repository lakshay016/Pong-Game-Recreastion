'''
Template
Lakshay 
May 24th 2023
ICS3UO-A
Mr.Manyanga
This program will create a functional replica of the game "Pong". It will contain 3 different levels, and help for users who need assisstance. 
INPUT: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if is_menu:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.collidepoint(event.pos):
                    is_menu = False
                    is_running = True
                    ball_speed_x = random.choice([-5, 5])
                    ball_speed_y = random.choice([-5, 5])
                    Lpaddle_speed = easy_paddle_speed - 1
                elif medium_button.collidepoint(event.pos):
                    is_menu = False
                    is_running = True
                    ball_speed_x = random.choice([-7, 7])
                    ball_speed_y = random.choice([-7, 7])
                    Lpaddle_speed = medium_paddle_speed - 1 
                elif hard_button.collidepoint(event.pos):
                    is_menu = False
                    is_running = True
                    ball_speed_x = random.choice([-10, 10])
                    ball_speed_y = random.choice([-10, 10])
                    Lpaddle_speed = hard_paddle_speed - 1
                elif help_button.collidepoint(event.pos):
                    is_menu = False 
                    is_help = True
                else:
                    if back_button.collidepoint(event.pos):
                        is_menu = True
        if is_running:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    Rpaddle_speed += Lpaddle_speed
                if event.key == pygame.K_UP:
                    Rpaddle_speed -= Lpaddle_speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    Rpaddle_speed -= Lpaddle_speed
                if event.key == pygame.K_UP:
                    Rpaddle_speed += Lpaddle_speed
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    is_running = False
                    is_menu = True
                    reset_game()
PROCESS:
    def display_text(text, x, y, font_size, color, centered=False):
        font = pygame.font.Font('freesansbold.ttf', font_size)
        rendered_text = font.render(text, True, color)
        text_rect = rendered_text.get_rect()
        if centered:
            text_rect.center = (x, y)
        else:
            text_rect.topleft = (x, y)
        screen.blit(rendered_text, text_rect)
    def ball_mechanism(ball_speed_x, ball_speed_y, Lpaddle_score, Rpaddle_score):
        ball.x += ball_speed_x #create an illusion of movement by updating the position of the ball by minimal pixels 
        ball.y += ball_speed_y
        if ball.top <= 0 or ball.bottom >= screen_height: 
            ball_speed_y *= -1
        if ball.left <= 0: 
            Rpaddle_score += 1
            ball_speed_x, ball_speed_y = ball_reset(ball_speed_x, ball_speed_y)
        if ball.right >= screen_width:
            Lpaddle_score += 1
            ball_speed_x, ball_speed_y = ball_reset(ball_speed_x, ball_speed_y)
        if ball.colliderect(Lpaddle) and ball_speed_x < 0:
            ball_speed_x *= -1
            ball.x = Lpaddle.right + 1  
        if ball.colliderect(Rpaddle) and ball_speed_x > 0: 
            ball_speed_x *= -1
            ball.x = Rpaddle.left - ball.width - 1  
        return ball_speed_x, ball_speed_y, Lpaddle_score, Rpaddle_score 
    def ball_reset(ball_speed_x, ball_speed_y):
        ball.center = (screen_width / 2, screen_height / 2)
        ball_speed_y *= random.choice((-1, 1)) 
        ball_speed_x *= random.choice((-1, 1))
        return ball_speed_x, ball_speed_y
    def Rpaddle_mechanism():
        Rpaddle.y += Rpaddle_speed
        if Rpaddle.top <= 0:
            Rpaddle.top = 0
        if Rpaddle.bottom >= screen_height:
            Rpaddle.bottom = screen_height
    def ai_Lpaddle_mechanism():
        if (Lpaddle.centery + 40 ) < ball.y:
            Lpaddle.top += Lpaddle_speed  
        if (Lpaddle.centery - 40 ) > ball.y:
            Lpaddle.bottom -= Lpaddle_speed 
        if Lpaddle.top <= 0:
            Lpaddle.top = 0
        if Lpaddle.bottom >= screen_height:
            Lpaddle.bottom = screen_height        
    def reset_game(): 
        global Rpaddle_speed, Rpaddle_score, Lpaddle_score, ball_speed_x, ball_speed_y
        Rpaddle_speed = 0
        Rpaddle_score = 0
        Lpaddle_score = 0
        ball.centerx = screen_width // 2
        ball.centery = screen_height // 2
        ball_speed_x = 5 * random.choice((-1, 1))
        ball_speed_y = 5 * random.choice((-1, 1))
        Lpaddle.y = screen_height / 2 - 70
        Rpaddle.y = screen_height / 2 - 70]]

                if Lpaddle_score >= 5:
                if Rpaddle_score >= 5:
                if Rpaddle_score == 5 and Lpaddle_score == 0:
                
OUTPUT:
    if is_menu:
        screen.fill((48, 50, 52))
        display_text("Pong", screen_width // 2, 100, 100, (200, 200, 200), centered=True)
        pygame.draw.rect(screen, (200, 200, 200), easy_button)
        pygame.draw.rect(screen, (200, 200, 200), medium_button)
        pygame.draw.rect(screen, (200, 200, 200), hard_button)
        pygame.draw.rect(screen, (48,50,52), help_button)
        display_text("Easy", easy_button.centerx, easy_button.centery, 40, (48, 50, 52), centered=True)
        display_text("Medium", medium_button.centerx, medium_button.centery, 40, (48, 50, 52), centered=True)
        display_text("Hard", hard_button.centerx, hard_button.centery, 40, (48, 50, 52), centered=True)
        display_text("Help", help_button.x + help_button.width // 2, help_button.y + help_button.height // 2, 20, (200,200,200), centered=True)
        pygame.display.update()
    if is_help:
        screen.fill((48, 50, 52))
        display_text("Welcome to Pong!", screen_width // 2, 50, 40, (200, 200, 200), centered=True)
        display_text("This is a recreation of the classic arcade game Pong.", screen_width // 2, 120, 14, (200, 200, 200), centered=True)
        display_text("In this game, you play on the right side and control the paddle with the up and down arrow keys to move up and down.", screen_width // 2, 140, 14, (200, 200, 200), centered=True)
        display_text("Your opponent is the left paddle which is controlled by the computer.", screen_width // 2, 180, 14, (200, 200, 200), centered=True)
        display_text("The objective is to score 5 points. To do this hit the ball past the opponent (hit the left wall)", screen_width // 2, 200, 14, (200, 200, 200), centered=True)
        display_text("However, the computer will also be trying to score points by hitting the ball past you (making it hit the right wall)", screen_width // 2, 220, 14, (200, 200, 200), centered=True)
        display_text("To start playing, return to the homepage using the back button on the top left and select a difficulty.", screen_width // 2, 260, 14, (200, 200, 200), centered=True)
        display_text("You can exit a game by pressing the back button to return to the homepage.", screen_width // 2, 280, 14, (200, 200, 200), centered=True)
        display_text("Too close the application, return to the homepage and then press the 'x' button on the top right of the window", screen_width // 2, 300, 14, (200, 200, 200), centered=True)
        display_text("Have Fun!", screen_width // 2, 320, 14, (200, 200, 200), centered=True)
        display_text("Is the game too easy for you?", screen_width // 2, 360, 14, (200, 200, 200), centered=True)
        display_text("Well, if you want to challenge yourself, try finding the easter egg...", screen_width // 2, 380, 14, (200, 200, 200), centered=True)
        display_text("(hint: You cannot let the opponent score... at all!)", screen_width // 2, 400, 14, (200, 200, 200), centered=True)
        pygame.draw.rect(screen, (48,50,52), back_button)
        display_text("Back", back_button.x + back_button.width // 2, back_button.y + back_button.height // 2, 14, (200,200,200), centered=True)
        pygame.display.update()
    if is_running:
            screen.fill((48, 50, 52))
            pygame.draw.rect(screen, (48,50,52), back_button)
            display_text("Back", back_button.x + back_button.width // 2, back_button.y + back_button.height // 2, 14, (200,200,200), centered=True)
            pygame.draw.rect(screen, (200, 200, 200), Lpaddle)
            pygame.draw.rect(screen, (200, 200, 200), Rpaddle)
            pygame.draw.ellipse(screen, (200, 200, 200), ball)
            pygame.draw.aaline(screen, (200, 200, 200), (screen_width / 2, 0), (screen_width / 2, screen_height))
            Rpaddle_mechanism()
            ai_Lpaddle_mechanism()
            ball_speed_x, ball_speed_y, Lpaddle_score, Rpaddle_score = ball_mechanism(ball_speed_x, ball_speed_y, Lpaddle_score, Rpaddle_score)
            display_text(str(Lpaddle_score), screen_width // 4, 10, 28, (200, 200, 200))
            display_text(str(Rpaddle_score), screen_width // 4 * 3, 10, 28, (200, 200, 200))
            if Lpaddle_score >= 10:
                display_text("You Lose!", screen_width // 2, screen_height // 2, 60, (200, 200, 200), centered=True)
                ball_speed_x = random.choice([-0, 0])
                ball_speed_y = random.choice([-0, 0])
                Lpaddle_speed = 0
            if Rpaddle_score >= 10:
                display_text("You Win!", screen_width // 2, screen_height // 2, 60, (200, 200, 200), centered=True)
                ball_speed_x = random.choice([-0, 0])
                ball_speed_y = random.choice([-0, 0])
                Lpaddle_speed = 0
            if Rpaddle_score == 10 and Lpaddle_score == 0:
                display_text("Congratulations, you found the Easter Egg!", screen_width // 2, screen_height // 2 + 55, 24, (200, 200, 200), centered=True)
                display_text("Hopefully you enjoyed my game... 100% in Computer Science???", screen_width // 2, screen_height // 2 + 100, 24, (200, 200, 200), centered=True)

VARIABLES: DEFINED IN CODE 
'''

import pygame, random, sys
#funtion to display text on the screen, taking required arguments to place the text at the correct place
def display_text(text, x, y, font_size, color, centered=False):
    font = pygame.font.Font('freesansbold.ttf', font_size)
    rendered_text = font.render(text, True, color)
    text_rect = rendered_text.get_rect()
    if centered:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
    screen.blit(rendered_text, text_rect)

#function contained the mechanics and logic of the ball. 
def ball_mechanism(ball_speed_x, ball_speed_y, Lpaddle_score, Rpaddle_score): #uses the same variable names as the actual code so that the values can be updated through the return statement
    ball.x += ball_speed_x #create an illusion of movement by updating the position of the ball by minimal pixels 
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height: #creates borders for the ball so it doesn't go outside the playing screen
        ball_speed_y *= -1
    if ball.left <= 0: #adds a point or the user after the ball passes a certain point
        Rpaddle_score += 1
        ball_speed_x, ball_speed_y = ball_reset(ball_speed_x, ball_speed_y)
    if ball.right >= screen_width: #adds a point for the computer after the ball passes a certain point
        Lpaddle_score += 1
        ball_speed_x, ball_speed_y = ball_reset(ball_speed_x, ball_speed_y)

    if ball.colliderect(Lpaddle) and ball_speed_x < 0: #causes the ball to "bounce" off the paddle. 
        ball_speed_x *= -1
        ball.x = Lpaddle.right + 1  # Move the ball slightly to the right
    if ball.colliderect(Rpaddle) and ball_speed_x > 0: 
        ball_speed_x *= -1
        ball.x = Rpaddle.left - ball.width - 1  # Move the ball slightly to the left

    return ball_speed_x, ball_speed_y, Lpaddle_score, Rpaddle_score #returns the variables with new values 

#function to reset the ball after a player scores
def ball_reset(ball_speed_x, ball_speed_y):
    ball.center = (screen_width / 2, screen_height / 2)
    ball_speed_y *= random.choice((-1, 1)) 
    ball_speed_x *= random.choice((-1, 1))
    return ball_speed_x, ball_speed_y

#function that handles logic of the players paddle, not going past the wall and setting the speed
def Rpaddle_mechanism():
    Rpaddle.y += Rpaddle_speed
    if Rpaddle.top <= 0:
        Rpaddle.top = 0
    if Rpaddle.bottom >= screen_height:
        Rpaddle.bottom = screen_height

#function that handles the logic of the computer paddle, including how moves on its own and tracks the ball
def ai_Lpaddle_mechanism():
    if (Lpaddle.centery + 40 ) < ball.y:
        Lpaddle.top += Lpaddle_speed  
    if (Lpaddle.centery - 40 ) > ball.y:
        Lpaddle.bottom -= Lpaddle_speed 
    if Lpaddle.top <= 0:
        Lpaddle.top = 0
    if Lpaddle.bottom >= screen_height:
        Lpaddle.bottom = screen_height
        
#function to reset the score and position of the paddles and ball
def reset_game(): 
    global Rpaddle_speed, Rpaddle_score, Lpaddle_score, ball_speed_x, ball_speed_y

    Rpaddle_speed = 0
    Rpaddle_score = 0
    Lpaddle_score = 0

    ball.centerx = screen_width // 2
    ball.centery = screen_height // 2

    ball_speed_x = 5 * random.choice((-1, 1))
    ball_speed_y = 5 * random.choice((-1, 1))

    Lpaddle.y = screen_height / 2 - 70
    Rpaddle.y = screen_height / 2 - 70

pygame.init() #initializes pygame to allow it's functions and methods to be used
clock = pygame.time.Clock() #creates variable for setting refresh rate

# Creating the window
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

#Calculate button positions
button_x = screen_width // 2 - 200 // 2
easy_button_y = screen_height // 2 - 80 // 2 - 80 - 20
medium_button_y = screen_height // 2 - 80 // 2
hard_button_y = screen_height // 2 - 80 // 2 + 80 + 20

#Create button rectangles
easy_button = pygame.Rect(button_x, easy_button_y, 200, 80)
medium_button = pygame.Rect(button_x, medium_button_y, 200, 80)
hard_button = pygame.Rect(button_x, hard_button_y, 200, 80)
help_button = pygame.Rect(10, 10, 80, 30)
back_button = pygame.Rect(10, 10, 60, 20)

#Creating the shapes
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 8, 16, 16)
Lpaddle = pygame.Rect(15, screen_height / 2 - 70, 10, 140)
Rpaddle = pygame.Rect(screen_width - 25, screen_height / 2 - 70, 10, 140)

#Positioning the ball to the center of the screen
ball.centerx = screen_width // 2
ball.centery = screen_height // 2

#setting the ball speed
ball_speed_x = 5 * random.choice((-1, 1))
ball_speed_y = 5 * random.choice((-1, 1))

#creates default paddle speeds
Rpaddle_speed = 0
Lpaddle_speed = 0  
#score of both sides
Rpaddle_score = 0
Lpaddle_score = 0

#Basic text setting
font = pygame.font.Font('freesansbold.ttf', 28)

# Game states (page)
is_menu = True
is_running = False
is_help = False

# Difficulty of game (specific speed values)
easy_paddle_speed = 5
medium_paddle_speed = 7
hard_paddle_speed = 10

while True: #main game loop
    #clicking buttons
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if is_menu:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.collidepoint(event.pos):
                    is_menu = False
                    is_running = True
                    ball_speed_x = random.choice([-5, 5])
                    ball_speed_y = random.choice([-5, 5])
                    Lpaddle_speed = easy_paddle_speed - 1
                elif medium_button.collidepoint(event.pos):
                    is_menu = False
                    is_running = True
                    ball_speed_x = random.choice([-7, 7])
                    ball_speed_y = random.choice([-7, 7])
                    Lpaddle_speed = medium_paddle_speed - 1
                elif hard_button.collidepoint(event.pos):
                    is_menu = False
                    is_running = True
                    ball_speed_x = random.choice([-10, 10])
                    ball_speed_y = random.choice([-10, 10])
                    Lpaddle_speed = hard_paddle_speed -1 
                elif help_button.collidepoint(event.pos):
                    is_menu = False 
                    is_help = True
                else:
                    if back_button.collidepoint(event.pos):
                        is_menu = True
        if is_running:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    Rpaddle_speed += Lpaddle_speed
                if event.key == pygame.K_UP:
                    Rpaddle_speed -= Lpaddle_speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    Rpaddle_speed -= Lpaddle_speed
                if event.key == pygame.K_UP:
                    Rpaddle_speed += Lpaddle_speed
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    is_running = False
                    is_menu = True
                    reset_game()
#creating displays/pages 
    if is_menu:
        screen.fill((48, 50, 52))
        display_text("Pong", screen_width // 2, 100, 100, (200, 200, 200), centered=True)
        pygame.draw.rect(screen, (200, 200, 200), easy_button)
        pygame.draw.rect(screen, (200, 200, 200), medium_button)
        pygame.draw.rect(screen, (200, 200, 200), hard_button)
        pygame.draw.rect(screen, (48,50,52), help_button)
        display_text("Easy", easy_button.centerx, easy_button.centery, 40, (48, 50, 52), centered=True)
        display_text("Medium", medium_button.centerx, medium_button.centery, 40, (48, 50, 52), centered=True)
        display_text("Hard", hard_button.centerx, hard_button.centery, 40, (48, 50, 52), centered=True)
        display_text("Help", help_button.x + help_button.width // 2, help_button.y + help_button.height // 2, 20, (200,200,200), centered=True)
        pygame.display.update()

    if is_help:
        screen.fill((48, 50, 52))
        display_text("Welcome to Pong!", screen_width // 2, 50, 40, (200, 200, 200), centered=True)
        display_text("This is a recreation of the classic arcade game Pong.", screen_width // 2, 120, 14, (200, 200, 200), centered=True)
        display_text("In this game, you play on the right side and control the paddle with the up and down arrow keys to move up and down.", screen_width // 2, 140, 14, (200, 200, 200), centered=True)
        display_text("Your opponent is the left paddle which is controlled by the computer.", screen_width // 2, 180, 14, (200, 200, 200), centered=True)
        display_text("The objective is to score 5 points. To do this hit the ball past the opponent (hit the left wall)", screen_width // 2, 200, 14, (200, 200, 200), centered=True)
        display_text("However, the computer will also be trying to score points by hitting the ball past you (making it hit the right wall)", screen_width // 2, 220, 14, (200, 200, 200), centered=True)
        display_text("To start playing, return to the homepage using the back button on the top left and select a difficulty.", screen_width // 2, 260, 14, (200, 200, 200), centered=True)
        display_text("You can exit a game by pressing the back button to return to the homepage.", screen_width // 2, 280, 14, (200, 200, 200), centered=True)
        display_text("Too close the application, return to the homepage and then press the 'x' button on the top right of the window", screen_width // 2, 300, 14, (200, 200, 200), centered=True)
        display_text("Have Fun!", screen_width // 2, 320, 14, (200, 200, 200), centered=True)
        display_text("Is the game too easy for you?", screen_width // 2, 360, 14, (200, 200, 200), centered=True)
        display_text("Well, if you want to challenge yourself, try finding the easter egg...", screen_width // 2, 380, 14, (200, 200, 200), centered=True)
        display_text("(hint: You cannot let the opponent score... at all!)", screen_width // 2, 400, 14, (200, 200, 200), centered=True)
        pygame.draw.rect(screen, (48,50,52), back_button)
        display_text("Back", back_button.x + back_button.width // 2, back_button.y + back_button.height // 2, 14, (200,200,200), centered=True)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    is_help = False
                    is_menu = True

    if is_running:
            screen.fill((48, 50, 52))
            pygame.draw.rect(screen, (48,50,52), back_button)
            display_text("Back", back_button.x + back_button.width // 2, back_button.y + back_button.height // 2, 14, (200,200,200), centered=True)
            pygame.draw.rect(screen, (200, 200, 200), Lpaddle)
            pygame.draw.rect(screen, (200, 200, 200), Rpaddle)
            pygame.draw.ellipse(screen, (200, 200, 200), ball)
            pygame.draw.aaline(screen, (200, 200, 200), (screen_width / 2, 0), (screen_width / 2, screen_height))

            Rpaddle_mechanism()
            ai_Lpaddle_mechanism()
            ball_speed_x, ball_speed_y, Lpaddle_score, Rpaddle_score = ball_mechanism(ball_speed_x, ball_speed_y, Lpaddle_score, Rpaddle_score)

            display_text(str(Lpaddle_score), screen_width // 4, 10, 28, (200, 200, 200))
            display_text(str(Rpaddle_score), screen_width // 4 * 3, 10, 28, (200, 200, 200))

            if Lpaddle_score >= 5:
                display_text("You Lose!", screen_width // 2, screen_height // 2, 60, (200, 200, 200), centered=True)
                ball_speed_x = random.choice([-0, 0])
                ball_speed_y = random.choice([-0, 0])
                Lpaddle_speed = 0
            if Rpaddle_score >= 5:
                display_text("You Win!", screen_width // 2, screen_height // 2, 60, (200, 200, 200), centered=True)
                ball_speed_x = random.choice([-0, 0])
                ball_speed_y = random.choice([-0, 0])
                Lpaddle_speed = 0
            if Rpaddle_score == 5 and Lpaddle_score == 0:
                display_text("Congratulations, you found the Easter Egg!", screen_width // 2, screen_height // 2 + 55, 24, (200, 200, 200), centered=True)
                display_text("Hopefully you enjoyed my game... 100% in Computer Science???", screen_width // 2, screen_height // 2 + 100, 24, (200, 200, 200), centered=True)

    pygame.display.update()
    clock.tick(60) #seting frames per second
