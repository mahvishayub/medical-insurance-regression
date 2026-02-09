# Medical Insurance Cost Prediction using Linear Regression

## 📌 Project Overview
This project focuses on predicting medical insurance costs based on individual demographic and health-related factors using Linear Regression. The objective is to analyze how features such as age, BMI, smoking status, and region influence insurance charges.

The project demonstrates a complete machine learning workflow, including data exploration, preprocessing, model training, evaluation, and interpretation.

---

## 📊 Dataset Description
The dataset includes the following features:

- **age**: Age of the individual
- **sex**: Gender (male/female)
- **bmi**: Body Mass Index
- **children**: Number of dependents
- **smoker**: Smoking status (yes/no)
- **region**: Residential region
- **charges**: Medical insurance cost (target variable)

---

## ⚙️ Methodology

### 1. Exploratory Data Analysis (EDA)
- Inspected data distributions
- Checked for missing values
- Analyzed relationships between features and insurance charges

### 2. Data Preprocessing
- Encoded categorical variables
- Performed train-test split
- Prepared data for linear regression modeling

### 3. Model Training
- Implemented Linear Regression using scikit-learn
- Trained the model on the training dataset

### 4. Model Evaluation
The model performance was evaluated using:
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score

---

## 📈 Results & Insights
- Smoking status and BMI were found to significantly impact insurance charges
- Linear Regression provided an interpretable baseline model
- The model performs reasonably well for insurance cost estimation

---

## 🛠️ Tools & Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

---

## Project Structure
medical-insurance-regression/
│
├── data/
│ └── insurance.csv
├── notebooks/
│ └── Medical_Insurance_Linear_Regression.ipynb
├── README.md
