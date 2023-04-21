from random import sample
from colorama import Fore, init
init()
class sort_algorithms:
    def __init__(self):
        self.number_list= range(100)
        self.burble_sort_list= sample(self.number_list,8)
        self.select_sort_list= sample(self.number_list,8)
        self.insert_sort_list= sample(self.number_list,8)
        self.merge_sort_list= sample(self.number_list,8)
        self.quick_sort_list= sample(self.number_list,8)
        self.radix_sort_list= sample(self.number_list,8)
        
    #Ordenamiento burbuja
    def burble_sort_function(self):
    #Comparacion por pares, iniciamos comparando los 2 primeros elementos 
        print(Fore.CYAN + "--------------------------------------" + Fore.RESET)
        print(Fore.GREEN + "---ORDENAMIENTO BURBUJA---" + Fore.RESET)
        #contador para conocer cantidad de elementos de la lista 
        count_item_list= 0
        print(self.burble_sort_list)
        #recorremos la lista self.burble_sort_list
        for i in self.burble_sort_list:
            #al contador de elementos cada vez que visitemos una posicion le sumamos 1
            count_item_list +=1
        print(count_item_list)
        print(      ">>Iteracion externa<<"     )
        for j in range(count_item_list-1):
            print(j)
            print(      ">>Iteracion interna<<"     )
            for k in range(count_item_list-j-1):
                print(k)
                if self.burble_sort_list[k]>self.burble_sort_list[k+1]:
                    #Transposicion de valores
                    self.burble_sort_list[k], self.burble_sort_list[k+1]= self.burble_sort_list[k+1], self.burble_sort_list[k]
        
        print(self.burble_sort_list)
        
    def burble_sort_function_refactor(self):
        change_position = True
        while change_position:
            change_position= False
            for i in range(len(self.burble_sort_list)-1):
                if self.burble_sort_list[i]>self.burble_sort_list[i+1]:
                    self.burble_sort_list[i], self.burble_sort_list[i+1] = self.burble_sort_list[i+1], self.burble_sort_list[i]
                    change_position=True
        print(self.burble_sort_list)
        
    def select_sort_function(self):
        print("-----------------------------------------------------------")
        print(Fore.GREEN + ">>Ordenamiento seleccion<<" + Fore.RESET)
        cont_list=0
        #inicializar contador 
        for i in self.select_sort_list:
            cont_list+=1
        #recorremos la lista y generamos la comparacion de valores entre posiciones
        for i in range(cont_list):
            min=i
            for j in range(i + 1, cont_list):
                if self.select_sort_list[min] > self.select_sort_list[j]:
                    min=j
                #generamos el intercambio
            self.select_sort_list[i], self.select_sort_list[min]=self.select_sort_list[min], self.select_sort_list[i] 
        print(self.select_sort_list)
        
    def insert_sort_function(self):
        print("-----------------------------------------------------------")
        print(Fore.GREEN + ">>Ordenamiento insertar<<" + Fore.RESET)
        print(self.insert_sort_list)
        #Separamos la lista en dos partes (puede o no estar)ordenadas
        for i in range(1, len(self.insert_sort_list)):
            item_visited= self.insert_sort_list[i]
            #visitamos la posicion anterior a la actual
            j= i-1
            #todos los elementos de valor mayor pasan adelante
            while j >=0 and self.insert_sort_list[j]>item_visited:
                print(Fore.CYAN + str(self.insert_sort_list[j])+ Fore.RESET + ">" + str(item_visited))
                self.insert_sort_list[j+1]= self.insert_sort_list[j]
                j-=1
                #transposicion
                self.insert_sort_list[j+1]=item_visited
            print(self.insert_sort_list)
            