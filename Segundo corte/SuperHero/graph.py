from io import BytesIO
import json
import random
import requests
import urllib.parse
import pygame
import networkx as nx
import matplotlib.pyplot as plt
from faker import Faker
from PIL import Image
from combo_box import ComboBox
from drawer import Drawer

fake = Faker("es_CO")

class Graph:
    def __init__(self, window):
        pygame.init()
        # Configuración de la ventana
        self.window= window
        self.WINDOW_WIDTH = 1280
        self.WINDOW_HEIGHT = 560
        self.WHITE_COLOR = (255, 255, 255)
        self.BLACK_COLOR= (0,0,0)
        self.font= pygame.font.SysFont("Times New Roman", 16)
        self.font2= pygame.font.SysFont("Cascadia Code", 24)
        pygame.display.set_caption("App management")
        self.quantity_users= 6
        self.clock = pygame.time.Clock()
        self.users=[]
        self.names= []
        self.friends=[]
        self.relationships={}
        self.button_rect= pygame.Rect((1016,546,227,38))
        self.combo_users_rect= pygame.Rect((1016,128,227,38))
        self.combo_graph_rect= pygame.Rect((1016,220,227,38))
        self.combo_friend_rect= pygame.Rect((1016,361,227,38))
        self.combo_friend_graph_rect= pygame.Rect((1016, 453,227,38))
        self.combo_users= ComboBox(self.window,[' '],self.combo_users_rect,self.BLACK_COLOR,'Cascadia Code',16,20,self.WHITE_COLOR,self.WHITE_COLOR,40,' ')
        self.combo_graph= ComboBox(self.window,['Red de amigos','Red de familia','Comunidades que sigue'],self.combo_graph_rect,self.BLACK_COLOR,'Cascadia Code', 16,20,self.WHITE_COLOR,self.WHITE_COLOR,40,' ')
        self.combo_friend= ComboBox(self.window,[' '],self.combo_friend_rect,self.BLACK_COLOR,'Times New Roman',16,20,self.WHITE_COLOR,self.WHITE_COLOR,40,' ')
        self.combo_friend_graph= ComboBox(self.window,['Comunidades que ambos siguen'],self.combo_friend_graph_rect,self.BLACK_COLOR,'Cascadia Code',16,20,self.WHITE_COLOR,self.WHITE_COLOR,40,' ')
        # Generar datos falsos y escribir el archivo JSON
        self.data, self.graph = self.generate_fake_data(self.quantity_users)
        self.write_json_file(self.data, "facebook_data.json")

        # Leer y mostrar los datos del archivo JSON
        self.read_facebook_data("facebook_data.json")

        # Ejecutar la función principal
        self.read_data()

        # print(self.users)
        self.drawer=Drawer(self.window,0,400,700,600,self.users,self.relationships)
        

    def generate_profile_image_url(self, name):
        # Generar una URL de imagen de perfil falsa con un avatar generado
        style = random.choice(["female", "male"])
        communities= random.choice(['REDDIT', 'COURSERA','STEAM-LATAM'])
        female_random= random.randint(1,18)
        male_random= random.randint(1,21)
        image= ""
        if style == "female":
            image= "SuperHero/Images/"+str(style)+"/"+str(female_random)+".png"
        elif style == "male":
            image= "SuperHero/Images/"+str(style)+"/"+str(male_random)+".png"
        return image

    def load_profile_images(self):
        for user in self.users:
            try:
                image= user["profile_image_url"]
                image= pygame.image.load(image)
                user["profile_image"]= image
                for family in user["family"]:
                    image= family["profile_image_url"]
                    image= pygame.image.load(image)
                    family["profile_image"]=image
                for community in user["communities"]:
                    image=community["profile_image_url"]
                    image= pygame.image.load(f"SuperHero/Images/communities/{image}")
                    community["profile_image"]= image
            except Exception as e:
                print(f"Error al cargar la imagen de perfil para el usuario {user['id']}: {e}")

    def generate_fake_data(self, num_users):
        for i in range(num_users):
            try:
                name = fake.name()
                profile_image_url = self.generate_profile_image_url(name)
                user = {
                    "id": i + 1,
                    "name": name,
                    "email": f"{name}@example.com",
                    "birthdate": "1990-01-01",
                    "profile_image_url": profile_image_url,
                    "liked_photos": [],
                    "family": [],
                    "groups": [],
                    "communities": []
                }
                self.users.append(user)
                self.names.append(user["name"])
                num_family_members = 3
                num_family_members = min(num_family_members, len(self.users))
                family_members = random.sample(self.users, num_family_members)
                for family_member in family_members:
                    if family_member["name"] != user["name"]:
                        member = {
                            "name": family_member["name"],
                            "id": family_member["id"],
                            "relation": random.choice(["Father", "Mother", "Sibling"]),
                            "profile_image_url":family_member["profile_image_url"]
                        }
                    else:
                        member = None
                    if member is not None and member not in user["family"]:
                        user["family"].append(member)
                num_communities = 3
                num_communities = min(num_communities, len(self.users))
                community_members = random.sample(self.users, num_communities)
                for community_member in community_members:
                    if community_member["name"]!=user["communities"]:
                        community = {
                            "id":str(random.randint(10,50)),
                            "name": random.choice(['REDDIT', 'COURSERA','STEAM-LATAM']),
                            "profile_image_url" :str("name")+".png"
                        }
                        community_name= community["name"]
                        community["profile_image_url"]= community_name+".png"
                    else:
                        community=None
                    if community is not None and community not in user["communities"]:
                        user["communities"].append(community)
                        
            except Exception as e:
                print(f"Error al generar el usuario {i + 1}: {e}")
            
            self.combo_users.updateOptions(self.names)

        graph = nx.Graph()
        for user in self.users:
            graph.add_node(user["id"], data=user)
        for user in self.users:
            num_friends = random.randint(1, 5)
            friends = random.sample(self.users, num_friends)
            relationship_ids = [friend["id"] for friend in friends]
            self.relationships[user["id"]] = relationship_ids
            for friend in friends:
                graph.add_edge(user["id"], friend["id"])
        data = {
            "users": self.users,
            "relationships": self.relationships
        }
        
        
        return data, graph


        
    def write_json_file(self, data, filename):
        with open(filename, "w") as file:
            json.dump(data, file, indent=2)

        print(f"El archivo {filename} ha sido creado exitosamente.")

    def read_facebook_data(self, filename):
        with open(filename, "r") as file:
            data = json.load(file)

            # Leer usuarios
            print("Usuarios:")
            for user in data["users"]:
                print("ID:", user["id"])
                print("Nombre:", user["name"])
                print("Email:", user)
                print("Fecha de nacimiento:", user["birthdate"])
                print("URL de imagen de perfil:", user["profile_image_url"])
                print("Miembros de la familia:")
                for family_member in user["family"]:
                    print("Nombre:", family_member["name"])
                    print("Relación:", family_member["relation"])
                print("Comunidades")
                for communities_member in user["communities"]:
                    print("Nombre:",communities_member["name"])
                print("------------------------")

            # Leer relaciones de amistad
            print("Relaciones de amistad:")
            for user_id, friends in data["relationships"].items():
                print("ID de usuario:", user_id)
                print("Amigos:", friends)
                print("------------------------")

        '''
        # Restablecer la posición vertical de los nodos
        
        for user in users:
            pos = self.node_positions.get(user["id"])
            if pos is not None:
                _, y = pos
                # Obtener la posición original del nodo
                y = y_positions[user["id"] - 1]  
                self.node_positions[user["id"]] = (x, y)
        '''

    def draw_friendships(self,user_id):
        relationships={}
        user= self.users[user_id]
        id_friends= self.relationships[str(user_id + 1)]
        friends = [user for user in self.users if user["id"] in id_friends]
        relationships[user["id"]] = id_friends
        self.drawer.set_data([user]+friends,relationships)

    def draw_family(self, name):
        for user in self.users:
            if user["name"] == name:
                relationships={}
                relationships[user["id"]]= [family["id"] for family in user["family"]]
                self.drawer.set_data([user]+user["family"],relationships)

    def draw_community(self,user_id):
        for user in self.users:
            if user["name"]==user_id:
                relationship={}
                relationship[user["id"]]=[community["id"]for community in user ["communities"]]
                self.drawer.set_data(user["communities"]+[user],relationship)

    def get_friends_of_user(self):
        name = self.combo_graph.getValue()
        for user in self.users:
            if user["name"] in name:
                self.list_friends_user=[]
                id_friends= self.relationships[str(user["id"]+1)]
                self.list_friends_user = [friend["name"] for friend in self.users if friend["id"] in id_friends]
                return self.list_friends_user

    def make_validations(self):
        # self.get_friends= []
        # self.get_friends.append(self.get_friends_of_user())
        # self.combo_friend.updateOptions(self.get_friends)
        if self.combo_graph.getIndex()==0:
            if self.button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                self.draw_friendships(self.combo_users.getIndex())
        if self.combo_graph.getIndex()==1:
            if self.button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                print(self.combo_graph.getValue())
                self.draw_family(self.combo_users.getValue())
        if self.combo_graph.getIndex()==2:
            if self.button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                print(self.combo_graph.getIndex())
                self.draw_community(self.combo_users.getValue())




    def read_data(self):
        # Leer y cargar los datos del archivo JSON
        with open("facebook_data.json", "r") as file:
            data = json.load(file)
            self.users = data["users"]
            self.relationships = data["relationships"]
            self.load_profile_images()

    def draw_graph(self):
        pygame.draw.rect(self.window, "White", (0, 87, 1280, 565))
        self.menu_rect= pygame.draw.rect(self.window,self.WHITE_COLOR,(981,87,299,559))
        pygame.draw.rect(self.window,self.BLACK_COLOR,self.combo_users_rect,0,20)
        pygame.draw.rect(self.window,self.BLACK_COLOR,self.combo_graph_rect,0,20)
        pygame.draw.rect(self.window,self.BLACK_COLOR,self.combo_friend_rect,0,20)
        pygame.draw.rect(self.window,self.BLACK_COLOR,self.combo_friend_graph_rect,0,20)
        pygame.draw.rect(self.window,self.BLACK_COLOR,self.button_rect,0,20)
        facebook=pygame.image.load("SuperHero/Images/facebook.png")
        self.combo_users.draw()
        self.combo_graph.draw()
        self.combo_friend.draw()
        self.combo_friend_graph.draw()
        self.select_user_text= self.font.render('Seleccione un usuario',True,self.BLACK_COLOR)
        self.select_graph_text= self.font.render('Seleccione el grafo a visualizar',True,self.BLACK_COLOR)
        self.select_user_friend_text= self.font.render('Seleccione un amigo del usuario',True,self.BLACK_COLOR)
        self.advise_text= self.font2.render('Estos datos son falsos y se leen a través de un archivo JSON',True,self.BLACK_COLOR)
        self.confirm_text= self.font.render('CONFIRMAR',True,self.WHITE_COLOR)
        self.window.blit(self.confirm_text,(1085,556))
        self.window.blit(self.select_graph_text,(1014,183))
        self.window.blit(self.select_graph_text,(1014,416))
        self.window.blit(self.select_user_friend_text,(1014,331))
        self.window.blit(self.select_user_text,(1047,98))
        self.window.blit(self.advise_text,(96,119))
        self.window.blit(facebook,(35,104))
        self.menu_top_line= pygame.draw.line(self.window,self.BLACK_COLOR,(981,87),(1280,87),1)
        self.menu_mid_line= pygame.draw.line(self.window,self.BLACK_COLOR,(981,276),(1280,276),1)
        self.menu_general_line= pygame.draw.line(self.window,self.BLACK_COLOR,(981,87),(981,645),1)
        self.menu_confirmation_line= pygame.draw.line(self.window,self.BLACK_COLOR,(981,523),(1280,523),1)
        self.botton_var_line=pygame.draw.line(self.window,self.BLACK_COLOR,(0,645),(1280,645),1)
        self.make_validations()
        self.drawer.draw()
        self.clock.tick(60)