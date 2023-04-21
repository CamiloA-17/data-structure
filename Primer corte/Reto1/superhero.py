'''Author: Camilo Andres
Date: 8/02/2023
'''
from colorama import Fore
class Superhero:
    def __init__(self):
        self.superhero_name=""
        self.superhero_powers=[]
        self.superhero_creators=[]
        self.superheroes_marvel=[]
        self.superheroes_dc=[]
        self.all_superheroes=[]
    
    def menu(self):
        self.superheroes_marvel.append(("Spider-man", ["Volar", "Atacar"], ["Stan Lee", "Steve Ditko"]))
        self.superheroes_marvel.append(("Super-man", ["Volar", "Velocidad"],["Stan Lee"]))
        self.superheroes_marvel.append(("Hulk", ["Transformarse"], ["Stan Lee", "Jack Kirby"]))
        self.superheroes_dc.append(("Batman", ["Conducir rápido", "Esconderse en la noche"], ["Bob Kane", "Bill Finger"]))
        self.superheroes_dc.append(("Mujer maravilla", ["Super fuerza","Volar","Supergrito"], ["William Mouton"]))
        while True:
            try:
                self.all_superheroes= self.superheroes_marvel + self.superheroes_dc
                print(Fore.LIGHTRED_EX + "------Menú principal------ ")
                print("1. Añadir superhéroe")
                print("2. Encontrar superhéroe")
                print("3. Eliminar superhéroe")
                print("4. Superhéroe con mayor cantidad de poderes")
                print("5. Superhéroe con menor cantidad de poderes")
                print("6. Ver la lista de todos los superhéroes")
                print("7. Salir" + Fore.RESET)
                opcion= int(input("Seleccione una opción: "))
                if opcion==1:
                    self.info()
                
                elif opcion==2:
                    self.get_powers()
                
                elif opcion==3:
                    self.delete_superheroe()
                elif opcion==4:
                    self.hero_higher_powers()
                elif opcion==5:
                    self.hero_lower_powers()
                elif opcion==6:
                    self.merge_lists()
                elif opcion==7:
                    break
            except ValueError:
                print("El valor ingresado no es una opción")
                
        
    def info(self):
        select_world= int(input("Ingrese el universo al que desea añadir el superhéroe: \n 1.Marvel \n 2.DC \n Opción: "))
        if select_world ==1:
            all_superheroes= input("Ingrese cuantos superhéroes desea añadir: ")
            for i in all_superheroes:
                self.superhero_name=  input("Nombre: ")
                all_powers= input("¿Cuántos poderes tiene?: ")
                for j in all_powers:
                    #split es para dividir los datos ingresados segun el parametro ','
                    self.superhero_powers= input("Poderes: ").split(',')
                all_creators= input("¿Cuántos creadores tiene?: ")
                if all_creators != 1:
                    for k in all_creators:
                        self.superhero_creators= input("Creadores: ").split(',')    
                else:
                    self.superhero_creators= input("Creador: ")
                    #creacion de la lista de marvel
            self.superheroes_marvel.append((self.superhero_name,self.superhero_powers,self.superhero_creators))
        elif select_world ==2:
            all_superheroes= input("Ingrese cuantos superhéroes desea añadir: ")
            for i in all_superheroes:
                self.superhero_name=  input("Nombre: ")
                all_powers= input("¿Cuántos poderes tiene?: ")
                for j in all_powers:
                    self.superhero_powers= input("Poderes: ").split(',')
                all_creators= input("¿Cuántos creadores tiene?: ")
                if all_creators != 1:
                    for k in all_creators:
                        self.superhero_creators= input("Creadores: ").split(',')    
                else:
                    self.superhero_creators= input("Creador: ")
                    #creacion de la lista de dc
            self.superheroes_dc.append((self.superhero_name,self.superhero_powers,self.superhero_creators))
        else:
            print("<<Opción no disponible>>")    
 
            
    def get_powers(self):
        self.superhero_name= input("Ingrese el nombre del superheroe que desea buscar:").capitalize()
        print(self.superhero_name)
        superhero_status= False
        for hero in self.all_superheroes:
                if self.superhero_name in hero[0]:
                    #Posicion 1 donde estan los poderes
                    print(hero[1])
                    superhero_status= True
        if superhero_status== False:
            print("No se encontro el superhéroe")
            add_superhero= int(input("¿Desea añadir al superhéroe? \n 1.si \ 2.no \n"))
            if add_superhero ==1:
                self.info()
            
            
    def delete_superheroe(self):
        select_world=int(input("Ingrese el mundo del superhéroe que desea eliminar: \n1. Marvel \n2. DC \nOpcion:"))
        self.superhero_name= input("Ingrese el nombre del superhéroe que desea eliminar: ").capitalize()
        superhero_status=False
        if select_world==1:
            for hero in self.superheroes_marvel:
                if self.superhero_name in hero[0]:
                    #remover el superhéro "hero" de la lista mas pequeña
                    self.superheroes_marvel.remove(hero)
                    print("El superhéroe se elimino exitosamente")
                    superhero_status=True
        elif select_world==2:
            for hero in self.superheroes_dc:
                if self.superhero_name in hero[0]:
                    #remover el superhéro "hero" de la lista mas pequeña
                    self.superheroes_dc.remove(hero)
                    print("El superhéroe se elimino exitosamente")
                    superhero_status=True
        elif superhero_status==False:
            print("El superhéroe no se encuentra en el programa")
            
    def hero_higher_powers(self):
        higher=-99999
        self.superhero_name=""
        for hero in self.all_superheroes:
            if len(hero[1]) > higher:
                higher=len(hero[1])
                self.superhero_name=str(hero[0])
        print(self.superhero_name)
    
    def hero_lower_powers(self):
        lower=99999
        self.superhero_name=""
        for hero in self.all_superheroes:
            if len(hero[1]) < lower:
                lower=len(hero[1])
                self.superhero_name=str(hero[0])
        print(self.superhero_name)
        
    def merge_lists(self):
        print(self.all_superheroes)
                
    


            
    
    
        
        
          
                       
    
    
        
        
            