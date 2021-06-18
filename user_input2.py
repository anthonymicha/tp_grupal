import sqlite3

print('\n')
print('~ Kissaten - ᴄᴀғᴇ ᴅᴇ ᴇsᴘᴇᴄɪᴀʟɪᴅᴀᴅ ~\n')
print('Bienvenido, le pediremos sus datos para el envio.')

#Datos inciales: Name, Tel & Dir
name = ''
while True:
    try:
        name = input(" Ingrese su nombre: ").strip()
    except:
        print("\n¡Error en el ingreso! Ingrese unicamente letras, tampoco espacios.")
    else:
        try:
            if name.isalpha() == False:
                raise Exception
            else:
                #print(name)
                break
        except:
            print("\n¡Error en el ingreso! Ingrese unicamente letras, tampoco espacios.")
    #Tel:
while True:
    tel = input("\n Ingrese su numero de celular: ")
    try:
        tel = int(tel)

    except ValueError:
        print("\n¡Error en el ingreso! Ingrese unicamente numeros.")

    else:
        try:
            tel = str(tel)
            if len(tel) != 10:
                raise Exception
            else:
                break
        except:
            print(f'\nEl numero "{tel}", no tiene 10 digitos.')
            print('Por favor ingrese 15 u 11, seguido de su numero.'
                  '\n\nRecuerde que debe tener 10 caracteres en total.')
    #Dir
dir = input(f'\nY por ultimo {name}...\n Ingrese su direccion por favor (donde espera recibir su pedido): ').strip()


#monto_final = 0

conn = sqlite3.connect('/Users/anthonymicha/Desktop/tp_grupal/kissaten.db')
c = conn.cursor()
c.execute(f"SELECT * FROM cafes")
cafes = c.fetchall()

class Cliente():

    def __init__(self, name, tel, dir):
        self.name = name
        self.tel = tel
        self.dir = dir

        print(f'\n¡Ahora si {name}!')


    def crear_pedido(self):
        opcion = 'No'
        acceptable = range(1, cafes[-1][0] + 1)
        esta = False
        print('\t¿Que desea llevar hoy?\n')

        for cafe in cafes:
            if len(cafe[1]) < 7:
                print(f'{cafe[0]}.\t {cafe[1]}\t\t\t{cafe[2]}gr\t ${cafe[3]}')
            else:
                print(f'{cafe[0]}.\t {cafe[1]}\t\t{cafe[2]}gr\t ${cafe[3]}')

        while opcion.isdigit() == False or esta == False:

            opcion = input(f'\ningrese un numero de cafe (1-{cafes[-1][0]}): ')

            if opcion.isdigit() == False:
                print('\nUps, eso no es un numero')

            if opcion.isdigit() == True:
                if int(opcion) in acceptable:
                    esta = True
                else:
                    print(f'\nElija un numero de la lista (1-{cafes[-1][0]})')
                    esta = False

        print(f'\nElegiste la opcion Nº{opcion}:')

        if int(opcion) == 1:
            #Bocaya 250gr
            Cliente.origen = 'Bocaya'
            Cliente.cantidad = '250'
            Cliente.monto = 1045

        if int(opcion) == 2:
            #Bocaya 500gr
            Cliente.origen = 'Bocaya'
            Cliente.cantidad = '500'
            Cliente.monto = 2090

        if int(opcion) == 3:
            #Bocaya 1000gr
            Cliente.origen = 'Bocaya'
            Cliente.cantidad = '1000'
            Cliente.monto = 3345

        if int(opcion) == 4:
            #Brasil 250gr
            Cliente.origen = 'Brasil'
            Cliente.cantidad = '250'
            Cliente.monto = 780

        if int(opcion) == 5:
            #Brasil 500gr
            Cliente.origen = 'Brasil'
            Cliente.cantidad = '500'
            Cliente.monto = 1560

        if int(opcion) == 6:
            #Brasil 1000gr
            Cliente.origen = 'Brasil'
            Cliente.cantidad = '1000'
            Cliente.monto = 2496

        if int(opcion) == 7:
            #Costa Rica 250gr
            Cliente.origen = 'Costa Rica'
            Cliente.cantidad = '250'
            Cliente.monto = 1490

        if int(opcion) == 8:
            #Costa Rica 500gr
            Cliente.origen = 'Costa Rica'
            Cliente.cantidad = '500'
            Cliente.monto = 2980

        if int(opcion) == 9:
            #Costa Rica 1000gr
            Cliente.origen = 'Costa Rica'
            Cliente.cantidad = '1000'
            Cliente.monto = 4768

        if int(opcion) == 10:
            #Guatemala 250gr
            Cliente.origen = 'Guatemala'
            Cliente.cantidad = '250'
            Cliente.monto = 1690

        if int(opcion) == 11:
            #Guatemala 500gr
            Cliente.origen = 'Guatemala'
            Cliente.cantidad = '500'
            Cliente.monto = 3380

        if int(opcion) == 12:
            #Guatemala 1000gr
            Cliente.origen = 'Guatemala'
            Cliente.cantidad = '1000'
            Cliente.monto = 5408

        if int(opcion) == 13:
            #Peru 250gr
            Cliente.origen = 'Peru'
            Cliente.cantidad = '250'
            Cliente.monto = 1100

        if int(opcion) == 14:
            #Peru 500gr
            Cliente.origen = 'Peru'
            Cliente.cantidad = '500'
            Cliente.monto = 2200

        if int(opcion) == 15:
            #Peru 1000gr
            Cliente.origen = 'Peru'
            Cliente.cantidad = '1000'
            Cliente.monto = 3520

        print(f'\t{Cliente.cantidad}gr de Cafe de {Cliente.origen}')
        print(f'\t\tx ${Cliente.monto}')
        print('___ __ ___ _____ __ ___ _____ ___   ')

    def cargar_pedido(self, name, origen, cantidad, tel, dir):
        with conn:
            c.execute(f"INSERT INTO pedidos VALUES (:name, :origen, :cantidad, :tel, :dir)",
                      {'name': self.name, 'origen': Cliente.origen, 'cantidad': Cliente.cantidad, 'tel': self.tel, 'dir': self.dir})

    def baja_stock(self, origen, cantidad):
        with conn:
            c.execute(f'UPDATE cafes SET stock = stock - 1 WHERE origen = :origen AND peso = :cantidad',
                      {'origen': Cliente.origen, 'cantidad': Cliente.cantidad})

#Logeo:


# Comandos del pedido:

def comenzar_orden():
    choice = "wrong"
    while choice not in ['s', 'n']:
        choice = input('\n¿Listo para ordenar? \n (s/n): ')
        if choice not in ['s', 'n']:
            print('Opcion no valida: (s/n)')

    if choice == 's':
        print('Comenzando proceso...\n\tAguarde...\n\n')
        cliente.crear_pedido()
    else:
        print('Adios...\n\tHasta la proxima...\n\n')

def confirmar_pedido():
    choice = "wrong"
    while choice not in ['s', 'n']:
        choice = input('\n¿Confirmamos pedido? \n (s/n): ')
        if choice not in ['s', 'n']:
            print('Opcion no valida: (s/n)')

    if choice == 's':
        print('\n\t...¡Pedido confirmado!')
        cliente.cargar_pedido(name, Cliente.origen, Cliente.cantidad, tel, dir)
        cliente.baja_stock(Cliente.origen, Cliente.cantidad)

        smtp_object.sendmail(from_address, to_address, msg)
        #monto_final += cliente.monto
    else:
        print('Repitiendo proceso...\n\tAguarde...\n\n')
        comenzar_orden()
        confirmar_pedido()

def agregar_mas():
    choice = "wrong"
    while choice not in ['s', 'n']:
        choice = input('\n¿Queres agregar algo mas? \n (s/n): ')
        if choice not in ['s', 'n']:
            print('Opcion no valida')

    if choice == 's':
        print('\tCreando nueva compra...\n\tAguarde...\n\n')
        comenzar_orden()
        confirmar_pedido()
    else:
        print('¡Ok!... Nada mas por hoy.')

def cerrar_carrito():
    choice = "wrong"

    while choice not in ['s', 'n']:
        choice = input('\n¿Finalizar carrito? \n (s/n): ')
        if choice not in ['s', 'n']:
            print('Opcion no valida')

    if choice == 's':
        #print(f'Monto final: \t\tx ${monto_final}')
        print('___ __ ___ _____ __ ___ _____ ___   \n')
        return False
    else:
        return True

cliente = Cliente(name, tel, dir)

import smtplib
smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
#465 o nada
smtp_object.ehlo()
smtp_object.starttls()

email = 'kissaten.bot@gmail.com'
password = 'chatbot11'
app_password = 'bawpknxltorjepqi'
smtp_object.login(email, app_password)

from_address = email
to_address = email
subject = "Nueva compra - chat_bot"
message = "Cliente {} ah realizado nueva compra".format(cliente.name)
msg = "Subject: " + subject + "\n" + message


compra_iniciada = True
while compra_iniciada:
    comenzar_orden()
    confirmar_pedido()
    #monto_final += cliente.monto
    agregar_mas()
    compra_iniciada = cerrar_carrito()


print('En seguida le enviaran link de pago y estimacion de llegada del pedido.')
print('\n¡Muchas gracias por su visita virtual!\nLo esperamos nuevamente')
print('\n\t~ Saludos del Kissaten Cafe Team ~')
print('\t\t~ ᴄᴀғᴇ ᴅᴇ ᴇsᴘᴇᴄɪᴀʟɪᴅᴀᴅ ~')


'''
choice = "wrong"
while choice not in ['s', 'n']:
    choice = input('\n¿Comoenzamos su orden? \n(s/n): ')
    if choice not in ['s', 'n']:
        print('Opcion no valida: (s/n)')

if choice == 's':
    print('Repitiendo proceso...\n\tAguarde...\n\n')
    cliente.crear_pedido()
else:
    print('Repitiendo proceso...\n\tAguarde...\n\n')
    cliente.crear_pedido()
'''
        #cliente.crear_pedido()
'''
choice = "wrong"
while choice not in ['s', 'n']:
    choice = input('\n¿Confirmamos pedido? \n(s/n): ')
    if choice not in ['s', 'n']:
        print('Opcion no valida: (s/n)')

if choice == 's':
    print('\n\t...¡Pedido confirmado!')
    cliente.cargar_pedido(name, Cliente.origen, Cliente.cantidad, tel, dir)
else:
    print('Repitiendo proceso...\n\tAguarde...\n\n')
    cliente.crear_pedido()
'''
#cliente.cargar_pedido(name, Cliente.origen, Cliente.cantidad, tel, dir)




