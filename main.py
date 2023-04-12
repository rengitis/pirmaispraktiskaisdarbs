import pygame
import sys
import random
from MaxMinAlgo import MinMaxA

# Inicialize pygame
pygame.init()

# Izveido ekranu
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mandarini")
icon = pygame.image.load('mandarins.png')
pygame.display.set_icon(icon)

# Fonti
score_font = pygame.font.Font('font.ttf', 60)
main_font = pygame.font.Font('font.ttf', 32)
text_font = pygame.font.Font('font.ttf', 24)
rule_font = pygame.font.Font('font.ttf', 20)

# Background
background_img = pygame.image.load('background.jpg').convert()
MainMenuBG = pygame.image.load('MainMenuBG.jpg').convert()

# Poga
button_surface = pygame.image.load("rectangle.png")
class Button():
    def __init__(self, image, x, y, txt):
        self.image = image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.txt = txt
        self.text = main_font.render(self.txt, True, "white")
        self.text_rect = self.text.get_rect(center=(self.x, self.y))

    def update(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)
    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = main_font.render(self.txt, True, "green")
        else:
            self.text = main_font.render(self.txt, True, "white")

AiTurn = None
Rez = random.randint(10, 20)
WinRez = None
AiChoice = None

def AiGame():
    global Rez, AiTurn, AiChoice, WinRez

    AiChoice = MinMaxA(Rez, AiTurn)
    Rez -= AiChoice
    if Rez <= 0:
        WinRez = False
        AiChoice = None
        EndMenu()
def Play():
    global Rez, AiChoice, button_surface
    while True:

        screen.blit(background_img, (0, 0))

        button_surface = pygame.transform.scale(button_surface, (150, 170))

        buttonOne = Button(button_surface, 200, 500, "-1")
        buttonTwo = Button(button_surface, 400, 500, "-2")
        buttonThree = Button(button_surface, 600, 500, "-3")

        Score = score_font.render(str(Rez), True, 'black')
        ScoreRect = Score.get_rect(center=(400, 200))

        AiTurnInfo = main_font.render("AI CHOSE " + str(AiChoice), True, 'black')
        AiTurnInfoRect = AiTurnInfo.get_rect(center=(400, 325))

        ChosenNumber = [1, 2, 3]

        def Game(UserIndex):
            global Rez, AiChoice, WinRez

            PickedNumber = ChosenNumber[UserIndex]
            Rez -= PickedNumber
            if Rez <= 0:
                WinRez = True
                AiChoice = None
                EndMenu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttonOne.checkForInput(pygame.mouse.get_pos()):
                    Game(0)
                    AiGame()
                elif buttonTwo.checkForInput(pygame.mouse.get_pos()):
                    Game(1)
                    AiGame()
                elif buttonThree.checkForInput(pygame.mouse.get_pos()):
                    Game(2)
                    AiGame()

        screen.blit(Score, ScoreRect)

        for button in [buttonOne, buttonTwo, buttonThree]:
            button.changeColor(pygame.mouse.get_pos())
            button.update()

        if AiChoice != None:
            screen.blit(AiTurnInfo, AiTurnInfoRect)
        pygame.display.update()
def EndMenu():
    global WinRez, button_surface
    while True:

        WinText = main_font.render("TU ESI UZVAREJIS! :)", True, 'black')
        WinRect = WinText.get_rect(center=(400,200))

        LoseText = main_font.render("DIEMZEL TU ZAUDEJI :(", True, 'black')
        LoseRect = LoseText.get_rect(center=(400, 200))

        button_surface = pygame.transform.scale(button_surface, (350, 250))

        buttonRestart = Button(button_surface, 200, 500, "RESTART")
        buttonExit = Button(button_surface, 600, 500, "QUIT")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttonRestart.checkForInput(pygame.mouse.get_pos()):
                    MainMenu()
                if buttonExit.checkForInput(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()

        screen.blit(MainMenuBG, (0, 0))

        if WinRez is True:
            screen.blit(WinText, WinRect)
        else:
            screen.blit(LoseText, LoseRect)

        for button in [buttonRestart, buttonExit]:
            button.changeColor(pygame.mouse.get_pos())
            button.update()

        pygame.display.update()
def MainMenu():
    global Rez, AiTurn, button_surface
    while True:

        MenuText = text_font.render("SODIEN SPELESIM MANDARINUS", True, 'black')
        MenuRect = MenuText.get_rect(center=(400,200))

        RuleText = rule_font.render("Kurs no jums saks speli?", True, 'black')
        RuleRect = MenuText.get_rect(center=(470, 365))

        button_surface = pygame.transform.scale(button_surface, (200, 200))

        buttonMe = Button(button_surface, 200, 500, "ME")
        buttonAi = Button(button_surface, 600, 500, "AI")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttonMe.checkForInput(pygame.mouse.get_pos()):
                    AiTurn = -1
                    if Rez <= 0:
                        Rez = random.randint(10, 20)
                    Play()

                if buttonAi.checkForInput(pygame.mouse.get_pos()):
                    AiTurn = 1
                    if Rez <= 0:
                        Rez = random.randint(10, 20)
                    AiGame()
                    Play()

        screen.blit(MainMenuBG, (0, 0))

        screen.blit(MenuText, MenuRect)
        screen.blit(RuleText, RuleRect)

        for button in [buttonMe, buttonAi]:
            button.changeColor(pygame.mouse.get_pos())
            button.update()

        pygame.display.update()

MainMenu()