class Dad:
    basketball = 1

class Son(Dad):
    dance = 1
    def isdance(self):
        return f"yes I can dance{self.dance()}number of time"

class Grandson(Dad):
    dance =6

    def isdance(self):
        return f"jackson yeah!"f"yes I dance veru awesomely {self.dance} no of times"

darry = Dad()
larry = Son()
harry = Grandson()

print(harry.isdance())