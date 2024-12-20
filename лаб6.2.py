class Vehicle():
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"Марка: {self.make} Модель: {self.model}"
    
class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type
    
    def get_info(self):
        return f'{super().get_info()} Тип топлива: {self.fuel_type}'
        
V1=Vehicle("KAWASAKI", "ELIMINATOR-400")
V2=Car("BMW", "X7 M60i xDrive", "Бензин")
print(V1.get_info())
print(V2.get_info())