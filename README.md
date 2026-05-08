# titanic-survival-prediction
Prédiction de survie sur le Titanic avec Machine Learning et API FastAPI
# Prédiction de Survie — Titanic

## Objectif
Prédire si un passager du Titanic a survécu ou non
en utilisant des algorithmes de Machine Learning.

## Résultats
| Modèle | Précision |
|---|---|
| Régression Logistique | 79.89% |
| Decision Tree | 79.89% |
| Random Forest | **81.56%**  |

## Technologies utilisées
- Python 3.11
- pandas, numpy, matplotlib, seaborn
- scikit-learn
- FastAPI + uvicorn
- TensorFlow / Keras

## Structure du projet
titanic-survival-prediction/
├── deploiement_titanic.ipynb  ← Analyse complète
├── modele_titanic.pkl         ← Modèle sauvegardé
├── api.py                     ← API FastAPI
└── README.md

## Ce qu'on a découvert
- **Les femmes** avaient 74% de chances de survivre
- **La 1ère classe** avait 63% de chances de survivre
- **Les hommes en 3ème classe** avaient seulement 13%

## Lancer l'API
```bash
uvicorn api:app --reload
```
Puis aller sur : http://127.0.0.1:8000/docs

## Auteur
**Oumar** — Data Scientist en formation
GitHub : [oumar-ds](https://github.com/oumar-ds)

