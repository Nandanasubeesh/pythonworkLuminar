class Parent:
    phone="samsunga57"
    vehicle="passionpro"

    def mobile(self):
        print(self.phone)
    def bike(self):
        print(self.vehicle)

class child(Parent):
    pass
obj=child()
obj.mobile()
obj.bike()