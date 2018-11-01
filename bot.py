class aprendiz:
    saludos = {
        'hola': 'buenas tardes',
        'buenas': 'en que puedo ayudarte',
        'holi': 'gg holi',
        'que se dice': 'nada ¿y tu?',
        'holita': 'hola compita'

    }
    pais = {
        'colombia': 'bogota',
        'venezuela': 'caracas',
        'chile': 'santiago de chile',
        'españa': 'madrid',
        'ecuador': 'quito',
        'francia': 'paris',
        'japon': 'tokio',
        'italia': 'roma',



    }
    despedidas = {
        'chao': ' que estés bien',
        'nos vemos': 'vemola',
        'hasta luego': 'Nospi',
        'adios': 'Que te vaya bien'
    }

    def setNombre(self, Nombre):
        self.Nombre = Nombre;

    def agregar_Palabra(self, pregunta, respuesta):
        self.pais[pregunta] = respuesta


def main():
    aprendiendo = aprendiz()
    Saludo = input("Hola \n")

    Nombre = input("¿como te llamas?\n")

    despedida = aprendiendo.despedidas

    print("Hola " + Nombre + " Espero que este bien")

    while True:
        pregunta = input("Dime un pais y yo te digo su capital o terminas el programa con una despedida\n")

        if pregunta in aprendiendo.pais:
            print("La capital es " + aprendiendo.pais[pregunta] + "\n")
        elif pregunta in despedida:
            print(despedida[pregunta] + " " + Nombre)
            break
        else:
            print("Hey yo que voy a saber responder eso \n")
            respuesta = input("como podría responder a eso? \n")
            aprendiendo.agregar_Palabra(pregunta, respuesta)
            print("agregado!")


main()