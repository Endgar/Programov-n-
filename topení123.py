import time


class centralheating:

    OutsideTemperature = 10
    centralHeating = False

    def __init__(self, name, capacity, begin_temp, start_heating, stop_heating):
        self.name = name
        self.capacity = capacity
        self.begin_temp = begin_temp
        self.start_heating = start_heating
        self.stop_heating = stop_heating
        
        self.heating = True
        self.actual_temp = begin_temp
        self.begin_time = time.time()
        print("Topení {self.name} je ZAPNUTO a má {self.actual_temp} °C")

    @staticmethod
    def boolToSwitch(toSwitch):
        if toSwitch:
            return "Zapnuto"
        else: 
            return "Vypnuto"
    @classmethod
    def setOutsideTemperature(cls, temperature):
        cls.OutsideTemperature = temperature

    @classmethod
    def startCentralHeating(cls):
        cls.centralHeating = True

    @classmethod
    def stopCentralHeating(cls):
        cls.centralHeating = False

    def regulateHeating(self):
        myTime = time.time() - self.begin_time
        if self.heating:
            self.actual_temp = self.begin_temp + myTime * self.capacity
        else:
            self.actual_temp = self.begin_temp - myTime * self.capacity
        
        print("Topení {self.name} je {self.boolToSwitch (self.heating)} a má {self.actual_temp} °C")

    centralHeating.setOutsideTemperature(12)
    centralHeating.startCentralHeating()
    
heating1 = centralheating("obývák", 0.7, 16, 19, 23) 

while True:
    heating1.regulateHeating()
    time.sleep(1)