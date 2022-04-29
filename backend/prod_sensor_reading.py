from pms5003 import PMS5003, ReadTimeoutError as pmsReadTimeoutError, SerialTimeoutError
from enviroplus import gas
from subprocess import PIPE, Popen
import logging
from bme280 import BME280
try:
    from ltr559 import LTR559
    ltr559 = LTR559()
except ImportError:
    import ltr559

bme280 = BME280()
pms5003 = PMS5003()

def get_humidity():
    return bme280.get_humidity()

def get_cpu_temperature():
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE, universal_newlines=True)
    output, _error = process.communicate()
    return float(output[output.index('=') + 1:output.rindex("'")])

def get_temperature():
    comp_factor = 2.25
    cpu_temp = get_cpu_temperature()
    raw_temp = bme280.get_temperature()
    temperature_data = raw_temp - ((cpu_temp - raw_temp) / comp_factor)
    return temperature_data

def get_pressure():
    pressure_data = bme280.get_pressure()
    return pressure_data

def get_light():
    proximity = ltr559.get_proximity()
    if proximity < 10:
        light_data = ltr559.get_lux()
    else:
        light_data = 1
    return light_data

def get_oxidised():
    data = gas.read_all()
    oxidised_data = data.oxidising / 1000
    return oxidised_data

def get_reduced():
    data = gas.read_all()
    reduced_data = data.reducing / 1000
    return reduced_data

def get_nh3():
    data = gas.read_all()
    nh3_data = data.nh3 / 1000
    return nh3_data

def get_pm1():
    try:
        pm1_data = pms5003.read()
    except pmsReadTimeoutError:
        logging.warning("Failed to read PMS5003")
    else:
        pm1_data = float(pm1_data.pm_ug_per_m3(1.0))
        return pm1_data

def get_pm25(): # luftdaten - P2
    try:
        pm25_data = pms5003.read()
    except pmsReadTimeoutError:
        logging.warning("Failed to read PMS5003")
    else:
        pm25_data = float(pm25_data.pm_ug_per_m3(2.5))
        return pm25_data

def get_pm10(): # luftdaten - P1
    try:
        pm10_data = pms5003.read()
    except pmsReadTimeoutError:
        logging.warning("Failed to read PMS5003")
    else:
        pm10_data = float(pm10_data.pm_ug_per_m3(10))
        return pm10_data

def get_enviroment():
    return "production"

def get_serial_number():
        with open('/proc/cpuinfo', 'r') as f:
            for line in f:
                if line[0:6] == 'Serial':
                    return line.split(":")[1].strip()