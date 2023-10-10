class Bike:
    def start(self):
        print("kicker start")
    def breaking(self):
        print("drum break")
class HeroHondaSplender(Bike):
    def start(self):
        print("self start")
    def breaking(self):
        print("abs breaking")

hobj=HeroHondaSplender()

hobj.start()
hobj.breaking()