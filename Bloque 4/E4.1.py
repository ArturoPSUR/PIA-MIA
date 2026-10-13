"""E4.1 Clase CuentaBancaria con saldo privado, ingresar, retirar(valida saldo suficiente)
 y propiedad saldo de solo lectura."""

class CuentaBancaria:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo

    @property
    def saldo(self):
        return self.saldo
    
    def ingresar(self,cantidad):
        self.saldo= self.saldo+cantidad

    def retirar(self,cantidad):
        if cantidad<=self.saldo:
            self.saldo= self.saldo-cantidad
        else:
            print("No se puede retirar una cantidad mayor al saldo actual")

CuentaBancaria1= CuentaBancaria("titular")
print(CuentaBancaria.saldo)            