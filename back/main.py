from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
import pandas as pd
import pickle
from back.data_preparing import preparing_data
import os
import joblib
import csv
from fastapi.middleware.cors import CORSMiddleware
from back.data_preparing import getting_ld_gr


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    'http://localhost:3000',
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


model = joblib.load('/Users/amina/garpix_prartice_2024/model/model.pkl')

class PredictionRequest(BaseModel):
    data: list


class PredictionResponse(BaseModel):
    predictions: list


@app.post("/uploadfile")
async def create_upload_file(file: UploadFile):
    try:
        if file.content_type not in ["application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                                     "application/vnd.ms-excel"]:
            raise HTTPException(status_code=400, detail="Uploaded file is not an Excel file")

        contents = await file.read()

        temp_file_path = "temp_uploaded_file.xlsx"

        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(contents)
        ld, group = getting_ld_gr(temp_file_path)
        csv_path = preparing_data(temp_file_path)

        os.remove(temp_file_path)

        # загружаем данные для предсказания
        data_for_prediction = pd.read_csv(csv_path)

        # удаление признака 'Доля 2 последний семестр', если он не был использован при обучении модели
        if 'Доля 2 последний семестр' not in model.feature_names_in_:
            data_for_prediction = data_for_prediction.drop(columns=['Доля 2 последний семестр'])

        y_pred = model.predict(data_for_prediction)

        # сохранение в CSV
        predictions_df = pd.DataFrame(y_pred, columns=['Predicted'])
        predictions_csv_path = 'predictions.csv'
        predictions_df.to_csv(predictions_csv_path, index=False)

        with open(predictions_csv_path, mode='r') as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                pred = lines

        return {"predicted_data": pred, "ld": ld, "group": group}
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
