from sensors import AmbientSensor
from observer import Observable
from update_firestore import UpdateFirestore

from observer import Observer

class UpdatePostgres(Observer):

    def __init__(self):
        Observer.__init__(self)

    def update(self, arg):
        print(arg)

    def error(self):
        pass


class SensorReadings(Observable):

    def __init__(self):
        Observable.__init__(self)
        self.ambient_sens_temp = ""
    def data_refresh(self):
        ambient_readings = AmbientSensor()
        self.ambient_sens_temp= ambient_readings.get_temp()

    def trigger_update(self):
        self.data_refresh()
        self.notify(value=self.ambient_sens_temp)

sr = SensorReadings()
uf = UpdateFirestore()
up = UpdatePostgres()
sr.add(uf)
sr.add(up)
sr.trigger_update()


#---------------------Sensor testing ------------------------#
#device_file: str, device_folder: str,
"""        device_folder_tom0 = glob.glob(base_dir + '28-0316b09095ff')[0]
        device_folder_tom1 = glob.glob(base_dir + '28-0516b045b5ff')[0]
        device_file_tom0 = device_folder_tom0 + '/w1_slave'
        device_file_tom1 = device_folder_tom1 + '/w1_slave'


"""
#Temperature readings.
#temp = Temperature(device_file="28-0316b09095ff")
#print("---")
#print(temp.get_temperature())


"""
    ADC pins for the GPIO. 
    transistor_pin_0 = 26
    transistor_pin_1 = 16
    adc_channels are 1,0
"""
#print("---")
# Moisture readings
#pins = GPIOPins((26, 16))
#soil_one = SoilMoisture(2, 0, pins)
#print(soil_one.read_values())

#Ambident sensors
ambient_readings = AmbientSensor()
#print("---")
# There is a bug in the source code from Adafruit for this module. You need to call the temp
# method first in order to get the rest of the readings. The temp method seems to be
# the only function that creates an object that is required to read. This is a deprecetated library
# that I am using so not going to bother fixing.
#print(ambient_readings.get_temp())
#print(ambient_readings.get_humidity())
#print(ambient_readings.get_pressure())
