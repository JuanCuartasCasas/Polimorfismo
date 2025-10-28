class Animal:
    def __init__(self,edad,dieta):
        self._especie = self._agregar_especie()
        self.edad = edad
        self.dieta = dieta

    
    @property
    def especie(self):
        return self._especie
    

    def comunicarse(self):
        #print("El animal se está comunicando")
        pass

    def moverse(self):
        print("Animal Moviendose...")



#Protegido
    def reproducirse(self):
        print("El animal se reproduce:")
   
    def alimentarse(self):
        print("de los siguientes alimentos, el animal digiere :")
        print("1) Carne")
        print("2) Vegetale")
        print("3) Ambos")
        diet = int(input("Su animal que come:"))

        while not(diet == {1,3}):
            print("Dieta desconocida,por favor ingrese nuevamente")
            diet = int(input("Su animal que come:"))
        self._asignar_dieta(diet)
        return self._asignar_dieta(diet)
    
    def _asignar_dieta(self,comida):
        if comida == 1:
            self.dieta = "Carnivoro"
            return self.dieta

        elif comida == 2:
            self.dieta = "Vegetariano"
            return self.dieta
        
        elif comida == 3:
            self.dieta = "Omnivoro"
            return self.dieta
        else:
            var = input("Que dieta tiene su animal:")
            self.dieta = var
            return self.dieta
        
        
    def _cambiardieta(self):
        self.alimentarse(self)
        print(f"el animal es {self.alimentarse()} ")
        
    def _agregar_especie(self,especie):
      self._especie = especie 
      print(f"el animal es de especie {especie}") 