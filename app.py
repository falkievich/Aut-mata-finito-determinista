import re

def automata(cadena):
    estado_actual = 'q0'
    for caracter in cadena:
        if estado_actual == 'q0':
            if caracter == '1':
                estado_actual = 'q1'
            elif caracter in ['0', '2']:
                estado_actual = 'q2'
            else:
                return False
        elif estado_actual == 'q1':
            if caracter == '1':
                estado_actual = 'q3'
            elif caracter == '2':
                estado_actual = 'q0'
            else:
                return False
        elif estado_actual == 'q2':
            if caracter == '1':
                estado_actual = 'q3'
            elif caracter in ['0', '2']:
                estado_actual = 'q0'
            else:
                return False
        elif estado_actual == 'q3':
            if caracter == '1':
                estado_actual = 'q1'
            elif caracter == '2':
                estado_actual = 'q2'
            else:
                return False
            
    if estado_actual in ['q1', 'q2']:
        return True
    else:
        return False

def main():
    cadena = input("Ingrese una cadena formada por los elementos de A (0, 1, 2): ")
    
    # Verificar si la cadena contiene un "10"
    if re.search(r'10', cadena):
        print("La cadena no puede contener '10'.")
        return
    
    # Verificar si la cadena tiene una cantidad impar de caracteres
    if len(cadena) % 2 == 0:
        print("La cadena debe tener una cantidad impar de caracteres.")
        return
    
    if automata(cadena):
        print("La cadena es válida según el autómata.")
    else:
        print("La cadena no es válida según el autómata.")

if __name__ == "__main__":
    main()  #La cadena debe tener una longitud impart y no terner un 10.