import faust
import json
from json import JSONEncoder

# defining the data structure to send to kafka
class BankModel(faust.Record, validation=True):
    age: int
    job: str
    marital: str
    education: str
    default: str
    balance: int
    housing: str
    loan: str
    day: int
    duration: int
    campaign: int
    pdays: int
    previous: int
    poutcome: str

# here I am going to define a custom json encoder we can use to serialize our values while passing them to kafka
class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        return o._asdict()   