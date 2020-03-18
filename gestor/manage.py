import re, helpers
#INICIALIZAMOS EL DICCIONARIO
clients = []

#AÑADIENDO REGISTRO AL DICIONARIO MEDIANTE LA CREACION DE VARIABLES
aleja = {'nombre': 'Alejandra', 'apellido': 'Pérez', 'dni': '15H'}
clients.append(aleja)

#AÑADIENDO REGISTROS AL DICIONARIO SIN NECESIDAD DE VARIABLES
clients.append({'nombre': 'Mario', 'apellido': 'López', 'dni': '44H'})
clients.append({'nombre': 'Ady', 'apellido': 'García', 'dni': '25Z'})

def show(client):
    print(f"{client['dni']}: {client['nombre']} {client['apellido']}")

#FUNCION PARA LISTAR CLIENTES
def show_all():
    for client in clients:
        show(client)

#FUNCION PARA CONSULTAR CLIENTES
def find():

    dni = input("Introduce el DNI del cliente\n> ")

    for i, client in enumerate(clients):

        if client['dni'] == dni:
            show(client)
            return i, client

    print("No se ha encontrado ningún cliente con ese DNI")

#FUNCION AUXILIAR PARA VALIDAR EL DNI INGRESADO
def is_valid(dni):

    #INDICAMOS LOS TEST QUE SE HARAN EN LA PRUEBA
    """
    >>> is_valid('44H')  # No válido, en uso
    False

    >>> is_valid('X88')  # No válido, incorrecto
    False

    >>> is_valid('22A')  # Válido
    True
    """

    # COMPRUEBA SI EL DNI COMIENZA CON UN PATRON
    if not re.match('[0-9]{2}[A-Z]', dni):
        return False

    #COMPRUEBA SI EL DNI ESTA REPETIDO
    for client in clients:
        if client['dni'] == dni:
            return False

    return True

#PRUEBAS EN LA DOCUMENTACION
if __name__ == "__main__":
    import doctest
    doctest.testmod()

#AÑADIR NUEVOS REGISTROS 
def add():

    client = dict()

    print("Introduce nombre (De 2 a 30 caracteres)")
    client['nombre'] = helpers.input_text(2, 30)

    print("Introduce apellido (De 2 a 30 caracteres)")
    client['apellido'] = helpers.input_text(2, 30)

    while True:
        print("Introduce DNI (2 números y 1 carácter en mayúscula)")
        dni = helpers.input_text(3, 3)
        if is_valid(dni):
            client['dni'] = dni
            break
        print("DNI incorrecto o en uso")

    clients.append(client)
    return client

#FUNCION PARA EDITAR LOS REGISTROS
def edit():

    i, client = find()

    if client:

        print(f"Introduce nuevo nombre ({client['nombre']})")
        clients[i]['nombre'] = helpers.input_text(2, 30)

        print(f"Introduce nuevo apellido ({client['apellido']})")
        clients[i]['apellido'] = helpers.input_text(2, 30)

        return True

    return False

#FUNCION PARA ELIMINAR UN REGISTRO
def delete():

    i, client = find()
    if client:
        client = clients.pop(i)
        return True

    return False