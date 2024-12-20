class Circle():
    #описание
    def __init__(self, radius):
        #свойства
        self.radius = radius



    def get_radius(self):
        print("Радиус: " + str(self.radius))
    
    
    def set_radius(self,new_radius):
        self.radius = new_radius


R1=Circle(12)


R1.get_radius()
R1.set_radius(34567)
R1.get_radius()