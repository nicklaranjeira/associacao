class Motor:
    def __init__(self, potencia, marca):
        self.__potencia = potencia
        self.__marca = marca

    # GETS
    def getPotencia(self):
        return self.__potencia
    
    def getMarca(self):
        return self.__marca
class Roda:
    def __init__(self, tamanho_roda, marca_roda):
        self.__tamanho_roda = tamanho_roda
        self.__marca_roda = marca_roda

    # GETS
    def getTamanhoroda(self):
        return self.__tamanho_roda
    def getMarcaroda(self):
        return self.__marca_roda
    
class Carro:
    def __init__(self, motor, roda):
        self.motor = motor
        self.roda = roda

    # GETS N' SETS


    def setMotor_carro(self, motor):
        self.motor = motor
        return self.motor
    def setRodas_carro(self,roda):
        self.roda = roda
        return self.roda 
    

    def getMotor_carro(self):
        return self.motor
    
    def getRodas_carro(self):
        return self.roda