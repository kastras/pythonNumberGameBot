import os
import adivina_multiple
import telebot
import random
import json

ARCHIVO = os.environ.get('USERS_FILE')
BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)
game = adivina_multiple.Game()
try:
    f = open(ARCHIVO,"r")
    usuario = json.load(f)
except:
    usuario = {}
    print("no existe")

def new_usuario(id,nombre,nick):
    id = str(id)
    nombre = nombre
    contador = 0 
    muertes = 0
    aciertos = 0
    numero = random.randint(0,9999)
    usuario[f"{id}"] = {"nombre": nombre, "nick" : nick, "contador" : contador, "muertes" : muertes , "aciertos" : aciertos, "numero" :numero}

def juego(id,elegido,numero):
        if numero < elegido:
            tamaño = "pequeño"
            # print("El número que has introducido es mas grande ")
        elif numero > elegido:
            tamaño = "grande"
            # print("El número que has introducido es mas pequeño ")
        elif numero == elegido:
            usuario[f"{id}"]["aciertos"] =+1
            usuario[f"{id}"]["contador"] = 0
            usuario[f"{id}"]["numero"] = random.randint(0,9999)
            return("ENHORABUENA, vuelve a probar")
        usuario[f"{id}"]["contador"]+=1
        coincidencias = game.contadorIg(numero,elegido)
        intentos = usuario[f"{id}"]["contador"]
        return(f"El numero es mas {tamaño} y hay {coincidencias} coincidencias, es el intento {intentos}")
        # time.sleep(1)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    mensaje = """Quieres jugar a un juego?
    voy a pensar en un numero aleatorio del 0 al 9999,
    tienes 10 intentos para adivinarlo, te ire dando pistas de cuantos numero coinciden con la posicion
    y si el numero es mayor o menor.
    Suerte!
    
    Para volver a empezar pulsa en /start"""
    bot.reply_to(message, mensaje)

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    if str(message.chat.id) in usuario:
        pass
    else:
        new_usuario(message.chat.id,message.chat.first_name,message.chat.username)
    print(usuario)

    try:
        int(message.text)

        if int(usuario[f"{message.chat.id}"]["contador"]) < 10:
            respuesta = juego(int(message.chat.id),int(message.text),usuario[f"{message.chat.id}"]["numero"])
        else:
            usuario[f"{message.chat.id}"]["contador"] = 0
            usuario[f"{message.chat.id}"]["muertes"] += 1
            numero_anterior = usuario[f"{message.chat.id}"]["numero"]
            respuesta = f"""Has fallado los 15 intentos.
            El número era: {numero_anterior}
            Vuelve a probar de 0
            Estadisticas:
            Derrotas: {usuario[f"{message.chat.id}"]["muertes"]}
            Aciertos: {usuario[f"{message.chat.id}"]["aciertos"]}"""
            usuario[f"{message.chat.id}"]["numero"] = random.randint(0,9999)

    except ValueError:
        respuesta = "Escribe solo números."
    # print(respuesta)
    bot.reply_to(message, f"{respuesta} ")

    # guardamos usuarios
    try:
        with open(ARCHIVO, 'w') as archivo:
            json.dump(usuario, archivo)
    except:
        pass
bot.infinity_polling()
