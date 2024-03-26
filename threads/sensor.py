from threading import current_thread
import time
import random
from writeAJson import writeAJson


def criaSensorTemp(name, value, database):
    sensor_doc = {
            'nomeSensor': nome_sensor,
            'valorSensor': valor_sensor,
            'unidadeMedida': 'C°',
            'sensorAlarmado': False
        }
    database.insert_one(sensor_doc)

def temperature(name, interval, database, limite):
    count = 0
    temp = 30
    local = {"nomeSensor": name}
    while count < limite:
        count += 1
        temp = random.randint(30, 40)
        if(temp >= 38):
            print('Atencao! Temperatura  muito  alta! Verificar Sensor', name, '!')
            database.update_one({'nomeSensor':name},{'$set':{'valorSensor':temp, 'sensorAlarmado':True}})

            sensor = database.find(local)
            writeAJson(sensor, f"Sensor{current_thread().getName()}")
        else:
            time.sleep(interval)
            database.update_one({'nomeSensor':name},{'$set':{'valorSensor':temp, 'sensorAlarmado':False}})
            print(name, '=', temp, 'C\n')

            sensor = database.find(local)
            writeAJson(sensor, f"Sensor{current_thread().getName()}")

    print(f'{name}: Atingiu o limite de execuções.')