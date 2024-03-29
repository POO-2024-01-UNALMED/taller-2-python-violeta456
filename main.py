class Asiento:
    def __init__(self, color, precio, registro):
        self.color=color
        self.precio=precio
        self.registro=registro
    
    def cambiarColor(self, color):
        if color=="rojo" or color=="verde" or color=="amarillo" or color=="negro" or color=="blanco":
            self.color=color

class Auto:
    cantidadCreados=0

    def __init__(self,modelo,precio,asientos,marca, motor, registro):
        self.modelo=modelo 
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro

    def cantidadAsientos(self):
        asientos=self.asientos
        cantidad=0
        for elemento in asientos:
            if isinstance(elemento, Asiento)==True:
                cantidad+=1
        return cantidad
    
    def verificarIntegridad(self):
        a=self.registro
        b=self.motor.registro
        for elemento in range(len(self.asientos)):
            if isinstance(self.asientos[elemento], Asiento)==True:
                c=self.asientos[elemento].registro
                if a!=b or a!=c or c!=b:
                    return "Las piezas no son originales"
        return "Auto original"
        

class Motor:
    def __init__(self, numeroCilindros,tipo,registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro
    
    def cambiarRegistro(self,registro):
        self.registro=registro
    
    def asignarTipo(self,tipo):
        if tipo=="electrico" or tipo=="gasolina":
            self.tipo=tipo





