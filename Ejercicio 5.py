def Fibonacci(numero):
    if(numero==0 or numero==1):
        return 1
    else:
        return Fibonacci(numero-1)+Fibonacci(numero-2)