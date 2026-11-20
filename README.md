# Prédiction de survie : Titanic

Projet complet de Data Science : analyse, modélisation Machine Learning et déploiement via une API FastAPI.

## Objectif

Prédire si un passager du Titanic a survécu ou non à partir de ses caractéristiques (classe, sexe, âge, famille à bord, prix du billet, port d'embarquement), en utilisant les données de 891 passagers.

## Résultats

| Modèle | Précision |
|---|---|
| Régression logistique | 79,89 % |
| Decision Tree | 79,89 % |
| Random Forest | 82,68 % |
| Réseau de neurones (TensorFlow/Keras) | 81,56 % |
| **XGBoost** | **83,80 %** |

Meilleur modèle : **XGBoost avec 83,80 % de précision**.

## Ce que les données révèlent

- Les femmes avaient 74 % de chances de survivre, contre 19 % pour les hommes.
- La 1ère classe avait 63 % de chances de survivre, contre 24 % pour la 3ème classe.
- Les passagers de Cherbourg survivaient à 55 %, majoritairement en 1ère classe.
- Les hommes en 3ème classe avaient seulement 13 % de chances de survivre.

## Technologies

- Langage : Python
- Analyse : pandas, numpy
- Visualisation : matplotlib, seaborn
- Machine Learning : scikit-learn, XGBoost
- Deep Learning : TensorFlow / Keras
- Déploiement : FastAPI, uvicorn, joblib

## Structure du projet

```
titanic-survival-prediction/
├── api.py               API FastAPI de prédiction
├── modele_titanic.pkl   Modèle XGBoost sauvegardé
├── untitled1.py         Réseau de neurones TensorFlow/Keras (export Colab)
└── README.md            Documentation
```

## Lancer l'API

```bash
pip install fastapi uvicorn joblib xgboost scikit-learn numpy
uvicorn api:app --reload
```

Puis ouvrir l'interface de test : http://127.0.0.1:8000/docs

## Exemple de prédiction

Requête envoyée à l'API, pour une femme de 1ère classe :

```json
{ "Pclass": 1, "Sex": 1, "Age": 35, "SibSp": 1, "Parch": 0, "Fare": 71.0, "Embarked": 1 }
```

L'API renvoie la prédiction (Survivant ou Décédé) et le niveau de confiance du modèle : ici, survivante avec 99 % de confiance. Pour un homme de 25 ans en 3ème classe, le modèle prédit un décès avec 97 % de confiance.

## Auteur

**KONATE ZANA Oumar**, Data Scientist
Master 2 Data & Intelligence Artificielle, Université Polytechnique de Bingerville (UPB)

Portfolio : [oumar-ds.github.io](https://oumar-ds.github.io) · GitHub : [Oumar-ds](https://github.com/Oumar-ds)
