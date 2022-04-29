import requests

def send_to_luftdaten(values, id):
    pm_values = dict(i for i in values.items() if i[0].startswith("P"))
    temp_values = dict(i for i in values.items() if not i[0].startswith("P"))

    pm_values_json = [{"value_type": key, "value": val} for key, val in pm_values.items()]
    temp_values_json = [{"value_type": key, "value": val} for key, val in temp_values.items()]

    resp_1 = requests.post(
        "https://api.luftdaten.info/v1/push-sensor-data/",
        json={
            "software_version": "enviro-plus 0.0.1",
            "sensordatavalues": pm_values_json
        },
        headers={
            "X-PIN": "1",
            "X-Sensor": id,
            "Content-Type": "application/json",
            "cache-control": "no-cache"
        }
    )

    resp_2 = requests.post(
        "https://api.luftdaten.info/v1/push-sensor-data/",
        json={
            "software_version": "enviro-plus 0.0.1",
            "sensordatavalues": temp_values_json
        },
        headers={
            "X-PIN": "11",
            "X-Sensor": id,
            "Content-Type": "application/json",
            "cache-control": "no-cache"
        }
    )

    if resp_1.ok and resp_2.ok:
        return True
    else:
        return False