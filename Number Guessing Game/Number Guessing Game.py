import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants for pygame application window
WIDTH, HEIGHT = 800, 600        #  Width and height of the application window
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 24) # Reduced font size
LINE_SPACING = 30                 # Increased line spacing between the text lines

# Creating the IAT game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(" IAT Guess the Mystery Number")



# Function that allows the user to input their name
def get_user_name():
    name = ""                      # Empty string that will store the user name
    input_active = True            # input is active and the name is being entered 
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:    #If ENTER is pressed then flag will become false
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]                # If BACKSPACE is pressed then the name string's last letter is removed
                else:
                    name += event.unicode
        screen.fill(WHITE)
        prompt_text = FONT.render("Enter your name:", True, BLACK)
        screen.blit(prompt_text, (20, 20))
        input_text = FONT.render(name, True, BLACK)
        screen.blit(input_text, (20, 70))
        pygame.display.flip()                      # updates the display screen
    return name                           

def explain_rules(name):
    rules = [
        "Hi, {}! In this game, I will think of a random number between 1 and 100.".format(name),
        "You will have 10 attempts to guess the number.",
        "I will tell you if your guess is high or low, and you have to guess the mystery number.",
        "Press ENTER to start the game.",
    ]

    input_active = True
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False

        screen.fill(WHITE)
        for i, rule in enumerate(rules):
            rule_text = FONT.render(rule, True, BLACK)
            screen.blit(rule_text, (20, 20 + i * LINE_SPACING))  # Adjusted line spacing

        pygame.display.flip()

def main():                          
    while True:                           # Loop that will repeatedly ask the user to enter their name and will explain the rules of the game 
        name = get_user_name()
        explain_rules(name)

        while True:
            secret_number = random.randint(1, 100)            # A variable which has a random module with int type integer and produce any number between 1 and 100
            attempts = 0                           # attempts are set to zero to represent the number of attempts user has made
            guess = ""                             # An empty string that will store user's input guess
            feedback = ""                          # An empty string that will store the feedback messages for the user

            while attempts < 10:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()
                        elif event.key == pygame.K_RETURN:
                            try:
                                if int(guess) < secret_number:
                                    feedback = "It is a low number!  Please try again."
                                elif int(guess) > secret_number:
                                    feedback = "It is a high number! Please try again."
                                else:
                                    feedback = f"Congratulations, {name}! You've guessed the mystery number {secret_number} in {attempts + 1} attempts."
                                    break
                            except ValueError:
                                feedback = "Invalid input. Please enter a valid number."
                            attempts += 1
                            guess = ""
                        else:
                            guess += event.unicode

                # Clear the screen
                screen.fill(WHITE)

                # Display instructions and user input
                instructions_text = FONT.render("Guess the Mystery Number (1-100):", True, BLACK)
                screen.blit(instructions_text, (20, 20))
                input_text = FONT.render(guess, True, BLACK)
                screen.blit(input_text, (20, 70))

                # Display feedback
                feedback_text = FONT.render(feedback, True, BLACK)
                screen.blit(feedback_text, (20, 120))

                # Update the screen
                pygame.display.flip()

            # Game over message
            if feedback.startswith("Congratulations"):
                game_over_text = FONT.render(f"The mystery number was {secret_number}.", True, BLACK)
                play_again_text = FONT.render(f"Press ENTER to play again or ESC to exit.", True, BLACK)
            else:
                game_over_text = FONT.render(f"Game Over. The mystery number was {secret_number}.", True, BLACK)
                play_again_text = FONT.render(f"Press ENTER to play again or ESC to exit.", True, BLACK)

            screen.blit(game_over_text, (20, 200))
            screen.blit(play_again_text, (20, 230))
            pygame.display.flip()

            # Wait for user input to play again or exit
            play_again = None
            while play_again is None:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()
                        elif event.key == pygame.K_RETURN:
                            play_again = True

        

if __name__ == "__main__":
    main()