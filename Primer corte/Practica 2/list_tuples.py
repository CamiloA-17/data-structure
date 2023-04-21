'''
    List methods 
    Date: 27/01/23
'''
class ListMethods:
    
    #1. Metodo inicializador de la clase
    def __init__(self):
        #Definicion de una lista vacia 
        self.pets=[]
        self.vehicles= list()
    
    #2. Metodo para añadir elementos en la lista
    def add_list_elements(self):
        # ["Dog", "Cat"]
        self.pets.append("dog")
        self.pets.append("cat")
        print(self.pets)
    
    #3. Metodo que solicita valores al usuario
    def input_data_vehicules_list(self):
        #variables locales: vehicles_number, vehicles_type
        vehicles_number= int(input("¿Cuántos vehiculos tienes?: "))
        #recorrer una lista
        for vehicle_item in range (vehicles_number):
            vehicle_type= input("Tipo de vehiculo: ")
            #Añadimos el vehiculo a la lista
            self.vehicles.append(vehicle_type)
        #Imprimir toda la lista
        print(self.vehicles)
        #Imprimir ultimo elemento de la lista
        print(self.vehicles[-1], self.vehicles[-2], self.vehicles[-3])
        
    #4. Extraer valores de una lista
    def show_collection_data_list(self):
        #Imprimir desde posicion 2 hasta 4-1
        print(self.vehicles[2:4])
        #Todos los elementos de la lista
        print(self.vehicles[:])
        #Elementos desde un indice especifico: 2 [2, 3,...]
        print(self.vehicles[2:])
        #Elemetnos hasta un indice especifico: 2[0,1,2]
        print(self.vehicles[:2])
        #Acceder a los elementos de 2 en 2 
        print(self.vehicles[::2])
        #Acceder a un SUBCONJUNTO de elementos de 2 en 2 
        print(self.vehicles[1:5:2])
        
    #5. Iterar los elementos de una lista con un for
    def iteration_list(self):
        for item in self.vehicles:
            print(item)
            #Validar si la lista contiene un valor especifico
        if "Carro".lower() in self.vehicles:
            print("Si se encontro el valor")
        else:
            print("No se encontro el valor")
    
    #6. Añadir varios elementos al final de la lista
    def add_elements(self):
        self.vehicles.extend(["Avion", "Tractomula", "Otro medio"])
        print(self.vehicles)
    #7. Añadir un elemento en posicion eespecifica de la lsita
    def add_specific_element(self):
        self.vehicles.insert(0, "Moto")
        print(self.vehicles)
        
    #8. Eliminar ulitmo elemento de la lista
    def remove_last_element(self):
        self.vehicles.pop()
    
    #9. Eliminar elemento de posicion especifica
    def remove_specific_element(self):
        self.vehicles.pop(0)
        print(self.vehicles) 
    
    #10. Eliminar todos los elementos de la lista
    def remove_all_elements(self):
        self.vehicles.clear()
    
    #11. Eliminar de la lista un valor especifico
    def remove_specific_element(self):
        self.vehicles.remove("tractomula".capitalize())
    
    #12. Eliminar todas las coincidencias de valor en la lista
    def remove_all_match_elements(self):
        new_list= list(filter("tractomula".capitalize).__ne__.self.vehicles)
        print(new_list)