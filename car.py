class Vehicle(object):
    def __init__(self, wheels, weight):
        self.setWheels(wheels)
        self.setWeight(weight)
    def setWheels(self, wheels):
        if type(wheels) != int:
            raise Exception('车轮个数必须是整数')
        self.__wheels=wheels
    def setWeight(self, weight):
        if type(weight) != int:
            raise Exception('车轮个数必须是整数')
        self.__wight=weight
    def display(self):
        print('汽车车轮数：%d'%self.__wheels, '汽车车重：%d'%self.__wight)
class Car(Vehicle):
    def __init__(self, wheels, weight, passenger_load=4):
        super(Car, self).__init__(wheels, weight)
        self.setPassenger_load(passenger_load)
    def setPassenger_load(self, passenger_load):
        if passenger_load not in range(1,7):
            raise Exception('小车可载人数不超过6人')
        self.__passenger_load=passenger_load
    def display(self):
        super(Car,self).display()
        print('小车载客人数为：%d'%self.__passenger_load)
class Truck(Vehicle):
    def __init__(self, wheels, weight, passenger_load, payload):
        super(Truck, self).__init__(wheels, weight)
        self.setPassenger_load(passenger_load)
        self.setPayload(payload)
    def setPassenger_load(self, passenger_load):
        if passenger_load not in range(1, 20):
            raise Exception('卡车可载人数不超过20人')
        self.__passenger_load=passenger_load
    def setPayload(self, payload):
        if type(payload) != int:
            raise Exception('卡车载重为整数')
        self.__payload=payload
    def display(self):
        super(Truck, self).display()
        print('卡车载客人数：%d'%self.__passenger_load,'卡车载重量：%d'%self.__payload)
if __name__== '__main__':
    qiche = Vehicle(4, 100)
    qiche.display()
    print('='*20)
    car = Car(4, 120, 5)
    car.display()
    print('='*20)
    truck = Truck(12, 400, 2, 500)
    truck.display()