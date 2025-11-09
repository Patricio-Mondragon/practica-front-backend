import requests

def readUsers():
    url = "https://queenlycrow-us.backendless.app/api/data/usuarios"
    response = requests.get(url)

    print(response.json())

def createUser(nuevo_usuario):
    url = "https://queenlycrow-us.backendless.app/api/data/usuarios"


    response = requests.post(url, json=nuevo_usuario)

    if response.status_code == 200:
        print("Usuario creado:", response.json())
    else:
        print("Error al crear usuario:", response.text)



objectId = "8B57C5A8-4DD7-43E7-82CB-64AFE95468EB"

def readSpecificUser(objectId):
    url = f"https://queenlycrow-us.backendless.app/api/data/usuarios/{objectId}"

    response = requests.get(url)
    print(response.json())

def updateUsers(objectId, actualizacion):
    url = f"https://queenlycrow-us.backendless.app/api/data/usuarios/{objectId}"

    response = requests.put(url, json=actualizacion)

    if response.status_code == 200:
        print("Usuario actualizado:", response.json())
    else:
        print("Error al actualizar usuario:", response.text)


def deleteUser(objectId):
    url = f"https://queenlycrow-us.backendless.app/api/data/usuarios/{objectId}"

    response = requests.delete(url)
    if response.status_code == 200:
        print("Usuario eliminado correctamente")
    else:
        print("Error al eliminar usuario:", response.text)



#readUsers()
#readSpecificUser(objectId)


actualizacion = {
    "telefono": "123456"
}

#updateUsers(objectId,actualizacion)

nuevo_usuario = {
    "nombre": "Juan",
    "email": "juan@example.com",
    "telefono": "555-1234",
    "contraseña": "juanito123",
    "tipo de usuario": "adoptante"
}

#createUser(nuevo_usuario)

deleteUser("35A8777F-C8DD-48D0-B51D-6449ED6014FE")