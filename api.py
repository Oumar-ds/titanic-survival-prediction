from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Charger le modèle
model = joblib.load("modele_titanic.pkl")

# Créer l'application
app = FastAPI()

# Définir la structure des données d'entrée
class Passager(BaseModel):
    Pclass   : int    # 1, 2 ou 3
    Sex      : int    # 0 = homme, 1 = femme
    Age      : float  # âge
    SibSp    : int    # frères/sœurs/conjoint
    Parch    : int    # parents/enfants
    Fare     : float  # prix du billet
    Embarked : int    # 0=S, 1=C, 2=Q

# Endpoint de prédiction
@app.post("/predire")
def predire(passager: Passager):
    donnees = np.array([[
        passager.Pclass,
        passager.Sex,
        passager.Age,
        passager.SibSp,
        passager.Parch,
        passager.Fare,
        passager.Embarked
    ]])
    
    prediction  = model.predict(donnees)[0]
    probabilite = model.predict_proba(donnees)[0].max()
    
    resultat = "Survivant ✅" if prediction == 1 else "Décédé ❌"
    
    return {
        "prediction"   : resultat,
        "confiance"    : f"{probabilite*100:.1f}%"
    }

# Page d'accueil
@app.get("/")
def accueil():
    return {"message": "API Titanic — Data Science par Oumar 🚀"}