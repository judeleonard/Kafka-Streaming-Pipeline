import csv
import json
from json import dumps
import uuid
from kafka import KafkaProducer
from time import sleep
from model import CustomEncoder

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         key_serializer=lambda x: dumps(x).encode('utf-8'),
                         value_serializer=lambda x: dumps(x).encode('utf-8'))


with open('../data/bank_marketing_data.csv', 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        # assign random key identifier for every record pushed to kafka
        key = str(uuid.uuid4())
        value = {"age": int(row[1]), "job": str(row[2]), "marital": str(row[3]), "education": str(row[4]), "default": str(row[5]),
                "balance": int(row[6]), "housing": str(row[7]), "loan": str(row[8]), "day": int(row[10]), "duration": int(row[12]), \
                "campaign": int(row[13]), "pdays": int(row[14]), "previous": int(row[15]), "poutcome": str(row[16])}
        producer.send('customer_pred', value=value, key=key)
        print("data with the ID {} sent successfully".format(key))
        print(value)
        sleep(3)
