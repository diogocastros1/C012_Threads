from pymongo import *
from sensor import criaSensorTemp, temperature
import threading

# Conexão com o banco
client =  MongoClient('mongodb+srv://root:6qAsN$-!8sUPVbg@cluster0.slkiyz1.mongodb.net/test')

# Criando ou acessando o database
db = client['bancoiot']

# Criando ou acessando a collection
sensores = db.sensores

# Para criar um novo sensor execute esta linha alterando de X para o numero do sensor
# criaSensorTemp('TempX', sensores)


x = threading.Thread(target=temperature, args=('Temp1', 5, sensores, 5))
y = threading.Thread(target=temperature, args=('Temp2', 5, sensores, 5))
z = threading.Thread(target=temperature, args=('Temp3', 5, sensores, 5))
x.start()
y.start()
z.start()
