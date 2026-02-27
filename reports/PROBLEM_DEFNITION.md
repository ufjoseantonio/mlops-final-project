# A) Problem Definition
## 1. AI/ML Use Case
**Problem Context:** A retail bank is facing a high customer attrition rate (churn), meaning customers are closing their bank accounts and moving their funds to competitors. Retaining existing bank customers is significantly more cost-effective than acquiring new ones. Currently, the retention team lacks a data-driven approach to identify which clients are at high risk of closing their accounts based on their financial behavior and account balance.

**Constraints**
* The model must be interpretable to understand why a customer is leaving.
* The inference API must be lightweight and respond in under 500ms.
* The project must be completed and deployed within a strict timeframe.

**Goals & Benefits:**
* **Goal:** Develop an end-to-end ML pipeline (classification model) to predict the probability of a customer churning based on their historical data and demographics.
* **Benefits** Enable the business to proactively offer targeted promotions to at-risk customers, potentially reducing the overall churn rate and saving revenue.

**Expeceted Results & Success Metrics**
* A deployed REST API serving predictions.
* **Success Metric:** Achieve an **F1-Score of at least 0.75** on the test set, as the dataset might be imbalanced and we need need to balance Precision and Recall.

## 2. Data Acquisition
**Dataset:** We will use the standard "Bank Customer Churn" dataset.
* **Description:** The dataset contains tabular data representing bank customer profiles.
* **Feautures:** It includes demographic information (Age, Gender, Geography), finantial products used (Credit Score, Balance, Number of Products), and behavioral data (Active Member status).
* **Target Variable:** `Exited` (Binary: 1 if the customer left, 0 if they stayed).
* **Format:** Raw CSV file, containing approximately 10,000 records.
