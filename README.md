# Unscript-Rookies-2022 

## 1. Problem Statement
*   The Financial Management System is a software that is used to check the 
authenticity of a particular transaction in a financial company.
*   In Financial Management System, participants must create a model for 
predicting fraudulent transactions for a financial company and then use the model's 
insights to create an actionable plan. The case's data is stored in a CSV file with 
6362620 rows and 10 columns.

## 2. Dataset link: 
* [Data Location](https://drive.google.com/file/d/12EEXQ8B_p-62ArFWd5ZyCK7fWhD-BRup/view?usp=sharing)

## 3. Tools, Libraries & Softwares used:
* pandas, matplotlib, numpy for Data Exploration and Cleaning
* scikit-learn for validation of our ML Model and creating metric insights
* Flask for creating our Backend and Tailwind to apply styles
* Github for Version Control and Collaboration among our team
* Heroku for Deployment

## 4. Our analysis on data and solution to some of imbalance
*   We found that 3 types of transactions had 0 Fraud Cases so we decided to neglect them from training and created certain conditions to judge if 
    their transactions are Fraud or not which are explained in our Data Exploration Notebook 
*   Dataset was completely unbalanced so we decided to randomly select our data based on 1:1 ration of Fraudulent and non-Fraudulent Data from our dataset
    which we trained our model on and got a 99% Recall and 99% F1-Score metrics on our data.

## 5. ML model used : 
* Decision Tree Classifier

## 6. Reason for selecting Decision Tree:
*   Decision Tree Classifier showed the highest recall, accuracyy and F1 score when compared to others:
*   **Recall - 99.1799 % | Acc - 99.124 % | f1 - 99.108 %**
*   **Rejecting other networks because:**
*   Neural Networks are rejected because it obviously takes a LOT of training time & computation power
*   Performance of other models that were tested are:
 ________________________________________________
| Model               |  Recall(%)  |  F1(%)     |
|---------------------|-------------|----------- |
| **Decision Tree**   | **99.1799** | **99.108** |
| Logistic Regression |   85.721    |   88.7021  |
| SVM                 |   84.02     |   88       |
| Naive bayes         |   46        |   88       |
| Kernel SVM          |   81.478    |   87.06    |
-------------------------------------------------

## 7. Challenges fased:
*   Data Analysis
*   Input for model 
*   Probemes in deployment due to data size

## 8. Deployed at: 
