from fastapi import APIRouter
from schemas.patient_data import PatientData
from services.diabetes_service import PredictionDiabetes
from utils.config import settings

router = APIRouter(
    prefix=settings.path_router,
)

@router.post("/diabetes/predict")
async def patient_predict(data: PatientData):

    prediction = PredictionDiabetes.predict(data)

    return {"prediction": prediction}
