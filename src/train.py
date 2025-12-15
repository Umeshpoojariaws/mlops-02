import pandas as pd
import mlflow
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from lightgbm import LGBMClassifier
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline as ImbPipeline
import optuna
from sklearn.model_selection import cross_val_score
import yaml
import pickle

with open('params.yaml') as f:
    params = yaml.safe_load(f)['train']

df = pd.read_csv('data/processed/train.csv')
X, y = df['clean_text'], df['sentiment']

def objective(trial):
    pipeline = ImbPipeline([
        ('tfidf', TfidfVectorizer(max_features=trial.suggest_int('max_features', 500, 5000))),
        ('smote', SMOTE() if params['smote'] else None),
        ('clf', LGBMClassifier(n_estimators=trial.suggest_int('n_estimators', 50, 200)))
    ])
    score = cross_val_score(pipeline, X, y, cv=params['cv'], scoring='f1_macro').mean()
    return score

study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=params['n_trials'])

# Train best model
best_pipeline = # Rebuild from best params
best_pipeline.fit(X, y)
with open('models/model.pkl', 'wb') as f:
    pickle.dump(best_pipeline, f)

# Log to MLflow
with mlflow.start_run():
    mlflow.log_params(study.best_params)
    mlflow.log_metric('f1', study.best_value)
    mlflow.sklearn.log_model(best_pipeline, 'model')