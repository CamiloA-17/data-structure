

def binario(lista, menor, mayor, x):
    if mayor >= menor:
        mid= (mayor+menor)//2
        if lista[mid] == x:
            return mid
        elif lista[mid]>x:
            return binario(lista,menor,mid-1,x)
        else:
            return binario(lista,mid+1,mayor,x)
    else:
        return -1
    

def lineal(lista,x):
    #i -> posicion actual en la lista, inicia en 0
    i=0
    #recorrer todos los elementos de la lista:
    for z in lista:
        #z contiene el valor de la lista[i]
        #si z es igual a x, devuelve i
        if z == x:
            return i
        #si z es distinto a x, incrementa i 
        i=i+1
    #si no encuentra el valor, retorna -1
    return -1



