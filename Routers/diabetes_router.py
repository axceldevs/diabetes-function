from fastapi import APIRouter
from Schemas.patient_data import PatientData
from Services.diabetes_service import PredictionDiabetes
from Utils.config import settings

router = APIRouter(
    prefix=settings.path_router,
)

@router.post("/diabetes/predict")
async def patient_predict(data: PatientData):

    prediction = PredictionDiabetes.predict(data)

    return {"prediction": prediction}
