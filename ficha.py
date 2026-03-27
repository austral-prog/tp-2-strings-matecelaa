def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)

    #input
    nombre_completo = input('Ingrese su nombre completo: ')
    correo_electronico = input('Ingrese su correo electronico: ')
    primer_nota = input('Ingrese la primer nota: ')
    segunda_nota = input('Ingrese la segunda nota: ')
    tercer_nota = input('Ingrese la tercer nota: ')

    #limpiar
    nombre = nombre_completo.strip().title()
    email = correo_electronico.lower().strip()
    nota1 = int(primer_nota)
    nota2 = int(segunda_nota)
    nota3 = int(tercer_nota)

    #calculos
    nombre_caracteres = len(nombre)
    espacio = nombre.find(' ')
    iniciales = nombre[0] + nombre[espacio + 1]
    apellido_usuario = nombre[espacio + 1 :].lower()
    nombre_usuario= nombre[:espacio].lower()
    user = apellido_usuario + '.' + nombre_usuario
    arroba = '@' in email
    buscar_arroba = email.find('@')
    dominio = email[buscar_arroba + 1:]
    nombre_guion = nombre.replace(' ', '_')
    a_nombre = nombre.lower().count('a')
    codigo = nombre[::-1].upper()
    suma_notas = nota1 + nota2 + nota3
    promedio_notas = suma_notas / 3
    promedio_notas_entero = suma_notas // 3

    #ficha
    cierre= '=' * 24
    ficha= f'''========================
    FICHA DEL ALUMNO
========================
Nombre: {nombre}
Email: {email}
Caracteres en nombre: {nombre_caracteres}
Iniciales: {iniciales}
Usuario: {user}
Email valido: {arroba}
Dominio: {dominio}
Nombre para archivo: {nombre_guion}
Cantidad de a: {a_nombre}
Codigo secreto: {codigo}
Nota 1: {nota1}
Nota 2: {nota2}
Nota 3: {nota3}
Suma: {suma_notas}
Promedio: {promedio_notas}
Promedio entero: {promedio_notas_entero}
{cierre}'''

    print(ficha)
    
#ficha()