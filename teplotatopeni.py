import time
import threading

class Heating:
    temperatureToHeat = 20
    temperatureToStop = 22

    def __init__(self, capacity, startingTemperature, outsideTemperature):
        self.heating = False
        self.capacity = capacity
        self.temperature = startingTemperature
        self.outsideTemperature = outsideTemperature

    def getTemperature(self):
        return self.temperature

    def setTemperatureToHeat(self, temperature):
        self.temperatureToHeat = temperature

    def setTemperatureToStop(self, temperature):
        self.temperatureToStop = temperature

    def startHeating(self):
        self.heating = True

    def stopHeating(self):
        self.heating = False

    def setOutsideTemperature(self, temperature):
        self.outsideTemperature = temperature

    def simulate(self):
        while True:
            if self.heating and self.temperature < self.temperatureToStop:
                self.temperature += self.capacity
            elif not self.heating and self.temperature > self.temperatureToHeat:
                self.temperature -= self.capacity
            time.sleep(1)

# create three heating objects in different rooms
heating1 = Heating(0.8, 18, 10)
heating2 = Heating(1, 17, 8)
heating3 = Heating(0.7, 20, 15)

# start the simulation for each heating object in a separate thread
threading.Thread(target=heating1.simulate).start()
threading.Thread(target=heating2.simulate).start()
threading.Thread(target=heating3.simulate).start()

# configure the heating objects with desired temperature thresholds
heating1.setTemperatureToHeat(22)
heating1.setTemperatureToStop(24)
heating1.startHeating()

heating2.setTemperatureToHeat(18)
heating2.setTemperatureToStop(20)

heating3.setTemperatureToHeat(22)
heating3.setTemperatureToStop(23)
heating3.startHeating()

# simulate the change in outside temperature over time
for i in range(20):
    heating1.outsideTemperature += 1
    heating2.outsideTemperature += 1
    heating3.outsideTemperature += 1
    print(f"Heating 1: {heating1.getTemperature()}, Heating 2: {heating2.getTemperature()}, Heating 3: {heating3.getTemperature()}")
    time.sleep(1)
