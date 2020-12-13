
import uvicorn
from fastapi import FastAPI
from cementpre import cementpre
import numpy as np
import pickle
import pandas as pd

app = FastAPI()
pickle_in = open("model.pkl","rb")
regressor=pickle.load(pickle_in)

@app.get('/')
def index():
    return {'message': 'Hello pro programmer. Welcome to our predication center'}


@app.get('/{name}')
def get_name(name: str):
    return {'Welcome to my predication center Mr.': f'{name}'}

@app.post('/predict')
def predict_cement(data:cementpre):
    data = data.dict()
    A=data['Cement']
    B=data['Slag']
    C=data['Ash']
    D=data['Water']
    E=data['Superplasticizer']
    F=data['Coarse']
    G=data['Fine']
    H=data['Age']
    prediction = regressor.predict([[A,B,C,D,E,F,G,H]])

    return {
        'prediction': prediction[0]
        
    }


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)