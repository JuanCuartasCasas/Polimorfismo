from domain.Animal import Animal

class Aereos(Animal):
    def __init__(self, especie,dieta, edad,apodo):
        super().__init__(especie,dieta, edad)
        self.apodo = apodo


    def comunicarse(self):
        #super().comunicarse()
        print(f"El {self.especie},tambien llamado {self.apodo} esta diciendo hola")
        
    def caminar(self):
        #super().moverse()
        print(f"{self.apodo} se traslada por aletas ")
    
    def comer(self):
        self._cambiardieta(self)
        print(f"El aereo es {self.dieta},por lo que digiere alimentos como pescados,vegetales,carne ")



