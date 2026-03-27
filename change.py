def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    
    gasto = float(input('Ingrese el gasto: '))
    dinero_recibido = float(input('Ingrese el dinero recibido: '))
    vuelto = dinero_recibido - gasto
    pesos = int(vuelto)
    centavos = round (int(vuelto - pesos) * 100)
    print('Ingresar gasto:')
    print(gasto)
    print('Ingresar dinero recibido:')
    print(dinero_recibido)
    print('')
    print('Vuelto')
    print('')
    print('Pesos:')
    print(pesos)
    print('Centavos:')
    print(centavos)
#change()