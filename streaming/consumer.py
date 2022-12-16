import json 
import requests
from kafka import KafkaConsumer
from model import CustomEncoder


if __name__ == '__main__':
    consumer = KafkaConsumer(
        'customer_pred',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest'
    )
    for event in consumer:
        jsonized = json.dumps(event, cls=CustomEncoder)
        result = requests.post('http://0.0.0.0:8000/predict', json=json.loads(jsonized))
        print(result.json())