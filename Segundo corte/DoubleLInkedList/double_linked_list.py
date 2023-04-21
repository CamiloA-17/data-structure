# pip install memory_profiler
import time
from memory_profiler import memory_usage
class Node:
    def __init__(self, value):
        self.value= value
        self.next= None
        self.prev= None
class DoubleLinkedList:
    def __init__(self):
        self.head= None
        self.tail=None
        self.lenght=0
        
    def add_node_at_end(self, value):
        new_node= Node(value)
        if self.head is None:
            self.head= new_node
        else:
            current= self.head
            while current.next is not None:
                current= current.next
            current.next= new_node
            new_node.prev=current
        self.lenght+=1
        
    def add_node_at_start(self, value):
        new_node= Node(value)
        if self.head is None:
            self.head= new_node
        else:
            new_node.next= self.head
            self.head.prev= new_node
            self.head= new_node
        self.lenght+=1
        
    def print_list(self):
        if self.head is None:
            return 
        current= self.head
        while current is not None:
            print(current.value, end='|')
            current= current.next
        print()
        
    def add_node_in_position(self, position, value):
        if position < 1 or position > self.lenght+1:
            raise IndexError('Posicion fuera de rango')
        new_node= Node(value)
        if position==1:
            self.add_node_at_start(value)
        elif position== self.lenght+1:
            self.add_node_at_end(value)
        else:
            current_node= self.head
            for i in range(1, position-1):
                current_node= current_node.next
            new_node.next= current_node.next
            new_node.prev= current_node
            #se hace primero el .next y a ese nodo se le haya el previo
            current_node.next.prev= new_node
            current_node.next= new_node
            self.lenght+=1
            
    def remove_node_at_start(self):
        if self.head is None:
            return
        else:
            self.head= self.head.next
            if self.head is not None:
                self.head.prev= None
        self.lenght-=1
        
    def remove_node_at_end(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head= None
        else:
            current= self.head
            while current.next is not None:
                current= current.next
            current.prev.next= None
        self.lenght-=1
        
    def remove_node_by_position(self, position):
        if position <1 or position> self.lenght:
            raise IndexError("Posicion fuera de rango")
        current_node= self.head
        if position==1:
            self.remove_node_at_start()
        elif position== self.lenght:
            self.remove_node_at_end()
        else:
            print("cantidad de nodos : " + str(self.lenght))
            print("valor: "+ str(position))
            for i in range(1, position):
                current_node= current_node.next
            current_node.prev.next= current_node.next
            current_node.next.prev= current_node.prev
            self.lenght-=1
    
    def remove_node_by_value(self, value):
        if self.head is None:
            return
        if self.head.value == value:
            self.remove_node_at_start()
        current_node= self.head
        while current_node is not None:
            if current_node.value==value:
                if current_node.next is not None:
                    current_node.next.prev= current_node.prev
                current_node.prev.next= current_node.next
                return
            current_node=current_node.next
        self.lenght-=1
            
    def get_node_at_index(self, position):
        if self.head is None:
            return None
        current_node= self.head
        i=1
        while current_node is not None and i< position:
            current_node= current_node.next
            i+=1
        print(current_node.value)
        
    def get_node_at_value(self, value):
        if self.head is None:
            return None
        current= self.head
        while current is not None:
            if current.value==value:
                print(current.value)
            current=current.next
        return None

    
    def update_node_at_index(self, position, value):
        if position <1 or position >self.lenght:
            print('Posicion fuera de rango')
        if self.head is None:
            return
        current= self.head
        i=1
        while current is not None and i < position:
            current=current.next
            i+=1
        if current is not None:
            current.value= value
            
    def update_node_at_value(self, value, newValue):
        if self.head is None:
            return
        current= self.head
        while current is not None:
            if current.value==value:
                current.value=newValue
            current= current.next
    
    def sort_asc(self):
        if self.head is None:
            return
        current= self.head
        while current.next is not None:
            next_node = current.next
            print("Valor next node")
            print(next_node.value)
            while next_node is not None:
                if current.value > next_node.value:
                    current.value, next_node.value = next_node.value, current.value
                next_node = next_node.next
            current=current.next
            
    def has_duplicates(self):
        if self.head is None:
            return 
        current= self.head
        values= set()
        while current is not None:
            if current.value in values:
                return print(f'Find duplicates')
            values.add(current.value)
            current= current.next
        return print(f'No duplicates')
    
    def has_duplicates_with_information(self):
        if self.head is None:
            return
        current= self.head 
        #Creamos un diccionario
        # listas|set()|diccionario{}
        values={}
        found_duplicates = False
        while current is not None:
            if current.value in values:
                values[current.value].append(current)
                found_duplicates = True
            else:
                values[current.value]=[current]
            current = current.next
        print(values)
        if found_duplicates:
            message = "The duplicates values are :\n"
            for value,nodes in values.items():
                if len (nodes) > 1:
                    message+=(f"{value}: {len(nodes)} times \n")
            print(message)
            return True
        else:
            return False

    def calculate_complexity(self, func):
        # Ejecutar la función una vez para que se compile
        func(0)

        # Calcular tiempo de ejecución
        start_time = time.time()
        func(0)
        end_time = time.time()
        exec_time = end_time - start_time

        # Calcular uso de memoria
        mem_usage = max(memory_usage((func, (0,)), interval=0.1))

        # Imprimir resultados
        print(f"Función {func.name}:")
        print(f"Tiempo de ejecución: {exec_time:.6f} segundos")
        print(f"Uso máximo de memoria: {mem_usage:.6f} MB")
        print("------------------------------------")