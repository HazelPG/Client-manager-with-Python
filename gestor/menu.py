import helpers
import manage


def loop():

    while True:
        
        #IMPORTAMOS LA FUNCION AUXILIAR CLEAR
        helpers.clear()

        print("========================")
        print("  BIENVENIDO AL GESTOR  ")
        print("========================")
        print("[1] Listar clientes     ")
        print("[2] Mostrar cliente     ")
        print("[3] Añadir cliente      ")
        print("[4] Modificar cliente   ")
        print("[5] Borrar cliente      ")
        print("[6] Salir               ")
        print("========================")

        option = input("> ")

        #IMPORTAMOS LA FUNCION AUXILIAR CLEAR
        helpers.clear()  

        if option == '1':
            print("*** Listando los clientes ***\n")
            manage.show_all()
        if option == '2':
            print("*** Mostrando un cliente ***\n")
            manage.find()
        if option == '3':
            print("*** Añadiendo un nuevo cliente ***\n")
            manage.add()
            print("Cliente añadido correctamente\n")
        if option == '4':
            print("*** Modificando un cliente ***\n")
            if manage.edit():
                print("Cliente modificado correctamente\n")
            else:
                print("Cliente no se a modificado correctamente\n")
        if option == '5':
            print("*** Borrando un cliente ***\n")
            if manage.delete():
                print("Cliente borrado correctamente\n")
        if option == '6':
            print("Saliendo...\n")
            break

        input("\nPresiona ENTER para continuar...")