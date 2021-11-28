

def llenarjarra3(jarra):
    añadido="litro"
    for i in range (0,3-len(jarra)):
        jarra.append(añadido)

def llenarjarra4(jarra):
    añadido="litro"
    for i in range (0,4-len(jarra)):
        jarra.append(añadido)

def traspasar(jarra1,jarra2,longitud2):
    añadido="litro"
    for i in range(0,longitud2-len(jarra2)):
        if(len(jarra1)!=0):
            jarra1.pop(0)
            jarra2.append(añadido)
    return jarra1, jarra2
def vaciar(jarra):
    jarra.clear()
def llenar2galones():
    jarra3=[]
    jarra4=[]
    llenarjarra3(jarra3)
    jarra3,jarra4=traspasar(jarra3,jarra4,4)
    llenarjarra3(jarra3)
    jarra3,jarra4=traspasar(jarra3,jarra4,4)
    vaciar(jarra4)
    jarra3,jarra4=traspasar(jarra3,jarra4,4)
    return jarra3,jarra4
if __name__ == "__main__":
    jarra,jarra2=llenar2galones()
    # llenarjarra3(jarra)
    # jarra2=["litro","litro"]
    # print(jarra)
    # jarra,jarra2=traspasar(jarra,jarra2,4)
    print("jarra3=",jarra)
    print("jarra4=",jarra2)