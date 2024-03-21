import time
import random

def criaSensorTemp(name, value, database):
    sensor_doc = {
            'nomeSensor': nome_sensor,
            'valorSensor': valor_sensor,
            'unidadeMedida': 'C°',
            'sensorAlarmado': False
        }
    database.insert_one(sensor_doc)

def temperature(name, interval, database):
    temp = 30
    while True:
        temp = random.randint(30, 40)
        if(temp >= 38):
            print('Atencao! Temperatura  muito  alta! Verificar Sensor', name, '!')
            database.update_one({'nomeSensor':name},{'$set':{'valorSensor':temp, 'sensorAlarmado':True}})
            break
        else:
            time.sleep(interval)
            database.update_one({'nomeSensor':name},{'$set':{'valorSensor':temp, 'sensorAlarmado':False}})
            print(name, '=', temp, 'C\n')
        
            
# faltando criar as consultas para validar se a temperatura subiu

    