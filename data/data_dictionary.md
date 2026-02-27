# Data Dictionary - Bank Customer Churn
This document describes the features present in the final training dataset ('data/training/train.csv') used to train the machine learning models.

## Target Variable
| Feature | Data Type | Description |
| :--- | :--- | :--- |
| **Exited** | Integer (Binary) | The target variable to predict. `1` indicates that the customer has left the bank (churned), and `0` indicates that the customer stayed. |

## Independent Variables (Features)
| Feature | Data Type | Description |
| :--- | :--- | :--- |
| **CreditScore** | Integer | A numerical value representing the customer's credit score indicate better creditworthiness. |
| **Geography** | String (Categorical) | The country where the customer resides (e.g., France, Spain, Germany). |
| **Gender** | String(Categorical) | The customer´s gender (Male, Female). |
| **Age** | Integer | The customer's age in years. |
| **Tenure** | Integer | The number of years the customer has been a client of the bank. |
| **Balance** | Float | The current amount of money in the customer's bank account. |
| **NumOfProducts** | Integer | The number of bank products the customer uses (e.g., saving account, credit card, loan). |
| **HasCrCard** | Integer (Binary) Indicates whether the customer holds a credit card with the bank (`1` = Yes, `0` = No). |
| **IsActiveMember** | Integer (Binary) | Indicates whether the customer is an active user of the bank's services (`1` = Active, `0` = Inactive). |
| **EstimatedSalary** | Float | The customer's estimated annual salary |