from itertools import product

def generar_lenguaje(alfabeto, longitud_maxima):
    lenguaje = []
    # Genera todas las combinaciones posibles de longitud desde 1 hasta longitud_maxima
    for longitud in range(1, longitud_maxima + 1):
        # Utiliza product para generar todas las combinaciones posibles
        for combinacion in product(alfabeto, repeat=longitud):
            # Une los caracteres de la combinación en una cadena y la agrega al lenguaje
            lenguaje.append(''.join(combinacion))
    return lenguaje

if __name__ == "__main__":
    # Solicitar al usuario que introduzca los elementos del alfabeto separados por comas
    entrada_alfabeto = input("Introduce los elementos del alfabeto: ")
    # Dividir la entrada por comas para obtener los elementos individuales
    alfabeto = entrada_alfabeto.split(',')
    
    longitud_maxima = int(input("Introduce la longitud máxima del lenguaje: "))

    # Generar el lenguaje y mostrar los elementos con sus índices
    lenguaje = generar_lenguaje(alfabeto, longitud_maxima)
    print("Los elementos del lenguaje generado son:")
    
    total_elementos_alfabeto = 0  # Inicializa el contador de elementos del alfabeto
    
    for elemento in lenguaje:
        cantidad_elementos = sum(1 for char in elemento if char in alfabeto)
        total_elementos_alfabeto += cantidad_elementos
        print(f"{elemento} = {cantidad_elementos}")

    print(f"\nTotal de elementos del alfabeto generados: {total_elementos_alfabeto}")
