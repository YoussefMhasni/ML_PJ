import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import joblib
import os
from PIL import Image
import base64
import io



app = FastAPI()

class ImageData(BaseModel):
    data: str
class Feedback(BaseModel):
    data : str
    predicted_value: int
    real_value: int
class Result(BaseModel):
    prediction:int

@app.post("/feedback")
async def feedback(fb: Feedback):
    try:
        file_path=r"../data/prod_data.csv"
        df = pd.read_csv(file_path)
        img_data=encoder(fb.data)
        data = np.append(img_data, [fb.real_value, fb.predicted_value])
        if len(data) == len(df.columns):
            new_row = pd.DataFrame([data], columns=df.columns)
            df = pd.concat([df, new_row], ignore_index=True)
            df.to_csv(str(file_path), index=False)
        else:
            print("Number of elements in 'data' does not match the number of columns in the DataFrame.")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/predict/")
async def upload_image(image: ImageData):
    try:
        img_array = encoder(image.data)
        data=np.array(img_array).astype('uint8')
        prediction = model().predict(data)
        result = prediction[0]
        return Result(prediction=result)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
