from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np


def prep_telco(df):
    df = df.drop(columns=['Unnamed: 0','payment_type_id', 'internet_service_type_id', 'contract_type_id','customer_id'])
    df['total_charges'] = (df.total_charges + '0').astype('float')
    addons = ['phone_service', 'multiple_lines', 'online_security','online_backup', 
          'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies']
    df['addons'] = np.where(df[addons]=='Yes',1,0).sum(axis=1)
    cols_bool = ['senior_citizen','partner', 'dependents', 'tenure', 'phone_service', 'multiple_lines',
             'online_security', 'online_backup', 'device_protection', 'tech_support','streaming_tv', 
             'streaming_movies', 'paperless_billing','churn']
    df[cols_bool] = np.where(df[cols_bool]=='Yes',1,0)
    dummies = df.select_dtypes(include='object').columns
    dummies = pd.get_dummies(df[dummies],drop_first=True)
    df = pd.concat([df, dummies], axis=1)
    return df

def split_data(df, target = 'churn'):
    train, val_test = train_test_split(df,test_size=.2,random_state=21,stratify=df[target])
    validate, test = train_test_split(val_test,test_size=.3,random_state=21,stratify=val_test[target])
    
    X_train = train.drop(columns=target)
    y_train = train.churn

    X_val = validate.drop(columns=target)
    y_val = validate.churn

    X_test = test.drop(columns=target)
    y_test = test.churn

    return train, X_train, y_train, X_val, y_val, X_test, y_test