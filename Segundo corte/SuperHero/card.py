import pygame
class  Card:
    def __init__(self, screen, character, spot, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.character = character
        self.spot = spot
        self.value = 0
        self.reversed = False
    
    def getValue(self):
        if self.character == 2:
            self.value = 2
        if self.character == 3:
            self.value = 3
        if self.character == 4:
            self.value = 4
        if self.character == 5:
            self.value = 5
        if self.character == 6:
            self.value = 6
        if self.character == 7:
            self.value = 7
        if self.character == 8:
            self.value = 8
        if self.character == 9:
            self.value = 9
        if self.character == 10 or self.character == 11 or self.character == 12 or self.character == 13:
            self.value = 10
        return self.value
    
    def draw(self):
        if not self.reversed:
            image = pygame.image.load("SuperHero/Images/blackjackimages/cards/" + self.character + "-" + self.spot +".png")
            self.screen.blit(image,(self.x, self.y))
        else:
            image = pygame.image.load("SuperHero/Images/blackjackimages/cards/background.png")
            self.screen.blit(image,(self.x,self.y))
            
    def set_visible(self, boolean):
        if boolean == False:
            self.reversed= True
