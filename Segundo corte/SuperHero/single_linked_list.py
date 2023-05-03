class SingleLinkedList:
    class Node:
        def __init__(self, value):
            self.value= value
            self.next=None
    #Por fuera de la clase nodo
    def __init__(self):
        self.head= None
        self.tail= None
        self.length= 0    
    
    def show_list(self):
        #1. Declarar un array(lista) vacío
        array_whit_nodes_value= list()
        current_node= self.head
        # mientras el nodo actual que estoy visitando sea diferente de none
        while(current_node!=None):
            # añado al final de la lista el valor extraido del nodo
            array_whit_nodes_value.append(current_node.value)
            # incrementar en 1 el valor del nodo visitado
            # current_node+=1 NO SIRVE PARA PASAR AL SIGUIENTE NODO DE UNA SINGLE LINKEDLIST
            # pasamos del nodo actual al siguiente nodo mediante el puntero
            current_node=current_node.next
        # imprimir valores de la lista
        return(array_whit_nodes_value)
    
    def create_node_sll_ends(self, value):
        #  creamos una variable que va a tener la estructura de un nodo
        new_node= self.Node(value)
        # validar si la SLL tiene nodos o no          
        # if self.length ==0:
        #     print('la lista simplemente enlazada no tiene nodos')
        # else:
        #     print('la lista simplemente enlazada si tiene nodos')
        if self.head == None:
            # al nuevo nodo se convierte en la cabeza y cola de la lista
            self.head=new_node
            self.tail=new_node
        else:
            # Si ingresa en esta condicion es porque ya existe al menos un nodo
            # 1. debemos de relacionar al nuevo nodo con la cola de la lista
            # 2. Convertir al nuevo nodo en la cola de la lista
            self.tail.next= new_node
            self.tail= new_node
        #Incrementamos en 1 el tamaño de la lista
        self.length +=1
    
    def create_node_sll_unshift(self, value):
        new_node= self.Node(value)
        if self.head == None:
            # al nuevo nodo se convierte en la cabeza y cola de la lista
            self.head=new_node
            self.tail=new_node
        else:
            # 1. debemos de relacionar al nuevo nodo con la cabeza de la lista
            # 2. Convertir al nuevo nodo en la cabeza de la lista
            new_node.next= self.head
            self.head= new_node
        self.length+=1
    
    def delete_node_sll_pop(self):
        # 1. validar si la lista esta vacia
        # 2. validar si la lista tiene un unico nodo
        # 3. Si tiene mas de un nodo eliminar el nodo que es la cola de la lista
        # 4. asignar el nodo anterior como la nueva cola de la lista
        if self.length==0:
            print('>>Lista vacia no hay nodos para eliminar<<')
        elif self.length==1:
            self.head=None
            self.tail=None
            self.length -=1
        else:
            #1. Recorrer la lista para identificar la cola 
            current_node= self.head
            #2. validar mediante el enlace del nodo actual que haya un nodo
            new_tail= current_node
            while current_node.next != None:
                #3. Convertimos en la cola de la lista el nodo que actualmente estamos visitando 
                new_tail=current_node
                #4. Pasamos al siguiente nodo antes del salir del while por medio del enlace 
                current_node= current_node.next
            #5. Actualizamos la cola de la lista
            self.tail= new_tail
            self.tail.next=None
            #6. Restamos en 1 el tamaño de la lista
            self.length -=1
            
    def shift_node_sll(self):
        if self.length==0:
            print(">>Lista vacia no hay nodos por eliminar<<")
        elif self.length==1:
            self.head=None
            self.tail=None
            self.length -=1
        else:
            #Actualizamos el nombre de la cabeza con la var auxiliar 
            remove_node=  self.head
            #Actualizamos la cabeza de la lista
            self.head= remove_node.next
            #Eliminamos el enlace de remove_node con la lista
            remove_node.next=None
            self.length -=1   
            
    def get_node_value(self, index):
        if index < 1 or index > self.length:
            print('No se encontro')
        elif index == 1:
            return self.head.value
        elif index == self.length:
            return self.tail.value
        else:
            current_node = self.head
            node_counter = 1
            #Validar que el nodo a consultar sea el mismo del contador
            while(index != node_counter):
                current_node = current_node.next
                node_counter += 1
            return current_node.value
    
    def get_node(self, index):
        if index < 1 or index > self.length:
            return None
        elif index == 1:
            return self.head
        elif index == self.length:
            return self.tail
        else:
            current_node = self.head
            node_counter = 1
            while(index != node_counter):
                current_node = current_node.next
                node_counter += 1
            return current_node
            
    def update_node_value(self, index, new_value):
        search_node= self.get_node(index)
        if search_node != None:
            #Encontro el nodo y se puede actualizar
            print(f'Actualizando el valor del nodo... \n {search_node.value} por {new_value}')
            search_node.value= new_value
        else:
            #No encuentra el nodo
            print(" >>No se encontro el nodo<<")
            
    def remove_node(self, index):
        if index == 1:
            self.shift_node_sll()
        elif index == self.length:
            self.delete_node_sll_pop()
        else:
            remove_node_sll = self.get_node(index)
            if remove_node_sll!= None:
                previous_node = self.get_node(index - 1)
                print(self.get_node(index).value)
                previous_node.next = remove_node_sll.next
                remove_node_sll.next = None
                self.length-=1
            else:
                print('     >> No se encontro el nodo <<')
                
    def reverse(self):
        if self.length > 1:
            aux_head = self.tail
            aux_tail = self.head
            if self.length == 2:
                self.head = aux_head
                self.head.next = aux_tail
                self.tail = aux_tail
                self.tail.next = None
                return
            
            current_node = self.tail
            for i in range (1, self.length - 1):
                node = self.get_node(self.length - i)
                current_node.next = node
                current_node = node
            node.next = aux_tail
            self.head = aux_head
            self.tail = aux_tail
            self.tail.next = None
            
    def remove_all_nodes(self):
        if self.head is not None:
            self.head.next=None
            self.head=None
            self.tail=None
            self.length=0
        else:
            print('Nada para eliminar')
            
    def insert_node(self, index, value):
        if self.length !=8:
            print(f"\n >>>>>> Agregar nodo en la posición {index} <<<<<<")
            if index == 1:
                self.create_node_sll_unshift(value)
            elif index == self.length + 1:
                self.create_node_sll_ends(value)
            else:
                new_node = self.Node(value)
                actual_node_sll = self.get_node(index)
                if actual_node_sll != None:
                    previous_node = self.get_node(index - 1)
                    print("Se va a mover: ",actual_node_sll.value)
                    previous_node.next = new_node
                    new_node.next = actual_node_sll
                    self.length+=1
                else:
                    print(" >>> El índice no es accesible <<< ")
            return True
        return False
    
    def get_length(self):
        return self.length
              
    # def has_duplicate(self,value):
    #     cont=0
    #     for item in self.show_list():
    #         if item == value:
    #             cont+=1
    #     if cont >=2:
    #         return True
    #     else:
    #         return False

    def remove_by_value(self,value):
        if self.head == None:
            print("lista vacia")
        elif self.head.value == value:
            self.shift_node_sll()
        elif self.tail.value == value:
            self.delete_node_sll_pop()
        else:
            index=1
            current_node=self.head
            while current_node != None:
                if current_node.value == value:
                    previous_node = self.get_node(index- 1)
                    previous_node.next = current_node.next
                    current_node.next=None
                current_node=current_node.next
                index+=1
            self.length-=1
            
    def get_index_by_value(self,value):
        if self.head == None:
            print("lista vacia")
        elif self.head.value == value:
            self.shift_node_sll()
        elif self.tail.value == value:
            self.delete_node_sll_pop()
        else:
            index=1
            current_node=self.head
            while current_node != None:
                if current_node.value == value:
                    return index
                index+=1
                current_node=current_node.next
            return
                
    # def eliminate_duplicates(self, value):
    #     current_node = self.head
    #     if self.search_duplicates(value) > 1:
    #         value_count = self.search_duplicates(value)
    #         while(current_node != None) and value_count>1:
    #             aux = current_node.next
    #             if current_node.value == value:
    #                 index = self.search_an_element_and_return_index(value)
    #                 self.remove_node(index)
    #                 value_count-=1
    #             current_node = aux
                
    def search_an_element_and_return_index(self, value):
        if(self.length==0):
            print('La lista esta vacia')
        elif(self.head.value==value):
            print('El indice donde se encuentra el elemento es 1')
            return 1
        elif(self.tail.value==value):
            print('El indice en el que se encuentra el elemento es: ',self.length)
            return self.length
        else:
            current_node=self.head
            counter=1
            while(current_node!=None):
                if(current_node.value==value):
                    print('El elemento se encuentra en la posicion', counter)
                    break
                    return counter
                else:
                    current_node=current_node.next
                    counter+=1
                if(counter==self.length):
                    print('El elemento buscado no se encuentra')  


    def search_duplicates(self, value):
        current_node = self.head
        cant= 0
        while(current_node != None):
            if current_node.value == value:
                cant +=1
            current_node = current_node.next
        return cant
    
    def remove_all_duplicates(self):
        if self.head is None:
            return
        current_node = self.head
        values = set()
        while current_node is not None:
            if current_node.value in values:
                self.remove_by_value(current_node.value)
            values.add(current_node.value)
            current_node = current_node.next
        
    def group_all_duplicates(self):
        array_duplicates = list()
        current_node = self.head 
        while(current_node != None):
            array_duplicates.append(current_node.value)
            current_node = current_node.next
        array_duplicates.sort()
        for i in range(self.length):
            self.update_node_value(i+1, array_duplicates[i])
        print (self.length)
        print(array_duplicates)
                
                    
                
    
                