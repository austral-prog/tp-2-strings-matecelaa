def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """
    nombre = input("Ingrese un nombre: ")
    nombre = nombre.lower()
    mensaje1 = f"Contiene a: {'a' in nombre}"
    mensaje2 = f"Contiene e: {'e' in nombre}"
    mensaje3 = f"Contiene i: {'i' in nombre}"
    mensaje4 = f"Contiene o: {'o' in nombre}"
    mensaje5 = f"Contiene u: {'u' in nombre}"
    print(mensaje1)
    print(mensaje2)
    print(mensaje3)
    print(mensaje4)
    print(mensaje5)
#check_vowels()