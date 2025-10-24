class Animal:
    def __init__(self,edad,dieta):
        self._especie = self.agregar_especie()
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
    def _reproducirse(self):
        print("El animal se reproduce:")
    def alimentarse(self):
        print("de los siguientes alimentos, el animal digiere :")
        print("1) Carne")
        print("2) Vegetale")
        print("3) Ambos")
        #diet = input("Su animal que come:")
        int(diet)

        while not(diet == "a" or diet== "b" or diet == "c"):
            print("Dieta desconocida,por favor ingrese nuevamente")
            diet = input("Su animal que come:")
        self.dieta = self._asignar_dieta(diet)
        return diet
    
    def _asignar_dieta(self,comida):
        if comida.lower() == "carne":
            self.dieta = "Carnivoro"

        elif comida.lower() == "vegetales":
            self.dieta = "Vegetariano"
        
        else:
            var = input("Que dieta tiene su animal:")
            self.dieta = var
        
    def _cambiardieta(self):
        self.alimentarse(self)
        print(f"el animal cóme {self._evaluardieta()} ")
        
    def _agregar_especie(self,especie):
      self._especie = especie 
      print(f"el animal es de especie {especie}") 