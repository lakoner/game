import time


def temporizador(func):
    def temporizador ():
        x = time.time()
        func()
        z = time.time() - x
        print(f"el tiempo que tarda esta funcion es: {z} segundos")
    return temporizador

@temporizador
def saludar():
    print("hola")




saludar()