class car:

    # constructor
    def __init__(self,model,brand):
        self.model= model
        self.brand = brand
    

    # Method
    def details_Car(self):
        print(f"The Model of Car: {self.model} And Brand of car:{self.brand}")


    # creating object
myCar=car("Toytata","Bmw")
myCar.details_Car()