# Consume data from kafka using python faust module

import faust
import requests
from model import BankModel, CustomEncoder
import json



app = faust.App('bank_customer_prediction_app', broker='kafka://localhost:9092', consumer_auto_offset_reset="earliest",
                 value_serializer='json',
)
topic = app.topic('customer_pred')



@app.agent(topic)
async def process(stream):
    """
    the data we sent to kafka is encoded and this would result to "TypeError" 
    when we call the model REST services against it, so to avoid this we need to 
    parse in our custom defined json encoder to be able to serialize the data, hence
    parse it to the model Rest services
    """
    async for event in stream:
        jsonized = json.dumps(event, cls=CustomEncoder)
        
        #print(jsonized)

        result = requests.post('http://0.0.0.0:8000/predict', json=json.loads(jsonized))
        print('Input data: ' + str(jsonized))
        print('Customer Prediction result: ' + str(result.json()))





if __name__ == '__main__':
    app.main()