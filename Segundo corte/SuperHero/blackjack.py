import pygame 
import os
import random
from player import Player
from card import Card
class BlackJack:
    def __init__(self, window):
        self.window= window
        self.background_blackjack= pygame.image.load("SuperHero/Images/blackjackimages/blackjack-background.png") 
        self.start_button= pygame.image.load("SuperHero/Images/blackjackimages/button-start.png")
        self.stay_button= pygame.image.load("SuperHero/Images/blackjackimages/button-stay.png")
        self.request_button= pygame.image.load("SuperHero/Images/blackjackimages/crupier.png")
        self.bench= pygame.image.load("SuperHero/Images/blackjackimages/bench.png")
        self.button_color= (238,35,35)
        self.white_color=(255,255,255)
        self.red_color=(255,0,0)
        self.font=pygame.font.SysFont('Times New Roman',20)
        self.font.set_bold(True)
        self.start_game_text= self.font.render('Para iniciar presione el boton start',True,self.white_color)
        self.player1_win= self.font.render('HAS GANADO!', True, self.white_color)
        self.player2_win= self.font.render('HAS GANADO!', True, self.white_color)
        self.player3_win= self.font.render('HAS GANADO!', True, self.white_color)
        self.crupier_win= self.font.render('HAS GANADO!', True, self.white_color)
        self.player1_lose= self.font.render('HAS PERDIDO!', True, self.white_color)
        self.player2_lose= self.font.render('HAS PERDIDO!', True, self.white_color)
        self.player3_lose= self.font.render('HAS PERDIDO!', True, self.white_color)
        self.crupier_lose= self.font.render('HAS PERDIDO!', True, self.white_color)
        self.start_button_rect= pygame.Rect(395,97,109,31)
        self.stay_player1_rect= pygame.Rect(68,461,171,31)
        self.stay_player2_rect= pygame.Rect(634,569,171,31)
        self.stay_player3_rect= pygame.Rect(1017,461,171,31)
        self.request_button_rect= pygame.Rect(575,307,171,31)
        self.stack= []
        self.list = []
        self.player1= Player(74,308,70,279)
        self.player2= Player(472,492,460,458)
        self.player3= Player(1027,308,1012,279)
        self.crupier= Player(769,140,445,161)
        self.players= [self.player1,self.player2,self.player3]
        self.turn_player=1
        self.clicked= True
        self.starter_stack()

    def draw(self):
        
        self.window.blit(self.background_blackjack,(0,87))
        self.window.blit(self.start_button,(395,97))
        self.window.blit(self.stay_button,(68,461))
        self.window.blit(self.stay_button,(634,569))
        self.window.blit(self.stay_button,(1017,461))
        self.window.blit(self.request_button,(508,102))
        self.window.blit(self.start_game_text,(70,102))
        self.render_text('JUGADOR 1',98,504,self.white_color)
        self.render_text('JUGADOR 2',668,603,self.white_color)
        self.render_text('JUGADOR 3',1051,504,self.white_color)    
        for player in self.players:
            player.draw()
        self.crupier.draw()
        self.start_game()
        self.rounds_game()

    def starter_stack(self):
        while len(self.stack)<26:
            num_pinta = random.randint(1, 2)
            num_character = random.randint(1, 13)
            if num_character > 1 and num_character <= 10:
                num_character = str(num_character)
            if num_character == 1:
                num_character = "as"
            if num_character == 11:
                num_character = "j"
            if num_character == 12:
                num_character = "q"
            if num_character == 13:
                num_character = "k"
            #pinta
            if num_pinta == 1:
                num_pinta = "corazon"
            if num_pinta == 2:
                num_pinta = "rombo"
            card=[num_character,num_pinta]
            if card not in self.list:
                self.list.append(card)
                self.stack.append(Card(self.window, num_character, num_pinta, 0, 0))

    def start_game(self):
        if pygame.mouse.get_pressed()[0] and not self.clicked:
            if self.start_button_rect.collidepoint(pygame.mouse.get_pos()):
                print("Click en botón")
                for player in self.players:
                    player.add_cards(self.stack.pop())
                    player.add_cards(self.stack.pop())
                card= self.stack.pop()
                card.reversed=True
                self.crupier.add_cards(card)
                self.crupier.add_cards(self.stack.pop())
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False

    def rounds_game(self):
        # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        if self.turn_player==1:
            self.render_text('JUGADOR 1',98,504,self.red_color)
            if self.player1.want_cards(self.request_button_rect):
                self.player1.add_cards(self.stack.pop())
                if self.player1.control:
                    self.turn_player+=1
                print('jugador 1: ', self.player1.control)
            elif self.player1.want_stay(self.stay_player1_rect):
                self.render_text('JUGADOR 1',98,504,self.white_color)
                self.turn_player+=1
        #Lógica jugador 2
        elif self.turn_player==2:
            self.render_text('JUGADOR 2',668,603,self.red_color)
            if self.player2.want_cards(self.request_button_rect):
                self.player2.add_cards(self.stack.pop())
                if self.player2.control:
                    self.turn_player+=1
                print('jugador 2: ' ,self.player2.control)
            elif self.player2.want_stay(self.stay_player2_rect):
                self.render_text('JUGADOR 2',668,603,self.white_color)
                self.turn_player+=1
        #Lógica jugador 3
        elif self.turn_player==3:
            self.render_text('JUGADOR 3',1051,504,self.red_color)    
            if self.player3.want_cards(self.request_button_rect):
                self.player3.add_cards(self.stack.pop())
                if self.player3.control:
                    self.turn_player+=1
                print('jugador 3: ' ,self.player1.control)
            elif self.player3.want_stay(self.stay_player3_rect):
                self.render_text('JUGADOR 3',1051,504,self.white_color)
                self.turn_player+=1
        # Lógica crupier
        elif self.turn_player==4:
            reversed_card= self.crupier.hand[0]
            reversed_card.reversed= False
            if self.crupier.crupier_want_cards():
                self.crupier.add_cards(self.stack.pop())
            else:
                self.turn_player=0
        elif self.turn_player==0:
            self.win_game()
            
    def win_game(self):
        for player in self.players:
            if not player.control and self.crupier.score<player.score or self.crupier.score>21 and not player.control:
                self.render_text('HAS GANADO!',player.x_text,player.y_text,self.white_color)
            if player.control or (player.score < self.crupier.score and not self.crupier.control):
                self.render_text('HAS PERDIDO!', player.x_text,player.y_text,self.white_color)
            if player.score == self.crupier.score and not player.control:
                self.render_text('EMPATE!', player.x_text, player.y_text,self.white_color)   
            #jugador gana -> si tiene menos de 22, si el crupier tiene menos que el jugador o si tiene mas de 22
            #pierde jugador -> menos que el crupier y si saca mas de 21
            #empate -> igual que crupier y que no tengan mas de 21

    def render_text(self, txt, x,y,color):
        text= self.font.render(txt, True,color)
        self.window.blit(text,(x,y))


