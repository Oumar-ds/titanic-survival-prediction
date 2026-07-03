#  Prédiction de Survie — Titanic

> Projet complet de Data Science : analyse, modélisation Machine Learning et déploiement via API FastAPI.

---

## 📌 Objectif

Prédire si un passager du Titanic a survécu ou non en utilisant des algorithmes de Machine Learning, à partir des données de 891 passagers.

---

## 📊 Résultats

| Modèle | Précision |
|---|---|
| Régression Logistique | 79.89% |
| Decision Tree | 79.89% |
| Random Forest | 82.68% |
| TensorFlow Deep Learning | 81.56% |
| **XGBoost** | **83.80% ✅** |

> **Meilleur modèle : XGBoost avec 83.80% de précision**

---

## 🔍 Ce qu'on a découvert

- **Les femmes** avaient **74%** de chances de survivre vs **19%** pour les hommes
- **La 1ère classe** avait **63%** de chances de survivre vs **24%** pour la 3ème classe
- **Les passagers de Cherbourg** survivaient à **55%** — majoritairement en 1ère classe
- **Les hommes en 3ème classe** avaient seulement **13%** de chances de survivre

---

## 🛠️ Technologies utilisées

- **Langage** : Python 3.11
- **Analyse** : pandas, numpy
- **Visualisation** : matplotlib, seaborn
- **Machine Learning** : scikit-learn, XGBoost
- **Deep Learning** : TensorFlow / Keras
- **Déploiement** : FastAPI, uvicorn, joblib

---

## 📁 Structure du projet

```
titanic-survival-prediction/
├── deploiement_titanic.ipynb  ← Analyse et modélisation complète
├── modele_titanic.pkl         ← Modèle XGBoost sauvegardé
├── api.py                     ← API FastAPI
└── README.md                  ← Documentation
```

---

## 🚀 Lancer l'API

```bash
# 1. Installer les dépendances
pip install fastapi uvicorn joblib xgboost scikit-learn

# 2. Lancer le serveur
uvicorn api:app --reload

# 3. Ouvrir l'interface de test
# http://127.0.0.1:8000/docs
```

---

## 🎯 Exemple de prédiction

**Entrée — Femme 1ère classe :**
```json
{
  "Pclass": 1,
  "Sex": 1,
  "Age": 35,
  "SibSp": 1,
  "Parch": 0,
  "Fare": 71.0,
  "Embarked": 1
}
```

**Sortie :**
```json
{
  "prediction": "Survivant ✅",
  "confiance": "99.0%"
}
```

---

**Entrée — Homme 3ème classe :**
```json
{
  "Pclass": 3,
  "Sex": 0,
  "Age": 25,
  "SibSp": 0,
  "Parch": 0,
  "Fare": 7.5,
  "Embarked": 0
}
```

**Sortie :**
```json
{
  "prediction": "Décédé ❌",
  "confiance": "97.0%"
}
```

---

## 👤 Auteur

**KONATE ZANA OOUMAR** — Data Scientist en formation  
🎓 Master 1 Data & Intelligence Artificielle — Université Polytechnique de Bingerville (UPB)  
GitHub : [oumar-ds](https://github.com/oumar-ds)
