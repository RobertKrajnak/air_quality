import random

print("Toto je z dev sensor reading")

# Get the temperature of the CPU for compensation
def get_cpu_temperature():
    return round( random.uniform(45.0,55.0), 1 )

def get_humidity():
    return round( random.uniform(1.0,100.0), 1 )

def get_temperature():
    return round( random.uniform(25.0,35.0), 10 )

def get_pressure():
    return round( random.uniform(950.0,1150.0), 9 )

def get_light():
    return round( random.uniform(0.0,5.0), 5 )

def get_oxidised():
    return round( random.uniform(0.0,10.0), 11 )

def get_reduced():
    return round( random.uniform(200.0,220.0), 9 )

def get_nh3():
    return round( random.uniform(60.0,80.0), 10 )

def get_pm1():
    return round( random.uniform(10.0,15.0), 1 )

def get_pm25():
    return round( random.uniform(15.0,20.0), 1 )

def get_pm10():
    return round( random.uniform(15.0,20.0), 1 )

def get_enviroment():
    return "development"

def get_serial_number():
    return str("123456789")