usuarios = {}
nombres=""

def NombreRepetido(repetido):
    for nombre in nombres:
        if nombre == repetido:
            print("El nombre no puede estar repetido")
            return False
    return True

def VerificarSexo(sexo):
    
    if sexo != "F" and sexo != "M":
        print("El sexo solo puede ser F o M")
        return False
    else:
        return True

def Contraseña(contraseña):
    contador_numero = 0
    contador_letra = 0
    for letra in str(contraseña):
        if letra.isnumeric():
            contador_numero += 1
        if letra.isalpha():
            contador_letra += 1
    
    if contador_numero < 1:
        print("La contraseña debe de tener al menos 1 numero")
        return False
    elif contador_letra < 1:
        print("La contraseña debe de tener al menos 1 letra")
        return False
    elif len(contraseña) < 8:
        print("La contraseña debe de ser de largo minimo 8")
        return False
    
    return True

def NombreUsuarioExiste(existe):
    for clave in usuarios:
        if clave == existe:
            print("el nombre si existe")
            return True
    print("El usuario no Existe")
    return False


opcion = "0"
while opcion != "4":
    print("******************************************")
    print("1.- Ingresar usuario")
    print("2.- Buscar usuario")
    print("3.- Eliminar usuario")
    print("4.- Salir")
    print("******************************************")

    opcion =input("Ingrese la opcion que desee: ")

    match opcion:
        case "1":
            while True:
                nombres=input("Ingrese su Nombre de usuario: ")
                if NombreRepetido(nombres)== True:
                    print("Nombre de usuario existoso")
                    usuarios[nombres] = []
                    break
                else:
                    print("El nombre de usuario no puede estar repetido")

            while True:
                sexo=input("Ingrese su sexo: ").upper()
                if VerificarSexo(sexo)== True:
                    print("Sexo verificado")
                    usuarios[nombres].append(sexo)
                    break
                else:
                    print("Solo puede colocar F(femenino) o M(masculino)")
            
            while True:
                contraseña=input("Ingrese su contraseña: ")
                if Contraseña(contraseña)== True:
                    print("contraseña guardada exitosamente")
                    usuarios[nombres].append(contraseña)
                    break
                    
                
                else:
                    print("Contraseña denegada")
        
        case "2":
            
                buscador_nombre=input("Ingrese el nombre de usuario que desee buscar: ")
                if NombreUsuarioExiste(buscador_nombre) == True:
                    
                    print(f"El sexo del usario es: {usuarios [buscador_nombre]}")
                    
                else:
                    print("El nombre de usuario que ingreso no se encontro en la lista")
        case "3":
            
                Nombre_eliminar=input("Ingrese el nombre que desee borrar sus datos: ")
                if NombreUsuarioExiste(Nombre_eliminar)== True:
                    del usuarios[Nombre_eliminar]
                    print("Los datos del usuario que ingreso se eliminaron exitosamente")
                    
                else:
                    print("El nombre que ingreso no existe")


                