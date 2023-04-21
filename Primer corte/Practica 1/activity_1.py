""" Author: Camilo Andres Molano
    Date: 25/01/2023
    Data type: list practice 
"""
# 1. Declarar la clase 
class ListPractice:
    #crear funcion inicializadora de la clase
    def __init__(self):
        #Definir las variables globales de la clase
        self.student_name= ""
        self.courses_list= ["POO", "TAD"]
        
    
    # 3. Funcion customizada 
    def show_info_list(self):
        #Imprimir contenido de la lista courses_list
        print(self.courses_list)
        #Cantidad de elemeentos que tiene la lista
        print(len(self.courses_list))
        
    #4. Funcion que solicita al usuario ingresar informacion
    def input_data_courses(self):
        #4.1 Declaramos una variable a nivel de método
        print("Ingrese la siguiente informacion:")
        #4.2 Solicitud de texto
        student_name = input("Nombre: ")
        #4.3 Solucitud de entero
        courses_number= int(input("Cantidad asignaturas: "))
        #Validamos si el courses:number es menor que el tamaño actual de la lista
        if courses_number <= len(self.courses_list):
            print(" <<Error: cursos a inscribir es menor que 2>>")
        else:
                for course in range(courses_number- len(self.courses_list)):
                    #variable que almacena el nombre de la asignatura
                    #Solicitar nombre de las asignaturas al usuario
                    course_name=input("Nombre asignatura: ")
                    if course_name in self.courses_list:
                        print("<<ERROR: La materia ya fue inscrita>>")
                    else:
                        self.courses_list.append(course_name)
                
                    print(self.courses_list)