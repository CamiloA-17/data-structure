import pygame, sys
import webbrowser
from pygame.locals import *
from single_linked_list import SingleLinkedList
from combo_box import ComboBox
from menu import Menu
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
        # self.options_image = pygame.image.load("SuperHero/Images/menu.png")
        # self.arbol_image = pygame.image.load("SuperHero/Images/arbol.png")
        # self.nodo_image= pygame.image.load("SuperHero/Images/nodo.png")
        self.combo_functions_rect= pygame.Rect(351,185,242,37)
        self.combo= ComboBox(self.window,['Añadir al inicio','Añadir al final','Eliminar al inicio','Eliminar al final','Invertir la lista', 'Eliminar todos los elementos','Eliminar por posicion','Añadir por posicion','Actualizar valor','Eliminar duplicados','Agrupar duplicados'],self.combo_functions_rect,self.black_color,'Times New Roman',16,20,self.white_color,self.white_color,40,' ')
        self.combo_selected= False
        self.combo_pos_rect= pygame.Rect(862,185,50,37)
        self.combo_pos= ComboBox(self.window,['1'],self.combo_pos_rect,self.black_color,'Times New Roman',16,20,self.white_color,self.white_color,40,' ')
        self.combo_pos_selected= False
        self.initial_window = True
        self.click_button= False
        self.rect_aux= None
        self.node_aux= None
        self.github_rect= pygame.Rect(850,665,38,36)
        self.menu= Menu(self.window,{"SLL": "SuperHero/Images/menu.png", "DLL": "SuperHero/Images/menu.png", "Pilas y Colas": "SuperHero/Images/menu.png", "Arbol": "SuperHero/Images/arbol.png", "Grafos": "SuperHero/Images/nodo.png"},self.gray_color,90, "Times New Roman", 22, self.black_color)
        
        
    def run_app(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if (self.menu.getSelectedOption()==0):
                    if self.initial_window:
                        self.initial()
                    else:
                        self.draw_sll_window()
                        self.visual_list() 
                        self.select_image()
                        self.combo.draw()
                        self.combo_pos.draw()
                elif (self.menu.getSelectedOption()==1):
                    pygame.draw.rect(self.window, self.black_color, (0, 40, self.window.get_width(), self.window.get_height() - 40))
                elif (self.menu.getSelectedOption()==2):
                    pygame.draw.rect(self.window,self.gray_color,(0, 40, self.window.get_width(), self.window.get_height() - 40))
                elif (self.menu.getSelectedOption()==3):
                    pygame.draw.rect(self.window,self.black_color,(0, 40, self.window.get_width(), self.window.get_height() - 40))
                elif (self.menu.getSelectedOption()==4):
                    pygame.draw.rect(self.window,self.gray_color,(0, 40, self.window.get_width(), self.window.get_height() - 40))
                elif (self.menu.getSelectedOption()==5):
                    pygame.draw.rect(self.window,self.black_color,(0, 40, self.window.get_width(), self.window.get_height() - 40))
                self.menu.draw()
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
        self.url= "https://github.com/CamiloA-17/data-structure"
        self.window.blit(sll_text,(154,133))
        self.window.blit(status_text,(154,423))
        self.window.blit(copyright_text,(485,661))
        self.window.blit(copyright_2_text,(569,683))
        # self.window.blit(self.options_image,(40,27))
        # self.window.blit(self.options_image,(254,27))
        # self.window.blit(self.options_image,(485,27))
        # self.window.blit(self.arbol_image,(822,27))
        # self.window.blit(self.options_image,(1082,27))
        
    def open_github(self):
        if pygame.mouse.get_pressed()[0]:
            if self.github_rect.collidepoint(pygame.mouse.get_pos()):
                webbrowser.open(self.url)
                     
    def draw_dll_window(self):
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
        self.open_github()        
    
    def draw_sll_window(self):
        self.combo.draw()
        self.combo_pos.draw()
        self.window.fill(self.gray_color)
        self.top_rect=pygame.draw.rect(self.window,self.white_color,(0,0,1280,87),0,0)
        self.bottom_rect= pygame.draw.rect(self.window, self.white_color,(0,649,1280,71),0,0)
        self.list_rect= pygame.draw.rect(self.window,self.white_color,(154,460,1044,159),0,20)
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
        self.rectGroup()
        self.open_github()
                
    
    def initial(self):
        self.window.fill(self.gray_color)
        self.top_rect=pygame.draw.rect(self.window,self.white_color,(0,0,1280,87),0,0)
        self.bottom_rect= pygame.draw.rect(self.window, self.white_color,(0,649,1280,71),0,0)
        self.list_rect= pygame.draw.rect(self.window,self.white_color,(154,460,1020,159),0,20)
        self.spotify_rect_initial = pygame.Rect(418,271,114,135)
        self.whatsapp_rect_initial = pygame.Rect(608,271,114,135)
        self.twitter_rect_initial = pygame.Rect(798,271,114,135)  
        self.text()
        init_text= self.font.render('PARA INICIAR DEBES SELECCIONAR UNA IMAGEN QUE SERÁ LA CABEZA DE LA LISTA',True, self.black_color)
        self.window.blit(init_text,(341,220))
        self.window.blit(self.spotify_image, (418,271))
        self.window.blit(self.whatsapp_image,(608,271))
        self.window.blit(self.twitter_image,(798,271))
        self.window.blit(self.uam_image,(1188,658))
        self.window.blit(self.github_image,(850,665))
        self.open_github()
        self.click_on_head()          
    
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
        gap=0
        for i in range(1,inst.length+1):
            if inst.get_node(i).value== 'Whatsapp':
                self.window.blit(self.whatsapp_image, (164+gap,472))
            elif inst.get_node(i).value == 'Spotify':
                self.window.blit(self.spotify_image,(164+gap,472))
            elif inst.get_node(i).value == 'Twitter':
                self.window.blit(self.twitter_image,(164+gap,472))
            elif inst.get_node(i).value == 'Discord':
                self.window.blit(self.discord_image,(164+gap,472))
            elif inst.get_node(i).value == 'YouTube':
                self.window.blit(self.youtube_image,(164+gap,472))
            elif inst.get_node(i).value == 'App Store':
                self.window.blit(self.appstore_image,(164+gap,472))    
            gap+=130

    # def clickOnButton(self):
    #     self.methodsSelection()
    #     if self.button_rect.collidepoint(pygame.mouse.get_pos()):
    #         if pygame.mouse.get_pressed()[0] == True and not self.click_button:
    #             inst.create_node_sll_unshift(self.dict[self.object])
    #             self.click_button = True
    #             return self.click_button
    #     if not pygame.mouse.get_pressed()[0]:
    #         self.click_button = False
    #         return self.click_button

    # def methodsSelection(self):
    #     if self.spotify_bool or self.whatsapp_bool or self.twitter_bool or self.discord_bool or self.youtube_bool or self.appstore_bool:
    #         if self.combo.getIndex() == '1':
    #             inst.create_node_sll_unshift(self.selectedApp())
    #             inst.show_list()

    def select_image(self):
        # self.click_item= bool
        if pygame.mouse.get_pressed()[0]:
            if self.whatsapp_rect.collidepoint(pygame.mouse.get_pos()):
                self.node_aux= 'Whatsapp'
                print('Nodo seleccionado')
            elif self.spotify_rect.collidepoint(pygame.mouse.get_pos()):
                self.node_aux= 'Spotify'
                print('Nodo seleccionado')
            elif self.twitter_rect.collidepoint(pygame.mouse.get_pos()):
                self.node_aux= 'Twitter'
                print('Nodo seleccionado')
            elif self.discord_rect.collidepoint(pygame.mouse.get_pos()):
                self.node_aux= 'Discord'
                print('Nodo seleccionado')
            elif self.youtube_rect.collidepoint(pygame.mouse.get_pos()):
                self.node_aux= 'YouTube'
                print('Nodo seleccionado')
            elif self.appstore_rect.collidepoint(pygame.mouse.get_pos()):
                self.node_aux= 'App Store'
                print('Nodo seleccionado')
            if self.button_rect.collidepoint(pygame.mouse.get_pos()):
                print('click en el boton')
                if self.combo.getIndex()== 0:
                    if inst.length<7:
                        if self.node_aux is not None:                        
                            inst.create_node_sll_unshift(self.node_aux)
                            inst.show_list()
                    else:
                        text= self.font.render('>>ERROR: LIMITE ALCANZADO<<',True,self.black_color)
                        self.window.blit(text,(906,628))
                        print(">>ERROR: LIMITE ALCANZADO<<")
                if self.combo.getIndex()== 1:
                    if inst.length<7:
                        if self.node_aux is not None:
                            inst.create_node_sll_ends(self.node_aux)
                            inst.show_list()
                    else:
                        text= self.font.render('>>ERROR: LIMITE ALCANZADO<<',True,self.black_color)
                        self.window.blit(text,(906,628))
                        print(">>ERROR: LIMITE ALCANZADO<<")
                if self.combo.getIndex()== 2:
                    inst.shift_node_sll()
                    inst.show_list()
                if self.combo.getIndex()== 3:
                    inst.delete_node_sll_pop()
                    inst.show_list()
                if self.combo.getIndex()== 4:
                    inst.reverse()
                    inst.show_list()
                if self.combo.getIndex()==5:
                    inst.remove_all_nodes()
                    self.node_aux=None
                    inst.show_list()
                if self.combo.getIndex()==6:
                    if self.combo_pos.getIndex() != -1:
                        inst.remove_node(int(self.combo_pos.getValue()))
                        self.node_aux=None
                        inst.show_list()
                if self.combo.getIndex()==7:
                    if self.node_aux is not None:
                        if inst.length<7:
                            if self.combo_pos.getIndex() != -1:
                                inst.insert_node(int(self.combo_pos.getValue()),self.node_aux)
                                self.node_aux=None
                                inst.show_list()
                        else:
                            text= self.font.render('>>ERROR: LIMITE ALCANZADO<<',True,self.black_color)
                            self.window.blit(text,(906,628))
                            print(">>ERROR: LIMITE ALCANZADO<<")
                if self.combo.getIndex()==8:
                    if self.node_aux is not None:
                        if self.combo_pos.getIndex() != -1:
                            inst.update_node_value(int(self.combo_pos.getValue()),self.node_aux)
                            self.node_aux=None
                            inst.show_list()
                if self.combo.getIndex()==9:
                    inst.remove_all_duplicates()
                if self.combo.getIndex()==10:
                    inst.group_all_duplicates()
                data_list = [str(x) for x in range(1, inst.get_length() + 1)]
                self.combo_pos.updateOptions(data_list)
