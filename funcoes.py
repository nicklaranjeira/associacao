from classes import *
motor1 = Motor(1.5,"Toyota")
motor2 = Motor(4.4,"Honda")
motor3 = Motor(1.8, "Mercedes")

roda1 = Roda(14, "Nissan")
roda2 = Roda(12, "GT-7")

carros = [] 

carro1 = Carro((motor1), (roda1))
carro2 = Carro((motor1), (roda2))
carro3 = Carro((motor2), (roda1))
carro4 = Carro((motor2), (roda2))
carro5 = Carro((motor3),(roda1))
carro6 = Carro((motor3), (roda2))

carros.append(carro1)
carros.append(carro2)
carros.append(carro3)
carros.append(carro4)
carros.append(carro5)
carros.append(carro6)



def Mostrar_carro(carros):
    for carro in carros: 
        print("Dados motor:")
        print(f'{carro.getMotor_carro().getMarca()} - {carro.getMotor_carro().getPotencia()}')
        print("Dados roda:")
        print(f"{carro.getRodas_carro().getTamanhoroda()} - {carro.getRodas_carro().getMarcaroda()}")
        print("\n--------------------------------------------")