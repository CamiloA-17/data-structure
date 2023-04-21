class ToupleList:
    def __init__(self):
        self.countries_list=[]
        self.country_name=""
        self.pupulation=0
        self.continent= ""
        
    def total_countries(self):
        print("Ingresa la siguiente informacion")
        print("================================")
        while True:
            try:
                number_countries= int(input("Cantidad a añadir: "))
                for country in range(number_countries):
                    self.country_name= input("Pais >> ")
                    self.pupulation= int(input("Poblacion >>"))
                    self.continent= input("Continente >>")
                    print("=============================")
                    #Añadimos una tupla a la lista append(valores de la tupla)
                    self.countries_list.append((self.country_name, self.pupulation, self.continent))
                print(self.countries_list)
                break
            except ValueError:
                print(" >> Error en el tipo de dato suministrado << ")