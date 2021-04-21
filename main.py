import csv
import time
import os
from claseFechaHora import FechaHora

#Funcion test para verificar fechas erroneas y funciones de modificacion del reloj
def test():
    #Evaluo distintas fechas mal ingresadas
    print('TEST DE LECTURA DE FECHAS Y HORAS.')
    nombreArch = 'fechaHoraTest.csv'
    time.sleep(0.5)
    print('Lectura archivo: {}'.format(nombreArch))
    archivo = open(nombreArch)
    reader = csv.reader(archivo,delimiter=',')
    bandera = True
    for fila in reader:
        if bandera:
            bandera = False
        else:
            time.sleep(0.5)
            dia = int(fila[0])
            mes = int(fila[1])
            anio = int(fila[2])
            hora = int(fila[3])
            min = int(fila[4])
            seg = int(fila[5])          
            r = FechaHora(dia,mes,anio,hora,min,seg)
    archivo.close()
    print('Test finalizado.')

    #Evaluo modificar la hora con valores erroneos
    input('Presione ENTER para iniciar el test de modificacion de hora ')
    print('TEST DE MODIFICACION DE HORAS.')
    nombreArch = 'horasTest.csv'
    print('Lectura archivo: {}'.format(nombreArch))
    archivo = open(nombreArch)
    reader = csv.reader(archivo,delimiter=',')
    r = FechaHora(10,10,2020,1,12,25)
    bandera = True
    for fila in reader:
        if bandera:
            bandera = False
        else:
            time.sleep(0.5)
            hora = int(fila[0])
            min = int(fila[1])
            seg = int(fila[2])       
            r.Mostrar()
            r.PonerEnHora(hora,min,seg)
            r.Mostrar()
            
    archivo.close()
    print('Test finalizado.')
    input('Presione ENTER para iniciar el test de incremento de hora...')
    print('TEST DE INCREMENTO DE HORAS.')
    r = FechaHora(31,12,2021,23,59,59) 
    r.Mostrar()
    r.AdelantarHora(0,0,1) #Adelanto 1 segundo 
    r.Mostrar() #Debe mostrar que se paso al 1 de enero de 2022   
    print('Test finalizado')
    input('Presione ENTER para continuar...')
    os.system('cls')

 
if __name__ == '__main__':
    correrTest = input('Desea ejecutar la funcion test? [S/N]: ')
    if correrTest.lower() == 's':
        test()
    
    #Enunciado ejercicio
    print('EJERCICIO 4')
    d=int(input("Ingrese Dia: "))
    mes=int(input("Ingrese Mes: "))
    a=int(input("Ingrese Año: "))
    h=int(input("Ingrese Hora: "))
    m=int(input("Ingrese Minutos: "))
    s=int(input("Ingrese Segundos: "))
    r = FechaHora() #  inicilizar día, mes, año con 1/1/2020, y hora, minutos y segundos con 0h, 0m, 0s.
    r1 = FechaHora(d,mes,a); # inicializar con 0h 0m 0s
    r2= FechaHora(d,mes,a,h, m, s)
    r.Mostrar()
    r1.Mostrar()
    r2.Mostrar()
    input('Presione ENTER para continuar...')
    r.PonerEnHora(5) # solamente la hora
    r.Mostrar()
    input('Presione ENTER para continuar...')
    r2.PonerEnHora(13,30) #hora y minutos
    r2.Mostrar()
    input('Presione ENTER para continuar...')
    r.PonerEnHora(14, 30, 25) #hora, minutos y segundos
    r.Mostrar()
    input('Presione ENTER para continuar...')
    r.AdelantarHora(3) #sumar 3 horas a la hora actual
    r.Mostrar()
    input('Presione ENTER para continuar...')
    r1.AdelantarHora(1,15) #sumar 1 hora y 15 minutos a la hora actual
    r1.Mostrar()
    input('Presione ENTER para continuar...')    
    
