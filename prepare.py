from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np


def prep_telco(df):
    df = df.drop(columns=['payment_type_id', 'internet_service_type_id', 'contract_type_id','customer_id'])
    df['total_charges'] = (df.total_charges + '0').astype('float')
    addons = ['phone_service', 'multiple_lines', 'online_security','online_backup', 
          'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies']
    df['addons'] = np.where(df[addons]=='Yes',1,0).sum(axis=1)
    cols_bool = ['senior_citizen','partner', 'dependents', 'tenure', 'phone_service', 'multiple_lines',
             'online_security', 'online_backup', 'device_protection', 'tech_support','streaming_tv', 
             'streaming_movies', 'paperless_billing','churn']
    df[cols_bool] = np.where(df[cols_bool]=='Yes',1,0)
    df['partner_dep'] = np.where((df.partner==1)|(df.dependents==1),1,0)
    dummies = df.select_dtypes(include='object').columns
    dummies = pd.get_dummies(df[dummies],drop_first=True)
    df = pd.concat([df, dummies], axis=1)
    return df

def split_data(df, target):
    train_validate, test = train_test_split(df, train_size =.8, random_state = 91, stratify = df[target])
    train, validate = train_test_split(train_validate, train_size = .7, random_state = 91, stratify = train_validate[target])
    X_train = train.drop(columns=target)
    y_train = train[target]
    X_val = validate.drop(columns=target)
    y_val = validate[target]
    X_test = test.drop(columns=target)
    y_test = test[target]
    return train, X_train, y_train, X_val, y_val, X_test, y_test