class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @property
    def get_name(self):
        return self.name
 
    @property
    def get_age(self):
        return self.age

obj=Student("hari",56)
print(obj.get_name)
print(obj.get_age)