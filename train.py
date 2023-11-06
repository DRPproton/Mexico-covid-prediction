"""
Midterm project
COVID death prediction using Mexico data 
Dashel Ruiz Perez 11/06/2023
"""
import pandas as pd
import numpy as np
import time
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.metrics import roc_auc_score
import pickle
import warnings
warnings.filterwarnings(action='ignore')

# Importing dataset
print('Importing dataset...')
df = pd.read_csv('covid_data_mex.csv')


print('Preparing dataset...')
cat_cols = df.describe(exclude='number').columns

# Making the encoder
encoder = OrdinalEncoder()

df[cat_cols] = encoder.fit_transform(df[cat_cols])


### Dividing the data set in X and y to check for multicoliniarity
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

### Data prep for modeling
X_full_train, X_test, y_full_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)
X_train, X_val, y_train, y_val = train_test_split(X_full_train, y_full_train, test_size=0.25, random_state=123)


# Making the model
xgb_model = xgb.XGBClassifier(
    objective='binary:logistic',  # Set the objective function for a binary classification task
    max_depth=5,                 # Maximum depth of trees
    learning_rate=0.3,           # Learning rate (shrinkage)
    n_estimators=50,            # Number of boosting rounds (trees)
    subsample=0.8,               # Fraction of samples used for each boosting round
    colsample_bytree=0.8,        # Fraction of features used for each boosting round
    reg_alpha=0.0,               # L1 regularization term on weights
    reg_lambda=1.0,              # L2 regularization term on weights
    random_state=1              # Set a seed for reproducibility
)

print('Training the model...')
xgb_model.fit(X_train.values, y_train)

# Make predictions on the test set using the best model
print('Making predictions')
time.sleep(1)

y_pred_xgb = xgb_model.predict_proba(X_val)[:,1]


auc = roc_auc_score(y_val, y_pred_xgb)
print(f'Result of te prediction with validation set, roc_auc -> {auc}')
print()
print(f'Result of te prediction with testing set, roc_auc -> {roc_auc_score(y_test, xgb_model.predict_proba(X_test)[:,1])}')


# Explorting the model
time.sleep(2)
with open('xgb_model.bin', 'wb') as f_out: 
    pickle.dump(xgb_model, f_out)
    print(f'Model exported as xgb_model.bin')
