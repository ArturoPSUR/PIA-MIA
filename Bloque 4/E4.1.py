"""E4.1 Clase CuentaBancaria con saldo privado, ingresar, retirar(valida saldo suficiente)
 y propiedad saldo de solo lectura."""

class CuentaBancaria:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo
    
    def ingresar(self,cantidad):
        self._saldo= self._saldo+cantidad

    def retirar(self,cantidad):
        if cantidad<=self._saldo:
            self._saldo= self._saldo-cantidad
        else:
            print("No se puede retirar una cantidad mayor al saldo actual")

CuentaBancaria1= CuentaBancaria("titular")
print(CuentaBancaria1.saldo)            