class Dress:
    data=[
        
        {"id":1,"name":"churidar","material":"cotton","price":1000},
        {"id":2,"name":"pallazo","material":"semi cotton","price":500},
        {"id":3,"name":"kurta","material":"cotton","price":800},
        {"id":4,"name":"jeans","material":"baniyan","price":1599},
        {"id":5,"name":"t-shirts","material":"baniyan","price":400},

    ]
    def get(self,*args,**kwargs):
        return self.data

    def retrieve(self,*args,**kwargs):
        id=kwargs.get("id")
        record=[d for d in self.data if d.get("id")==id]
        return record

    def create(self,*args,**kwargs):
        self.data.append(kwargs)

    def destroy(self,*args,**kwargs):
        id=kwargs.get("id")
        obj=[d for d in self.data if d.get("id")==id].pop()
        self.data.remove(obj)

    


obj=Dress()
# 1) print(obj.get())
# 2)print(obj.retrieve(id=4))
# 3)obj.create(id=6,name="frocks",material="net",price=1500)
# 3)print(obj.get())

# 4) obj.destroy(id=5)
# 4)print(obj.get())