def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    precio = input('Ingrese el precio: ')
    descuento = input('Ingrese el descuento: ')
    cantidad = input('Ingrese la cantidad: ')
    precio_con_descuento = int(precio) - float(descuento)
    precio_total = precio_con_descuento * int(cantidad)
    print('Precio: ', precio)
    print('Descuento: ', descuento)
    print('Precio con descuento: ', precio_con_descuento)
    print('Total: ', precio_total)
#casting()