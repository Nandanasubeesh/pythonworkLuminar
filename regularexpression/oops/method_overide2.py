class Parent:
    vehicles=["Passion pro","swift"]

    def Properties(self):
        return self.vehicles

class Child(Parent):
    def Properties(self):
        self.veh=super().Properties()
        self.veh.append("hunter")
        return self.veh 

ch=Child()
print(ch.Properties())
