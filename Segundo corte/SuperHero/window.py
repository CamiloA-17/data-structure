import pygame, sys
from pygame.locals import *
from single_linked_list import SingleLinkedList
from combo_box import ComboBox
inst=SingleLinkedList()
class main:
    def __init__(self):
        pygame.init()
        self.window_size=(1280,720)
        self.window= pygame.display.set_mode(self.window_size)
        self.gray_color=(211,211,211)
        self.white_color=(255,255,255)
        self.black_color=(0,0,0)
        self.font=pygame.font.SysFont('Times New Roman',16)
        self.spotify_image = pygame.image.load("SuperHero/Images/SpotifyNode.png")
        self.whatsapp_image = pygame.image.load("SuperHero/Images/WhatsappNode.png")
        self.twitter_image = pygame.image.load("SuperHero/Images/twitterNode.png")
        self.appstore_image = pygame.image.load("SuperHero/Images/appstoreNode.png")
        self.youtube_image = pygame.image.load("SuperHero/Images/youtubeNode.png")
        self.discord_image = pygame.image.load("SuperHero/Images/discordNode.png")
        self.uam_image = pygame.image.load("SuperHero/Images/uam.png")
        self.github_image = pygame.image.load("SuperHero/Images/github.png")
        self.options_image = pygame.image.load("SuperHero/Images/menu.png")
        self.arbol_image = pygame.image.load("SuperHero/Images/arbol.png")
        self.nodo_image= pygame.image.load("SuperHero/Images/nodo.png")
        self.combo_functions_rect= pygame.Rect(351,185,242,37)
        self.combo= ComboBox(self.window,['Añadir al inicio','Añadir al final','Eliminar de la lista'],self.combo_functions_rect,self.black_color,'Times New Roman',16,20,self.white_color,self.white_color,40,'MÉTODOS')
        self.combo_selected= False
        self.combo_pos_rect= pygame.Rect(862,185,50,37)
        self.combo_pos= ComboBox(self.window,['1','2','3','4','5','6'],self.combo_pos_rect,self.black_color,'Times New Roman',16,20,self.white_color,self.white_color,40,'A')
        self.combo_pos_selected= False
        self.initial_window = True
        self.click_button= False
        self.bools()
        
    def bools(self):
        self.spotify_bool= False
        self.whatsapp_bool= False
        self.twitter_bool= False
        self.discord_bool= False
        self.youtube_bool= False
        self.appstore_bool= False
        
    def selectedApp(self):
        if self.spotify_rect.collidepoint(pygame.mouse.get_pos()):
            self.spotify_bool=True
            return 'Spotify'
        elif self.whatsapp_rect.collidepoint(pygame.mouse.get_pos()):
            self.whatsapp_bool= True
            return 'Whatsapp'
        elif self.twitter_rect.collidepoint(pygame.mouse.get_pos()):
            self.twitter_bool= True
            return 'Twitter'
        elif self.discord_rect.collidepoint(pygame.mouse.get_pos()):
            self.discord_bool= True
            return 'Discord'
        elif self.youtube_rect.collidepoint(pygame.mouse.get_pos()):
            self.youtube_bool= True
            return 'YouTube'
        elif self.appstore_rect.collidepoint(pygame.mouse.get_pos()):
            self.appstore_bool= True
            return 'App Store'

    def run_app(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit() 
                if self.initial_window:
                    self.initial()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.mouse_pos= pygame.mouse.get_pos()
                        self.click_on_head()
                else:
                    self.draw_sll_window()
                    self.combo.draw()
                    self.combo_pos.draw()  
            pygame.display.flip()    
            
    def rectGroup(self):
        self.discord_rect = pygame.Rect(683,265,114,135)
        self.spotify_rect = pygame.Rect(269,265,114,135)
        self.whatsapp_rect = pygame.Rect(407,265,114,135)
        self.twitter_rect = pygame.Rect(545,265,114,135)                 
        self.youtube_rect = pygame.Rect(821,265,114,135)
        self.appstore_rect = pygame.Rect(959,265,114,135) 
    
    def text(self):
        pygame.display.set_caption('App management')
        self.font.set_bold(True)
        sll_text= self.font.render('Single Linked List', True, self.black_color)
        self.font.set_bold(False)
        status_text= self.font.render('Estado de la lista: ', True,self.black_color)
        copyright_text= self.font.render('Desarrollado por : Camilo Andres Molano Aristizabal',True,self.black_color)
        copyright_2_text= self.font.render('@ I SEM -2023',True,self.black_color)
        sll_option= self.font.render('SLL',True,self.black_color)
        dll_option= self.font.render('DLL',True,self.black_color)
        pyc_option= self.font.render('PILAS Y COLAS',True,self.black_color)
        arbol_option= self.font.render('ÁRBOL',True,self.black_color)
        grafo_option= self.font.render('GRAFO',True,self.black_color)
        self.window.blit(sll_option,(89,30))
        self.window.blit(dll_option,(312,30))
        self.window.blit(pyc_option,(540,30))
        self.window.blit(arbol_option,(874,30))
        self.window.blit(grafo_option,(1134,30))
        self.window.blit(sll_text,(154,133))
        self.window.blit(status_text,(154,423))
        self.window.blit(copyright_text,(485,661))
        self.window.blit(copyright_2_text,(569,683))
        self.window.blit(self.options_image,(40,27))
        self.window.blit(self.options_image,(254,27))
        self.window.blit(self.options_image,(485,27))
        self.window.blit(self.arbol_image,(822,27))
        self.window.blit(self.options_image,(1082,27))
        
     
    def draw_sll_window(self):
        self.window.fill(self.gray_color)
        self.top_rect=pygame.draw.rect(self.window,self.white_color,(0,0,1280,87),0,0)
        self.bottom_rect= pygame.draw.rect(self.window, self.white_color,(0,649,1280,71),0,0)
        self.list_rect= pygame.draw.rect(self.window,self.white_color,(154,460,1020,159),0,20)
        self.button_rect= pygame.draw.rect(self.window,self.black_color,(959,185,129,38),0,20)
        self.text()
        agree_text= self.font.render('Aceptar', True,self.white_color)
        methods_text= self.font.render('Seleccione un método: ',True,self.black_color)
        pos_text= self.font.render('Seleccione una posición: ',True,self.black_color)
        pygame.draw.rect(self.window,self.black_color,self.combo_functions_rect,0,20)
        pygame.draw.rect(self.window,self.black_color,self.combo_pos_rect,0,20)
        self.window.blit(methods_text,(154,192))
        self.window.blit(pos_text,(666,192))
        self.window.blit(agree_text,(990,192))
        self.window.blit(self.spotify_image, (269,265))
        self.window.blit(self.whatsapp_image,(407,265))
        self.window.blit(self.twitter_image,(545,265))
        self.window.blit(self.discord_image,(683,265))
        self.window.blit(self.youtube_image,(821,265))
        self.window.blit(self.appstore_image,(959,265))
        self.window.blit(self.uam_image,(1188,658))
        self.window.blit(self.github_image,(850,665)) 
        self.methodsSelection()
        self.rectGroup()
        self.visual_list()           
    
    def initial(self):
            self.window.fill(self.gray_color)
            self.top_rect=pygame.draw.rect(self.window,self.white_color,(0,0,1280,87),0,0)
            self.bottom_rect= pygame.draw.rect(self.window, self.white_color,(0,649,1280,71),0,0)
            self.list_rect= pygame.draw.rect(self.window,self.white_color,(154,460,1020,159),0,20)
            self.spotify_rect_initial = pygame.Rect(418,271,114,135)
            self.whatsapp_rect_initial = pygame.Rect(608,271,114,135)
            self.twitter_rect_initial = pygame.Rect(798,271,114,135)  
            self.text()
            init_text= self.font.render('PARA INICIAR DEBES SELECCINAR UNA IMAGEN QUE SERA LA CABEZA DE LA LISTA',True, self.black_color)
            self.window.blit(init_text,(341,220))
            self.window.blit(self.spotify_image, (418,271))
            self.window.blit(self.whatsapp_image,(608,271))
            self.window.blit(self.twitter_image,(798,271))
            self.window.blit(self.uam_image,(1188,658))
            self.window.blit(self.github_image,(850,665))
            
            
    def click_on_head(self):
        mouse_pos= pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if self.whatsapp_rect_initial.collidepoint(mouse_pos):
                inst.create_node_sll_unshift('Whatsapp')
                inst.show_list()
                self.initial_window = False
            elif self.spotify_rect_initial.collidepoint(mouse_pos):
                inst.create_node_sll_unshift('Spotify')
                inst.show_list()
                self.initial_window = False
            elif self.twitter_rect_initial.collidepoint(mouse_pos):
                inst.create_node_sll_unshift('Twitter')
                inst.show_list()
                self.initial_window = False
                
    def visual_list(self):
        for i in range(1,inst.length+1):
            if inst.get_node_value(1)== 'Whatsapp':
                self.window.blit(self.whatsapp_image, (164,472))
            elif inst.get_node_value(1) == 'Spotify':
                self.window.blit(self.spotify_image,(164,472))
            elif inst.get_node_value(1) == 'Twitter':
                self.window.blit(self.twitter_image,(164,472))
            
                
    def clickOnButton(self):
        self.methodsSelection()
        if self.button_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == True and not self.click_button:
                inst.create_node_sll_unshift(self.dict[self.object])
                self.click_button = True
                return self.click_button
        if not pygame.mouse.get_pressed()[0]:
            self.click_button = False
            return self.click_button
     
    def methodsSelection(self):
        if self.spotify_bool or self.whatsapp_bool or self.twitter_bool or self.discord_bool or self.youtube_bool or self.appstore_bool:
            if self.combo.getIndex() == '1':
                inst.create_node_sll_unshift(self.selectedApp())
                
                             
                    
                    
                    
        
    
        
                    
        
        
        
    