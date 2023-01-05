#!/usr/bin/env python
# coding: utf-8

# In[1]:


import env
import pandas as pd
import os



def get_telco_data():   
    '''
    Checks to see if telco.csv is saved locally and if so loads it as a df. If it is not saved this function will query
    the sql server to pull the information then save is locally. Returns a df.
    '''
    if os.path.exists('telco.csv'):
        df = pd.read_csv('telco.csv')
    else:
        url = env.get_connection('telco_churn')
        query = 'select * from customers join contract_types using (contract_type_id) join internet_service_types using (internet_service_type_id) join payment_types using (payment_type_id) left join customer_churn using (customer_id)'
        df = pd.read_sql(query,url)
        df.to_csv('telco.csv',index=False)
    return df



