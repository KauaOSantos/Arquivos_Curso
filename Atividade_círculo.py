class Circulo:


    def __init__(self, raio):
        self.raio = raio
    
    def calculo_area(self):
        area = 3.14159 * (self.raio ** 2)  
        return area
    
    def calculo_perimetro(self):
        perimetro = 2 * 3.14159 * self.raio  
        return perimetro

raio = float(input("Digite o raio do círculo: "))
circulo = Circulo(raio)
area = circulo.calculo_area()
perimetro = circulo.calculo_perimetro()
print(f"A área do círculo com raio {raio} é {area:.2f}")
print(f"O perímetro do círculo com raio {raio} é {perimetro:.2f}")