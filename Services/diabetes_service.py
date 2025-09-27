from Schemas.patient_data import PatientData
import pickle
import numpy as np

with open("./Resources/RFDiabetesv132.pkl",'rb') as file:
    model = pickle.load(file)

labels = ["Sano", "Enfermo"]

class PredictionDiabetes():

    def predict(data: PatientData):

        xin = np.array([
            data.pregnancies, 
            data.glucose, 
            data.blood_pressure, 
            data.skinthickness, 
            data.insulin, 
            data.bmi, 
            data.diabetespedigreefunction,
            data.age 
        ]).reshape(1,8)

        prediction = model.predict(xin)

        print("Prediction", prediction)

        return labels[prediction[0]]