class Employee:
    def __init__(self, name='Неизвестно', id='00000', **kwargs):
        self.name = name
        self.id = id

    def get_info(self):
        return f'Имя: {self.name}, id номер: {self.id}'


class Manager(Employee):
    def __init__(self, name='Неизвестно', id='00000', department='Неизвестно', **kwargs):
        super().__init__(name, id, **kwargs)
        self.department = department
        
    def manage_project(self):
        return f'Отдел {self.department} занят проектом'

    def get_info(self):
        return f'{super().get_info()}, Отдел: {self.department}'


class Technician(Employee):
    def __init__(self, name='Неизвестно', id='00000', specialization='Неизвестно', **kwargs):
        super().__init__(name, id, **kwargs)
        self.specialization = specialization

    def perform_maintenance(self):
        return f'{self.specialization} занят тех.обслуживанием'

    def get_info(self):
        return f'{super().get_info()}, Специальность: {self.specialization}'


class TechManager(Manager, Technician):
    def __init__(self, name='Неизвестно', id='00000', department='Неизвестно', specialization='Неизвестно'):
        super().__init__(name=name, id=id, department=department, specialization=specialization)
        self.employees = []

    def manage_maintenance(self):
        return f'{self.specialization} из отдела {self.department} занят тех.управлением'
    
    def add_employee(self, employee):
        self.employees.append(employee)
    

    def get_team_info(self):
        for i in self.employees:
            print(f'{i.get_info()}')
            

employee = TechManager()
employee1 = Employee('Алкаш', '11111')
employee2 = Manager('Валера', '22222', 'Маркейтинг')
print(employee2.manage_project())
employee3 = Technician('Абоба', '33333', 'Электрик')
print(employee3.perform_maintenance())
employee4 = TechManager('Амогус', '44444', 'Бизнес', 'Сантехник')
print(employee4.manage_maintenance())
employee.add_employee(employee1)
employee.add_employee(employee2)
employee.add_employee(employee3)
employee.add_employee(employee4)
employee.add_employee(Employee('БлекАнгус', '55555'))
print(employee.get_team_info())