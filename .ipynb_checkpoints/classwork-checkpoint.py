class vehicle:

    def __init__(self,name):
        self.name = name
        
    def car(self):
        print("New ride with insane feats arriving next week!")
        return "Sports car"
    
class Brand(vehicle):

    def Performance(self):
        self.car()
        print(f"Name of car brand is {self.name}")
        return "can reach up to 350kmph"
    
speed= Brand("BMW!")

print(speed.Performance())
print(speed.car())
print(" ")

class Employee:

    def __init__(self,name,id,department,monthly_salary):
        self.name=name
        self.id=id
        self.department=department
        self.monthly_salary=monthly_salary

    def l1(self):
        print(f"Name of employee: {self.name}")

    def l2(self):
        print(f"ID of employee: {self.id}")

    def l3(self):
        print(f"Employee department: {self.department}")

    def l4(self):
        print(f"Monthly salary: {self.monthly_salary}")

    def yearly_salary(self):
        print("yearly salary: ",self.monthly_salary * 12)

fil= Employee("idris",2102,"UI/UX design",15000)

print(fil.l1(),
      fil.l2(),
      fil.l3(),
      fil.l4(),
      fil.yearly_salary())