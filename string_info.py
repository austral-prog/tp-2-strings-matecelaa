def string_info():
    """Dada la palabra 'Programacion', imprime su longitud, primera y última letra,
    la palabra repetida 3 veces y decorada con '***'.
    """
    palabra = 'Programacion'
    mensaje1 = f'Palabra: {palabra}'
    mensaje2 = f'Longitud: {len(palabra)}'
    mensaje3 = f'Primera letra: {palabra[0]}'
    mensaje4 = f'Ultima letra: {palabra[-1]}'
    mensaje5 = f'Repetida: {palabra * 3}'
    mensaje6 = f'Decorada: ***{palabra}***'
    print(mensaje1)
    print(mensaje2)
    print(mensaje3)
    print(mensaje4)
    print(mensaje5)
    print(mensaje6)
#string_info()