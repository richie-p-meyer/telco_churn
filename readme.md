Project Description:
Telco is experiencing a large amount of customer churn. Why are customers churning and are there ways we can decrease it?

Goals:
Find drivers for customer churn at Telco. Why are customers churning?
Construct a ML classification model that accurately predicts customer churn.
Deliver a report that a non-data scientist can read through and understand what steps were taken, why and what was the outcome?

Initial Questions:
1) Do customers churn after they've spent a certain amount of money with the company?
2) Do customers with a partner and dependents churn at a different rate?
3) What month are customers most likely to churn?
4) Do customers with more addons churn at a different rate?

Data Dictionary: 
    'customer_id' - Unique customer identifier
    'gender' - Male/Female
    'senior_citizen' - Over 55
    'partner' - With a spouse
    'dependents' - With dependents
    'tenure' - Length of time with company in months
    'phone_service' - With phone service
    'multiple_lines' - Has multiple lines
    'online_security' - With online security
    'online_backup' - With online backup 
    'device_protection' - With device protection
    'tech_support' - With tech support
    'streaming_tv' - With streaming tv
    'streaming_movies' - With streaming movies
    'paperless_billing' - With paperless billing
    'monthly_charges' - Monthly charges in USD
    'total_charges' - Total charges with Telco in USD
    'churn' - Is customer still with company
    'contract_type' - Which contract type
    'internet_service_type' - Which internet service type
    'payment_type' - Which payment type
    'churn_month' - If a customer has churned, which month did it happen?

Project Planning:
1) Determine which columns I need and which I can drop. 
2) Add column with an 'addon' count
3) Answer questions one at a time
    a) Do customers with higher monthly_charges churn at a different rate?
        viz
        stat test
    b) Do customers with a partner or dependents churn at a different rate?
        viz
        stat test

    c) What month are customers most likely to churn?
        viz
        stat test
    d) Do customers with more addons churn at a different rate?
        viz
        stat test
4) Add Ho and Ha
5) Pick and run 3 classification methods
6) Make predictions on full data set, save as csv
7) Comment all code, add markdown cells




Key Findings 

Recommendations

Steps to Reproduce