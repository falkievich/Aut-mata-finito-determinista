import re

#Si la cadena cumple los creterios esta función realiza las transiciones 
def transicion(cadena):
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

#Esta función valida si la cadena cumple con los criterios de aceptación
def validacion(cadena):
    
    # Verificar si la cadena contiene un "10"
    if re.search(r'10', cadena):
        return "La cadena no puede contener '10'."
    
    # Verificar si la cadena tiene una cantidad impar de caracteres
    if len(cadena) % 2 == 0:
        return"La cadena debe tener una cantidad impar de caracteres."
    
    if transicion(cadena):
        return "La cadena es válida según el autómata."
    else:
        return "La cadena no es válida según el autómata."
