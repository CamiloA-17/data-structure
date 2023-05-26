#pip install --upgrade pygame
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
class Graphs:

    def __init__(self):
        # Configuración de la ventana
        pygame.init()
        pygame.display.set_caption("Red de Usuarios de Facebook")
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 600
        self.BACKGROUND_COLOR = (255, 255, 255)
        self.users=[]
        self.fake = Faker()
        self.relationships= {}
        self.node_positions= {}
        self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.data, self.graph = self.generate_fake_data(5)
        self.write_json_file(self.data, "facebook_data.json")
        self.read_facebook_data("facebook_data.json")
        self.draw_network()

    def run(self):
        while True:
            # Manejar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            # Actualizar la ventana
            self.window.fill(self.BACKGROUND_COLOR)
            self.draw_relationships()
            pygame.display.flip()
            self.clock.tick(60)

    def draw_network(self):
        # Calcular las coordenadas de los nodos
        node_radius = 20
        x_spacing = self.WINDOW_WIDTH // (len(self.users) + 1)
        y_spacing = self.WINDOW_HEIGHT // (len(self.users) + 1)
        y_positions = [random.randint(y_spacing, self.WINDOW_HEIGHT - y_spacing) for _ in range(len(self.users))]
        for i, user in enumerate(self.users):
            x = (i + 1) * x_spacing
            y = y_positions[i]
            self.node_positions[user["id"]] = (x, y)

    def draw_relationships(self):
    # Dibujar las relaciones de amistad
        for user_id, friends in self.relationships.items():
            start_pos = self.node_positions.get(int(user_id))  # Verificar si la clave existe en node_positions
            if start_pos is not None:
                for friend_id in friends:
                    end_pos = self.node_positions.get(friend_id)  # Verificar si la clave existe en node_positions
                    if end_pos is not None:
                        pygame.draw.line(self.window, (100, 100, 100), start_pos, end_pos, 1)

        # Dibujar los nodos
        node_radius= 20
        for user in self.users:
            pos = self.node_positions.get(user["id"])  # Verificar si la clave existe en node_positions
            if pos is not None:
                x, y = pos
                profile_image = user.get("profile_image")
                print(profile_image)
                if profile_image is not None:
                    image_width, image_height = profile_image.get_size()
                    image_x = x - image_width // 2
                    image_y = y - image_height // 2
                    self.window.blit(profile_image, (image_x, image_y))
                # pygame.draw.circle(self.window, (0, 0, 0), pos, node_radius)

    def generate_profile_image_url(self, name):
        # Generar una URL de imagen de perfil falsa con un avatar generado
        style = random.choice(["female", "male"])
        encoded_name = urllib.parse.quote(name)
        url = f"https://avatars.dicebear.com/api/{style}/{encoded_name}.png"
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Error al generar la imagen de perfil: {response.status_code}")
        content_type = response.headers.get("content-type")
        if "image" not in content_type: # type: ignore
            raise Exception("La respuesta no es una imagen válida.")
        return url

    def generate_fake_data(self,num_users):
        for i in range(num_users):
            try:
                name = self.fake.name()
                profile_image_url = self.generate_profile_image_url(name)
                print(profile_image_url)
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
                num_family_members = 3
                num_family_members = min(num_family_members, len(self.users))
                family_members = random.sample(self.users, num_family_members)
                for family_member in family_members:
                    if family_member["name"] != user["name"]:
                        member = {
                            "name": family_member["name"],
                            "relation": random.choice(["Father", "Mother", "Sibling"])
                        }
                    else:
                        member = None
                    if member is not None:
                        user["family"].append(member)
            except Exception as e:
                print(f"Error al generar el usuario {i + 1}: {e}")

        graph = nx.DiGraph()

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

    def write_json_file(self,data, filename):
        with open(filename, "w") as file:
            json.dump(data, file, indent=2)

        print(f"El archivo {filename} ha sido creado exitosamente.")

    def read_facebook_data(self,filename):
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
                print("------------------------")

            # Leer relaciones de amistad
            print("Relaciones de amistad:")
            for user_id, friends in data["relationships"].items():
                print("ID de usuario:", user_id)
                print("Amigos:", friends)
                print("------------------------")

    def load_profile_images(self):
        for user in self.users:
            try:
                response = requests.get(user["profile_image_url"])
                if response.status_code == 200:
                    image_data = response.content
                    image = Image.open(BytesIO(image_data))
                    image = image.resize((80, 80))  # Ajusta el tamaño de la imagen si es necesario
                    image = pygame.image.fromstring(image.tobytes(), image.size, image.mode) # type: ignore
                    user["profile_image"] = image
            except Exception as e:
                print(f"Error al cargar la imagen de perfil para el usuario {user['id']}: {e}")

    # Restablecer la posición vertical de los nodos
    # for user in users:
    #     pos = node_positions.get(user["id"])
    #     if pos is not None:
    #         x, y = pos
    #         # Obtener la posición original del nodo
    #         y = y_positions[user["id"] - 1]  
    #         node_positions[user["id"]] = (x, y)

    def load_json(self):
        # Leer y cargar los datos del archivo JSON
        with open("facebook_data.json", "r") as file:
            data = json.load(file)
            self.users = data["users"]
            self.relationships = data["relationships"]
            self.load_profile_images()

if __name__ == "__main__":
    graph = Graphs()
    graph.run()
