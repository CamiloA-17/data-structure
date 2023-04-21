class metodosord:
    def __init__(self):
        self.vector = [2,1,5,3,6,4,8,9,7]

    def mostrarVector(self):
        print(self.vector)

    
    def bubble_sort(self):
        booleano=True
        while booleano:
            booleano=False
            for i in range (len(self.vector)-1):
                if self.vector[i] > self.vector[i+1]:
                    self.vector[i], self.vector[i+1]= self.vector[i+1], self.vector[i]
                    booleano = True
        print(self.vector)
    

    
    def selectSort(self):
        count=0
        for i in self.vector:
            count+=1

        for k in range(count):
            min=k
            for j in range(k+1, count):
                if self.vector[min] > self.vector[j]:
                    min=j
            self.vector[min], self.vector[k] =  self.vector[k], self.vector[min]
        print(self.vector)
    

    


    def insert_sort_function_v2(self):

        for i in range(1, len(self.vector)):
            item_visited = self.vector[i]
            # Visitamos la posición anterior a la actual
            j = i - 1
            # Todos los elementos de valor mayor pasan adelante
            while j >= 0 and self.vector[j] > item_visited:
                self.vector[j + 1]= self.vector[j]
                j -= 1
            self.vector[j + 1] = item_visited  

        print("Vector final: " + str(self.vector))