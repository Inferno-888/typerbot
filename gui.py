from type import type
import pygame
from button_template1 import button1


# Initializing PyGame...
pygame.init()

# Creating the app window:
screen = pygame.display.set_mode((900, 600))

# Loading the background image:
backgroundImg = pygame.image.load('background2.jpg')

# Title & Icon
pygame.display.set_caption('Eve')
icon = pygame.image.load('icon.jpg')
pygame.display.set_icon(icon)

# Application font
font = pygame.font.Font('Robotica.ttf', 24)

# UI texts...
welcome_txt = font.render("Welcome! I am Eve, your new typing master!", True, (255, 255, 255))
cta = font.render("What to do next:", True, (255, 255, 255))

# UI buttons...
btn1 = button1(color=(0, 168, 107), x=600, y=280, width=150, height=50, text='Race!')
btn2 = button1(color=(166, 68, 82), x=150, y=280, width=150, height=50, text='QUIT')


# Main application loop
running = True
while running:
    # Looping through all the events that happen:
    for e in pygame.event.get():
        mousePos = pygame.mouse.get_pos()
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.MOUSEBUTTONDOWN:
            if btn1.isMouseOver(mousePos):
                type()
            if btn2.isMouseOver(mousePos):
                running = False

        if e.type == pygame.MOUSEMOTION:
            if btn1.isMouseOver(mousePos):
                btn1.color = (11, 102, 35)
            else:
                btn1.color = (0, 168, 107)

            if btn2.isMouseOver(mousePos):
                btn2.color = (208, 52, 44)
            else:
                btn2.color = (166, 68, 82)

    # Filling the screen with black
    screen.fill((0, 0, 0))

    # Applying the background image on top of the black color
    screen.blit(backgroundImg, (0, 0))

    # Writing the welcome message
    screen.blit(welcome_txt, (130, 25))

    # Writing call to action #1
    screen.blit(cta, (320, 85))

    # Drawing the cta buttons...
    btn1.draw(screen, (255, 255, 255))
    btn2.draw(screen, (255, 255, 255))

    # Updating the display after all the changes have been made
    pygame.display.update()
