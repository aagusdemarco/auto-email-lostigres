import funciones as func
import pandas as pd

# Iniciamos sesión en el email del club

ruta_email = 'los-tigres\credenciales.txt'
mail, contrasenia = func.usuario_constrasenia(ruta_email)

# Creamos la funcion principal

def main():

    # Elegimos como obtener los datos 
    
    while True: 
        print('Bienvenido al sistema de gestión de envío de emails.\nPuede elegir la base de datos a utilizar mediante los siguientes comandos:')
        opcion = int(input('Presione 1 para la base proporcionada por la aplicación.\nPresione 2 para usar una base de datos propia.\nPresione 3 para salir: '))
        
        # Utilizando la base proporcionada por nosotros
        if opcion == 1:
            path = 'los-tigres\club-de-futbol-los-tigres(base-datos).xlsx'
            datos = pd.read_excel(path)
            datos_df = pd.DataFrame(datos)
            datos_df = datos_df.drop('Marca temporal', axis=1)

            lista_socios = []
            for index, fila in datos_df.iterrows():
                socio = {'nombre': fila['Nombre'], 'email': fila['Email'], 'pedido': fila['Request']}
                lista_socios.append(socio)

        # Utilizando su propia base de datos
        elif opcion == 2:
            path = str(input('Ingrese la dirección de su base de datos: '))
            datos = pd.read_excel(path)
            datos_df = pd.DataFrame(datos)

            lista_socios = []
            for index, fila in datos_df.iterrows():
                socio = {'nombre': fila['Nombre'], 'email': fila['Email'], 'pedido': fila['Request']}
                lista_socios.append(socio)

        # Opción para salir del programa
        elif opcion == 3:
            print('El programa se cerrará')
            break

        # Diccionario con mensajes para enviar por email

        mensajes = {
            'bienvenida': 
            {
                'asunto': 'Bienvenida',
                'mensaje': f'¡Querido/a {socio["nombre"]}!\n\nEn nombre de todos nosotros en el Club de Futbol Los Tigres, te damos una cálida bienvenida. Estamos emocionados de tenerte como nuevo socio. Tu decisión de unirte a nuestra familia futbolística significa mucho para nosotros. Esperamos que tu experiencia sea llena de emociones, camaradería y, por supuesto, muchos goles. Siéntete libre de explorar todo lo que nuestro club tiene para ofrecer\n¡Vamos Tigres!'
            },
            'fixture': 
            {
                'asunto': 'Próximos Partidos',
                'mensaje': f'¡Hola {socio["nombre"]}!\n\nNos complace informarte sobre los emocionantes partidos que el Club de Futbol Los Tigres tiene programados para los próximos meses. Desde enfrentamientos en nuestra casa hasta épicas batallas en campos rivales, cada partido es una oportunidad para fortalecer nuestro lazo como comunidad. Esperamos verte en las gradas, alentando con pasión y celebrando cada victoria. ¡Prepárate para una temporada llena de emoción y adrenalina!\n¡Vamos Tigres!'
            },
            'promociones': 
            {
                'asunto': 'Promociones',
                'mensaje': f'Estimado/a {socio["nombre"]},\n\nAgradecemos tu lealtad y apoyo continuo al Club de Futbol Los Tigres. Como muestra de nuestro agradecimiento, hemos preparado promociones exclusivas para ti. Desde descuentos en mercancía del club hasta ofertas especiales en entradas, queremos asegurarnos de que tu experiencia como socio sea aún más gratificante. ¡No te pierdas estas increíbles oportunidades y continúa siendo parte de nuestra historia!\n¡Vamos Tigres!'
            },
            'eventos': 
            {
                'asunto': 'Eventos',
                'mensaje': f'¡Hola {socio["nombre"]}!\n\nTe extendemos una cordial invitación a los eventos especiales que el Club de Futbol Los Tigres ha organizado exclusivamente para nuestros socios. Desde encuentros con jugadores hasta sesiones de entrenamiento exclusivas, estamos emocionados de ofrecerte experiencias únicas que van más allá del campo de juego. Esperamos que aproveches al máximo tu membresía participando en estas oportunidades de conexión y celebración. ¡Esperamos verte pronto!\n¡Vamos Tigres!'
            }
        }

        # Método de envío de emails

        for socio in lista_socios:
                if socio['pedido'] == 'Asociarse':
                        func.enviar_mail(mail, contrasenia, mensajes['bienvenida']['asunto'], mensajes['bienvenida']['mensaje'], socio['email'])
                elif socio['pedido'] == 'Fixture':
                        func.enviar_mail(mail, contrasenia, mensajes['fixture']['asunto'], mensajes['fixture']['mensaje'], socio['email'])
                elif socio['pedido'] == 'Promociones':
                        func.enviar_mail(mail, contrasenia, mensajes['promociones']['asunto'], mensajes['promociones']['mensaje'], socio['email'])
                elif socio['pedido'] == 'Eventos':
                        func.enviar_mail(mail, contrasenia, mensajes['eventos']['asunto'], mensajes['eventos']['mensaje'], socio['email'])

if __name__ == '__main__':
    main()