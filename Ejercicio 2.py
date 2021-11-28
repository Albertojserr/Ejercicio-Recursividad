def invertirlista(lista):
    if(lista==[]):
        listafinal=lista
    else:
        lista2=lista
        elemento=lista2.pop(-1)
        listafinal=[elemento]+invertirlista(lista2)
    return listafinal


if __name__ == "__main__":
    lista=[1,2,3,4,5]
    inversa=invertirlista(lista)
    print(lista)
    print(inversa)