from random import sample
from colorama import Fore, Back
from os import system
import time

class SortAlgorithms:
    def __init__(self):
        self.number_list = range(100)
        self.list_bubble_sort = sample(self.number_list, 8)
        self.list_select_sort = sample(self.number_list, 8)
        self.list_insert_sort = sample(self.number_list, 8)
        self.list_merge_sort = sample(self.number_list, 11)
        self.list_quick_sort = sample(self.number_list, 8)
        self.list_radix_sort = sample(self.number_list, 8)
        self.aux_num = 0
        self.aux_list = []
        self.sum_list = []

    # Ordenamiento burbuja
    def bubble_sort_function(self):
        # Comparación por pares, iniciamos comparando los 2 primeros elementos de la lista
        print("--------------------------------------------")
        print("           Ordenamiento burbuja")
        # Crear un contador para conocer la cantidad de elementos de la lista
        count_item_list = 0
        # Recorremos la lista self.list_burble_sort
        for i in self.list_bubble_sort:
            # al contador de elementos, cada vez que visitemos una posición le sumamos 1
            count_item_list += 1
        
        print(self.list_bubble_sort)
        # Recorremos la lista e imprimimos su contenido en cada iteración
        print("Primer for contador - 1: ", count_item_list-1)
        for j in range(count_item_list-1):
            print(f"     {j}")
            for k in range(count_item_list - j - 1):
                print(f"{k}")
                print(self.prueba(k))
                print(self.list_bubble_sort)
                # Compramos el valor de la posición actual con el valor de la siguiente posicion
                if self.list_bubble_sort[k] > self.list_bubble_sort[k+1]:
                    # Transposición de valores
                    self.list_bubble_sort[k], self.list_bubble_sort[k+1] = self.list_bubble_sort[k+1], self.list_bubble_sort[k]
                
        print(self.list_bubble_sort)

    # Comparar por pares. Ordena primero los más grandes
    def bubble_sort_function_refactor(self):
        change_position = True
        print(self.list_bubble_sort)
        while change_position:
            change_position = False
            for i in range(len(self.list_bubble_sort) - 1):
                if self.list_bubble_sort[i] > self.list_bubble_sort[i + 1]:
                    self.list_bubble_sort[i], self.list_bubble_sort[i+1] = self.list_bubble_sort[i+1], self.list_bubble_sort[i]
                    change_position = True
        print(self.list_bubble_sort)

    # Buscar el mínimo. Ordena primero los más pequeños
    def select_sort_function(self):
        print("--------------------------------------------")
        print("           Ordenamiento selección")
        count_item_list = 0
        print(self.list_select_sort)
        # Inicializamos el contador
        for i in self.list_select_sort:
            count_item_list += 1
        
        # Recorremos la lista y generamos la comparación de valores entre posiciones:
        for i in range(count_item_list):    
            min = i
            print(">>> ", i)
            for j in range(min + 1, count_item_list):
                print("> ", j)
                # Comparación de valores
                print("Comparacion: " + str(self.list_select_sort[min]) + " - " + str(self.list_select_sort[j]))
                if self.list_select_sort[min] > self.list_select_sort[j]:
                    min = j
            # Generamos el intercambio, la transposición
            self.list_select_sort[i], self.list_select_sort[min] = self.list_select_sort[min], self.list_select_sort[i]
            print(self.list_select_sort)
        print(self.list_select_sort)


    def insert_sort_function(self):
        print("Vector inicial: " + str(self.list_insert_sort))
        # Separar la lista en dos partes (puede o no estar) ordenadas
        for i in range(1, len(self.list_insert_sort)):
            print(f"--------[{i}]--------")
            print("Revisando: " + str(self.list_insert_sort[:i+1]))
            item_visited = self.list_insert_sort[i]
            # Visitamos la posición anterior a la actual
            j = i - 1
            # Todos los elementos de valor mayor pasan adelante
            while j >= 0 and self.list_insert_sort[j] > item_visited:
                print(str(self.list_insert_sort[j]) + " > " + str(item_visited))
                self.list_insert_sort[j + 1], self.list_insert_sort[j]  = self.list_insert_sort[j], item_visited
                j -= 1
                print(self.list_insert_sort)
                
        print("Vector final: " + str(self.list_insert_sort))

    # Se analiza por subconjuntos. Organiza los primeros
    def insert_sort_function_v2(self):
        print("Vector inicial: " + str(self.list_insert_sort))
        # Separar la lista en dos partes (puede o no estar) ordenadas
        for i in range(1, len(self.list_insert_sort)):
            print(f"--------[{i}]--------")
            print("Revisando: " + str(self.list_insert_sort[:i+1]))
            item_visited = self.list_insert_sort[i]
            # Visitamos la posición anterior a la actual
            j = i - 1
            # Todos los elementos de valor mayor pasan adelante
            while j >= 0 and self.list_insert_sort[j] > item_visited:
                print(str(self.list_insert_sort[j]) + " > " + str(item_visited))
                self.list_insert_sort[j + 1]= self.list_insert_sort[j]
                j -= 1
                print(self.list_insert_sort)
            self.list_insert_sort[j + 1] = item_visited  
            print(self.list_insert_sort)
        print("Vector final: " + str(self.list_insert_sort))

    # Función recursiva
    def merge_sort_function(self, list):
        print(list)
        # En el caso de que el tamaño de la lista sea menor a 2, se rompe la función recursiva y retornamos el valor
        if len(list) < 2:
            return list
        # En el caso de que sea 2 o mayor, se divide de nuevo
        else:
            middle = len(list) // 2 # Divide y redondea hacia abajo el resultado
            left = self.merge_sort_function(list[:middle]) # list[:1]
            right = self.merge_sort_function(list[middle:]) # list[1:]
            return self.merge(left, right)
        
    # Función para ordenar
    def merge(self, list1, list2):
        i, j = 0, 0 # Variables de incremento
        result = [] # Lista de resultado

        while(i < len(list1) and j < len(list2)):
            if (list1[i] < list2[j]):
                result.append(list1[i])
                i += 1 
            else:
                result.append(list2[j])
                j += 1 
        # Agregamos datos faltantes al resultado
        result += list1[i:]
        result += list2[j:]

        # Retornamos el resultados
        return result



    def test_merge_sort_function(self, list):
        self.test_show_data(list)
        """
        Lo primero que se ve en el psudocódigo es un if que
        comprueba la longitud de la lista. Si es menor que 2, 1 o 0, se devuelve la lista.
        ¿Por que? Ya esta ordenada. 
        """
        # En el caso de que el tamaño de la lista sea menor a 2, retornamos la lista (Esto pasa porque ya está ordenada, o se dividió hasta ser sólo 1 elemento)
        if len(list) < 2:
            #print("Entró if con " + str(list))
            return list
        # En el caso de que sea 2 o mayor, se divide de nuevo
        else:
            middle = len(list) // 2 # Divide y redondea hacia abajo el resultado
            #print("left")
            left = self.test_merge_sort_function(list[:middle])
            #print("right")
            right = self.test_merge_sort_function(list[middle:])
            input(Fore.BLACK+"--------------------------------------------------------------"+Fore.RESET)
            return self.test_merge(left, right)

    def test_merge(self, list1, list2):
        print(Fore.RED + "Ordenando subconjuntos" + Fore.RESET)
        print("Lista 1: " + Fore.BLUE + str(list1) + Fore.RESET)
        print("Lista 2: " + Fore.BLUE + str(list2) + Fore.RESET)
        """
        merge se encargara de intercalar los elementos de las dos
        divisiones.
        """
        i, j = 0, 0 # Variables de incremento
        result = [] # Lista de resultado

        # Intercalar ordenadamente
        while(i < len(list1) and j < len(list2)):
            if (list1[i] < list2[j]):
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1

        # Agregamos los resultados a la lista
        result += list1[i:]
        result += list2[j:]
    
        # Retornamos el resultados
        print(Fore.RED + "Resultado: " + Fore.RESET)
        print(Fore.BLUE + str(result) + Fore.RESET)
        #input()
        #self.parcial_result(result)
        return result
    
    def test_show_data(self, list):
        if len(list) == len(self.list_merge_sort):
            print(Fore.RED + "                       Lista inicial                   " + Fore.RESET)
            print("              "+ Fore.CYAN + str(list) + Fore.RESET + "              ")   
        elif len(list) > 1:
            input()
            system("cls")
            print(Fore.RED + "                       Lista inicial                   " + Fore.RESET)
            print("              "+ Fore.CYAN + str(self.list_merge_sort)+ Fore.RESET + "              ")
            print("              "+ Fore.BLUE + str(list) + Fore.RESET + "              ") 
    
    def parcial_result(self, result):
        system("cls")
        # Separar por niveles
        # Nivel 1 (Respueta final)
        if len(result) == len(self.list_merge_sort):
            print(Fore.RED + "                       Lista inicial                   " + Fore.RESET)
            print("              "+ Fore.CYAN + str(self.list_merge_sort)+ Fore.RESET + "              ") 
            print(Fore.RED + "                      Resultado final                   " + Fore.RESET)
            print("              "+ Fore.CYAN + str(result) + Fore.RESET + "              ")   
        
        # Nivel 2
        if len(result) < len(self.list_merge_sort):
            print(Fore.RED + "                       Lista inicial                   " + Fore.RESET)
            print("              "+ Fore.CYAN + str(self.list_merge_sort)+ Fore.RESET + "              ")
            if len(result) == self.aux_num or len(result) < self.aux_num: 
                print(Fore.RED + "                     Resultado parcial                   " + Fore.RESET)
                print("              "+ Fore.CYAN + str(self.aux_list) + str(result) + Fore.RESET + "              ")
                self.sum_list = self.aux_list + result
            else:
                self.aux_num = len(result)
                print(Fore.RED + "                     Resultado parcial                   " + Fore.RESET)
                print("              "+ Fore.CYAN + str(result) + Fore.RESET + "              ")
                self.aux_list = result

        input()

    def pruebaBubble(self, k):
        texto = " |    |"
        flechas = " v    v"
        for i in range (k):
            texto = "    " + texto
            flechas = "    " + flechas  
        return texto + "\n"+ flechas


    def quick_sort_function(self, list):
        print(list)
        if len(list) < 2:
            return list
        else:
            pivot = list.pop()
            items_greater = []
            items_lower = []

            for item in list:
                if item > pivot:
                    items_greater.append(item)
                else:
                    items_lower.append(item)
            
            return self.quick_sort_function(items_lower) + [pivot] + self.quick_sort_function(items_greater) 

    def countingSort(self, arr, exp1):
        print("Potencia: " + str(exp1))

        n = len(arr)
    
        # The output array elements that will have sorted arr
        output = [0] * (n)
    
        # initialize count array as 0
        count = [0] * (10)
    
        # Store count of occurrences in count[]
        for i in range(0, n):
            index = arr[i] // exp1
            count[index % 10] += 1
        print("Cantidad de ocurrencias de cada dígito " + str(count))
        # Change count[i] so that count[i] now contains actual
        # position of this digit in output array
        for i in range(1, 10):
            count[i] += count[i - 1]

        print("Suma valores arreglo \n" + str(count))
        print("[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]")
        # Build the output array
        i = n - 1
        while i >= 0:
            index = arr[i] // exp1
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1

        print("Salida \n" + str(output))
        print("[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]")
        # Copying the output array to arr[],
        # so that arr now contains sorted numbers
        i = 0
        for i in range(0, len(arr)):
            arr[i] = output[i]
        
    # Method to do Radix Sort
    def radixSort(self, arr):
    
        # Find the maximum number to know number of digits
        max1 = max(arr)
    
        # Do counting sort for every digit. Note that instead
        # of passing digit number, exp is passed. exp is 10^i
        # where i is current digit number
        exp = 1
        while max1 / exp >= 1:
            self.countingSort(arr, exp)
            exp *= 10
    
    

    ''' 
        Prueba de escritorio quick-sort:
        list = [61, 29, 24, 71, 75, 27, 37, 49]
        1. f([61, 29, 24, 71, 75, 27, 37, 49])
            pivot = 49
            greater = [61, 71, 75]
            lower = [29, 24, 27, 37]
            return (¿? -> 2 -> [24, 27, 29, 37]) + [49] + (¿? -> 7 -> [61, 71, 75])

        2. f([29, 24, 27, 37])
            pivot = 37
            greater = []
            lower = [29, 24, 27]
            return (¿? -> 3 -> [24, 27, 29]) + [37] + (¿? -> 6 -> [])

        3. f([29, 24, 27])
            pivot = 27
            greater = [29]
            lower = [24]
            return (¿? -> 4 -> [24]) + [27] + (¿? -> 5 -> [29])
        
        4. f([24])
            Entra en el if
            return [24]
        
        5. f([29])
            Entra en el if
            return [29]
        
        6. f([])
            Entra en el if
            return []
        
        7. f([61, 71, 75])
            pivot = 75
            greater = []
            lower = [61, 71]
            return (¿? -> 8 -> [61, 71]) + [75] + (¿? -> 11 -> [])

        8. f([61, 71])
            pivot = 71
            greater = []
            lower = [61]
            return (¿? -> 9 - > [61]) + [71] + (¿? -> 10 -> [])
        
        9. f([61])
            Entra en el if
            return [61]
        
        10. f([])
            Entra en el if
            return []
        
        11. f([])
            Entra en el if
            return []
        

        Prueba de escritorio merge-sort:
        list = [94, 68, 14, 92, 35, 17, 9, 20]
        1. merge_sort_function(list)
            left = ¿? -> 2 -> [14, 68, 92, 94]
            right = ¿? -> 9 -> [9, 17, 20, 35]
            merge([14, 68, 92, 94], [9, 17, 20, 35])
                return [9, 14, 17, 20, 35, 68, 92, 94]
        
        2. merge_sort_function([94, 68, 14, 92])
            left = ¿? -> 3 -> [68, 94]
            right = ¿? -> 6 -> [14, 92]
            merge([68, 94], [14, 92])
                return [14, 68, 92, 94]
        
        3. merge_sort_function([94, 68])
            left = ¿? -> 4 -> 94
            right = ¿? -> 5 -> 68
            merge([94], [68])
                return [68, 94]

        
        4. merge_sort_function([94])
            Entra en el if (tam < 2)
            return 94
        
        5. merge_sort_function([68])
            Entra en el if (tam < 2)
            return 68
        
        6. merge_sort_function([14, 92])
            left = ¿? -> 7 -> 14
            right = ¿? -> 8 -> 92
            merge([14], [92])
                return [14, 92]

        
        7. merge_sort_function([14])
            Entra en el if (tam < 2)
            return 14

        8. merge_sort_function([92])
            Entra en el if (tam < 2)
            return 92
        
        9. merge_sort_function([35, 17, 9, 20])
            left = ¿? -> 10 -> [17, 35]
            right = ¿? -> 13 -> [9 , 20]
            merge([17, 35], [9, 20])
                return [9, 17, 20, 35]
        
        10. merge_sort_function([35, 17])
            left = ¿? -> 11 -> 35
            right = ¿? -> 12 -> 17
            merge([35], [17])
                return [17, 35]
        
        11. merge_sort_function([35])
            Entra en el if (tam < 2)
            return 35
        
        12. merge_sort_function([17])
            Entra en el if (tam < 2)
            return 17
        
        13. merge_sort_function([9, 20])
            left = ¿? -> 14 -> 9
            right = ¿? -> 15 -> 20
            merge([9], [20])
                return [9, 20]
        
        14. merge_sort_function([9])
            Entra en el if (tam < 2)
            return 9
        
        15. merge_sort_function([20])
            Entra en el if (tam < 2)
            return 20
    '''