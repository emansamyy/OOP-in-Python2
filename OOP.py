
class Employee:

    #class attribute
    alias = "Keyboard Player"

    # first arguemnt is always self, it refers to the instancw
    def __init__(self, name, age, level, salary):
        # instance attributes (different from class attribute, class attributes are the same for every instance)
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
  #instance method, now we can access instance attributes
    def work(self):
        print(f"{self.name} is working.. ")

  #this double underscore method is built to be able to print objects
    def __str__(self):
        information = f"name= {self.name} , age = {self.age} , level = {self.level}"
        return information

    #equal method
    #by default it compares the memory address, therefore you have to implement it
    def __eq__(self,other):
        return self.name ==other.name and self.age == other.age
    #this is now working on the class but not instances because we did not use self parameter
   
    #staticmethod is a decorator that makes it work without using self parameter cuz it means that it is not tied to a specific instance
    @staticmethod
    def entry_salary(age):
        if age<25:
            return 5000
        if age<30:
            return 7000
        return 9000
# We use the base class to show that this class is a child class to the parent(Employee)
class Software_Engineer(Employee):
    def __init__(self,name,age, level, salary, Tech):
        #to avoid re-initiallizing/retyping same attributes, we call the initiallizer of the parent class
        super().__init__(name,age,level,salary)
        self.Tech = Tech
        
#NOW we extend this child's functionality
#this is only specific to a software engineer
    def debug(self):
        print(f"{self.name} is debugging ...")

 # Overriding the work method inside the child
    def work(self):
        #this is overrding not extending
        print(f"{self.name} is coding.. ")


# We use the base class to show that this class is a child class to the parent(Employee)
class Designer(Employee):
    def draw(self):
        print(f"{self.name} is drawing ...")
     # Overriding the work method inside the child
    def work(self):
        #this is overrding not extending
        print(f"{self.name} is designing.. ")

se1 = Software_Engineer("Lisa" , "27" , "Senior" , "7000", "PHP")
se2 = Software_Engineer("Andrew" , "20" , "Junior" , "5000" , "python")
se3 = Software_Engineer("Andrew" , "20" , "Junior" , "5000", "Cloud")

############ Testing Out Outputs ##############

#print(se1==se2)
#print(se2==se3)
#print(se1.entry_salary(27))
#print(Software_Engineer.entry_salary(24))
#print(se1.name + " " +se1.age)

#d = Designer("Andrew" , "20" , "Junior" , "5000")
#print(d.name + " " +d.age)
#se1.work()
#d.work()
#se1.debug()
#d.draw()



#Polymorphism (in greek it means many shapes) It is closely related to inheritance, it gives us a way to use a class exactly like its parent
#but still each child class keeps its own methods as they are

#we do not care what the actual child class is
employees = [Software_Engineer("Lisa" , "27" , "Senior" , "6000", "PHP"), Software_Engineer("Andrew" , "20" , "Junior" , "9000" , "python")
, Designer("Andrew" , "20" , "Junior" , "5000")]

#this is the concept of polymorphism
def motivate_employees(employees):
    for employee in employees:
        employee.work()

motivate_employees(employees)

