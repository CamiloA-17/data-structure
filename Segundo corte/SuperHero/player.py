import pygame
from card import Card
class Player:
    def __init__(self ,x , y,x_text,y_text):
        self.hand= []
        self.x = x
        self.y = y
        self.score=0
        self.control= False
        self.x_text= x_text
        self.y_text= y_text

    def add_cards(self, card):
            gap = len(self.hand) * 20
            card.x= self.x + gap
            card.y= self.y
            if card.character == "j" or card.character == "q" or card.character == "k":
                self.score+=10
                self.hand.append(card)
            elif card.character == "as":
                if self.score >=11:
                    self.score+=1
                    self.hand.append(card)
                else:
                    self.score+=11
                    self.hand.append(card)
            else:
                self.score+=int(card.character)
                self.hand.append(card)
            if self.score>21:
                self.control=True

    def want_cards(self, rect):
        if pygame.mouse.get_pressed()[0]:
            if rect.collidepoint(pygame.mouse.get_pos()):
                return True
        return False
    
    def crupier_want_cards(self):
        if self.score<=16:
            return True
        return False

    def crupier_reversed_card(self,card):
        card.set_visible(False)

    def want_stay(self, rect):
        if pygame.mouse.get_pressed()[0]:
            if rect.collidepoint(pygame.mouse.get_pos()):
                return True
        return False

    def draw(self):
        for card in self.hand:
            card.draw()