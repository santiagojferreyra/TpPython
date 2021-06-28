import matplotlib.pyplot as plt
import requests
import sqlite3
import pandas as pd
import  time

nombre1 = "Descubrí las criptomonedas lider del mercado mundial."
print("|{:>10}|".format(nombre1))

print("\n")
print("Antes de empezar por favor ingrese algunos datos", "\n")
conn = sqlite3.connect("clientes.db")
c = conn.cursor()


nombre = input("Por favor escriba su nombre a continuacion: ")
apellido = input("por favor escriba su apellido: ")
ciudad = input("por favor escriba el nombre de su ciudad: ")
c.execute("insert into usuarios4 values('{}','{}','{}')".format(nombre,apellido,ciudad))
c.execute("update usuarios4 set ciudad = 'CABA' where ciudad = 'Buenos Aires'")
print("Muchisimas Gracias!")

conn.commit()

input("\n""Apriete enter para continuar: ")
c.execute("delete from usuarios4 where nombre = ''")
conn.commit()
conn.close()




headers = {
    "X-CMC_PRO_API_KEY" : "c30144af-ada3-4ada-a96c-0af5327ebbb9",
    "accepts" : "application/jason"
}

params = {
    "start" : "1",  #Empieza en la moneda lider y observa las primeras 10 en USD
    "limit" : "10",
    "convert" : "USD"
}

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

json = requests.get(url, params=params,headers=headers).json() #Si no poniamos el .sjon() nos devolvia el estado que sería 200 y que significa que esta todo bien



coins = json["data"]


precio_bitcoin = coins[0]["quote"]["USD"]["price"]




class wallet:

    precio_bitcoin = coins[0]["quote"]["USD"]["price"]

    def __init__(self,first,last,dollars):
        self.first = first
        self.last = last
        self.dollars = dollars

    def convert(self):
        self.dollars = float(self.dollars / self.precio_bitcoin)
 
transferencia1 = wallet("Jose", "Fernandez", float(input("Introduzca su monto en dolares: ")))

transferencia1.convert()
print("El valor de tus USD son:", transferencia1.dollars, "BTC")
 



class Bitcoin():
    def transferencias24h(self):
        print(coins[0]["quote"]["USD"]["percent_change_24h"])


class Etherium():
    def transferencias24h(self):
        print(coins[1]["quote"]["USD"]["percent_change_24h"])


class Binancecoin():
    def transferencias24h(self):
        print(coins[2]["quote"]["USD"]["percent_change_24h"])


def moneda(lang):
    lang.transferencias24h()

Bitcoin = Bitcoin()
Etherium = Etherium()
Binancecoin = Binancecoin()


print("La variacion porcentual del Bitcoin en las ultimas 24h es de: ")
moneda(Bitcoin)
print("\n")
print("La variacion porcentual del Etherium en las ultimas 24h es de: ")
moneda(Etherium)
print("\n")
print("La variacion porcentual del Binancecoin en las ultimas 24h es de: ")
moneda(Binancecoin)
print("\n")


conect = sqlite3.connect('clientes.db')
cur = conect.cursor()
cur.execute("create table if not exists precios (btc, eth)")
conect.commit()
precio_bit = coins[0]["quote"]["USD"]["price"]
precio_eth = coins[1]["quote"]["USD"]["price"]
cur.execute("insert into precios values('{}','{}')".format(precio_bit,precio_eth))
conect.commit()
cur.execute("select * from precios")

conect.close()





print("\n")
opcion = int(input("A continuacion elija una de las siguientes opciones para obtener informacion sobre la misma:"
          "\n" "1 - Bitcoin" "\n""2 - Etherium" "\n" "3 - Tether"
          "\n""4 - Binance Coin""\n""5 - Cardano""\n""6 - Ver Grafico de las 2 principales""\n""0 - Salir""\n""\n""Seleccione una opcion: "))
while opcion != 0:
        if opcion == 1:
            opcion2 = int(input("A continuacion que quiere ver sobre la moneda elegida:"
                               "\n" "1 - precio" "\n""2 - market caps" "\n" "3 - cantidad de tokens"
                               "\n""0 - Salir""\n""\n""Seleccione una opcion: "))
            while opcion2 != 0:
                if opcion2 == 1:
                    print("El precio els: $", coins[0]["quote"]["USD"]["price"])
                elif opcion2 == 2:
                    print("El market cap es de:",coins[0]["max_supply"] )
                elif opcion2 == 3:
                    print("la cantidad de tokens en circulacion es de:",coins[0]["circulating_supply"])
                else:
                    print("por favor seleccione una opcion valida")

                opcion2 = int(input("\n""Elija otra opcion o pulse 0 para volver al menu de inicio "))

        if opcion == 2:
            opcion3 = int(input("a continuacion que quiere ver sobre la moneda elegida:"
                               "\n" "1 - precio" "\n""2 - market caps" "\n" "3 - cantidad de tokens"
                               "\n""0 - Salir""\n""\n""Seleccione una opcion: "))
            while opcion3 != 0:
                if opcion3 == 1:
                    print("El precio els: $", coins[1]["quote"]["USD"]["price"])
                elif opcion3 == 2:
                    print("El market cap es de:",coins[1]["max_supply"] )
                elif opcion3 == 3:
                    print("la cantidad de tokens en circulacion es de:",coins[1]["circulating_supply"])
                else:
                    print("por favor seleccione una opcion valida")

                opcion3 = int(input("\n""Elija otra opcion o pulse 0 para volver al menu de inicio "))
        if opcion == 3:
            opcion4 = int(input("a continuacion que quiere ver sobre la moneda elegida:"
                                "\n" "1 - precio" "\n""2 - market caps" "\n" "3 - cantidad de tokens"
                                "\n""0 - Salir""\n""\n""Seleccione una opcion: "))
            while opcion4 != 0:
                if opcion4 == 1:
                    print("El precio els: $", coins[2]["quote"]["USD"]["price"])
                elif opcion4 == 2:
                    print("El market cap es de:", coins[2]["max_supply"])
                elif opcion4 == 3:
                    print("la cantidad de tokens en circulacion es de:", coins[2]["circulating_supply"])
                else:
                    print("por favor seleccione una opcion valida")

                opcion4 = int(input("\n""Elija otra opcion o pulse 0 para volver al menu de inicio "))
        if opcion == 4:
            opcion5 = int(input("a continuacion que quiere ver sobre la moneda elegida:"
                                "\n" "1 - precio" "\n""2 - market caps" "\n" "3 - cantidad de tokens"
                                "\n""0 - Salir""\n""\n""Seleccione una opcion: "))
            while opcion5 != 0:
                if opcion5 == 1:
                    print("El precio els: $", coins[3]["quote"]["USD"]["price"])
                elif opcion5 == 2:
                    print("El market cap es de:", coins[3]["max_supply"])
                elif opcion5 == 3:
                    print("la cantidad de tokens en circulacion es de:", coins[3]["circulating_supply"])
                else:
                    print("por favor seleccione una opcion valida")

                opcion5 = int(input("\n""Elija otra opcion o pulse 0 para volver al menu de inicio "))
        if opcion == 5:
            opcion6 = int(input("a continuacion que quiere ver sobre la moneda elegida:"
                                "\n" "1 - precio" "\n""2 - market caps" "\n" "3 - cantidad de tokens"
                                "\n""0 - Salir""\n""\n""Seleccione una opcion: "))
            while opcion6 != 0:
                if opcion6 == 1:
                    print("El precio els: $", coins[4]["quote"]["USD"]["price"])
                elif opcion6 == 2:
                    print("El market cap es de:", coins[4]["max_supply"])
                elif opcion6 == 3:
                    print("la cantidad de tokens en circulacion es de:", coins[4]["circulating_supply"])
                else:
                    print("por favor seleccione una opcion valida")

                opcion6 = int(input("\n""Elija otra opcion o pulse 0 para volver al menu de inicio "))
        if opcion ==  6:
            db = sqlite3.connect('clientes.db')
            data = pd.read_sql_query("select * from precios", db)
            print(data)
            plt.plot(data)
            plt.show()

        else:
            print("por favor seleccione una opcion valida")

        opcion = int(input("A continuacion elija una de las siguientes opciones para conocer su precio actual:"
                           "\n" "1 - Bitcoin" "\n""2 - Etherium" "\n" "3 - Tether"
                           "\n""4 - Binance Coin""\n""5 - Cardano""\n""0 - Salir""\n""\n""Seleccione una opcion: "))










try:
    f = open("comentarios.txt", "a")
    f.write("\n")
    f.write(input("Antes de irte por favor dejanos un comentario acerca de tu experiencia:" ))
    f = open("comentarios.txt", "r")
    contenido = f.read()
    print("\n")
    print("Algunas de las reseñas son:")
    print(contenido)
    print("\n")
    nombre2 = "Ha finalizado el programa"
    print("|{:>10}|".format(nombre2))
finally:
    f.close()





for x in range (0,50):
    time.sleep(3600)
    conect = sqlite3.connect('clientes.db')
    cur = conect.cursor()
    cur.execute("create table if not exists precios (btc, eth)")
    conect.commit()
    precio_bit = coins[0]["quote"]["USD"]["price"]
    precio_eth = coins[1]["quote"]["USD"]["price"]
    cur.execute("insert into precios values('{}','{}')".format(precio_bit, precio_eth))
    conect.commit()
    cur.execute("select * from precios")
    print(cur.fetchall())
    conect.close()




