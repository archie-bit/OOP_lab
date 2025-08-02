class Person:
    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate =healthRate
    
    def sleep(self, hrs):
        if(hrs>7):
            self.mood = "Lazy"
        elif(hrs<7):
            self.mood = "Tired"
        elif(hrs==7):
            self.mood = "Happy"
        
        print(f"{self.name} is {self.mood}")    


    def eating(self, meals):
        if(meals == 3):
            self.healthRate=100
        elif(meals == 2):
            self.healthRate=75
        elif(meals == 1):
            self.healthRate=50
        print(f"{self.name}'s health is {self.healthRate}")    

    def buy(self, items):
        if(items>0 and isinstance(items, int)):
            self.money = self.money - (items*10)
        elif(items==0):
            print(f"{self.name} didn't buy anything")
        else:
            print("Please enter a valid number of items")


class Car:
    maxVelo=200
    maxFuel=100
    def __init__(self, fuelRate, velocity):
        self.fuelRate = (fuelRate 
                         if fuelRate <= Car.maxFuel
                         else Car.maxFuel)
        self.velocity = (velocity
                         if velocity <= Car.maxVelo
                         else Car.maxVelo)

    
    def run(self, velocity, distance):
        self.velocity = velocity
        dest_to_fuel = distance*.5
        remainingDest=0

        if dest_to_fuel > self.fuelRate:
            remainingDest = (self.fuelRate * 2)-distance
            self.fuelRate = 0
        else: 
            self.fuelRate -= dest_to_fuel

        self.stop(self.fuelRate, remainingDest 
                                 if remainingDest
                                 else 0)

    def stop(self, fuelRate,  remainingDest=0):
        self.velocity = 0
        if fuelRate == 0 and remainingDest!=0:
            print(f"""
                  Car stopped to due no fuel
                  Remaining to destination: {remainingDest}""")




class Employee(Person): 
    def __init__(self,
                 name,
                 money,
                 mood,
                 healthRate,
                 id,
                 car,
                 email,
                 salary,
                 distanceToWork,
                 score= 100):
        super.__init__(name, money, mood, healthRate)
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork
        self.score = score

    def work(self, hours):
        if(hours == 8):
            self.mood = "Happy"
            print(f"{self.name} is {self.mood}")
        elif(hours > 8):
            self.mood = "Tired"
            print(f"{self.name} is {self.mood}")
        if(hours < 8):
            self.mood = "Lazy"
            print(f"{self.name} is {self.mood}")
    
    def drive(self, distance, velocity):
        self.car.run(velocity, distance)

    def refuel(self, gasAmount = 100):
        self.money -= gasAmount*19 #بنزين 92
        self.car.fuelRate +=  gasAmount
    
        

class Office:
    employeesNum = {"total": 0}
    def __init__(self, name, employees=[]):
        self.name = name
        self.employees= employees
        Office.employeesNum[name] = len(employees)
        Office.employeesNum["total"] += len(employees)

    @classmethod
    def change_emps_num(officeName, num):
        Office.employeesNum[officeName] -= num  
        Office.employeesNum["total"] -= num


        
    def hire(self, Employee):
        self.employees.append(Employee)
        Office.employeesNum[self.name] += 1 
        Office.employeesNum["total"] += 1
        
    def fire(self, empId):
        self.employees = [e for e in self.employees if e.id != empId]
        print(f"Fired Employee {empId} from {self.name}")
        Office.employeesNum[self.name] -= 1 
        Office.employeesNum["total"] -= 1

    def get_all_emp(self):
        return self.employees
    
    def get_employee(self, empId):
        for emp in self.employees:
            if emp.id == empId:
                return emp
        return None
    
    
    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        if velocity == 0:
            return True

        travel_time = distance/velocity
        arrival_time = moveHour + travel_time

        is_late = arrival_time > targetHour


        return is_late


    def check_lateness(self, empId, moveHour, distance, velocity):
        emp = self.get_employee(empId)
        if not emp:
            return None
        is_late = Office.calculate_lateness(self.targetHour,
                                             moveHour,
                                             distance,
                                             velocity)
        if is_late:
            emp.score -=10
            return f"{emp.name} is late"
        else:
            emp.score +=10
            return f"{emp.name} on time"
        

        


