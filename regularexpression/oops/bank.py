class Bank:
    bank_name:str
    acno:str
    person_name:str
    ac_type:str
    balance:int

    def create(self,b_name,acno,p_name,ac_type,bal):
        self.bank_name=b_name
        self.acno=acno
        self.person_name=p_name
        self.ac_type=ac_type
        self.balance=bal

obj1=Bank()
obj1.create("sbi","19076","vijay","savings",4000)

obj2=Bank()
obj2.create("sbi","12345","rahul","savings",50000)
