import uvicorn
from fastapi import FastAPI
import joblib,os

app = FastAPI()

web_phish_model = open('web_phishing.pkl', 'rb')
web_phish_model_ls = joblib.load(web_phish_model)

@app.get('/predict/{feature}')
async def predict(features):
    X_predict = []
    X_predict.append(str(features))
    y_Predict = web_phish_model_ls.predict(X_predict)
    if y_Predict == 'bad':
        result = "Ini adalah web phishing!"
    else:
        result = "Ini bukan web phishing"

    return (features, result)
if __name__ == '__main__':
    uvicorn.run(app,host="127.0.0.1",port=8000)
    